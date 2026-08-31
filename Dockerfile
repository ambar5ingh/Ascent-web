# ASCENT Web — container image for AWS App Runner (also runs on Render/Fly/Cloud Run)
FROM python:3.12-slim

# System deps kept minimal — all Python deps are pure-Python wheels.
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Install dependencies first (better layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application
COPY . .

# App Runner sends traffic to port 8080 by default
EXPOSE 8080

# One worker, multiple threads — the app keeps its session cache in-process.
# S3 is the durable store (set ASCENT_S3_BUCKET), so a single worker is fine.
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "1", "--threads", "8", "--timeout", "120", "app:app"]
