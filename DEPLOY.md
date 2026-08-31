# ASCENT Web — AWS App Runner Deployment Guide

This app is packaged as a **Docker container** and deployed on **AWS App Runner**.
App Runner builds the image, runs it, and gives you an HTTPS URL — no EC2, no load
balancer, no `.ebextensions`. User accounts and saved questionnaires persist in
**S3**, so they survive redeploys.

The same container also runs unchanged on Render, Fly.io, Railway, or Google Cloud
Run if you ever want to move.

---

## What's in this bundle

```
ascent_web/
├── Dockerfile              # builds the container (python:3.12-slim + gunicorn)
├── .dockerignore           # keeps the image slim
├── requirements.txt        # Flask, plotly 5.24.1 (lean), openpyxl, gunicorn, boto3
├── app.py                  # Flask backend — S3-or-local storage, full calc engine
├── data/                   # calc constants + metadata.db (13.5 MB secondary data)
├── templates/              # Questionnaire, Target tool, results, login
└── static/                 # css / js / images
```

Storage is controlled by environment variables:
- `ASCENT_S3_BUCKET` — set this to your S3 bucket → accounts persist in S3
- `ASCENT_S3_PREFIX` — optional folder prefix inside the bucket (default `ascent`)
- `SECRET_KEY` — Flask session secret (set a random value)

If `ASCENT_S3_BUCKET` is not set, the app falls back to local file storage
(fine for running on a laptop; resets on container redeploy).

---

## Deploy — the two ways

App Runner can deploy **from source (GitHub)** or **from a container image (ECR)**.
The source path is simplest and needs no Docker on your machine. Use that unless you
have a reason not to.

---

## OPTION A — Deploy from source via GitHub (recommended, no Docker needed)

### Step 1 — Create the S3 bucket (for persistent accounts)

1. AWS Console → **S3** → **Create bucket**
2. Name it something unique, e.g. `ascent-web-data-<yourname>`
3. Region: **ap-south-1 (Mumbai)** (same region you'll deploy App Runner in)
4. Leave "Block all public access" **ON** (the app reaches it privately, not the public)
5. Create. Note the bucket name.

### Step 2 — Put the code in a GitHub repo

1. Create a new GitHub repo (private is fine), e.g. `ascent-web`
2. Unzip this bundle and push all files to the repo root. Either:
   - GitHub web UI: **Add file → Upload files**, drag everything in, commit; **or**
   - Command line:
     ```bash
     cd ascent_web
     git init
     git add .
     git commit -m "ASCENT web app"
     git branch -M main
     git remote add origin https://github.com/<you>/ascent-web.git
     git push -u origin main
     ```
   - **Note:** `data/metadata.db` is 13.5 MB — under GitHub's 100 MB limit, so a normal
     push works. No Git LFS needed.

### Step 3 — Create the App Runner service

1. AWS Console → **App Runner** → **Create service**
2. **Source:** Source code repository → **Add new** → connect your GitHub account
   (this opens a GitHub authorization popup; approve it, pick the `ascent-web` repo)
3. **Branch:** `main`
4. **Deployment trigger:** Automatic (redeploys on every push) or Manual — your choice
5. Click **Next**

### Step 4 — Configure the build

App Runner detects the `Dockerfile` automatically. On the build page:
- **Configuration file:** it should say it found the `Dockerfile` — leave the
  Dockerfile-based build selected.
- If it instead asks for build/run commands (no Dockerfile detected), point it at the
  Dockerfile or re-check the repo root has it.

### Step 5 — Configure the service

- **Service name:** `ascent-web`
- **Virtual CPU & memory:** **1 vCPU, 2 GB** (the metadata DB + plotly need the 2 GB)
- **Port:** **8080** (the Dockerfile exposes 8080)
- **Environment variables** — add these:
  | Key | Value |
  |-----|-------|
  | `SECRET_KEY` | a random string (run `python -c "import secrets;print(secrets.token_hex(32))"`) |
  | `ASCENT_S3_BUCKET` | your bucket name from Step 1 |
  | `ASCENT_S3_PREFIX` | `ascent` |

### Step 6 — Give the service permission to use S3

App Runner runs with an **instance role**. It needs S3 access to your bucket.

1. On the service config page, under **Security → Instance role**, choose
   **Create new role** (or create one in IAM first — see below).
2. If creating in IAM manually:
   - IAM → Roles → Create role → Trusted entity: **AWS service** →
     use case **App Runner** (search "App Runner - Tasks")
   - Attach this inline policy (replace the bucket name):
     ```json
     {
       "Version": "2012-10-17",
       "Statement": [{
         "Effect": "Allow",
         "Action": ["s3:GetObject", "s3:PutObject", "s3:DeleteObject", "s3:ListBucket"],
         "Resource": [
           "arn:aws:s3:::ascent-web-data-<yourname>",
           "arn:aws:s3:::ascent-web-data-<yourname>/*"
         ]
       }]
     }
     ```
   - Name it `ascent-apprunner-role`, then select it as the instance role.

### Step 7 — Create & wait

Click **Create & deploy**. First build takes **~5–8 minutes** (App Runner builds the
Docker image, installs deps, starts gunicorn). Watch the **Logs** tab — App Runner
streams the build and application logs live, so if anything fails you see the real
error immediately (unlike Elastic Beanstalk).

When it's done, the service shows a **Default domain** like
`https://xxxx.ap-south-1.awsapprunner.com` — that's your app.

### Step 8 — Use it

Open the URL → register a username/password → fill the Questionnaire → open the
Target Setting tool. Because accounts are in S3, they persist across redeploys and
anyone can log in from any browser.

---

## OPTION B — Deploy from a container image via ECR (if you prefer Docker)

Use this if you have Docker installed and want to build/push the image yourself.

```bash
# 1. Build
cd ascent_web
docker build -t ascent-web .

# 2. Create an ECR repo (once)
aws ecr create-repository --repository-name ascent-web --region ap-south-1

# 3. Log in to ECR (replace <acct> with your AWS account ID)
aws ecr get-login-password --region ap-south-1 \
  | docker login --username AWS --password-stdin \
    <acct>.dkr.ecr.ap-south-1.amazonaws.com

# 4. Tag & push
docker tag ascent-web:latest \
  <acct>.dkr.ecr.ap-south-1.amazonaws.com/ascent-web:latest
docker push <acct>.dkr.ecr.ap-south-1.amazonaws.com/ascent-web:latest
```

Then in App Runner → Create service → **Container registry** → **Amazon ECR** →
pick the `ascent-web:latest` image → same Steps 5–8 as above (port 8080, 2 GB,
env vars, S3 instance role).

To test locally before pushing:
```bash
docker run -p 8080:8080 -e SECRET_KEY=dev ascent-web
# open http://localhost:8080
```

---

## Updating later

- **Option A (GitHub):** push to `main`. If you set automatic deploys, App Runner
  rebuilds and redeploys on its own. Otherwise click **Deploy** in the console.
- **Option B (ECR):** rebuild, push a new `:latest`, then **Deploy** in the console.

User accounts and forms in S3 are untouched by redeploys.

---

## Cost note

App Runner bills for the compute while the service runs. A 1 vCPU / 2 GB service left
running 24/7 is roughly **$25–40/month**. To cut cost during a pilot, you can pause
the service (App Runner → **Pause**) when it's not in use and resume it later — pausing
stops compute billing. S3 storage for these small JSON files is a few cents/month.

---

## Why App Runner instead of Elastic Beanstalk

EB provisions EC2 + load balancer + auto-scaling; any of those failing gives the
opaque "failed to deploy, no logs" you hit. App Runner just builds the container and
runs it, streams logs live, and needs no VPC/instance-profile setup. For a single
Flask app it's the right-sized tool.

## Contact

Mehulkumar Patel · Mehul.Patel@wri.org · +91 9909926908
