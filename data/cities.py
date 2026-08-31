"""
India city master list (4,900+ urban local bodies) — extracted from
City_master sheet of WRI_India___ASCENT_Beta_V9.xlsm.

Each entry: {state, district, city, climate, [code]}
Climate zones: Hot and Dry | Warm & humid | Temperate | Cold | Composite

This file is large; keep it out of app.py to avoid bloating the main module.
"""

INDIA_CITIES = [
{
"state": "Andaman & Nicobar Islands",
"district": "South Andaman",
"city": "Port Blair",
"climate": "Warm & humid",
"code": 804041
},
{
"state": "Andhra Pradesh",
"district": "Anakapalli",
"city": "Narsipatnam",
"climate": "Warm & humid",
"code": 900077
},
{
"state": "Andhra Pradesh",
"district": "Anakapalli",
"city": "Yelamanchili",
"climate": "Warm & humid",
"code": 900078
},
{
"state": "Andhra Pradesh",
"district": "Anantapur",
"city": "Anantapur",
"climate": "Hot and Dry",
"code": 803009
},
{
"state": "Andhra Pradesh",
"district": "Anantapur",
"city": "Dharmavaram",
"climate": "Hot and Dry",
"code": 803010
},
{
"state": "Andhra Pradesh",
"district": "Anantapur",
"city": "Gooty",
"climate": "Hot and Dry",
"code": 900089
},
{
"state": "Andhra Pradesh",
"district": "Anantapur",
"city": "Guntakal",
"climate": "Hot and Dry",
"code": 803007
},
{
"state": "Andhra Pradesh",
"district": "Anantapur",
"city": "Kadiri",
"climate": "Hot and Dry",
"code": 803011
},
{
"state": "Andhra Pradesh",
"district": "Anantapur",
"city": "Kalyandurgam",
"climate": "Hot and Dry",
"code": 900090
},
{
"state": "Andhra Pradesh",
"district": "Anantapur",
"city": "Rayadurg",
"climate": "Hot and Dry",
"code": 803006
},
{
"state": "Andhra Pradesh",
"district": "Anantapur",
"city": "Tadipatri",
"climate": "Hot and Dry",
"code": 803008
},
{
"state": "Andhra Pradesh",
"district": "Annamayya",
"city": "B Kothakota",
"climate": "Warm & humid",
"code": 900856
},
{
"state": "Andhra Pradesh",
"district": "Annamayya",
"city": "Madanapalle",
"climate": "Warm & humid",
"code": 803015
},
{
"state": "Andhra Pradesh",
"district": "Annamayya",
"city": "Rajampeta",
"climate": "Warm & humid",
"code": 803000
},
{
"state": "Andhra Pradesh",
"district": "Annamayya",
"city": "Rayachoty",
"climate": "Warm & humid",
"code": 802999
},
{
"state": "Andhra Pradesh",
"district": "Bapatla",
"city": "Addanki",
"climate": "Warm & humid",
"code": 900149
},
{
"state": "Andhra Pradesh",
"district": "Bapatla",
"city": "Repalle",
"climate": "Warm & humid",
"code": 802985
},
{
"state": "Andhra Pradesh",
"district": "Chittoor",
"city": "Chittoor",
"climate": "Warm & humid",
"code": 803019
},
{
"state": "Andhra Pradesh",
"district": "Chittoor",
"city": "Kuppam",
"climate": "Warm & humid",
"code": 900726
},
{
"state": "Andhra Pradesh",
"district": "Chittoor",
"city": "Nagari",
"climate": "Warm & humid",
"code": 803016
},
{
"state": "Andhra Pradesh",
"district": "Chittoor",
"city": "Palamaneru",
"climate": "Warm & humid",
"code": 803020
},
{
"state": "Andhra Pradesh",
"district": "Chittoor",
"city": "Punganur",
"climate": "Warm & humid",
"code": 803018
},
{
"state": "Andhra Pradesh",
"district": "East Godavari",
"city": "Kovvur",
"climate": "Warm & humid",
"code": 802959
},
{
"state": "Andhra Pradesh",
"district": "East Godavari",
"city": "Nidadavole",
"climate": "Warm & humid",
"code": 802960
},
{
"state": "Andhra Pradesh",
"district": "East Godavari",
"city": "Rajahmundry",
"climate": "Warm & humid",
"code": 802952
},
{
"state": "Andhra Pradesh",
"district": "Eluru",
"city": "Chintalapudi",
"climate": "Warm & humid",
"code": 900857
},
{
"state": "Andhra Pradesh",
"district": "Eluru",
"city": "Eluru",
"climate": "Warm & humid",
"code": 802962
},
{
"state": "Andhra Pradesh",
"district": "Eluru",
"city": "Jangareddygudem",
"climate": "Warm & humid",
"code": 900084
},
{
"state": "Andhra Pradesh",
"district": "Eluru",
"city": "Nuzivid",
"climate": "Warm & humid",
"code": 802968
},
{
"state": "Andhra Pradesh",
"district": "Guntur",
"city": "Bapatla",
"climate": "Warm & humid",
"code": 802984
},
{
"state": "Andhra Pradesh",
"district": "Guntur",
"city": "Guntur",
"climate": "Warm & humid",
"code": 802981
},
{
"state": "Andhra Pradesh",
"district": "Guntur",
"city": "Mangalagiri Tadepalli",
"climate": "Warm & humid",
"code": 802976
},
{
"state": "Andhra Pradesh",
"district": "Guntur",
"city": "Ponnur",
"climate": "Warm & humid",
"code": 802983
},
{
"state": "Andhra Pradesh",
"district": "Guntur",
"city": "Tadepalli",
"climate": "Warm & humid",
"code": 802975
},
{
"state": "Andhra Pradesh",
"district": "Guntur",
"city": "Tenali",
"climate": "Warm & humid",
"code": 802982
},
{
"state": "Andhra Pradesh",
"district": "Kadapa",
"city": "Badvel",
"climate": "Warm & humid",
"code": 802994
},
{
"state": "Andhra Pradesh",
"district": "Kadapa",
"city": "Jammalamadugu",
"climate": "Warm & humid",
"code": 802996
},
{
"state": "Andhra Pradesh",
"district": "Kadapa",
"city": "Kadapa",
"climate": "Warm & humid",
"code": 802998
},
{
"state": "Andhra Pradesh",
"district": "Kadapa",
"city": "Kamalapuram",
"climate": "Warm & humid",
"code": 900728
},
{
"state": "Andhra Pradesh",
"district": "Kadapa",
"city": "Mydukur",
"climate": "Warm & humid",
"code": 900087
},
{
"state": "Andhra Pradesh",
"district": "Kadapa",
"city": "Proddatur",
"climate": "Warm & humid",
"code": 802995
},
{
"state": "Andhra Pradesh",
"district": "Kadapa",
"city": "Pulivendula",
"climate": "Warm & humid",
"code": 802997
},
{
"state": "Andhra Pradesh",
"district": "Kadapa",
"city": "Yerraguntla",
"climate": "Warm & humid",
"code": 900088
},
{
"state": "Andhra Pradesh",
"district": "Kakinada",
"city": "Gollaprolu",
"climate": "Warm & humid",
"code": 900081
},
{
"state": "Andhra Pradesh",
"district": "Kakinada",
"city": "Kakinada",
"climate": "Warm & humid",
"code": 802955
},
{
"state": "Andhra Pradesh",
"district": "Kakinada",
"city": "Peddapuram",
"climate": "Warm & humid",
"code": 802951
},
{
"state": "Andhra Pradesh",
"district": "Kakinada",
"city": "Pithapuram",
"climate": "Warm & humid",
"code": 802954
},
{
"state": "Andhra Pradesh",
"district": "Kakinada",
"city": "Samalkot",
"climate": "Warm & humid",
"code": 802953
},
{
"state": "Andhra Pradesh",
"district": "Kakinada",
"city": "Tuni",
"climate": "Warm & humid",
"code": 802950
},
{
"state": "Andhra Pradesh",
"district": "Kakinada",
"city": "Yeleswaram",
"climate": "Warm & humid",
"code": 900080
},
{
"state": "Andhra Pradesh",
"district": "Konaseema",
"city": "Amalapuram",
"climate": "Warm & humid",
"code": 802958
},
{
"state": "Andhra Pradesh",
"district": "Konaseema",
"city": "Mandapeta",
"climate": "Warm & humid",
"code": 802956
},
{
"state": "Andhra Pradesh",
"district": "Konaseema",
"city": "Mummidivaram",
"climate": "Warm & humid",
"code": 900082
},
{
"state": "Andhra Pradesh",
"district": "Konaseema",
"city": "Ramachandrapuram",
"climate": "Warm & humid",
"code": 802957
},
{
"state": "Andhra Pradesh",
"district": "Krishna",
"city": "Gudivada",
"climate": "Warm & humid",
"code": 802970
},
{
"state": "Andhra Pradesh",
"district": "Krishna",
"city": "Machilipatnam",
"climate": "Warm & humid",
"code": 802972
},
{
"state": "Andhra Pradesh",
"district": "Krishna",
"city": "Pedana",
"climate": "Warm & humid",
"code": 802971
},
{
"state": "Andhra Pradesh",
"district": "Krishna",
"city": "Vuyyuru",
"climate": "Warm & humid",
"code": 900102
},
{
"state": "Andhra Pradesh",
"district": "Krishna",
"city": "Ysr Tadigadapa",
"climate": "Warm & humid",
"code": 900853
},
{
"state": "Andhra Pradesh",
"district": "Kurnool",
"city": "Adoni",
"climate": "Warm & humid",
"code": 803003
},
{
"state": "Andhra Pradesh",
"district": "Kurnool",
"city": "Guduru",
"climate": "Warm & humid",
"code": 900153
},
{
"state": "Andhra Pradesh",
"district": "Kurnool",
"city": "Kurnool",
"climate": "Warm & humid",
"code": 803002
},
{
"state": "Andhra Pradesh",
"district": "Kurnool",
"city": "Yemmiganur",
"climate": "Warm & humid",
"code": 803001
},
{
"state": "Andhra Pradesh",
"district": "Manyam",
"city": "Palakonda",
"climate": "Warm & humid",
"code": 900076
},
{
"state": "Andhra Pradesh",
"district": "Manyam",
"city": "Parvathipuram",
"climate": "Warm & humid",
"code": 802943
},
{
"state": "Andhra Pradesh",
"district": "Manyam",
"city": "Salur",
"climate": "Warm & humid",
"code": 802945
},
{
"state": "Andhra Pradesh",
"district": "NTR",
"city": "Jaggaiahpet",
"climate": "Warm & humid",
"code": 802967
},
{
"state": "Andhra Pradesh",
"district": "NTR",
"city": "Kondapalli",
"climate": "Warm & humid",
"code": 900730
},
{
"state": "Andhra Pradesh",
"district": "NTR",
"city": "Nandigama",
"climate": "Warm & humid",
"code": 900129
},
{
"state": "Andhra Pradesh",
"district": "NTR",
"city": "Tiruvuru",
"climate": "Warm & humid",
"code": 900104
},
{
"state": "Andhra Pradesh",
"district": "NTR",
"city": "Vijayawada",
"climate": "Warm & humid",
"code": 802969
},
{
"state": "Andhra Pradesh",
"district": "Nandyal",
"city": "Allagadda",
"climate": "Warm & humid",
"code": 900095
},
{
"state": "Andhra Pradesh",
"district": "Nandyal",
"city": "Atmakur",
"climate": "Warm & humid",
"code": 900063
},
{
"state": "Andhra Pradesh",
"district": "Nandyal",
"city": "Bethamcherla",
"climate": "Warm & humid",
"code": 900727
},
{
"state": "Andhra Pradesh",
"district": "Nandyal",
"city": "Dhone",
"climate": "Warm & humid",
"code": 803005
},
{
"state": "Andhra Pradesh",
"district": "Nandyal",
"city": "Nandikotkur",
"climate": "Warm & humid",
"code": 900094
},
{
"state": "Andhra Pradesh",
"district": "Nandyal",
"city": "Nandyal",
"climate": "Warm & humid",
"code": 803004
},
{
"state": "Andhra Pradesh",
"district": "Nellore",
"city": "Alluru",
"climate": "Warm & humid",
"code": 900855
},
{
"state": "Andhra Pradesh",
"district": "Nellore",
"city": "Atmakur (N)",
"climate": "Warm & humid",
"code": 900064
},
{
"state": "Andhra Pradesh",
"district": "Nellore",
"city": "Buchireddypalem",
"climate": "Warm & humid",
"code": 900725
},
{
"state": "Andhra Pradesh",
"district": "Nellore",
"city": "Kandukur",
"climate": "Warm & humid",
"code": 802989
},
{
"state": "Andhra Pradesh",
"district": "Nellore",
"city": "Kavali",
"climate": "Warm & humid",
"code": 802990
},
{
"state": "Andhra Pradesh",
"district": "Nellore",
"city": "Nellore",
"climate": "Warm & humid",
"code": 802991
},
{
"state": "Andhra Pradesh",
"district": "Palnadu",
"city": "Chilakaluripet",
"climate": "Warm & humid",
"code": 802980
},
{
"state": "Andhra Pradesh",
"district": "Palnadu",
"city": "Dachepalli",
"climate": "Warm & humid",
"code": 900731
},
{
"state": "Andhra Pradesh",
"district": "Palnadu",
"city": "Gurajala",
"climate": "Warm & humid",
"code": 900723
},
{
"state": "Andhra Pradesh",
"district": "Palnadu",
"city": "Macherla",
"climate": "Warm & humid",
"code": 802973
},
{
"state": "Andhra Pradesh",
"district": "Palnadu",
"city": "Narasaraopet",
"climate": "Warm & humid",
"code": 802979
},
{
"state": "Andhra Pradesh",
"district": "Palnadu",
"city": "Piduguralla",
"climate": "Warm & humid",
"code": 802974
},
{
"state": "Andhra Pradesh",
"district": "Palnadu",
"city": "Sattenapalli",
"climate": "Warm & humid",
"code": 802977
},
{
"state": "Andhra Pradesh",
"district": "Palnadu",
"city": "Vinukonda",
"climate": "Warm & humid",
"code": 802978
},
{
"state": "Andhra Pradesh",
"district": "Prakasam",
"city": "Chimakurthy",
"climate": "Warm & humid",
"code": 900098
},
{
"state": "Andhra Pradesh",
"district": "Prakasam",
"city": "Chirala",
"climate": "Warm & humid",
"code": 802987
},
{
"state": "Andhra Pradesh",
"district": "Prakasam",
"city": "Darsi",
"climate": "Warm & humid",
"code": 900724
},
{
"state": "Andhra Pradesh",
"district": "Prakasam",
"city": "Giddaluru",
"climate": "Warm & humid",
"code": 900001
},
{
"state": "Andhra Pradesh",
"district": "Prakasam",
"city": "Kanigiri",
"climate": "Warm & humid",
"code": 900099
},
{
"state": "Andhra Pradesh",
"district": "Prakasam",
"city": "Markapur",
"climate": "Warm & humid",
"code": 802986
},
{
"state": "Andhra Pradesh",
"district": "Prakasam",
"city": "Ongole",
"climate": "Warm & humid",
"code": 802988
},
{
"state": "Andhra Pradesh",
"district": "Prakasam",
"city": "Podili",
"climate": "Warm & humid",
"code": 900854
},
{
"state": "Andhra Pradesh",
"district": "Sri Satyasai",
"city": "Hindupur",
"climate": "Warm & humid",
"code": 803012
},
{
"state": "Andhra Pradesh",
"district": "Sri Satyasai",
"city": "Madakasira",
"climate": "Warm & humid",
"code": 900093
},
{
"state": "Andhra Pradesh",
"district": "Sri Satyasai",
"city": "Penukonda",
"climate": "Warm & humid",
"code": 900729
},
{
"state": "Andhra Pradesh",
"district": "Sri Satyasai",
"city": "Puttaparthi",
"climate": "Warm & humid",
"code": 900092
},
{
"state": "Andhra Pradesh",
"district": "Srikakulam",
"city": "Amadalavalasa",
"climate": "Warm & humid",
"code": 802941
},
{
"state": "Andhra Pradesh",
"district": "Srikakulam",
"city": "Ichchapuram",
"climate": "Warm & humid",
"code": 802939
},
{
"state": "Andhra Pradesh",
"district": "Srikakulam",
"city": "Palasa Kasibugga",
"climate": "Warm & humid",
"code": 802938
},
{
"state": "Andhra Pradesh",
"district": "Srikakulam",
"city": "Srikakulam",
"climate": "Warm & humid",
"code": 802942
},
{
"state": "Andhra Pradesh",
"district": "Tirupati",
"city": "Gudur",
"climate": "Warm & humid",
"code": 802992
},
{
"state": "Andhra Pradesh",
"district": "Tirupati",
"city": "Naidupet",
"climate": "Warm & humid",
"code": 900101
},
{
"state": "Andhra Pradesh",
"district": "Tirupati",
"city": "Puttur",
"climate": "Warm & humid",
"code": 803017
},
{
"state": "Andhra Pradesh",
"district": "Tirupati",
"city": "Srikalahasti",
"climate": "Warm & humid",
"code": 803013
},
{
"state": "Andhra Pradesh",
"district": "Tirupati",
"city": "Sullurpet",
"climate": "Warm & humid",
"code": 900100
},
{
"state": "Andhra Pradesh",
"district": "Tirupati",
"city": "Tirupati",
"climate": "Warm & humid",
"code": 803014
},
{
"state": "Andhra Pradesh",
"district": "Tirupati",
"city": "Venkatagiri",
"climate": "Warm & humid",
"code": 802993
},
{
"state": "Andhra Pradesh",
"district": "Visakhapatnam",
"city": "Gvmc Visakhapatnam",
"climate": "Warm & humid",
"code": 802947
},
{
"state": "Andhra Pradesh",
"district": "Vizianagaram",
"city": "Bobbili",
"climate": "Warm & humid",
"code": 802944
},
{
"state": "Andhra Pradesh",
"district": "Vizianagaram",
"city": "Nellimarla",
"climate": "Warm & humid",
"code": 900148
},
{
"state": "Andhra Pradesh",
"district": "Vizianagaram",
"city": "Rajam",
"climate": "Warm & humid",
"code": 802940
},
{
"state": "Andhra Pradesh",
"district": "Vizianagaram",
"city": "Vizianagaram",
"climate": "Warm & humid",
"code": 802946
},
{
"state": "Andhra Pradesh",
"district": "West Godavari",
"city": "Akiveedu",
"climate": "Warm & humid",
"code": 900722
},
{
"state": "Andhra Pradesh",
"district": "West Godavari",
"city": "Bhimavaram",
"climate": "Warm & humid",
"code": 802964
},
{
"state": "Andhra Pradesh",
"district": "West Godavari",
"city": "Narasapur",
"climate": "Warm & humid",
"code": 802965
},
{
"state": "Andhra Pradesh",
"district": "West Godavari",
"city": "Palacole",
"climate": "Warm & humid",
"code": 802966
},
{
"state": "Andhra Pradesh",
"district": "West Godavari",
"city": "Tadepalligudem",
"climate": "Warm & humid",
"code": 802961
},
{
"state": "Andhra Pradesh",
"district": "West Godavari",
"city": "Tanuku",
"climate": "Warm & humid",
"code": 802963
},
{
"state": "Arunachal Pradesh",
"district": "Anjaw",
"city": "Hawai",
"climate": "Warm & humid",
"code": 801449
},
{
"state": "Arunachal Pradesh",
"district": "Anjaw",
"city": "Hayuliang",
"climate": "Warm & humid",
"code": 900828
},
{
"state": "Arunachal Pradesh",
"district": "Changlang",
"city": "Bordumsa",
"climate": "Warm & humid",
"code": 900826
},
{
"state": "Arunachal Pradesh",
"district": "Changlang",
"city": "Changlang",
"climate": "Warm & humid",
"code": 801437
},
{
"state": "Arunachal Pradesh",
"district": "Changlang",
"city": "Jairampur",
"climate": "Warm & humid",
"code": 801438
},
{
"state": "Arunachal Pradesh",
"district": "Changlang",
"city": "Kharsang",
"climate": "Warm & humid",
"code": 900830
},
{
"state": "Arunachal Pradesh",
"district": "Changlang",
"city": "Miao",
"climate": "Warm & humid",
"code": 801439
},
{
"state": "Arunachal Pradesh",
"district": "Dibang Valley",
"city": "Anini",
"climate": "Warm & humid",
"code": 801445
},
{
"state": "Arunachal Pradesh",
"district": "East Kameng",
"city": "Chyantajo",
"climate": "Warm & humid",
"code": 900827
},
{
"state": "Arunachal Pradesh",
"district": "East Kameng",
"city": "Seppa",
"climate": "Warm & humid",
"code": 801427
},
{
"state": "Arunachal Pradesh",
"district": "East Siang",
"city": "Boleng",
"climate": "Warm & humid",
"code": 801434
},
{
"state": "Arunachal Pradesh",
"district": "East Siang",
"city": "Kaying",
"climate": "Warm & humid",
"code": 900840
},
{
"state": "Arunachal Pradesh",
"district": "East Siang",
"city": "Pangin",
"climate": "Warm & humid",
"code": 900468
},
{
"state": "Arunachal Pradesh",
"district": "East Siang",
"city": "Pasighat",
"climate": "Warm & humid",
"code": 801435
},
{
"state": "Arunachal Pradesh",
"district": "East Siang",
"city": "Ruksin",
"climate": "Warm & humid",
"code": 900831
},
{
"state": "Arunachal Pradesh",
"district": "Karung Kumey",
"city": "Koloriang",
"climate": "Cold",
"code": 801444
},
{
"state": "Arunachal Pradesh",
"district": "Karung Kumey",
"city": "Sangram",
"climate": "Cold",
"code": 900833
},
{
"state": "Arunachal Pradesh",
"district": "Kra Dadi",
"city": "Palin",
"climate": "Cold",
"code": 900464
},
{
"state": "Arunachal Pradesh",
"district": "Lohit",
"city": "Namsai",
"climate": "Warm & humid",
"code": 801448
},
{
"state": "Arunachal Pradesh",
"district": "Lohit",
"city": "Tezu",
"climate": "Warm & humid",
"code": 801447
},
{
"state": "Arunachal Pradesh",
"district": "Longding",
"city": "Kanubari",
"climate": "Warm & humid"
},
{
"state": "Arunachal Pradesh",
"district": "Longding",
"city": "Longding",
"climate": "Warm & humid",
"code": 801442
},
{
"state": "Arunachal Pradesh",
"district": "Lower Dibang Valley",
"city": "Roing",
"climate": "Warm & humid",
"code": 801446
},
{
"state": "Arunachal Pradesh",
"district": "Lower Subansari",
"city": "Raga",
"climate": "Warm & humid",
"code": 900465
},
{
"state": "Arunachal Pradesh",
"district": "Lower Subansari",
"city": "Yachuli",
"climate": "Warm & humid",
"code": 900834
},
{
"state": "Arunachal Pradesh",
"district": "Lower Subansari",
"city": "Ziro",
"climate": "Warm & humid",
"code": 801443
},
{
"state": "Arunachal Pradesh",
"district": "Pakke Kesan",
"city": "Lemmi",
"climate": "Warm & humid",
"code": 900835
},
{
"state": "Arunachal Pradesh",
"district": "Papum Pare",
"city": "Doimukh",
"climate": "Warm & humid",
"code": 900462
},
{
"state": "Arunachal Pradesh",
"district": "Papum Pare",
"city": "Itanagar",
"climate": "Warm & humid",
"code": 801428
},
{
"state": "Arunachal Pradesh",
"district": "Papum Pare",
"city": "Kimin",
"climate": "Warm & humid",
"code": 900463
},
{
"state": "Arunachal Pradesh",
"district": "Papum Pare",
"city": "Naharlagun",
"climate": "Warm & humid",
"code": 801429
},
{
"state": "Arunachal Pradesh",
"district": "Papum Pare",
"city": "Sagalee",
"climate": "Warm & humid",
"code": 801430
},
{
"state": "Arunachal Pradesh",
"district": "Shi Yomi",
"city": "Mechuka",
"climate": "Cold",
"code": 900837
},
{
"state": "Arunachal Pradesh",
"district": "Shi Yomi",
"city": "Tato",
"climate": "Cold",
"code": 900836
},
{
"state": "Arunachal Pradesh",
"district": "Tawang",
"city": "Tawang",
"climate": "Cold",
"code": 801424
},
{
"state": "Arunachal Pradesh",
"district": "Tirap",
"city": "Deomali",
"climate": "Warm & humid",
"code": 801440
},
{
"state": "Arunachal Pradesh",
"district": "Tirap",
"city": "Khonsa",
"climate": "Warm & humid",
"code": 801441
},
{
"state": "Arunachal Pradesh",
"district": "Upper Siang",
"city": "Mariyang",
"climate": "Cold",
"code": 900467
},
{
"state": "Arunachal Pradesh",
"district": "Upper Siang",
"city": "Yingkiong",
"climate": "Cold",
"code": 801436
},
{
"state": "Arunachal Pradesh",
"district": "Upper Subansiri",
"city": "Daporijo",
"climate": "Cold",
"code": 801431
},
{
"state": "Arunachal Pradesh",
"district": "Upper Subansiri",
"city": "Dumporijo",
"climate": "Cold",
"code": 900466
},
{
"state": "Arunachal Pradesh",
"district": "West Kameng",
"city": "Bomdila",
"climate": "Cold",
"code": 801426
},
{
"state": "Arunachal Pradesh",
"district": "West Kameng",
"city": "Dirang",
"climate": "Cold",
"code": 801425
},
{
"state": "Arunachal Pradesh",
"district": "West Kameng",
"city": "Kalaktang",
"climate": "Cold",
"code": 900829
},
{
"state": "Arunachal Pradesh",
"district": "West Kameng",
"city": "Rupa",
"climate": "Cold",
"code": 900832
},
{
"state": "Arunachal Pradesh",
"district": "West Siang",
"city": "Aalo",
"climate": "Cold",
"code": 801432
},
{
"state": "Arunachal Pradesh",
"district": "West Siang",
"city": "Basar",
"climate": "Cold",
"code": 801433
},
{
"state": "Assam",
"district": "Baksa",
"city": "Goreswar",
"climate": "Warm & humid",
"code": 900324
},
{
"state": "Assam",
"district": "Barpeta",
"city": "Barpeta",
"climate": "Warm & humid",
"code": 801557
},
{
"state": "Assam",
"district": "Barpeta",
"city": "Barpeta Road",
"climate": "Warm & humid",
"code": 801555
},
{
"state": "Assam",
"district": "Barpeta",
"city": "Howli",
"climate": "Warm & humid",
"code": 801558
},
{
"state": "Assam",
"district": "Barpeta",
"city": "Patacharkuchi",
"climate": "Warm & humid",
"code": 900073
},
{
"state": "Assam",
"district": "Barpeta",
"city": "Pathsala",
"climate": "Warm & humid",
"code": 801560
},
{
"state": "Assam",
"district": "Barpeta",
"city": "Sarbhog",
"climate": "Warm & humid",
"code": 801556
},
{
"state": "Assam",
"district": "Barpeta",
"city": "Sarthebari",
"climate": "Warm & humid",
"code": 801559
},
{
"state": "Assam",
"district": "Bongaigaon",
"city": "Abhayapuri",
"climate": "Warm & humid",
"code": 801621
},
{
"state": "Assam",
"district": "Bongaigaon",
"city": "Bongaigaon",
"climate": "Warm & humid",
"code": 801620
},
{
"state": "Assam",
"district": "Bongaigaon",
"city": "Kajalgaon",
"climate": "Warm & humid",
"code": 900126
},
{
"state": "Assam",
"district": "Cachar",
"city": "Lakhipur",
"climate": "Warm & humid",
"code": 801615
},
{
"state": "Assam",
"district": "Cachar",
"city": "Silchar",
"climate": "Warm & humid",
"code": 801614
},
{
"state": "Assam",
"district": "Cachar",
"city": "Sonai Tc",
"climate": "Warm & humid",
"code": 900323
},
{
"state": "Assam",
"district": "Darrang",
"city": "Kharupatia",
"climate": "Cold",
"code": 801631
},
{
"state": "Assam",
"district": "Darrang",
"city": "Mangaldoi",
"climate": "Cold",
"code": 801630
},
{
"state": "Assam",
"district": "Dhemaji",
"city": "Dhemaji",
"climate": "Warm & humid",
"code": 801579
},
{
"state": "Assam",
"district": "Dhemaji",
"city": "Silapathar",
"climate": "Warm & humid",
"code": 801580
},
{
"state": "Assam",
"district": "Dhubri",
"city": "Bilasipara",
"climate": "Warm & humid",
"code": 801551
},
{
"state": "Assam",
"district": "Dhubri",
"city": "Chapar",
"climate": "Warm & humid",
"code": 801552
},
{
"state": "Assam",
"district": "Dhubri",
"city": "Dhubri",
"climate": "Warm & humid",
"code": 801549
},
{
"state": "Assam",
"district": "Dhubri",
"city": "Gauripur",
"climate": "Warm & humid",
"code": 801548
},
{
"state": "Assam",
"district": "Dhubri",
"city": "Sapatgram",
"climate": "Warm & humid",
"code": 801550
},
{
"state": "Assam",
"district": "Dibrugarh",
"city": "Chabua",
"climate": "Warm & humid",
"code": 801587
},
{
"state": "Assam",
"district": "Dibrugarh",
"city": "Dibrugarh",
"climate": "Warm & humid",
"code": 801586
},
{
"state": "Assam",
"district": "Dibrugarh",
"city": "Naharkatiya",
"climate": "Warm & humid",
"code": 801588
},
{
"state": "Assam",
"district": "Dibrugarh",
"city": "Namrup",
"climate": "Warm & humid",
"code": 900008
},
{
"state": "Assam",
"district": "Dima Hasao",
"city": "Haflong",
"climate": "Warm & humid",
"code": 801611
},
{
"state": "Assam",
"district": "Dima Hasao",
"city": "Mahur",
"climate": "Warm & humid",
"code": 801612
},
{
"state": "Assam",
"district": "Dima Hasao",
"city": "Maibong",
"climate": "Warm & humid",
"code": 801613
},
{
"state": "Assam",
"district": "Dima Hasao",
"city": "Umrangso",
"climate": "Warm & humid",
"code": 801610
},
{
"state": "Assam",
"district": "Goalpara",
"city": "Goalpara",
"climate": "Warm & humid",
"code": 801554
},
{
"state": "Assam",
"district": "Goalpara",
"city": "Lakhipur",
"climate": "Warm & humid",
"code": 801553
},
{
"state": "Assam",
"district": "Golaghat",
"city": "Barpathar",
"climate": "Warm & humid",
"code": 801603
},
{
"state": "Assam",
"district": "Golaghat",
"city": "Bokakhat",
"climate": "Warm & humid",
"code": 801599
},
{
"state": "Assam",
"district": "Golaghat",
"city": "Dergaon",
"climate": "Warm & humid",
"code": 801600
},
{
"state": "Assam",
"district": "Golaghat",
"city": "Golaghat",
"climate": "Warm & humid",
"code": 801601
},
{
"state": "Assam",
"district": "Golaghat",
"city": "Sarupathar",
"climate": "Warm & humid",
"code": 801602
},
{
"state": "Assam",
"district": "Hailakandi",
"city": "Hailakandi",
"climate": "Warm & humid",
"code": 801618
},
{
"state": "Assam",
"district": "Hailakandi",
"city": "Lala",
"climate": "Warm & humid",
"code": 801619
},
{
"state": "Assam",
"district": "Jorhat",
"city": "Jorhat",
"climate": "Warm & humid",
"code": 801595
},
{
"state": "Assam",
"district": "Jorhat",
"city": "Mariani",
"climate": "Warm & humid",
"code": 801598
},
{
"state": "Assam",
"district": "Jorhat",
"city": "Teok",
"climate": "Warm & humid",
"code": 801596
},
{
"state": "Assam",
"district": "Jorhat",
"city": "Titabor Town",
"climate": "Warm & humid",
"code": 801597
},
{
"state": "Assam",
"district": "Kamrup",
"city": "Guwahati",
"climate": "Warm & humid",
"code": 801627
},
{
"state": "Assam",
"district": "Kamrup",
"city": "North Guwahati",
"climate": "Warm & humid",
"code": 801626
},
{
"state": "Assam",
"district": "Kamrup",
"city": "Palasbari",
"climate": "Warm & humid",
"code": 801625
},
{
"state": "Assam",
"district": "Kamrup",
"city": "Rangia",
"climate": "Warm & humid",
"code": 801624
},
{
"state": "Assam",
"district": "Karbi Anlong",
"city": "Bakalia",
"climate": "Warm & humid",
"code": 900075
},
{
"state": "Assam",
"district": "Karbi Anlong",
"city": "Bokajan",
"climate": "Warm & humid",
"code": 801607
},
{
"state": "Assam",
"district": "Karbi Anlong",
"city": "Diphu",
"climate": "Warm & humid",
"code": 801606
},
{
"state": "Assam",
"district": "Karbi Anlong",
"city": "Dokmoka",
"climate": "Warm & humid",
"code": 801609
},
{
"state": "Assam",
"district": "Karbi Anlong",
"city": "Donkamokam",
"climate": "Warm & humid",
"code": 801605
},
{
"state": "Assam",
"district": "Karbi Anlong",
"city": "Hamren",
"climate": "Warm & humid",
"code": 801604
},
{
"state": "Assam",
"district": "Karbi Anlong",
"city": "Howraghat",
"climate": "Warm & humid",
"code": 801608
},
{
"state": "Assam",
"district": "Karimganj",
"city": "Badarpur",
"climate": "Warm & humid",
"code": 801617
},
{
"state": "Assam",
"district": "Karimganj",
"city": "Karimganj",
"climate": "Warm & humid",
"code": 801616
},
{
"state": "Assam",
"district": "Kokrajhar",
"city": "Gossaigaon",
"climate": "Warm & humid",
"code": 801546
},
{
"state": "Assam",
"district": "Kokrajhar",
"city": "Kokrajhar",
"climate": "Warm & humid",
"code": 801547
},
{
"state": "Assam",
"district": "Marigaon",
"city": "Marigaon",
"climate": "Cold",
"code": 801561
},
{
"state": "Assam",
"district": "Nagaon",
"city": "Dhing",
"climate": "Warm & humid",
"code": 801562
},
{
"state": "Assam",
"district": "Nagaon",
"city": "Doboka",
"climate": "Warm & humid",
"code": 801567
},
{
"state": "Assam",
"district": "Nagaon",
"city": "Hojai",
"climate": "Warm & humid",
"code": 801566
},
{
"state": "Assam",
"district": "Nagaon",
"city": "Kampur Town",
"climate": "Warm & humid",
"code": 801565
},
{
"state": "Assam",
"district": "Nagaon",
"city": "Lanka",
"climate": "Warm & humid",
"code": 801569
},
{
"state": "Assam",
"district": "Nagaon",
"city": "Lumding",
"climate": "Warm & humid",
"code": 801568
},
{
"state": "Assam",
"district": "Nagaon",
"city": "Nagaon",
"climate": "Warm & humid",
"code": 801563
},
{
"state": "Assam",
"district": "Nagaon",
"city": "Raha",
"climate": "Warm & humid",
"code": 801564
},
{
"state": "Assam",
"district": "Nalbari",
"city": "Nalbari",
"climate": "Warm & humid",
"code": 801629
},
{
"state": "Assam",
"district": "Nalbari",
"city": "Tihu",
"climate": "Warm & humid",
"code": 801628
},
{
"state": "Assam",
"district": "North Lakhimpur",
"city": "Bihpuria",
"climate": "Warm & humid",
"code": 801576
},
{
"state": "Assam",
"district": "North Lakhimpur",
"city": "Dhakuakhana",
"climate": "Warm & humid",
"code": 801578
},
{
"state": "Assam",
"district": "North Lakhimpur",
"city": "Narayanpur",
"climate": "Warm & humid",
"code": 801575
},
{
"state": "Assam",
"district": "North Lakhimpur",
"city": "North Lakhimpur",
"climate": "Warm & humid",
"code": 801577
},
{
"state": "Assam",
"district": "Sibsagar",
"city": "Amguri",
"climate": "Warm & humid",
"code": 801590
},
{
"state": "Assam",
"district": "Sibsagar",
"city": "Demow",
"climate": "Warm & humid",
"code": 900007
},
{
"state": "Assam",
"district": "Sibsagar",
"city": "Moranhat",
"climate": "Warm & humid",
"code": 801594
},
{
"state": "Assam",
"district": "Sibsagar",
"city": "Nazira",
"climate": "Warm & humid",
"code": 801591
},
{
"state": "Assam",
"district": "Sibsagar",
"city": "Sibsagar",
"climate": "Warm & humid",
"code": 801589
},
{
"state": "Assam",
"district": "Sibsagar",
"city": "Simaluguri",
"climate": "Warm & humid",
"code": 801592
},
{
"state": "Assam",
"district": "Sibsagar",
"city": "Sonari",
"climate": "Warm & humid",
"code": 801593
},
{
"state": "Assam",
"district": "Sonitpur",
"city": "Biswanath Chariali",
"climate": "Warm & humid",
"code": 801573
},
{
"state": "Assam",
"district": "Sonitpur",
"city": "Dhekiajuli",
"climate": "Warm & humid",
"code": 801570
},
{
"state": "Assam",
"district": "Sonitpur",
"city": "Gohpur",
"climate": "Warm & humid",
"code": 801574
},
{
"state": "Assam",
"district": "Sonitpur",
"city": "Rangapara",
"climate": "Warm & humid",
"code": 801571
},
{
"state": "Assam",
"district": "Sonitpur",
"city": "Tezpur",
"climate": "Warm & humid",
"code": 801572
},
{
"state": "Assam",
"district": "Tinsukia",
"city": "Chapakhowa",
"climate": "Warm & humid",
"code": 900074
},
{
"state": "Assam",
"district": "Tinsukia",
"city": "Digboi",
"climate": "Warm & humid",
"code": 801584
},
{
"state": "Assam",
"district": "Tinsukia",
"city": "Doom Dooma",
"climate": "Warm & humid",
"code": 801581
},
{
"state": "Assam",
"district": "Tinsukia",
"city": "Makum",
"climate": "Warm & humid",
"code": 801582
},
{
"state": "Assam",
"district": "Tinsukia",
"city": "Margherita",
"climate": "Warm & humid",
"code": 801585
},
{
"state": "Assam",
"district": "Tinsukia",
"city": "Tinsukia",
"climate": "Warm & humid",
"code": 801583
},
{
"state": "Assam",
"district": "Udalguri",
"city": "Basugaon",
"climate": "Warm & humid",
"code": 801622
},
{
"state": "Assam",
"district": "Udalguri",
"city": "Bijni",
"climate": "Warm & humid",
"code": 801623
},
{
"state": "Assam",
"district": "Udalguri",
"city": "Tangla",
"climate": "Warm & humid",
"code": 801632
},
{
"state": "Assam",
"district": "Udalguri",
"city": "Udalguri",
"climate": "Warm & humid",
"code": 801633
},
{
"state": "Bihar",
"district": "Araria",
"city": "Araria",
"climate": "Warm & humid",
"code": 801307
},
{
"state": "Bihar",
"district": "Araria",
"city": "Forbesganj",
"climate": "Warm & humid",
"code": 801306
},
{
"state": "Bihar",
"district": "Araria",
"city": "Jogabani",
"climate": "Warm & humid",
"code": 801305
},
{
"state": "Bihar",
"district": "Araria",
"city": "Jokihaat Nagar Panchayat",
"climate": "Warm & humid",
"code": 900869
},
{
"state": "Bihar",
"district": "Araria",
"city": "Narpatganj Nagar Panchayat",
"climate": "Warm & humid",
"code": 900870
},
{
"state": "Bihar",
"district": "Araria",
"city": "Raniganj Nagar Panchayat",
"climate": "Warm & humid",
"code": 900871
},
{
"state": "Bihar",
"district": "Arwal",
"city": "Arwal",
"climate": "Composite",
"code": 801415
},
{
"state": "Bihar",
"district": "Arwal",
"city": "Kurtha Nagar Panchayat",
"climate": "Composite",
"code": 900872
},
{
"state": "Bihar",
"district": "Aurangabad",
"city": "Aurangabad",
"climate": "Composite",
"code": 801401
},
{
"state": "Bihar",
"district": "Aurangabad",
"city": "Barun Nagar Panchayat",
"climate": "Composite",
"code": 900873
},
{
"state": "Bihar",
"district": "Aurangabad",
"city": "Daudnagar",
"climate": "Composite",
"code": 801399
},
{
"state": "Bihar",
"district": "Aurangabad",
"city": "Dev Nagar Panchayat",
"climate": "Composite",
"code": 900874
},
{
"state": "Bihar",
"district": "Aurangabad",
"city": "Nabinagar",
"climate": "Composite",
"code": 801402
},
{
"state": "Bihar",
"district": "Aurangabad",
"city": "Rafiganj",
"climate": "Composite",
"code": 801400
},
{
"state": "Bihar",
"district": "Banka",
"city": "Amarpur",
"climate": "Composite",
"code": 801355
},
{
"state": "Bihar",
"district": "Banka",
"city": "Banka",
"climate": "Composite",
"code": 801356
},
{
"state": "Bihar",
"district": "Banka",
"city": "Katoria Nagar Panchayat",
"climate": "Composite",
"code": 900875
},
{
"state": "Bihar",
"district": "Banka",
"city": "baunsi",
"climate": "Composite"
},
{
"state": "Bihar",
"district": "Begusarai",
"city": "Bakhri",
"climate": "Composite",
"code": 801347
},
{
"state": "Bihar",
"district": "Begusarai",
"city": "Balia",
"climate": "Composite",
"code": 801348
},
{
"state": "Bihar",
"district": "Begusarai",
"city": "Begusarai",
"climate": "Composite",
"code": 801346
},
{
"state": "Bihar",
"district": "Begusarai",
"city": "Bihat",
"climate": "Composite",
"code": 801345
},
{
"state": "Bihar",
"district": "Begusarai",
"city": "Teghra",
"climate": "Composite",
"code": 801344
},
{
"state": "Bihar",
"district": "Begusarai",
"city": "barauni",
"climate": "Composite"
},
{
"state": "Bihar",
"district": "Bhagalpur",
"city": "Akbarnagar Nagar Panchayat",
"climate": "Warm & humid",
"code": 900876
},
{
"state": "Bihar",
"district": "Bhagalpur",
"city": "Bhagalpur",
"climate": "Warm & humid",
"code": 801354
},
{
"state": "Bihar",
"district": "Bhagalpur",
"city": "Habibpur Nagar Panchayat",
"climate": "Warm & humid",
"code": 900877
},
{
"state": "Bihar",
"district": "Bhagalpur",
"city": "Kahalgaon",
"climate": "Warm & humid",
"code": 900096
},
{
"state": "Bihar",
"district": "Bhagalpur",
"city": "Naugachhia",
"climate": "Warm & humid",
"code": 801351
},
{
"state": "Bihar",
"district": "Bhagalpur",
"city": "Pirpainti Nagar Panchayat",
"climate": "Warm & humid",
"code": 900878
},
{
"state": "Bihar",
"district": "Bhagalpur",
"city": "Sabour Nagar Panchayat",
"climate": "Warm & humid",
"code": 900879
},
{
"state": "Bihar",
"district": "Bhagalpur",
"city": "Sultanganj",
"climate": "Warm & humid",
"code": 801353
},
{
"state": "Bihar",
"district": "Bhojpur",
"city": "Ara",
"climate": "Composite",
"code": 801385
},
{
"state": "Bihar",
"district": "Bhojpur",
"city": "Behea",
"climate": "Composite",
"code": 801387
},
{
"state": "Bihar",
"district": "Bhojpur",
"city": "Gadhani",
"climate": "Composite"
},
{
"state": "Bihar",
"district": "Bhojpur",
"city": "Garhani Nagar Panchayat",
"climate": "Composite",
"code": 900880
},
{
"state": "Bihar",
"district": "Bhojpur",
"city": "Jagdishpur",
"climate": "Composite",
"code": 801388
},
{
"state": "Bihar",
"district": "Bhojpur",
"city": "Koilwar",
"climate": "Composite",
"code": 801386
},
{
"state": "Bihar",
"district": "Bhojpur",
"city": "Piro",
"climate": "Composite",
"code": 801389
},
{
"state": "Bihar",
"district": "Bhojpur",
"city": "Shahpur",
"climate": "Composite",
"code": 801384
},
{
"state": "Bihar",
"district": "Bhojpur",
"city": "bihiyan",
"climate": "Composite"
},
{
"state": "Bihar",
"district": "Buxar",
"city": "Buxar",
"climate": "Composite",
"code": 801391
},
{
"state": "Bihar",
"district": "Buxar",
"city": "Chausa",
"climate": "Composite"
},
{
"state": "Bihar",
"district": "Buxar",
"city": "Dumraon",
"climate": "Composite",
"code": 801390
},
{
"state": "Bihar",
"district": "Buxar",
"city": "Itarhi",
"climate": "Composite"
},
{
"state": "Bihar",
"district": "Darbhanga",
"city": "Baheri Nagar Panchayat",
"climate": "Warm & humid",
"code": 900881
},
{
"state": "Bihar",
"district": "Darbhanga",
"city": "Benipur",
"climate": "Warm & humid",
"code": 801320
},
{
"state": "Bihar",
"district": "Darbhanga",
"city": "Bharwada",
"climate": "Warm & humid"
},
{
"state": "Bihar",
"district": "Darbhanga",
"city": "Bharwara Nagar Panchayat",
"climate": "Warm & humid",
"code": 900882
},
{
"state": "Bihar",
"district": "Darbhanga",
"city": "Biraul Nagar Panchayat",
"climate": "Warm & humid",
"code": 900883
},
{
"state": "Bihar",
"district": "Darbhanga",
"city": "Darbhanga",
"climate": "Warm & humid",
"code": 801319
},
{
"state": "Bihar",
"district": "Darbhanga",
"city": "Ghanshyampur Nagar Panchayat",
"climate": "Warm & humid",
"code": 900884
},
{
"state": "Bihar",
"district": "Darbhanga",
"city": "Hayaghat Nagar Panchayat",
"climate": "Warm & humid",
"code": 900885
},
{
"state": "Bihar",
"district": "Darbhanga",
"city": "Jale Nagar Parishad",
"climate": "Warm & humid",
"code": 900886
},
{
"state": "Bihar",
"district": "Darbhanga",
"city": "Kamtaul Nagar Panchayat",
"climate": "Warm & humid",
"code": 900887
},
{
"state": "Bihar",
"district": "Darbhanga",
"city": "Kusheshwarsthan Purvi Nagar Panchayat",
"climate": "Warm & humid",
"code": 900888
},
{
"state": "Bihar",
"district": "Darbhanga",
"city": "Singhwara Nagar Panchayat",
"climate": "Warm & humid",
"code": 900889
},
{
"state": "Bihar",
"district": "Gaya",
"city": "Bodh Gaya",
"climate": "Composite",
"code": 801406
},
{
"state": "Bihar",
"district": "Gaya",
"city": "Dobhi Nagar Panchayat",
"climate": "Composite",
"code": 900890
},
{
"state": "Bihar",
"district": "Gaya",
"city": "Fatehpur Nagar Panchayat",
"climate": "Composite",
"code": 900891
},
{
"state": "Bihar",
"district": "Gaya",
"city": "Gaya",
"climate": "Composite",
"code": 801404
},
{
"state": "Bihar",
"district": "Gaya",
"city": "Imamganj Nagar Panchayat",
"climate": "Composite",
"code": 900892
},
{
"state": "Bihar",
"district": "Gaya",
"city": "Khizarsarai Nagar Panchayat",
"climate": "Composite",
"code": 900893
},
{
"state": "Bihar",
"district": "Gaya",
"city": "Sherghati",
"climate": "Composite",
"code": 801405
},
{
"state": "Bihar",
"district": "Gaya",
"city": "Tikari",
"climate": "Composite",
"code": 801403
},
{
"state": "Bihar",
"district": "Gaya",
"city": "Wazirganj Nagar Panchayat",
"climate": "Composite",
"code": 900894
},
{
"state": "Bihar",
"district": "Gopalganj",
"city": "Barauli",
"climate": "Composite",
"code": 801328
},
{
"state": "Bihar",
"district": "Gopalganj",
"city": "Gopalganj",
"climate": "Composite",
"code": 801327
},
{
"state": "Bihar",
"district": "Gopalganj",
"city": "Hathua Nagar Panchayat",
"climate": "Composite",
"code": 900895
},
{
"state": "Bihar",
"district": "Gopalganj",
"city": "Kataiya",
"climate": "Composite",
"code": 801325
},
{
"state": "Bihar",
"district": "Gopalganj",
"city": "Mirganj",
"climate": "Composite",
"code": 801326
},
{
"state": "Bihar",
"district": "Jahanabad",
"city": "Jehanabad",
"climate": "Composite",
"code": 801413
},
{
"state": "Bihar",
"district": "Jahanabad",
"city": "Kako Nagar Panchayat",
"climate": "Composite",
"code": 900897
},
{
"state": "Bihar",
"district": "Jahanabad",
"city": "Makhdumpur",
"climate": "Composite",
"code": 801414
},
{
"state": "Bihar",
"district": "Jahanabad",
"city": "ghoshi",
"climate": "Composite"
},
{
"state": "Bihar",
"district": "Jamui",
"city": "Jamui",
"climate": "Composite",
"code": 801411
},
{
"state": "Bihar",
"district": "Jamui",
"city": "Jhajha",
"climate": "Composite",
"code": 801412
},
{
"state": "Bihar",
"district": "Jamui",
"city": "Sikandra Nagar Panchayat",
"climate": "Composite",
"code": 900896
},
{
"state": "Bihar",
"district": "Kaimur(Bhabua)",
"city": "Bhabua",
"climate": "Composite",
"code": 801392
},
{
"state": "Bihar",
"district": "Kaimur(Bhabua)",
"city": "Hata Nagar Panchayat",
"climate": "Composite",
"code": 900898
},
{
"state": "Bihar",
"district": "Kaimur(Bhabua)",
"city": "Kudra Nagar Panchayat",
"climate": "Composite",
"code": 900899
},
{
"state": "Bihar",
"district": "Kaimur(Bhabua)",
"city": "Mohania",
"climate": "Composite",
"code": 900097
},
{
"state": "Bihar",
"district": "Kaimur(Bhabua)",
"city": "Ramgarh Nagar Panchayat",
"climate": "Composite",
"code": 900900
},
{
"state": "Bihar",
"district": "Katihar",
"city": "Amdabad Nagar Panchayat",
"climate": "Warm & humid",
"code": 900901
},
{
"state": "Bihar",
"district": "Katihar",
"city": "Balrampur Nagar Panchayat",
"climate": "Warm & humid",
"code": 900902
},
{
"state": "Bihar",
"district": "Katihar",
"city": "Barari Nagar Panchayat",
"climate": "Warm & humid",
"code": 900903
},
{
"state": "Bihar",
"district": "Katihar",
"city": "Barsoi",
"climate": "Warm & humid",
"code": 900501
},
{
"state": "Bihar",
"district": "Katihar",
"city": "Katihar",
"climate": "Warm & humid",
"code": 801314
},
{
"state": "Bihar",
"district": "Katihar",
"city": "Korha Nagar Panchayat",
"climate": "Warm & humid",
"code": 900904
},
{
"state": "Bihar",
"district": "Katihar",
"city": "Kursela Nagar Panchayat",
"climate": "Warm & humid",
"code": 900905
},
{
"state": "Bihar",
"district": "Katihar",
"city": "Manihari",
"climate": "Warm & humid",
"code": 801315
},
{
"state": "Bihar",
"district": "Katihar",
"city": "kodha",
"climate": "Warm & humid"
},
{
"state": "Bihar",
"district": "Khagariya",
"city": "Alauli Nagar Panchayat",
"climate": "Composite",
"code": 900906
},
{
"state": "Bihar",
"district": "Khagariya",
"city": "Beldaur Nagar Panchayat",
"climate": "Composite",
"code": 900907
},
{
"state": "Bihar",
"district": "Khagariya",
"city": "Gogri Jamalpur",
"climate": "Composite",
"code": 801350
},
{
"state": "Bihar",
"district": "Khagariya",
"city": "Khagaria",
"climate": "Composite",
"code": 801349
},
{
"state": "Bihar",
"district": "Khagariya",
"city": "Mansi Nagar Panchayat",
"climate": "Composite",
"code": 900908
},
{
"state": "Bihar",
"district": "Khagariya",
"city": "Parbatta Nagar Panchayat",
"climate": "Composite",
"code": 900909
},
{
"state": "Bihar",
"district": "Kishanganj",
"city": "Bahadurganj",
"climate": "Warm & humid",
"code": 801309
},
{
"state": "Bihar",
"district": "Kishanganj",
"city": "Kishanganj",
"climate": "Warm & humid",
"code": 801310
},
{
"state": "Bihar",
"district": "Kishanganj",
"city": "Pauwakhali Nagar Panchayat",
"climate": "Warm & humid",
"code": 900910
},
{
"state": "Bihar",
"district": "Kishanganj",
"city": "Thakurganj",
"climate": "Warm & humid",
"code": 801308
},
{
"state": "Bihar",
"district": "Lakhisarai",
"city": "Barahiya",
"climate": "Composite",
"code": 801360
},
{
"state": "Bihar",
"district": "Lakhisarai",
"city": "Lakhisarai",
"climate": "Composite",
"code": 801361
},
{
"state": "Bihar",
"district": "Lakhisarai",
"city": "Suryagadha Nagar Parishad",
"climate": "Composite",
"code": 900911
},
{
"state": "Bihar",
"district": "Madhepura",
"city": "Aalamnagar Nagar Panchayat",
"climate": "Warm & humid",
"code": 900912
},
{
"state": "Bihar",
"district": "Madhepura",
"city": "Bihariganj Nagar Panchayat",
"climate": "Warm & humid",
"code": 900913
},
{
"state": "Bihar",
"district": "Madhepura",
"city": "Madhepura",
"climate": "Warm & humid",
"code": 801316
},
{
"state": "Bihar",
"district": "Madhepura",
"city": "Murliganj",
"climate": "Warm & humid",
"code": 801317
},
{
"state": "Bihar",
"district": "Madhepura",
"city": "Singeshwar Nagar Panchayat",
"climate": "Warm & humid",
"code": 900914
},
{
"state": "Bihar",
"district": "Madhepura",
"city": "Sinheshwar",
"climate": "Warm & humid"
},
{
"state": "Bihar",
"district": "Madhepura",
"city": "Udakishanganj Nagar Parishad",
"climate": "Warm & humid",
"code": 900915
},
{
"state": "Bihar",
"district": "Madhubani",
"city": "Benipatti Nagar Panchayat",
"climate": "Warm & humid",
"code": 900916
},
{
"state": "Bihar",
"district": "Madhubani",
"city": "Ghoghardiha",
"climate": "Warm & humid",
"code": 801301
},
{
"state": "Bihar",
"district": "Madhubani",
"city": "Jainagar",
"climate": "Warm & humid",
"code": 801298
},
{
"state": "Bihar",
"district": "Madhubani",
"city": "Jhanjharpur",
"climate": "Warm & humid",
"code": 801300
},
{
"state": "Bihar",
"district": "Madhubani",
"city": "Madhubani",
"climate": "Warm & humid",
"code": 801299
},
{
"state": "Bihar",
"district": "Madhubani",
"city": "Phulparas Nagar Panchayat",
"climate": "Warm & humid",
"code": 900917
},
{
"state": "Bihar",
"district": "Munger",
"city": "Asarganj",
"climate": "Composite"
},
{
"state": "Bihar",
"district": "Munger",
"city": "Haweli Kharagpur",
"climate": "Composite"
},
{
"state": "Bihar",
"district": "Munger",
"city": "Jamalpur",
"climate": "Composite",
"code": 801358
},
{
"state": "Bihar",
"district": "Munger",
"city": "Kharagpur",
"climate": "Composite",
"code": 801359
},
{
"state": "Bihar",
"district": "Munger",
"city": "Munger",
"climate": "Composite",
"code": 801357
},
{
"state": "Bihar",
"district": "Munger",
"city": "Sangrampur",
"climate": "Composite"
},
{
"state": "Bihar",
"district": "Munger",
"city": "Tarapur Nagar Panchayat",
"climate": "Composite",
"code": 900918
},
{
"state": "Bihar",
"district": "Muzaffarpur",
"city": "Baruraj",
"climate": "Composite"
},
{
"state": "Bihar",
"district": "Muzaffarpur",
"city": "Goraul",
"climate": "Composite"
},
{
"state": "Bihar",
"district": "Muzaffarpur",
"city": "Kanti",
"climate": "Composite",
"code": 801323
},
{
"state": "Bihar",
"district": "Muzaffarpur",
"city": "Kurahni Nagar Panchayat",
"climate": "Composite",
"code": 900919
},
{
"state": "Bihar",
"district": "Muzaffarpur",
"city": "Macharganwa",
"climate": "Composite"
},
{
"state": "Bihar",
"district": "Muzaffarpur",
"city": "Madhopursusta",
"climate": "Composite"
},
{
"state": "Bihar",
"district": "Muzaffarpur",
"city": "Meenapur Nagar Panchayat",
"climate": "Composite",
"code": 900920
},
{
"state": "Bihar",
"district": "Muzaffarpur",
"city": "Motipur",
"climate": "Composite",
"code": 801322
},
{
"state": "Bihar",
"district": "Muzaffarpur",
"city": "Muraul",
"climate": "Composite"
},
{
"state": "Bihar",
"district": "Muzaffarpur",
"city": "Muzaffarpur",
"climate": "Composite",
"code": 801324
},
{
"state": "Bihar",
"district": "Muzaffarpur",
"city": "Sahebganj",
"climate": "Composite",
"code": 801321
},
{
"state": "Bihar",
"district": "Muzaffarpur",
"city": "Sakra Nagar Panchayat",
"climate": "Composite",
"code": 900921
},
{
"state": "Bihar",
"district": "Muzaffarpur",
"city": "Saraiya Nagar Panchayat",
"climate": "Composite",
"code": 900922
},
{
"state": "Bihar",
"district": "Nalanda",
"city": "Asthawan Nagar Panchayat",
"climate": "Composite",
"code": 900923
},
{
"state": "Bihar",
"district": "Nalanda",
"city": "Biharsharif",
"climate": "Composite",
"code": 801364
},
{
"state": "Bihar",
"district": "Nalanda",
"city": "Chandi Nagar Panchayat",
"climate": "Composite",
"code": 900924
},
{
"state": "Bihar",
"district": "Nalanda",
"city": "Ekangarsarai Nagar Panchayat",
"climate": "Composite",
"code": 900925
},
{
"state": "Bihar",
"district": "Nalanda",
"city": "Giriyak Nagar Panchayat",
"climate": "Composite",
"code": 900926
},
{
"state": "Bihar",
"district": "Nalanda",
"city": "Harnaut Nagar Panchayat",
"climate": "Composite",
"code": 900927
},
{
"state": "Bihar",
"district": "Nalanda",
"city": "Hilsa",
"climate": "Composite",
"code": 801365
},
{
"state": "Bihar",
"district": "Nalanda",
"city": "Islampur",
"climate": "Composite",
"code": 801366
},
{
"state": "Bihar",
"district": "Nalanda",
"city": "Nalanda",
"climate": "Composite"
},
{
"state": "Bihar",
"district": "Nalanda",
"city": "Parwalpur Nagar Panchayat",
"climate": "Composite",
"code": 900928
},
{
"state": "Bihar",
"district": "Nalanda",
"city": "Pawapuri",
"climate": "Composite"
},
{
"state": "Bihar",
"district": "Nalanda",
"city": "Rahui Nagar Panchayat",
"climate": "Composite",
"code": 900929
},
{
"state": "Bihar",
"district": "Nalanda",
"city": "Rajgir",
"climate": "Composite",
"code": 801367
},
{
"state": "Bihar",
"district": "Nalanda",
"city": "Sarmera Nagar Panchayat",
"climate": "Composite",
"code": 900930
},
{
"state": "Bihar",
"district": "Nalanda",
"city": "Silao",
"climate": "Composite",
"code": 801368
},
{
"state": "Bihar",
"district": "Nawada",
"city": "Hisua",
"climate": "Composite",
"code": 801409
},
{
"state": "Bihar",
"district": "Nawada",
"city": "Nawada",
"climate": "Composite",
"code": 801407
},
{
"state": "Bihar",
"district": "Nawada",
"city": "Rajauli",
"climate": "Composite"
},
{
"state": "Bihar",
"district": "Nawada",
"city": "Warisaliganj",
"climate": "Composite",
"code": 801408
},
{
"state": "Bihar",
"district": "Paschim Champaran",
"city": "Bagaha",
"climate": "Composite",
"code": 801279
},
{
"state": "Bihar",
"district": "Paschim Champaran",
"city": "Bettiah",
"climate": "Composite",
"code": 801281
},
{
"state": "Bihar",
"district": "Paschim Champaran",
"city": "Chanpatia",
"climate": "Composite",
"code": 801280
},
{
"state": "Bihar",
"district": "Paschim Champaran",
"city": "Lauriya",
"climate": "Composite"
},
{
"state": "Bihar",
"district": "Paschim Champaran",
"city": "Macharganwa",
"climate": "Composite"
},
{
"state": "Bihar",
"district": "Paschim Champaran",
"city": "Narkatiaganj",
"climate": "Composite",
"code": 801278
},
{
"state": "Bihar",
"district": "Paschim Champaran",
"city": "Ramnagar",
"climate": "Composite",
"code": 801277
},
{
"state": "Bihar",
"district": "Patna",
"city": "Bakhtiarpur",
"climate": "Composite",
"code": 801381
},
{
"state": "Bihar",
"district": "Patna",
"city": "Barh",
"climate": "Composite",
"code": 801382
},
{
"state": "Bihar",
"district": "Patna",
"city": "Bihta Nagar Parishad",
"climate": "Composite",
"code": 900931
},
{
"state": "Bihar",
"district": "Patna",
"city": "Bikram",
"climate": "Composite",
"code": 801377
},
{
"state": "Bihar",
"district": "Patna",
"city": "Danapur",
"climate": "Composite",
"code": 801370
},
{
"state": "Bihar",
"district": "Patna",
"city": "Danapur Cantonment",
"climate": "Composite",
"code": 801371
},
{
"state": "Bihar",
"district": "Patna",
"city": "Fatwah",
"climate": "Composite",
"code": 801379
},
{
"state": "Bihar",
"district": "Patna",
"city": "Khagaul",
"climate": "Composite",
"code": 801372
},
{
"state": "Bihar",
"district": "Patna",
"city": "Khusrupur",
"climate": "Composite",
"code": 801380
},
{
"state": "Bihar",
"district": "Patna",
"city": "Maner",
"climate": "Composite",
"code": 801369
},
{
"state": "Bihar",
"district": "Patna",
"city": "Masaurhi",
"climate": "Composite",
"code": 801378
},
{
"state": "Bihar",
"district": "Patna",
"city": "Mokameh",
"climate": "Composite",
"code": 801383
},
{
"state": "Bihar",
"district": "Patna",
"city": "Naubatpur",
"climate": "Composite",
"code": 801376
},
{
"state": "Bihar",
"district": "Patna",
"city": "Paliganj",
"climate": "Composite"
},
{
"state": "Bihar",
"district": "Patna",
"city": "Patna",
"climate": "Composite",
"code": 801373
},
{
"state": "Bihar",
"district": "Patna",
"city": "Phulwari Sharif",
"climate": "Composite",
"code": 801374
},
{
"state": "Bihar",
"district": "Patna",
"city": "Punpun Nagar Panchayat",
"climate": "Composite",
"code": 900932
},
{
"state": "Bihar",
"district": "Patna",
"city": "Sampatchak Nagar Parishad",
"climate": "Composite",
"code": 900933
},
{
"state": "Bihar",
"district": "Purnia",
"city": "Amour Nagar Panchayat",
"climate": "Composite",
"code": 900934
},
{
"state": "Bihar",
"district": "Purnia",
"city": "Baisi Nagar Panchayat",
"climate": "Composite",
"code": 900935
},
{
"state": "Bihar",
"district": "Purnia",
"city": "Banmankhi Bazar",
"climate": "Composite",
"code": 801311
},
{
"state": "Bihar",
"district": "Purnia",
"city": "Bhawanipur Nagar Panchayat",
"climate": "Composite",
"code": 900936
},
{
"state": "Bihar",
"district": "Purnia",
"city": "Champanagar Nagar Panchayat",
"climate": "Composite",
"code": 900937
},
{
"state": "Bihar",
"district": "Purnia",
"city": "Dhamdaha Nagar Panchayat",
"climate": "Composite",
"code": 900938
},
{
"state": "Bihar",
"district": "Purnia",
"city": "Janakinagar",
"climate": "Composite"
},
{
"state": "Bihar",
"district": "Purnia",
"city": "Kasba",
"climate": "Composite",
"code": 801313
},
{
"state": "Bihar",
"district": "Purnia",
"city": "Mirganj Nagar Panchayat",
"climate": "Composite",
"code": 900939
},
{
"state": "Bihar",
"district": "Purnia",
"city": "Purnia",
"climate": "Composite",
"code": 801312
},
{
"state": "Bihar",
"district": "Purnia",
"city": "Rupauli Nagar Panchayat",
"climate": "Composite",
"code": 900940
},
{
"state": "Bihar",
"district": "Purvi Champaran",
"city": "Areraj",
"climate": "Warm & humid",
"code": 801286
},
{
"state": "Bihar",
"district": "Purvi Champaran",
"city": "Chakia",
"climate": "Warm & humid",
"code": 801288
},
{
"state": "Bihar",
"district": "Purvi Champaran",
"city": "Dhaka",
"climate": "Warm & humid",
"code": 801284
},
{
"state": "Bihar",
"district": "Purvi Champaran",
"city": "Kesaria",
"climate": "Warm & humid",
"code": 801287
},
{
"state": "Bihar",
"district": "Purvi Champaran",
"city": "Mehsi",
"climate": "Warm & humid",
"code": 801291
},
{
"state": "Bihar",
"district": "Purvi Champaran",
"city": "Motihari",
"climate": "Warm & humid",
"code": 801285
},
{
"state": "Bihar",
"district": "Purvi Champaran",
"city": "Pakri Dayal",
"climate": "Warm & humid",
"code": 801289
},
{
"state": "Bihar",
"district": "Purvi Champaran",
"city": "Raxaul Bazar",
"climate": "Warm & humid",
"code": 801282
},
{
"state": "Bihar",
"district": "Purvi Champaran",
"city": "Sugauli",
"climate": "Warm & humid",
"code": 801283
},
{
"state": "Bihar",
"district": "Rohtas",
"city": "Bikramganj",
"climate": "Composite",
"code": 801394
},
{
"state": "Bihar",
"district": "Rohtas",
"city": "Chenari Nagar Panchayat",
"climate": "Composite",
"code": 900941
},
{
"state": "Bihar",
"district": "Rohtas",
"city": "Dalmiya Nagar",
"climate": "Composite",
"code": 801398
},
{
"state": "Bihar",
"district": "Rohtas",
"city": "Dinara Nagar Panchayat",
"climate": "Composite",
"code": 900942
},
{
"state": "Bihar",
"district": "Rohtas",
"city": "Karakat Nagar Panchayat",
"climate": "Composite",
"code": 900943
},
{
"state": "Bihar",
"district": "Rohtas",
"city": "Koath",
"climate": "Composite",
"code": 801393
},
{
"state": "Bihar",
"district": "Rohtas",
"city": "Kochas",
"climate": "Composite",
"code": 900123
},
{
"state": "Bihar",
"district": "Rohtas",
"city": "Nasriganj",
"climate": "Composite",
"code": 801395
},
{
"state": "Bihar",
"district": "Rohtas",
"city": "Nokha",
"climate": "Composite",
"code": 801396
},
{
"state": "Bihar",
"district": "Rohtas",
"city": "Rohtas Nagar Panchayat",
"climate": "Composite",
"code": 900944
},
{
"state": "Bihar",
"district": "Rohtas",
"city": "Sasaram",
"climate": "Composite",
"code": 801397
},
{
"state": "Bihar",
"district": "Saharsa",
"city": "Nauhatta Nagar Panchayat",
"climate": "Warm & humid",
"code": 900945
},
{
"state": "Bihar",
"district": "Saharsa",
"city": "Saharsa",
"climate": "Warm & humid",
"code": 801318
},
{
"state": "Bihar",
"district": "Saharsa",
"city": "Simari Bakhtiyarpur",
"climate": "Warm & humid",
"code": 900125
},
{
"state": "Bihar",
"district": "Saharsa",
"city": "Sonvarsha Nagar Panchayat",
"climate": "Warm & humid",
"code": 900946
},
{
"state": "Bihar",
"district": "Saharsa",
"city": "Sour Bazar Nagar Panchayat",
"climate": "Warm & humid",
"code": 900947
},
{
"state": "Bihar",
"district": "Saharsa",
"city": "bangaon",
"climate": "Warm & humid"
},
{
"state": "Bihar",
"district": "Samastipur",
"city": "Dalsinghsarai",
"climate": "Composite",
"code": 801341
},
{
"state": "Bihar",
"district": "Samastipur",
"city": "Musriharari",
"climate": "Composite"
},
{
"state": "Bihar",
"district": "Samastipur",
"city": "Rosera",
"climate": "Composite",
"code": 801342
},
{
"state": "Bihar",
"district": "Samastipur",
"city": "Samastipur",
"climate": "Composite",
"code": 801340
},
{
"state": "Bihar",
"district": "Samastipur",
"city": "Sarairanjan Nagar Panchayat",
"climate": "Composite",
"code": 900948
},
{
"state": "Bihar",
"district": "Samastipur",
"city": "Shahpur Patori Nagar Parishad",
"climate": "Composite",
"code": 900949
},
{
"state": "Bihar",
"district": "Samastipur",
"city": "Singhiya Nagar Panchayat",
"climate": "Composite",
"code": 900950
},
{
"state": "Bihar",
"district": "Samastipur",
"city": "Tajpur Nagar Parishad",
"climate": "Composite",
"code": 900951
},
{
"state": "Bihar",
"district": "Saran",
"city": "Chapra",
"climate": "Composite",
"code": 801333
},
{
"state": "Bihar",
"district": "Saran",
"city": "Dighwara",
"climate": "Composite",
"code": 801335
},
{
"state": "Bihar",
"district": "Saran",
"city": "Ekma Bazar",
"climate": "Composite",
"code": 900122
},
{
"state": "Bihar",
"district": "Saran",
"city": "Kopa",
"climate": "Composite"
},
{
"state": "Bihar",
"district": "Saran",
"city": "Manjhi Nagar Panchayat",
"climate": "Composite",
"code": 900952
},
{
"state": "Bihar",
"district": "Saran",
"city": "Marhaura",
"climate": "Composite",
"code": 801334
},
{
"state": "Bihar",
"district": "Saran",
"city": "Mashrakh Nagar Panchayat",
"climate": "Composite",
"code": 900953
},
{
"state": "Bihar",
"district": "Saran",
"city": "Parsa Bazar",
"climate": "Composite",
"code": 900121
},
{
"state": "Bihar",
"district": "Saran",
"city": "Revelganj",
"climate": "Composite",
"code": 801332
},
{
"state": "Bihar",
"district": "Saran",
"city": "Sonepur",
"climate": "Composite",
"code": 801336
},
{
"state": "Bihar",
"district": "Sheikhpura",
"city": "Barbigha",
"climate": "Composite",
"code": 801362
},
{
"state": "Bihar",
"district": "Sheikhpura",
"city": "Chewara Nagar Panchayat",
"climate": "Composite",
"code": 900954
},
{
"state": "Bihar",
"district": "Sheikhpura",
"city": "Sheikhopur Sarai Nagar Panchayat",
"climate": "Composite",
"code": 900955
},
{
"state": "Bihar",
"district": "Sheikhpura",
"city": "Sheikhpura",
"climate": "Composite",
"code": 801363
},
{
"state": "Bihar",
"district": "Sheohar",
"city": "Sheohar",
"climate": "Warm & humid",
"code": 801292
},
{
"state": "Bihar",
"district": "Sitamarhi",
"city": "Bairgania",
"climate": "Warm & humid",
"code": 801293
},
{
"state": "Bihar",
"district": "Sitamarhi",
"city": "Belsand",
"climate": "Warm & humid",
"code": 801294
},
{
"state": "Bihar",
"district": "Sitamarhi",
"city": "Dumra",
"climate": "Warm & humid",
"code": 801296
},
{
"state": "Bihar",
"district": "Sitamarhi",
"city": "Janakpur Road",
"climate": "Warm & humid",
"code": 801297
},
{
"state": "Bihar",
"district": "Sitamarhi",
"city": "Sitamarhi",
"climate": "Warm & humid",
"code": 801295
},
{
"state": "Bihar",
"district": "Sitamarhi",
"city": "Sursand",
"climate": "Warm & humid",
"code": 900505
},
{
"state": "Bihar",
"district": "Siwan",
"city": "Aandar Nagar Panchayat",
"climate": "Composite",
"code": 900956
},
{
"state": "Bihar",
"district": "Siwan",
"city": "Barharia Nagar Panchayat",
"climate": "Composite",
"code": 900957
},
{
"state": "Bihar",
"district": "Siwan",
"city": "Basantpur Nagar Panchayat",
"climate": "Composite",
"code": 900958
},
{
"state": "Bihar",
"district": "Siwan",
"city": "Guthni Nagar Panchayat",
"climate": "Composite",
"code": 900959
},
{
"state": "Bihar",
"district": "Siwan",
"city": "Hasanpura Nagar Panchayat",
"climate": "Composite",
"code": 900960
},
{
"state": "Bihar",
"district": "Siwan",
"city": "Maharajganj",
"climate": "Composite",
"code": 801330
},
{
"state": "Bihar",
"district": "Siwan",
"city": "Mairwa",
"climate": "Composite",
"code": 801331
},
{
"state": "Bihar",
"district": "Siwan",
"city": "Siwan",
"climate": "Composite",
"code": 801329
},
{
"state": "Bihar",
"district": "Siwan",
"city": "gopalpur",
"climate": "Composite"
},
{
"state": "Bihar",
"district": "Supaul",
"city": "Birpur",
"climate": "Warm & humid",
"code": 801303
},
{
"state": "Bihar",
"district": "Supaul",
"city": "Nirmali",
"climate": "Warm & humid",
"code": 801302
},
{
"state": "Bihar",
"district": "Supaul",
"city": "Pipara Nagar Panchayat",
"climate": "Warm & humid",
"code": 900961
},
{
"state": "Bihar",
"district": "Supaul",
"city": "Simrahi",
"climate": "Warm & humid"
},
{
"state": "Bihar",
"district": "Supaul",
"city": "Supaul",
"climate": "Warm & humid",
"code": 801304
},
{
"state": "Bihar",
"district": "Supaul",
"city": "Triveniganj Nagar Parishad",
"climate": "Warm & humid",
"code": 900962
},
{
"state": "Bihar",
"district": "Vaishali",
"city": "Goraul",
"climate": "Composite"
},
{
"state": "Bihar",
"district": "Vaishali",
"city": "Hajipur",
"climate": "Composite",
"code": 801338
},
{
"state": "Bihar",
"district": "Vaishali",
"city": "Jandaha Nagar Panchayat",
"climate": "Composite",
"code": 900963
},
{
"state": "Bihar",
"district": "Vaishali",
"city": "Lalganj",
"climate": "Composite",
"code": 801337
},
{
"state": "Bihar",
"district": "Vaishali",
"city": "Mahnar Bazar",
"climate": "Composite",
"code": 801339
},
{
"state": "Bihar",
"district": "Vaishali",
"city": "Mahua",
"climate": "Composite",
"code": 900124
},
{
"state": "Bihar",
"district": "Vaishali",
"city": "Patepur Nagar Panchayat",
"climate": "Composite",
"code": 900964
},
{
"state": "Chandigarh",
"district": "Chandigarh",
"city": "Chandigarh",
"climate": "Composite",
"code": 800286
},
{
"state": "Chhattisgarh",
"district": "Balod",
"city": "Arjunda",
"climate": "Composite",
"code": 802012
},
{
"state": "Chhattisgarh",
"district": "Balod",
"city": "Balod",
"climate": "Composite",
"code": 802015
},
{
"state": "Chhattisgarh",
"district": "Balod",
"city": "Chikhalakasa",
"climate": "Composite",
"code": 802017
},
{
"state": "Chhattisgarh",
"district": "Balod",
"city": "Dalli-Rajhara",
"climate": "Composite",
"code": 802016
},
{
"state": "Chhattisgarh",
"district": "Balod",
"city": "Daundi Lohara",
"climate": "Composite",
"code": 802014
},
{
"state": "Chhattisgarh",
"district": "Balod",
"city": "Doundi",
"climate": "Composite",
"code": 802018
},
{
"state": "Chhattisgarh",
"district": "Balod",
"city": "Gunderdehi",
"climate": "Composite",
"code": 802013
},
{
"state": "Chhattisgarh",
"district": "Balod",
"city": "Gurur",
"climate": "Composite",
"code": 802019
},
{
"state": "Chhattisgarh",
"district": "Balodabazaar-Bhatapara",
"city": "Baloda Bazar",
"climate": "Composite",
"code": 802022
},
{
"state": "Chhattisgarh",
"district": "Balodabazaar-Bhatapara",
"city": "Bhatapara",
"climate": "Composite",
"code": 802021
},
{
"state": "Chhattisgarh",
"district": "Balodabazaar-Bhatapara",
"city": "Bhatgaon_Bb",
"climate": "Composite",
"code": 802027
},
{
"state": "Chhattisgarh",
"district": "Balodabazaar-Bhatapara",
"city": "Bilaigarh",
"climate": "Composite",
"code": 802028
},
{
"state": "Chhattisgarh",
"district": "Balodabazaar-Bhatapara",
"city": "Kasdol",
"climate": "Composite",
"code": 802026
},
{
"state": "Chhattisgarh",
"district": "Balodabazaar-Bhatapara",
"city": "Lawan",
"climate": "Composite",
"code": 802023
},
{
"state": "Chhattisgarh",
"district": "Balodabazaar-Bhatapara",
"city": "Palari",
"climate": "Composite",
"code": 802024
},
{
"state": "Chhattisgarh",
"district": "Balodabazaar-Bhatapara",
"city": "Simga",
"climate": "Composite",
"code": 802020
},
{
"state": "Chhattisgarh",
"district": "Balodabazaar-Bhatapara",
"city": "Tundra",
"climate": "Composite",
"code": 802025
},
{
"state": "Chhattisgarh",
"district": "Balrampur",
"city": "Balrampur",
"climate": "Composite",
"code": 801918
},
{
"state": "Chhattisgarh",
"district": "Balrampur",
"city": "Kusmi",
"climate": "Composite",
"code": 801922
},
{
"state": "Chhattisgarh",
"district": "Balrampur",
"city": "Rajpur",
"climate": "Composite",
"code": 801929
},
{
"state": "Chhattisgarh",
"district": "Balrampur",
"city": "Ramanujganj",
"climate": "Composite",
"code": 801917
},
{
"state": "Chhattisgarh",
"district": "Balrampur",
"city": "Wadrafnagar",
"climate": "Composite",
"code": 801919
},
{
"state": "Chhattisgarh",
"district": "Bastar",
"city": "Bastar",
"climate": "Composite",
"code": 802065
},
{
"state": "Chhattisgarh",
"district": "Bastar",
"city": "Jagdalpur",
"climate": "Composite",
"code": 802064
},
{
"state": "Chhattisgarh",
"district": "Bemetara",
"city": "Bemetara",
"climate": "Composite",
"code": 801997
},
{
"state": "Chhattisgarh",
"district": "Bemetara",
"city": "Berla",
"climate": "Composite",
"code": 802002
},
{
"state": "Chhattisgarh",
"district": "Bemetara",
"city": "Devkar",
"climate": "Composite",
"code": 801999
},
{
"state": "Chhattisgarh",
"district": "Bemetara",
"city": "Khamhariya",
"climate": "Composite",
"code": 900105
},
{
"state": "Chhattisgarh",
"district": "Bemetara",
"city": "Maro",
"climate": "Composite",
"code": 801996
},
{
"state": "Chhattisgarh",
"district": "Bemetara",
"city": "Nawagarh_B",
"climate": "Composite",
"code": 801995
},
{
"state": "Chhattisgarh",
"district": "Bemetara",
"city": "Parpondi",
"climate": "Composite",
"code": 802000
},
{
"state": "Chhattisgarh",
"district": "Bemetara",
"city": "Saja",
"climate": "Composite",
"code": 801998
},
{
"state": "Chhattisgarh",
"district": "Bijapur",
"city": "Bhairamgarh",
"climate": "Composite",
"code": 802077
},
{
"state": "Chhattisgarh",
"district": "Bijapur",
"city": "Bhopalpattanam",
"climate": "Composite",
"code": 802075
},
{
"state": "Chhattisgarh",
"district": "Bijapur",
"city": "Bijapur",
"climate": "Composite",
"code": 802076
},
{
"state": "Chhattisgarh",
"district": "Bilaspur",
"city": "Bilaspur",
"climate": "Composite",
"code": 801975
},
{
"state": "Chhattisgarh",
"district": "Bilaspur",
"city": "Bilha",
"climate": "Composite",
"code": 801980
},
{
"state": "Chhattisgarh",
"district": "Bilaspur",
"city": "Bodri",
"climate": "Composite",
"code": 801979
},
{
"state": "Chhattisgarh",
"district": "Bilaspur",
"city": "Kota",
"climate": "Composite",
"code": 801968
},
{
"state": "Chhattisgarh",
"district": "Bilaspur",
"city": "Malhar",
"climate": "Composite",
"code": 801978
},
{
"state": "Chhattisgarh",
"district": "Bilaspur",
"city": "Ratanpur",
"climate": "Composite",
"code": 801969
},
{
"state": "Chhattisgarh",
"district": "Bilaspur",
"city": "Takhatpur",
"climate": "Composite",
"code": 801973
},
{
"state": "Chhattisgarh",
"district": "Dantewada",
"city": "Bade Bacheli",
"climate": "Warm & humid",
"code": 802068
},
{
"state": "Chhattisgarh",
"district": "Dantewada",
"city": "Barsur",
"climate": "Warm & humid",
"code": 802069
},
{
"state": "Chhattisgarh",
"district": "Dantewada",
"city": "Dantewada",
"climate": "Warm & humid",
"code": 802067
},
{
"state": "Chhattisgarh",
"district": "Dantewada",
"city": "Geedam",
"climate": "Warm & humid",
"code": 802070
},
{
"state": "Chhattisgarh",
"district": "Dantewada",
"city": "Kirandul",
"climate": "Warm & humid",
"code": 802071
},
{
"state": "Chhattisgarh",
"district": "Dhamtari",
"city": "Aamadi",
"climate": "Composite",
"code": 802051
},
{
"state": "Chhattisgarh",
"district": "Dhamtari",
"city": "Bhakhara",
"climate": "Composite",
"code": 802048
},
{
"state": "Chhattisgarh",
"district": "Dhamtari",
"city": "Dhamtari",
"climate": "Composite",
"code": 802052
},
{
"state": "Chhattisgarh",
"district": "Dhamtari",
"city": "Kurud",
"climate": "Composite",
"code": 802049
},
{
"state": "Chhattisgarh",
"district": "Dhamtari",
"city": "Magarlod",
"climate": "Composite",
"code": 802050
},
{
"state": "Chhattisgarh",
"district": "Dhamtari",
"city": "Nagari",
"climate": "Composite",
"code": 802053
},
{
"state": "Chhattisgarh",
"district": "Durg",
"city": "Ahiwara",
"climate": "Composite",
"code": 802004
},
{
"state": "Chhattisgarh",
"district": "Durg",
"city": "Bhilai Charoda",
"climate": "Composite",
"code": 802007
},
{
"state": "Chhattisgarh",
"district": "Durg",
"city": "Bhilai Nagar",
"climate": "Composite",
"code": 802008
},
{
"state": "Chhattisgarh",
"district": "Durg",
"city": "Dhamdha",
"climate": "Composite",
"code": 802003
},
{
"state": "Chhattisgarh",
"district": "Durg",
"city": "Durg",
"climate": "Composite",
"code": 802009
},
{
"state": "Chhattisgarh",
"district": "Durg",
"city": "Jamul",
"climate": "Composite",
"code": 802006
},
{
"state": "Chhattisgarh",
"district": "Durg",
"city": "Kumhari",
"climate": "Composite",
"code": 802005
},
{
"state": "Chhattisgarh",
"district": "Durg",
"city": "Patan",
"climate": "Composite",
"code": 802011
},
{
"state": "Chhattisgarh",
"district": "Durg",
"city": "Risali",
"climate": "Composite",
"code": 900507
},
{
"state": "Chhattisgarh",
"district": "Durg",
"city": "Utai",
"climate": "Composite",
"code": 802010
},
{
"state": "Chhattisgarh",
"district": "Gariyaband",
"city": "Chhura",
"climate": "Composite",
"code": 802041
},
{
"state": "Chhattisgarh",
"district": "Gariyaband",
"city": "Fingeshwar",
"climate": "Composite",
"code": 802036
},
{
"state": "Chhattisgarh",
"district": "Gariyaband",
"city": "Gariyaband",
"climate": "Composite",
"code": 802040
},
{
"state": "Chhattisgarh",
"district": "Gariyaband",
"city": "Rajim",
"climate": "Composite",
"code": 802037
},
{
"state": "Chhattisgarh",
"district": "Gaurella-Pendra-Marwahi",
"city": "Gaurella",
"climate": "Composite",
"code": 801965
},
{
"state": "Chhattisgarh",
"district": "Gaurella-Pendra-Marwahi",
"city": "Pendra",
"climate": "Composite",
"code": 801966
},
{
"state": "Chhattisgarh",
"district": "Janjgir Champa",
"city": "Adbhar",
"climate": "Composite",
"code": 801963
},
{
"state": "Chhattisgarh",
"district": "Janjgir Champa",
"city": "Akaltara",
"climate": "Composite",
"code": 801951
},
{
"state": "Chhattisgarh",
"district": "Janjgir Champa",
"city": "Baloda",
"climate": "Composite",
"code": 801952
},
{
"state": "Chhattisgarh",
"district": "Janjgir Champa",
"city": "Champa",
"climate": "Composite",
"code": 801955
},
{
"state": "Chhattisgarh",
"district": "Janjgir Champa",
"city": "Chandrapur",
"climate": "Composite",
"code": 801962
},
{
"state": "Chhattisgarh",
"district": "Janjgir Champa",
"city": "Dabhra",
"climate": "Composite",
"code": 801961
},
{
"state": "Chhattisgarh",
"district": "Janjgir Champa",
"city": "Jaijepur",
"climate": "Composite",
"code": 801964
},
{
"state": "Chhattisgarh",
"district": "Janjgir Champa",
"city": "Janjgirnaila",
"climate": "Composite",
"code": 801950
},
{
"state": "Chhattisgarh",
"district": "Janjgir Champa",
"city": "Kharod",
"climate": "Composite",
"code": 801960
},
{
"state": "Chhattisgarh",
"district": "Janjgir Champa",
"city": "Nawagarh_Jc",
"climate": "Composite",
"code": 801953
},
{
"state": "Chhattisgarh",
"district": "Janjgir Champa",
"city": "Naya Baradwar",
"climate": "Composite",
"code": 801958
},
{
"state": "Chhattisgarh",
"district": "Janjgir Champa",
"city": "Rahaud",
"climate": "Composite",
"code": 801959
},
{
"state": "Chhattisgarh",
"district": "Janjgir Champa",
"city": "Sakti",
"climate": "Composite",
"code": 801957
},
{
"state": "Chhattisgarh",
"district": "Janjgir Champa",
"city": "Saragaon",
"climate": "Composite",
"code": 801956
},
{
"state": "Chhattisgarh",
"district": "Janjgir Champa",
"city": "Shivrinarayan",
"climate": "Composite",
"code": 801954
},
{
"state": "Chhattisgarh",
"district": "Jashpurnagar",
"city": "Bagicha",
"climate": "Composite",
"code": 801931
},
{
"state": "Chhattisgarh",
"district": "Jashpurnagar",
"city": "Jashpur Nagar",
"climate": "Composite",
"code": 801932
},
{
"state": "Chhattisgarh",
"district": "Jashpurnagar",
"city": "Kotba",
"climate": "Composite",
"code": 801934
},
{
"state": "Chhattisgarh",
"district": "Jashpurnagar",
"city": "Kunkuri",
"climate": "Composite",
"code": 900006
},
{
"state": "Chhattisgarh",
"district": "Jashpurnagar",
"city": "Pathalgaon",
"climate": "Composite",
"code": 801933
},
{
"state": "Chhattisgarh",
"district": "Kanker",
"city": "Antagarh",
"climate": "Composite",
"code": 802058
},
{
"state": "Chhattisgarh",
"district": "Kanker",
"city": "Bhanupratappur",
"climate": "Composite",
"code": 802055
},
{
"state": "Chhattisgarh",
"district": "Kanker",
"city": "Charama",
"climate": "Composite",
"code": 802054
},
{
"state": "Chhattisgarh",
"district": "Kanker",
"city": "Kanker",
"climate": "Composite",
"code": 802056
},
{
"state": "Chhattisgarh",
"district": "Kanker",
"city": "Narharpur",
"climate": "Composite",
"code": 802057
},
{
"state": "Chhattisgarh",
"district": "Kanker",
"city": "Pakhanjur",
"climate": "Composite",
"code": 802059
},
{
"state": "Chhattisgarh",
"district": "Kawardha",
"city": "Bodla",
"climate": "Composite",
"code": 801983
},
{
"state": "Chhattisgarh",
"district": "Kawardha",
"city": "Kawardha",
"climate": "Composite",
"code": 801981
},
{
"state": "Chhattisgarh",
"district": "Kawardha",
"city": "Pandariya",
"climate": "Composite",
"code": 801985
},
{
"state": "Chhattisgarh",
"district": "Kawardha",
"city": "Pandatarai",
"climate": "Composite",
"code": 801986
},
{
"state": "Chhattisgarh",
"district": "Kawardha",
"city": "Pipariya",
"climate": "Composite",
"code": 801982
},
{
"state": "Chhattisgarh",
"district": "Kawardha",
"city": "Sahaspur-Lohara",
"climate": "Composite",
"code": 801984
},
{
"state": "Chhattisgarh",
"district": "Kondagaon",
"city": "Farasgaon",
"climate": "Composite",
"code": 802063
},
{
"state": "Chhattisgarh",
"district": "Kondagaon",
"city": "Keskal",
"climate": "Composite",
"code": 802060
},
{
"state": "Chhattisgarh",
"district": "Kondagaon",
"city": "Kondagaon",
"climate": "Composite",
"code": 802062
},
{
"state": "Chhattisgarh",
"district": "Korba",
"city": "Chhurikala",
"climate": "Composite",
"code": 801946
},
{
"state": "Chhattisgarh",
"district": "Korba",
"city": "Dipka",
"climate": "Composite",
"code": 801947
},
{
"state": "Chhattisgarh",
"district": "Korba",
"city": "Katghora",
"climate": "Composite",
"code": 801945
},
{
"state": "Chhattisgarh",
"district": "Korba",
"city": "Korba",
"climate": "Composite",
"code": 801949
},
{
"state": "Chhattisgarh",
"district": "Korba",
"city": "Pali",
"climate": "Composite",
"code": 801948
},
{
"state": "Chhattisgarh",
"district": "Koriya",
"city": "Baikunthpur",
"climate": "Composite",
"code": 801911
},
{
"state": "Chhattisgarh",
"district": "Koriya",
"city": "Chirmiri",
"climate": "Composite",
"code": 801916
},
{
"state": "Chhattisgarh",
"district": "Koriya",
"city": "Jhagrakhand",
"climate": "Composite",
"code": 801914
},
{
"state": "Chhattisgarh",
"district": "Koriya",
"city": "Khongapani",
"climate": "Composite",
"code": 801913
},
{
"state": "Chhattisgarh",
"district": "Koriya",
"city": "Manendragarh",
"climate": "Composite",
"code": 801912
},
{
"state": "Chhattisgarh",
"district": "Koriya",
"city": "Nai-Ledri",
"climate": "Composite",
"code": 801915
},
{
"state": "Chhattisgarh",
"district": "Koriya",
"city": "Shivpur Charcha",
"climate": "Composite",
"code": 801910
},
{
"state": "Chhattisgarh",
"district": "Mahasamund",
"city": "Bagbahara",
"climate": "Composite",
"code": 802047
},
{
"state": "Chhattisgarh",
"district": "Mahasamund",
"city": "Basna",
"climate": "Composite",
"code": 802042
},
{
"state": "Chhattisgarh",
"district": "Mahasamund",
"city": "Mahasamund",
"climate": "Composite",
"code": 802045
},
{
"state": "Chhattisgarh",
"district": "Mahasamund",
"city": "Pithora",
"climate": "Composite",
"code": 802046
},
{
"state": "Chhattisgarh",
"district": "Mahasamund",
"city": "Saraipali",
"climate": "Composite",
"code": 802043
},
{
"state": "Chhattisgarh",
"district": "Mahasamund",
"city": "Tumgaon",
"climate": "Composite",
"code": 802044
},
{
"state": "Chhattisgarh",
"district": "Mungeli",
"city": "Lormi",
"climate": "Composite",
"code": 801967
},
{
"state": "Chhattisgarh",
"district": "Mungeli",
"city": "Mungeli",
"climate": "Composite",
"code": 801970
},
{
"state": "Chhattisgarh",
"district": "Mungeli",
"city": "Pathariya",
"climate": "Composite",
"code": 801971
},
{
"state": "Chhattisgarh",
"district": "Mungeli",
"city": "Sargaon",
"climate": "Composite",
"code": 801972
},
{
"state": "Chhattisgarh",
"district": "Narayanpur",
"city": "Narayanpur",
"climate": "Composite",
"code": 802066
},
{
"state": "Chhattisgarh",
"district": "Raigarh",
"city": "Baramkela",
"climate": "Composite",
"code": 801944
},
{
"state": "Chhattisgarh",
"district": "Raigarh",
"city": "Dharamjaigarh",
"climate": "Composite",
"code": 801935
},
{
"state": "Chhattisgarh",
"district": "Raigarh",
"city": "Gharghoda",
"climate": "Composite",
"code": 801937
},
{
"state": "Chhattisgarh",
"district": "Raigarh",
"city": "Kharsia",
"climate": "Composite",
"code": 801941
},
{
"state": "Chhattisgarh",
"district": "Raigarh",
"city": "Kirodimalnagar",
"climate": "Composite",
"code": 801938
},
{
"state": "Chhattisgarh",
"district": "Raigarh",
"city": "Lailunga",
"climate": "Composite",
"code": 801936
},
{
"state": "Chhattisgarh",
"district": "Raigarh",
"city": "Pusaur",
"climate": "Composite",
"code": 801940
},
{
"state": "Chhattisgarh",
"district": "Raigarh",
"city": "Raigarh",
"climate": "Composite",
"code": 801939
},
{
"state": "Chhattisgarh",
"district": "Raigarh",
"city": "Sarangarh",
"climate": "Composite",
"code": 801942
},
{
"state": "Chhattisgarh",
"district": "Raigarh",
"city": "Sariya",
"climate": "Composite",
"code": 801943
},
{
"state": "Chhattisgarh",
"district": "Raipur",
"city": "Abhanpur",
"climate": "Composite",
"code": 802030
},
{
"state": "Chhattisgarh",
"district": "Raipur",
"city": "ArangÃ¢Â",
"climate": "Composite",
"code": 802029
},
{
"state": "Chhattisgarh",
"district": "Raipur",
"city": "Birgaon",
"climate": "Composite",
"code": 802033
},
{
"state": "Chhattisgarh",
"district": "Raipur",
"city": "Chandkhuri",
"climate": "Composite",
"code": 900603
},
{
"state": "Chhattisgarh",
"district": "Raipur",
"city": "Gobra Nawapara",
"climate": "Composite",
"code": 802031
},
{
"state": "Chhattisgarh",
"district": "Raipur",
"city": "Kharora",
"climate": "Composite",
"code": 802039
},
{
"state": "Chhattisgarh",
"district": "Raipur",
"city": "Kura",
"climate": "Composite",
"code": 802032
},
{
"state": "Chhattisgarh",
"district": "Raipur",
"city": "Mana-Camp",
"climate": "Composite",
"code": 802035
},
{
"state": "Chhattisgarh",
"district": "Raipur",
"city": "Mandir Hasoud",
"climate": "Composite",
"code": 900601
},
{
"state": "Chhattisgarh",
"district": "Raipur",
"city": "Raipur",
"climate": "Composite",
"code": 802034
},
{
"state": "Chhattisgarh",
"district": "Raipur",
"city": "Samoda",
"climate": "Composite",
"code": 900602
},
{
"state": "Chhattisgarh",
"district": "Raipur",
"city": "Tilda Newra",
"climate": "Composite",
"code": 802038
},
{
"state": "Chhattisgarh",
"district": "Rajnandgaon",
"city": "Ambagarh Chowki",
"climate": "Composite",
"code": 801994
},
{
"state": "Chhattisgarh",
"district": "Rajnandgaon",
"city": "Chhuikhadan",
"climate": "Composite",
"code": 801988
},
{
"state": "Chhattisgarh",
"district": "Rajnandgaon",
"city": "Chhuriya",
"climate": "Composite",
"code": 801992
},
{
"state": "Chhattisgarh",
"district": "Rajnandgaon",
"city": "Dongargaon",
"climate": "Composite",
"code": 801993
},
{
"state": "Chhattisgarh",
"district": "Rajnandgaon",
"city": "Dongargarh",
"climate": "Composite",
"code": 801990
},
{
"state": "Chhattisgarh",
"district": "Rajnandgaon",
"city": "Gandai",
"climate": "Composite",
"code": 801987
},
{
"state": "Chhattisgarh",
"district": "Rajnandgaon",
"city": "Khairagarh",
"climate": "Composite",
"code": 801989
},
{
"state": "Chhattisgarh",
"district": "Rajnandgaon",
"city": "Rajnandgaon",
"climate": "Composite",
"code": 801991
},
{
"state": "Chhattisgarh",
"district": "Sarguja",
"city": "Ambikapur",
"climate": "Composite",
"code": 801927
},
{
"state": "Chhattisgarh",
"district": "Sarguja",
"city": "Lakhanpur",
"climate": "Composite",
"code": 801928
},
{
"state": "Chhattisgarh",
"district": "Sarguja",
"city": "Sitapur",
"climate": "Composite",
"code": 801930
},
{
"state": "Chhattisgarh",
"district": "Sukma",
"city": "Dornapal",
"climate": "Composite",
"code": 802072
},
{
"state": "Chhattisgarh",
"district": "Sukma",
"city": "Konta",
"climate": "Composite",
"code": 802073
},
{
"state": "Chhattisgarh",
"district": "Sukma",
"city": "Sukma",
"climate": "Composite",
"code": 802074
},
{
"state": "Chhattisgarh",
"district": "Surajpur",
"city": "Bhatgaon_S",
"climate": "Composite",
"code": 801925
},
{
"state": "Chhattisgarh",
"district": "Surajpur",
"city": "Bishrampur",
"climate": "Composite",
"code": 801924
},
{
"state": "Chhattisgarh",
"district": "Surajpur",
"city": "Jarhi",
"climate": "Composite",
"code": 801921
},
{
"state": "Chhattisgarh",
"district": "Surajpur",
"city": "Pratappur",
"climate": "Composite",
"code": 801920
},
{
"state": "Chhattisgarh",
"district": "Surajpur",
"city": "Premnagar",
"climate": "Composite",
"code": 801926
},
{
"state": "Chhattisgarh",
"district": "Surajpur",
"city": "Surajpur",
"climate": "Composite",
"code": 801923
},
{
"state": "Dadra & Nagar Haveli",
"district": "Dadra And Nagar Haveli",
"city": "Silvassa",
"climate": "Warm & humid",
"code": 802639
},
{
"state": "Daman & Diu",
"district": "Daman",
"city": "Daman",
"climate": "Warm & humid",
"code": 802638
},
{
"state": "Daman & Diu",
"district": "Diu",
"city": "Diu",
"climate": "Warm & humid",
"code": 802637
},
{
"state": "Delhi",
"district": "New Delhi",
"city": "New Delhi",
"climate": "Composite",
"code": 800442
},
{
"state": "Delhi",
"district": "South Delhi",
"city": "Municipal Corporation Of Delhi",
"climate": "Composite",
"code": 800441
},
{
"state": "Delhi",
"district": "South West",
"city": "Delhi Cantonment",
"climate": "Composite",
"code": 800443
},
{
"state": "Goa",
"district": "North Goa",
"city": "Bicholim",
"climate": "Warm & humid",
"code": 803244
},
{
"state": "Goa",
"district": "North Goa",
"city": "Mapusa",
"climate": "Warm & humid",
"code": 803242
},
{
"state": "Goa",
"district": "North Goa",
"city": "Panaji",
"climate": "Warm & humid",
"code": 803243
},
{
"state": "Goa",
"district": "North Goa",
"city": "Pernem",
"climate": "Warm & humid",
"code": 803241
},
{
"state": "Goa",
"district": "North Goa",
"city": "Ponda",
"climate": "Warm & humid",
"code": 803247
},
{
"state": "Goa",
"district": "North Goa",
"city": "Sanquelim",
"climate": "Warm & humid",
"code": 803245
},
{
"state": "Goa",
"district": "North Goa",
"city": "Valpoi",
"climate": "Warm & humid",
"code": 803246
},
{
"state": "Goa",
"district": "South Goa",
"city": "Canacona",
"climate": "Warm & humid",
"code": 803254
},
{
"state": "Goa",
"district": "South Goa",
"city": "Cuncolim",
"climate": "Warm & humid",
"code": 803250
},
{
"state": "Goa",
"district": "South Goa",
"city": "Curchorem-Cacora",
"climate": "Warm & humid",
"code": 803252
},
{
"state": "Goa",
"district": "South Goa",
"city": "Margao",
"climate": "Warm & humid",
"code": 803249
},
{
"state": "Goa",
"district": "South Goa",
"city": "Mormugao",
"climate": "Warm & humid",
"code": 803248
},
{
"state": "Goa",
"district": "South Goa",
"city": "Quepem",
"climate": "Warm & humid",
"code": 803251
},
{
"state": "Goa",
"district": "South Goa",
"city": "Sanguem",
"climate": "Warm & humid",
"code": 803253
},
{
"state": "Gujarat",
"district": "Ahmedabad",
"city": "Ahmedabad",
"climate": "Hot and Dry",
"code": 802484
},
{
"state": "Gujarat",
"district": "Ahmedabad",
"city": "Ahmedabad Cantonment",
"climate": "Hot and Dry",
"code": 802483
},
{
"state": "Gujarat",
"district": "Ahmedabad",
"city": "Bareja",
"climate": "Hot and Dry",
"code": 802485
},
{
"state": "Gujarat",
"district": "Ahmedabad",
"city": "Bavla",
"climate": "Hot and Dry",
"code": 802487
},
{
"state": "Gujarat",
"district": "Ahmedabad",
"city": "Dhandhuka",
"climate": "Hot and Dry",
"code": 802489
},
{
"state": "Gujarat",
"district": "Ahmedabad",
"city": "Dholka",
"climate": "Hot and Dry",
"code": 802486
},
{
"state": "Gujarat",
"district": "Ahmedabad",
"city": "Sanand",
"climate": "Hot and Dry",
"code": 802482
},
{
"state": "Gujarat",
"district": "Ahmedabad",
"city": "Viramgam",
"climate": "Hot and Dry",
"code": 802481
},
{
"state": "Gujarat",
"district": "Amreli",
"city": "Amreli",
"climate": "Composite",
"code": 802542
},
{
"state": "Gujarat",
"district": "Amreli",
"city": "Babra",
"climate": "Composite",
"code": 802539
},
{
"state": "Gujarat",
"district": "Amreli",
"city": "Bagasra",
"climate": "Composite",
"code": 802543
},
{
"state": "Gujarat",
"district": "Amreli",
"city": "Chalala",
"climate": "Composite",
"code": 802544
},
{
"state": "Gujarat",
"district": "Amreli",
"city": "Damnagar",
"climate": "Composite",
"code": 802541
},
{
"state": "Gujarat",
"district": "Amreli",
"city": "Jafarabad",
"climate": "Composite",
"code": 802546
},
{
"state": "Gujarat",
"district": "Amreli",
"city": "Lathi",
"climate": "Composite",
"code": 802540
},
{
"state": "Gujarat",
"district": "Amreli",
"city": "Rajula",
"climate": "Composite",
"code": 802547
},
{
"state": "Gujarat",
"district": "Amreli",
"city": "Savarkundla",
"climate": "Composite",
"code": 802545
},
{
"state": "Gujarat",
"district": "Anand",
"city": "Anand",
"climate": "Warm & humid",
"code": 802562
},
{
"state": "Gujarat",
"district": "Anand",
"city": "Anklav",
"climate": "Warm & humid",
"code": 802570
},
{
"state": "Gujarat",
"district": "Anand",
"city": "Boriyavi",
"climate": "Warm & humid",
"code": 802560
},
{
"state": "Gujarat",
"district": "Anand",
"city": "Borsad",
"climate": "Warm & humid",
"code": 802568
},
{
"state": "Gujarat",
"district": "Anand",
"city": "Karamsad",
"climate": "Warm & humid",
"code": 802564
},
{
"state": "Gujarat",
"district": "Anand",
"city": "Khambhat",
"climate": "Warm & humid",
"code": 802567
},
{
"state": "Gujarat",
"district": "Anand",
"city": "Ode",
"climate": "Warm & humid",
"code": 802561
},
{
"state": "Gujarat",
"district": "Anand",
"city": "Petlad",
"climate": "Warm & humid",
"code": 802566
},
{
"state": "Gujarat",
"district": "Anand",
"city": "Sojitra",
"climate": "Warm & humid",
"code": 802558
},
{
"state": "Gujarat",
"district": "Anand",
"city": "Umreth",
"climate": "Warm & humid",
"code": 802559
},
{
"state": "Gujarat",
"district": "Anand",
"city": "Vallabh Vidhyanagar",
"climate": "Warm & humid",
"code": 802563
},
{
"state": "Gujarat",
"district": "Aravalli",
"city": "Bayad",
"climate": "Warm & humid",
"code": 802473
},
{
"state": "Gujarat",
"district": "Aravalli",
"city": "Modasa",
"climate": "Warm & humid",
"code": 802472
},
{
"state": "Gujarat",
"district": "Banas Kantha",
"city": "Bhabhar",
"climate": "Warm & humid",
"code": 802452
},
{
"state": "Gujarat",
"district": "Banas Kantha",
"city": "Deesa",
"climate": "Warm & humid",
"code": 802451
},
{
"state": "Gujarat",
"district": "Banas Kantha",
"city": "Dhanera",
"climate": "Warm & humid",
"code": 802449
},
{
"state": "Gujarat",
"district": "Banas Kantha",
"city": "Palanpur",
"climate": "Warm & humid",
"code": 802450
},
{
"state": "Gujarat",
"district": "Banas Kantha",
"city": "Thara",
"climate": "Warm & humid",
"code": 802453
},
{
"state": "Gujarat",
"district": "Banas Kantha",
"city": "Tharad",
"climate": "Warm & humid",
"code": 802448
},
{
"state": "Gujarat",
"district": "Bharuch",
"city": "Amod",
"climate": "Warm & humid",
"code": 802605
},
{
"state": "Gujarat",
"district": "Bharuch",
"city": "Ankleshwer",
"climate": "Warm & humid",
"code": 802608
},
{
"state": "Gujarat",
"district": "Bharuch",
"city": "Bharuch",
"climate": "Warm & humid",
"code": 802607
},
{
"state": "Gujarat",
"district": "Bharuch",
"city": "Jambusar",
"climate": "Warm & humid",
"code": 802604
},
{
"state": "Gujarat",
"district": "Bhavnagar",
"city": "Bhavnagar",
"climate": "Composite",
"code": 802551
},
{
"state": "Gujarat",
"district": "Bhavnagar",
"city": "Gariyadhar",
"climate": "Composite",
"code": 802553
},
{
"state": "Gujarat",
"district": "Bhavnagar",
"city": "Mahuva",
"climate": "Composite",
"code": 802557
},
{
"state": "Gujarat",
"district": "Bhavnagar",
"city": "Palitana",
"climate": "Composite",
"code": 802554
},
{
"state": "Gujarat",
"district": "Bhavnagar",
"city": "Sihor",
"climate": "Composite",
"code": 802552
},
{
"state": "Gujarat",
"district": "Bhavnagar",
"city": "Talaja",
"climate": "Composite",
"code": 802555
},
{
"state": "Gujarat",
"district": "Bhavnagar",
"city": "Vallabhipur",
"climate": "Composite",
"code": 802549
},
{
"state": "Gujarat",
"district": "Botad",
"city": "Barvala",
"climate": "Warm & humid",
"code": 802488
},
{
"state": "Gujarat",
"district": "Botad",
"city": "Botad",
"climate": "Warm & humid",
"code": 802548
},
{
"state": "Gujarat",
"district": "Botad",
"city": "Gadhada",
"climate": "Warm & humid",
"code": 802550
},
{
"state": "Gujarat",
"district": "Chhotaudepur",
"city": "Chhota Udepur",
"climate": "Warm & humid",
"code": 802599
},
{
"state": "Gujarat",
"district": "Dahod",
"city": "Dahod",
"climate": "Warm & humid",
"code": 802590
},
{
"state": "Gujarat",
"district": "Dahod",
"city": "Devgadhbariya",
"climate": "Warm & humid",
"code": 802591
},
{
"state": "Gujarat",
"district": "Dahod",
"city": "Jhalod",
"climate": "Warm & humid",
"code": 802589
},
{
"state": "Gujarat",
"district": "Devbhoomi Dwarka",
"city": "Bhanvad",
"climate": "Warm & humid",
"code": 802520
},
{
"state": "Gujarat",
"district": "Devbhoomi Dwarka",
"city": "Dwarka",
"climate": "Warm & humid",
"code": 802510
},
{
"state": "Gujarat",
"district": "Devbhoomi Dwarka",
"city": "Jamraval",
"climate": "Warm & humid",
"code": 802519
},
{
"state": "Gujarat",
"district": "Devbhoomi Dwarka",
"city": "Khambhaliya",
"climate": "Warm & humid",
"code": 802512
},
{
"state": "Gujarat",
"district": "Devbhoomi Dwarka",
"city": "Okha",
"climate": "Warm & humid",
"code": 802509
},
{
"state": "Gujarat",
"district": "Devbhoomi Dwarka",
"city": "Salaya",
"climate": "Warm & humid",
"code": 802511
},
{
"state": "Gujarat",
"district": "Gandhinagar",
"city": "Dahegam",
"climate": "Warm & humid",
"code": 802480
},
{
"state": "Gujarat",
"district": "Gandhinagar",
"city": "Gandhinagar",
"climate": "Warm & humid",
"code": 802479
},
{
"state": "Gujarat",
"district": "Gandhinagar",
"city": "Kalol",
"climate": "Warm & humid",
"code": 802475
},
{
"state": "Gujarat",
"district": "Gandhinagar",
"city": "Mansa_G",
"climate": "Warm & humid",
"code": 802477
},
{
"state": "Gujarat",
"district": "Gir Somnath",
"city": "Kodinar",
"climate": "Warm & humid",
"code": 802537
},
{
"state": "Gujarat",
"district": "Gir Somnath",
"city": "Sutrapada",
"climate": "Warm & humid",
"code": 802536
},
{
"state": "Gujarat",
"district": "Gir Somnath",
"city": "Talala",
"climate": "Warm & humid",
"code": 802534
},
{
"state": "Gujarat",
"district": "Gir Somnath",
"city": "Una_G",
"climate": "Warm & humid",
"code": 802538
},
{
"state": "Gujarat",
"district": "Gir Somnath",
"city": "Veraval",
"climate": "Warm & humid",
"code": 802535
},
{
"state": "Gujarat",
"district": "Jamnagar",
"city": "Dhrol",
"climate": "Warm & humid",
"code": 802517
},
{
"state": "Gujarat",
"district": "Jamnagar",
"city": "Jamjodhpur",
"climate": "Warm & humid",
"code": 802521
},
{
"state": "Gujarat",
"district": "Jamnagar",
"city": "Jamnagar",
"climate": "Warm & humid",
"code": 802516
},
{
"state": "Gujarat",
"district": "Jamnagar",
"city": "Kalavad",
"climate": "Warm & humid",
"code": 802518
},
{
"state": "Gujarat",
"district": "Jamnagar",
"city": "Sikka",
"climate": "Warm & humid",
"code": 802513
},
{
"state": "Gujarat",
"district": "Junagadh",
"city": "Bantva",
"climate": "Warm & humid",
"code": 802526
},
{
"state": "Gujarat",
"district": "Junagadh",
"city": "Chorvad",
"climate": "Warm & humid",
"code": 802533
},
{
"state": "Gujarat",
"district": "Junagadh",
"city": "Junagadh",
"climate": "Warm & humid",
"code": 802529
},
{
"state": "Gujarat",
"district": "Junagadh",
"city": "Keshod",
"climate": "Warm & humid",
"code": 802531
},
{
"state": "Gujarat",
"district": "Junagadh",
"city": "Manavadar",
"climate": "Warm & humid",
"code": 802527
},
{
"state": "Gujarat",
"district": "Junagadh",
"city": "Mangrol_J",
"climate": "Warm & humid",
"code": 802532
},
{
"state": "Gujarat",
"district": "Junagadh",
"city": "Vanthali",
"climate": "Warm & humid",
"code": 802528
},
{
"state": "Gujarat",
"district": "Junagadh",
"city": "Visavadar",
"climate": "Warm & humid",
"code": 802530
},
{
"state": "Gujarat",
"district": "Kachchh",
"city": "Anjar",
"climate": "Composite",
"code": 802444
},
{
"state": "Gujarat",
"district": "Kachchh",
"city": "Bhachau",
"climate": "Composite",
"code": 802443
},
{
"state": "Gujarat",
"district": "Kachchh",
"city": "Bhuj",
"climate": "Composite",
"code": 802445
},
{
"state": "Gujarat",
"district": "Kachchh",
"city": "Gandhidham",
"climate": "Composite",
"code": 802447
},
{
"state": "Gujarat",
"district": "Kachchh",
"city": "Mandvi",
"climate": "Composite",
"code": 802446
},
{
"state": "Gujarat",
"district": "Kachchh",
"city": "Mundra Baroi",
"climate": "Composite",
"code": 900605
},
{
"state": "Gujarat",
"district": "Kachchh",
"city": "Rapar",
"climate": "Composite",
"code": 802442
},
{
"state": "Gujarat",
"district": "Kheda",
"city": "Chakalasi",
"climate": "Warm & humid",
"code": 802577
},
{
"state": "Gujarat",
"district": "Kheda",
"city": "Dakor",
"climate": "Warm & humid",
"code": 802581
},
{
"state": "Gujarat",
"district": "Kheda",
"city": "Kanjari",
"climate": "Warm & humid",
"code": 802578
},
{
"state": "Gujarat",
"district": "Kheda",
"city": "Kapadwanj",
"climate": "Warm & humid",
"code": 802571
},
{
"state": "Gujarat",
"district": "Kheda",
"city": "Kathlal",
"climate": "Warm & humid",
"code": 802573
},
{
"state": "Gujarat",
"district": "Kheda",
"city": "Kheda",
"climate": "Warm & humid",
"code": 802575
},
{
"state": "Gujarat",
"district": "Kheda",
"city": "Mahudha",
"climate": "Warm & humid",
"code": 802579
},
{
"state": "Gujarat",
"district": "Kheda",
"city": "Mehemdabad",
"climate": "Warm & humid",
"code": 802574
},
{
"state": "Gujarat",
"district": "Kheda",
"city": "Nadiad",
"climate": "Warm & humid",
"code": 802576
},
{
"state": "Gujarat",
"district": "Kheda",
"city": "Thasra",
"climate": "Warm & humid",
"code": 802580
},
{
"state": "Gujarat",
"district": "Mahesana",
"city": "Kadi",
"climate": "Hot and Dry",
"code": 802465
},
{
"state": "Gujarat",
"district": "Mahesana",
"city": "Kheralu",
"climate": "Hot and Dry",
"code": 802459
},
{
"state": "Gujarat",
"district": "Mahesana",
"city": "Mahesana",
"climate": "Hot and Dry",
"code": 802464
},
{
"state": "Gujarat",
"district": "Mahesana",
"city": "Unjha",
"climate": "Hot and Dry",
"code": 802460
},
{
"state": "Gujarat",
"district": "Mahesana",
"city": "Vadnagar",
"climate": "Hot and Dry",
"code": 802462
},
{
"state": "Gujarat",
"district": "Mahesana",
"city": "Vijapur",
"climate": "Hot and Dry",
"code": 802463
},
{
"state": "Gujarat",
"district": "Mahesana",
"city": "Visnagar",
"climate": "Hot and Dry",
"code": 802461
},
{
"state": "Gujarat",
"district": "Mahisagar",
"city": "Balasinor",
"climate": "Hot and Dry",
"code": 802572
},
{
"state": "Gujarat",
"district": "Mahisagar",
"city": "Lunavada",
"climate": "Hot and Dry",
"code": 802583
},
{
"state": "Gujarat",
"district": "Mahisagar",
"city": "Santrampur",
"climate": "Hot and Dry",
"code": 802582
},
{
"state": "Gujarat",
"district": "Morbi",
"city": "Halvad",
"climate": "Composite",
"code": 802490
},
{
"state": "Gujarat",
"district": "Morbi",
"city": "Maliya Miyana",
"climate": "Composite",
"code": 802498
},
{
"state": "Gujarat",
"district": "Morbi",
"city": "Morbi",
"climate": "Composite",
"code": 802499
},
{
"state": "Gujarat",
"district": "Morbi",
"city": "Wankaner",
"climate": "Composite",
"code": 802500
},
{
"state": "Gujarat",
"district": "Narmada",
"city": "Rajpipla",
"climate": "Hot and Dry",
"code": 802603
},
{
"state": "Gujarat",
"district": "Navsari",
"city": "Bilimora",
"climate": "Hot and Dry",
"code": 802617
},
{
"state": "Gujarat",
"district": "Navsari",
"city": "Gandevi",
"climate": "Hot and Dry",
"code": 802616
},
{
"state": "Gujarat",
"district": "Navsari",
"city": "Navsari",
"climate": "Hot and Dry",
"code": 802614
},
{
"state": "Gujarat",
"district": "Panch Mahals",
"city": "Godhra",
"climate": "Hot and Dry",
"code": 802585
},
{
"state": "Gujarat",
"district": "Panch Mahals",
"city": "Halol",
"climate": "Hot and Dry",
"code": 802588
},
{
"state": "Gujarat",
"district": "Panch Mahals",
"city": "Kaalol",
"climate": "Hot and Dry",
"code": 802586
},
{
"state": "Gujarat",
"district": "Panch Mahals",
"city": "Shahera",
"climate": "Hot and Dry",
"code": 802584
},
{
"state": "Gujarat",
"district": "Patan",
"city": "Chanasma",
"climate": "Hot and Dry",
"code": 802458
},
{
"state": "Gujarat",
"district": "Patan",
"city": "Harij",
"climate": "Hot and Dry",
"code": 802457
},
{
"state": "Gujarat",
"district": "Patan",
"city": "Patan_Gu",
"climate": "Hot and Dry",
"code": 802456
},
{
"state": "Gujarat",
"district": "Patan",
"city": "Radhanpur",
"climate": "Hot and Dry",
"code": 802454
},
{
"state": "Gujarat",
"district": "Patan",
"city": "Siddhpur",
"climate": "Hot and Dry",
"code": 802455
},
{
"state": "Gujarat",
"district": "Porbandar",
"city": "Kutiyana",
"climate": "Warm & humid",
"code": 802525
},
{
"state": "Gujarat",
"district": "Porbandar",
"city": "Porbandar",
"climate": "Warm & humid",
"code": 802522
},
{
"state": "Gujarat",
"district": "Porbandar",
"city": "Ranavav",
"climate": "Warm & humid",
"code": 802524
},
{
"state": "Gujarat",
"district": "Rajkot",
"city": "Bhayavadar",
"climate": "Composite",
"code": 802505
},
{
"state": "Gujarat",
"district": "Rajkot",
"city": "Dhoraji",
"climate": "Composite",
"code": 802507
},
{
"state": "Gujarat",
"district": "Rajkot",
"city": "Gondal",
"climate": "Composite",
"code": 802504
},
{
"state": "Gujarat",
"district": "Rajkot",
"city": "Jasdan",
"climate": "Composite",
"code": 802503
},
{
"state": "Gujarat",
"district": "Rajkot",
"city": "Jetpur Navagadh",
"climate": "Composite",
"code": 802508
},
{
"state": "Gujarat",
"district": "Rajkot",
"city": "Rajkot",
"climate": "Composite",
"code": 802501
},
{
"state": "Gujarat",
"district": "Rajkot",
"city": "Upleta",
"climate": "Composite",
"code": 802506
},
{
"state": "Gujarat",
"district": "Sabar Kantha",
"city": "Himmatnagar",
"climate": "Hot and Dry",
"code": 802469
},
{
"state": "Gujarat",
"district": "Sabar Kantha",
"city": "Idar",
"climate": "Hot and Dry",
"code": 802468
},
{
"state": "Gujarat",
"district": "Sabar Kantha",
"city": "Khedbrahma",
"climate": "Hot and Dry",
"code": 802466
},
{
"state": "Gujarat",
"district": "Sabar Kantha",
"city": "Prantij",
"climate": "Hot and Dry",
"code": 802470
},
{
"state": "Gujarat",
"district": "Sabar Kantha",
"city": "Talod",
"climate": "Hot and Dry",
"code": 802471
},
{
"state": "Gujarat",
"district": "Sabar Kantha",
"city": "Vadali",
"climate": "Hot and Dry",
"code": 802467
},
{
"state": "Gujarat",
"district": "Surat",
"city": "Bardoli",
"climate": "Hot and Dry",
"code": 802634
},
{
"state": "Gujarat",
"district": "Surat",
"city": "Kadodara",
"climate": "Hot and Dry",
"code": 900198
},
{
"state": "Gujarat",
"district": "Surat",
"city": "Mandvi_S",
"climate": "Hot and Dry",
"code": 802628
},
{
"state": "Gujarat",
"district": "Surat",
"city": "Surat",
"climate": "Hot and Dry",
"code": 802629
},
{
"state": "Gujarat",
"district": "Surat",
"city": "Tarsadi",
"climate": "Hot and Dry",
"code": 802627
},
{
"state": "Gujarat",
"district": "Surendranagar Dudhrej",
"city": "Chotila",
"climate": "Hot and Dry",
"code": 802496
},
{
"state": "Gujarat",
"district": "Surendranagar Dudhrej",
"city": "Dhrangadhra",
"climate": "Hot and Dry",
"code": 802491
},
{
"state": "Gujarat",
"district": "Surendranagar Dudhrej",
"city": "Limbdi",
"climate": "Hot and Dry",
"code": 802497
},
{
"state": "Gujarat",
"district": "Surendranagar Dudhrej",
"city": "Patdi",
"climate": "Hot and Dry",
"code": 802492
},
{
"state": "Gujarat",
"district": "Surendranagar Dudhrej",
"city": "Surendranagar",
"climate": "Hot and Dry",
"code": 802493
},
{
"state": "Gujarat",
"district": "Surendranagar Dudhrej",
"city": "Thangadh",
"climate": "Hot and Dry",
"code": 802495
},
{
"state": "Gujarat",
"district": "Tapi",
"city": "Songadh",
"climate": "Hot and Dry",
"code": 802635
},
{
"state": "Gujarat",
"district": "Tapi",
"city": "Vyara",
"climate": "Hot and Dry",
"code": 802636
},
{
"state": "Gujarat",
"district": "Vadodara",
"city": "Dabhoi",
"climate": "Hot and Dry",
"code": 802600
},
{
"state": "Gujarat",
"district": "Vadodara",
"city": "Karjan",
"climate": "Hot and Dry",
"code": 802602
},
{
"state": "Gujarat",
"district": "Vadodara",
"city": "Padra",
"climate": "Hot and Dry",
"code": 802601
},
{
"state": "Gujarat",
"district": "Vadodara",
"city": "Savli",
"climate": "Hot and Dry",
"code": 802592
},
{
"state": "Gujarat",
"district": "Vadodara",
"city": "Vadodara",
"climate": "Hot and Dry",
"code": 802596
},
{
"state": "Gujarat",
"district": "Valsad",
"city": "Dharampur",
"climate": "Hot and Dry",
"code": 802620
},
{
"state": "Gujarat",
"district": "Valsad",
"city": "Pardi",
"climate": "Hot and Dry",
"code": 802621
},
{
"state": "Gujarat",
"district": "Valsad",
"city": "Umargam",
"climate": "Hot and Dry",
"code": 802625
},
{
"state": "Gujarat",
"district": "Valsad",
"city": "Valsad",
"climate": "Hot and Dry",
"code": 802618
},
{
"state": "Gujarat",
"district": "Valsad",
"city": "Vapi",
"climate": "Hot and Dry",
"code": 802622
},
{
"state": "Haryana",
"district": "Ambala",
"city": "Ambala",
"climate": "Composite",
"code": 800365
},
{
"state": "Haryana",
"district": "Ambala",
"city": "Ambala Cantonment",
"climate": "Composite",
"code": 800366
},
{
"state": "Haryana",
"district": "Ambala",
"city": "Ambala Sadar",
"climate": "Composite",
"code": 800367
},
{
"state": "Haryana",
"district": "Ambala",
"city": "Barara",
"climate": "Composite",
"code": 900228
},
{
"state": "Haryana",
"district": "Ambala",
"city": "Naraingarh",
"climate": "Composite",
"code": 800364
},
{
"state": "Haryana",
"district": "Bhiwani",
"city": "Bawani Khera",
"climate": "Composite",
"code": 800408
},
{
"state": "Haryana",
"district": "Bhiwani",
"city": "Bhiwani",
"climate": "Composite",
"code": 800409
},
{
"state": "Haryana",
"district": "Bhiwani",
"city": "Charkhi Dadri",
"climate": "Composite",
"code": 800412
},
{
"state": "Haryana",
"district": "Bhiwani",
"city": "Loharu",
"climate": "Composite",
"code": 800411
},
{
"state": "Haryana",
"district": "Bhiwani",
"city": "Siwani",
"climate": "Composite",
"code": 800410
},
{
"state": "Haryana",
"district": "Faridabad",
"city": "Faridabad",
"climate": "Composite",
"code": 800436
},
{
"state": "Haryana",
"district": "Fatehabad",
"city": "Bhuna",
"climate": "Composite",
"code": 900116
},
{
"state": "Haryana",
"district": "Fatehabad",
"city": "Fatehabad",
"climate": "Composite",
"code": 800398
},
{
"state": "Haryana",
"district": "Fatehabad",
"city": "Jakhal Mandi",
"climate": "Composite",
"code": 900513
},
{
"state": "Haryana",
"district": "Fatehabad",
"city": "Ratia",
"climate": "Composite",
"code": 800396
},
{
"state": "Haryana",
"district": "Fatehabad",
"city": "Tohana",
"climate": "Composite",
"code": 800397
},
{
"state": "Haryana",
"district": "Gurgaon",
"city": "Farrukhnagar",
"climate": "Composite",
"code": 800430
},
{
"state": "Haryana",
"district": "Gurgaon",
"city": "Gurgaon",
"climate": "Composite",
"code": 800429
},
{
"state": "Haryana",
"district": "Gurgaon",
"city": "Hailey Mandi",
"climate": "Composite",
"code": 800427
},
{
"state": "Haryana",
"district": "Gurgaon",
"city": "Manesar",
"climate": "Composite",
"code": 900672
},
{
"state": "Haryana",
"district": "Gurgaon",
"city": "Pataudi",
"climate": "Composite",
"code": 800428
},
{
"state": "Haryana",
"district": "Gurgaon",
"city": "Sohna",
"climate": "Composite",
"code": 800431
},
{
"state": "Haryana",
"district": "Hisar",
"city": "Adampur",
"climate": "Composite",
"code": 900676
},
{
"state": "Haryana",
"district": "Hisar",
"city": "Barwala",
"climate": "Composite",
"code": 800404
},
{
"state": "Haryana",
"district": "Hisar",
"city": "Hansi",
"climate": "Composite",
"code": 800407
},
{
"state": "Haryana",
"district": "Hisar",
"city": "Hisar",
"climate": "Composite",
"code": 800405
},
{
"state": "Haryana",
"district": "Hisar",
"city": "Narnaund",
"climate": "Composite",
"code": 800406
},
{
"state": "Haryana",
"district": "Hisar",
"city": "Uklana",
"climate": "Composite",
"code": 900117
},
{
"state": "Haryana",
"district": "Jhajjar",
"city": "Badli",
"climate": "Composite",
"code": 900674
},
{
"state": "Haryana",
"district": "Jhajjar",
"city": "Bahadurgarh",
"climate": "Composite",
"code": 800418
},
{
"state": "Haryana",
"district": "Jhajjar",
"city": "Beri",
"climate": "Composite",
"code": 800417
},
{
"state": "Haryana",
"district": "Jhajjar",
"city": "Jhajjar",
"climate": "Composite",
"code": 800419
},
{
"state": "Haryana",
"district": "Jind",
"city": "Jind",
"climate": "Composite",
"code": 800393
},
{
"state": "Haryana",
"district": "Jind",
"city": "Julana",
"climate": "Composite",
"code": 800394
},
{
"state": "Haryana",
"district": "Jind",
"city": "Narwana",
"climate": "Composite",
"code": 800391
},
{
"state": "Haryana",
"district": "Jind",
"city": "Safidon",
"climate": "Composite",
"code": 800395
},
{
"state": "Haryana",
"district": "Jind",
"city": "Uchana",
"climate": "Composite",
"code": 800392
},
{
"state": "Haryana",
"district": "Kaithal",
"city": "Cheeka",
"climate": "Composite",
"code": 800374
},
{
"state": "Haryana",
"district": "Kaithal",
"city": "Kaithal",
"climate": "Composite",
"code": 800375
},
{
"state": "Haryana",
"district": "Kaithal",
"city": "Kalayat",
"climate": "Composite",
"code": 800376
},
{
"state": "Haryana",
"district": "Kaithal",
"city": "Pundri",
"climate": "Composite",
"code": 800377
},
{
"state": "Haryana",
"district": "Kaithal",
"city": "Rajound",
"climate": "Composite",
"code": 900227
},
{
"state": "Haryana",
"district": "Kaithal",
"city": "Siwan",
"climate": "Composite",
"code": 900675
},
{
"state": "Haryana",
"district": "Karnal",
"city": "Assandh",
"climate": "Composite",
"code": 800383
},
{
"state": "Haryana",
"district": "Karnal",
"city": "Gharaunda",
"climate": "Composite",
"code": 800384
},
{
"state": "Haryana",
"district": "Karnal",
"city": "Indri",
"climate": "Composite",
"code": 800380
},
{
"state": "Haryana",
"district": "Karnal",
"city": "Karnal",
"climate": "Composite",
"code": 800381
},
{
"state": "Haryana",
"district": "Karnal",
"city": "Nilokheri",
"climate": "Composite",
"code": 800378
},
{
"state": "Haryana",
"district": "Karnal",
"city": "Nissing",
"climate": "Composite",
"code": 800382
},
{
"state": "Haryana",
"district": "Karnal",
"city": "Taraori",
"climate": "Composite",
"code": 800379
},
{
"state": "Haryana",
"district": "Kurukshetra",
"city": "Ismailabad",
"climate": "Composite",
"code": 900511
},
{
"state": "Haryana",
"district": "Kurukshetra",
"city": "Ladwa",
"climate": "Composite",
"code": 800373
},
{
"state": "Haryana",
"district": "Kurukshetra",
"city": "Pehowa",
"climate": "Composite",
"code": 800371
},
{
"state": "Haryana",
"district": "Kurukshetra",
"city": "Shahbad",
"climate": "Composite",
"code": 800370
},
{
"state": "Haryana",
"district": "Kurukshetra",
"city": "Thanesar",
"climate": "Composite",
"code": 800372
},
{
"state": "Haryana",
"district": "Mahendragarh",
"city": "Ateli",
"climate": "Composite",
"code": 800422
},
{
"state": "Haryana",
"district": "Mahendragarh",
"city": "Kanina",
"climate": "Composite",
"code": 800420
},
{
"state": "Haryana",
"district": "Mahendragarh",
"city": "Mahendragarh",
"climate": "Composite",
"code": 800421
},
{
"state": "Haryana",
"district": "Mahendragarh",
"city": "Nangal Chaudhary",
"climate": "Composite",
"code": 900115
},
{
"state": "Haryana",
"district": "Mahendragarh",
"city": "Narnaul",
"climate": "Composite",
"code": 800423
},
{
"state": "Haryana",
"district": "Mewat",
"city": "Ferozepur Jhirka",
"climate": "Composite",
"code": 800434
},
{
"state": "Haryana",
"district": "Mewat",
"city": "Nuh",
"climate": "Composite",
"code": 800433
},
{
"state": "Haryana",
"district": "Mewat",
"city": "Punahana",
"climate": "Composite",
"code": 800435
},
{
"state": "Haryana",
"district": "Mewat",
"city": "Taoru",
"climate": "Composite",
"code": 800432
},
{
"state": "Haryana",
"district": "Palwal",
"city": "Hathin",
"climate": "Composite",
"code": 800438
},
{
"state": "Haryana",
"district": "Palwal",
"city": "Hodal",
"climate": "Composite",
"code": 800440
},
{
"state": "Haryana",
"district": "Palwal",
"city": "Palwal",
"climate": "Composite",
"code": 800437
},
{
"state": "Haryana",
"district": "Panchkula",
"city": "Kalka",
"climate": "Composite",
"code": 800361
},
{
"state": "Haryana",
"district": "Panchkula",
"city": "Panchkula",
"climate": "Composite",
"code": 800363
},
{
"state": "Haryana",
"district": "Panipat",
"city": "Panipat",
"climate": "Composite",
"code": 800385
},
{
"state": "Haryana",
"district": "Panipat",
"city": "Samalkha",
"climate": "Composite",
"code": 800386
},
{
"state": "Haryana",
"district": "Rewari",
"city": "Bawal",
"climate": "Composite",
"code": 800426
},
{
"state": "Haryana",
"district": "Rewari",
"city": "Dharuhera",
"climate": "Composite",
"code": 800424
},
{
"state": "Haryana",
"district": "Rewari",
"city": "Rewari",
"climate": "Composite",
"code": 800425
},
{
"state": "Haryana",
"district": "Rohtak",
"city": "Kalanaur",
"climate": "Composite",
"code": 800415
},
{
"state": "Haryana",
"district": "Rohtak",
"city": "Maham",
"climate": "Composite",
"code": 800413
},
{
"state": "Haryana",
"district": "Rohtak",
"city": "Rohtak",
"climate": "Composite",
"code": 800414
},
{
"state": "Haryana",
"district": "Rohtak",
"city": "Sampla",
"climate": "Composite",
"code": 800416
},
{
"state": "Haryana",
"district": "Sirsa",
"city": "Ellenabad",
"climate": "Composite",
"code": 800403
},
{
"state": "Haryana",
"district": "Sirsa",
"city": "Kalanwali",
"climate": "Composite",
"code": 800400
},
{
"state": "Haryana",
"district": "Sirsa",
"city": "Mandi Dabwali",
"climate": "Composite",
"code": 800399
},
{
"state": "Haryana",
"district": "Sirsa",
"city": "Rania",
"climate": "Composite",
"code": 800402
},
{
"state": "Haryana",
"district": "Sirsa",
"city": "Sirsa",
"climate": "Composite",
"code": 800401
},
{
"state": "Haryana",
"district": "Sonipat",
"city": "Ganaur",
"climate": "Composite",
"code": 800388
},
{
"state": "Haryana",
"district": "Sonipat",
"city": "Gohana",
"climate": "Composite",
"code": 800387
},
{
"state": "Haryana",
"district": "Sonipat",
"city": "Kharkhoda",
"climate": "Composite",
"code": 800390
},
{
"state": "Haryana",
"district": "Sonipat",
"city": "Kundli",
"climate": "Composite",
"code": 900510
},
{
"state": "Haryana",
"district": "Sonipat",
"city": "Sonipat",
"climate": "Composite",
"code": 800389
},
{
"state": "Haryana",
"district": "Yamunanagar",
"city": "Radaur",
"climate": "Composite",
"code": 900322
},
{
"state": "Haryana",
"district": "Yamunanagar",
"city": "Sadhaura",
"climate": "Composite",
"code": 900512
},
{
"state": "Haryana",
"district": "Yamunanagar",
"city": "Yamunanagar",
"climate": "Composite",
"code": 800369
},
{
"state": "Himachal Pradesh",
"district": "Bilaspur",
"city": "Bilaspur",
"climate": "Composite",
"code": 800121
},
{
"state": "Himachal Pradesh",
"district": "Bilaspur",
"city": "Ghumarwin",
"climate": "Composite",
"code": 800118
},
{
"state": "Himachal Pradesh",
"district": "Bilaspur",
"city": "Naina Devi",
"climate": "Composite",
"code": 800120
},
{
"state": "Himachal Pradesh",
"district": "Bilaspur",
"city": "Talai",
"climate": "Composite",
"code": 800119
},
{
"state": "Himachal Pradesh",
"district": "Chamba",
"city": "Bakloh Cantonment",
"climate": "Cold",
"code": 800089
},
{
"state": "Himachal Pradesh",
"district": "Chamba",
"city": "Chamba",
"climate": "Cold",
"code": 800091
},
{
"state": "Himachal Pradesh",
"district": "Chamba",
"city": "Chuari Khas",
"climate": "Cold",
"code": 800090
},
{
"state": "Himachal Pradesh",
"district": "Chamba",
"city": "Dalhousie",
"climate": "Cold",
"code": 800088
},
{
"state": "Himachal Pradesh",
"district": "Chamba",
"city": "Dalhousie Cantonment",
"climate": "Cold",
"code": 800087
},
{
"state": "Himachal Pradesh",
"district": "Hamirpur",
"city": "Bhota",
"climate": "Composite",
"code": 800112
},
{
"state": "Himachal Pradesh",
"district": "Hamirpur",
"city": "Hamirpur",
"climate": "Composite",
"code": 800111
},
{
"state": "Himachal Pradesh",
"district": "Hamirpur",
"city": "Nadaun",
"climate": "Composite",
"code": 800110
},
{
"state": "Himachal Pradesh",
"district": "Hamirpur",
"city": "Sujanpur",
"climate": "Composite",
"code": 800109
},
{
"state": "Himachal Pradesh",
"district": "Kangra",
"city": "Dera Gopipur",
"climate": "Composite",
"code": 800097
},
{
"state": "Himachal Pradesh",
"district": "Kangra",
"city": "Dharmsala",
"climate": "Composite",
"code": 800093
},
{
"state": "Himachal Pradesh",
"district": "Kangra",
"city": "Jawalamukhi",
"climate": "Composite",
"code": 800098
},
{
"state": "Himachal Pradesh",
"district": "Kangra",
"city": "Jawali",
"climate": "Composite",
"code": 900460
},
{
"state": "Himachal Pradesh",
"district": "Kangra",
"city": "Kangra",
"climate": "Composite",
"code": 800095
},
{
"state": "Himachal Pradesh",
"district": "Kangra",
"city": "Nagrota Bagwan",
"climate": "Composite",
"code": 800096
},
{
"state": "Himachal Pradesh",
"district": "Kangra",
"city": "Nurpur",
"climate": "Composite",
"code": 800092
},
{
"state": "Himachal Pradesh",
"district": "Kangra",
"city": "Palampur",
"climate": "Composite",
"code": 800099
},
{
"state": "Himachal Pradesh",
"district": "Kangra",
"city": "Shahpur",
"climate": "Composite",
"code": 900811
},
{
"state": "Himachal Pradesh",
"district": "Kangra",
"city": "Yol Cantonment",
"climate": "Composite",
"code": 800094
},
{
"state": "Himachal Pradesh",
"district": "Kullu",
"city": "Ani",
"climate": "Cold",
"code": 900809
},
{
"state": "Himachal Pradesh",
"district": "Kullu",
"city": "Banjar",
"climate": "Cold",
"code": 800103
},
{
"state": "Himachal Pradesh",
"district": "Kullu",
"city": "Bhuntar",
"climate": "Cold",
"code": 800102
},
{
"state": "Himachal Pradesh",
"district": "Kullu",
"city": "Kullu",
"climate": "Cold",
"code": 800101
},
{
"state": "Himachal Pradesh",
"district": "Kullu",
"city": "Manali",
"climate": "Cold",
"code": 800100
},
{
"state": "Himachal Pradesh",
"district": "Kullu",
"city": "Nirmand",
"climate": "Cold",
"code": 900808
},
{
"state": "Himachal Pradesh",
"district": "Mandi",
"city": "Baijnathpaprola",
"climate": "Composite",
"code": 900500
},
{
"state": "Himachal Pradesh",
"district": "Mandi",
"city": "Jogindarnagar",
"climate": "Composite",
"code": 800104
},
{
"state": "Himachal Pradesh",
"district": "Mandi",
"city": "Karsog",
"climate": "Composite",
"code": 900134
},
{
"state": "Himachal Pradesh",
"district": "Mandi",
"city": "Mandi",
"climate": "Composite",
"code": 800107
},
{
"state": "Himachal Pradesh",
"district": "Mandi",
"city": "Nerchowk",
"climate": "Composite",
"code": 900470
},
{
"state": "Himachal Pradesh",
"district": "Mandi",
"city": "Rawalsar",
"climate": "Composite",
"code": 800108
},
{
"state": "Himachal Pradesh",
"district": "Mandi",
"city": "Sarkaghat",
"climate": "Composite",
"code": 800105
},
{
"state": "Himachal Pradesh",
"district": "Mandi",
"city": "Sundarnagar",
"climate": "Composite",
"code": 800106
},
{
"state": "Himachal Pradesh",
"district": "Shimla",
"city": "Chaupal",
"climate": "Cold",
"code": 800139
},
{
"state": "Himachal Pradesh",
"district": "Shimla",
"city": "Chirgaon",
"climate": "Cold",
"code": 900805
},
{
"state": "Himachal Pradesh",
"district": "Shimla",
"city": "Jubbal",
"climate": "Cold",
"code": 800140
},
{
"state": "Himachal Pradesh",
"district": "Shimla",
"city": "Jutogh Cantonment",
"climate": "Cold",
"code": 800136
},
{
"state": "Himachal Pradesh",
"district": "Shimla",
"city": "Kotkhai",
"climate": "Cold",
"code": 800141
},
{
"state": "Himachal Pradesh",
"district": "Shimla",
"city": "Narkanda",
"climate": "Cold",
"code": 800134
},
{
"state": "Himachal Pradesh",
"district": "Shimla",
"city": "Nerwa",
"climate": "Cold",
"code": 900806
},
{
"state": "Himachal Pradesh",
"district": "Shimla",
"city": "Rampur",
"climate": "Cold",
"code": 800133
},
{
"state": "Himachal Pradesh",
"district": "Shimla",
"city": "Rohru",
"climate": "Cold",
"code": 800142
},
{
"state": "Himachal Pradesh",
"district": "Shimla",
"city": "Seoni",
"climate": "Cold",
"code": 800135
},
{
"state": "Himachal Pradesh",
"district": "Shimla",
"city": "Shimla",
"climate": "Cold",
"code": 800137
},
{
"state": "Himachal Pradesh",
"district": "Shimla",
"city": "Theog",
"climate": "Cold",
"code": 800138
},
{
"state": "Himachal Pradesh",
"district": "Sirmour",
"city": "Nahan",
"climate": "Composite",
"code": 800131
},
{
"state": "Himachal Pradesh",
"district": "Sirmour",
"city": "Paonta Sahib",
"climate": "Composite",
"code": 800132
},
{
"state": "Himachal Pradesh",
"district": "Sirmour",
"city": "Rajgarh",
"climate": "Composite",
"code": 800130
},
{
"state": "Himachal Pradesh",
"district": "Solan",
"city": "Arki",
"climate": "Composite",
"code": 800122
},
{
"state": "Himachal Pradesh",
"district": "Solan",
"city": "Baddi",
"climate": "Composite",
"code": 800124
},
{
"state": "Himachal Pradesh",
"district": "Solan",
"city": "Dagshai Cantonment",
"climate": "Composite",
"code": 800127
},
{
"state": "Himachal Pradesh",
"district": "Solan",
"city": "Kandaghat",
"climate": "Composite",
"code": 900807
},
{
"state": "Himachal Pradesh",
"district": "Solan",
"city": "Kasauli Cantonment",
"climate": "Composite",
"code": 800125
},
{
"state": "Himachal Pradesh",
"district": "Solan",
"city": "Nalagarh",
"climate": "Composite",
"code": 800123
},
{
"state": "Himachal Pradesh",
"district": "Solan",
"city": "Parwanoo",
"climate": "Composite",
"code": 800126
},
{
"state": "Himachal Pradesh",
"district": "Solan",
"city": "Sabathu Cantonment",
"climate": "Composite",
"code": 800129
},
{
"state": "Himachal Pradesh",
"district": "Solan",
"city": "Solan",
"climate": "Composite",
"code": 800128
},
{
"state": "Himachal Pradesh",
"district": "Una",
"city": "Amb",
"climate": "Composite",
"code": 900810
},
{
"state": "Himachal Pradesh",
"district": "Una",
"city": "Daulatpur",
"climate": "Composite",
"code": 800113
},
{
"state": "Himachal Pradesh",
"district": "Una",
"city": "Gagret",
"climate": "Composite",
"code": 800114
},
{
"state": "Himachal Pradesh",
"district": "Una",
"city": "Mehatpur Basdehra",
"climate": "Composite",
"code": 800116
},
{
"state": "Himachal Pradesh",
"district": "Una",
"city": "Santokhgarh",
"climate": "Composite",
"code": 800117
},
{
"state": "Himachal Pradesh",
"district": "Una",
"city": "Tahliwal",
"climate": "Composite",
"code": 900238
},
{
"state": "Himachal Pradesh",
"district": "Una",
"city": "Una",
"climate": "Composite",
"code": 800115
},
{
"state": "Jammu & Kashmir",
"district": "Anantnag",
"city": "Achhabal",
"climate": "Cold",
"code": 800034
},
{
"state": "Jammu & Kashmir",
"district": "Anantnag",
"city": "Aishmuquam",
"climate": "Cold",
"code": 800029
},
{
"state": "Jammu & Kashmir",
"district": "Anantnag",
"city": "Bijbehara",
"climate": "Cold",
"code": 800030
},
{
"state": "Jammu & Kashmir",
"district": "Anantnag",
"city": "Duru Verinag",
"climate": "Cold",
"code": 800039
},
{
"state": "Jammu & Kashmir",
"district": "Anantnag",
"city": "Koker Nag",
"climate": "Cold",
"code": 800037
},
{
"state": "Jammu & Kashmir",
"district": "Anantnag",
"city": "Mattan",
"climate": "Cold",
"code": 800032
},
{
"state": "Jammu & Kashmir",
"district": "Anantnag",
"city": "Pahalgam",
"climate": "Cold",
"code": 800028
},
{
"state": "Jammu & Kashmir",
"district": "Anantnag",
"city": "Qazi Gund",
"climate": "Cold",
"code": 800038
},
{
"state": "Jammu & Kashmir",
"district": "Anantnag",
"city": "Seer Hamdan",
"climate": "Cold",
"code": 800035
},
{
"state": "Jammu & Kashmir",
"district": "Badgam",
"city": "Badgam",
"climate": "Cold",
"code": 800019
},
{
"state": "Jammu & Kashmir",
"district": "Badgam",
"city": "Beerwah",
"climate": "Cold",
"code": 800017
},
{
"state": "Jammu & Kashmir",
"district": "Badgam",
"city": "Chadura",
"climate": "Cold",
"code": 800020
},
{
"state": "Jammu & Kashmir",
"district": "Badgam",
"city": "Charar-I-Sharief",
"climate": "Cold",
"code": 800021
},
{
"state": "Jammu & Kashmir",
"district": "Badgam",
"city": "Khansahib",
"climate": "Cold",
"code": 800018
},
{
"state": "Jammu & Kashmir",
"district": "Badgam",
"city": "Magam",
"climate": "Cold",
"code": 800016
},
{
"state": "Jammu & Kashmir",
"district": "Bandipore",
"city": "Bandipore",
"climate": "Cold",
"code": 800010
},
{
"state": "Jammu & Kashmir",
"district": "Bandipore",
"city": "Hajan",
"climate": "Cold",
"code": 800011
},
{
"state": "Jammu & Kashmir",
"district": "Bandipore",
"city": "Srinagar",
"climate": "Cold",
"code": 800013
},
{
"state": "Jammu & Kashmir",
"district": "Bandipore",
"city": "Sumbal",
"climate": "Cold",
"code": 800012
},
{
"state": "Jammu & Kashmir",
"district": "Baramula",
"city": "Baramula",
"climate": "Cold",
"code": 800006
},
{
"state": "Jammu & Kashmir",
"district": "Baramula",
"city": "Kunzer",
"climate": "Cold",
"code": 800008
},
{
"state": "Jammu & Kashmir",
"district": "Baramula",
"city": "Pattan",
"climate": "Cold",
"code": 800005
},
{
"state": "Jammu & Kashmir",
"district": "Baramula",
"city": "Sopore",
"climate": "Cold",
"code": 800003
},
{
"state": "Jammu & Kashmir",
"district": "Baramula",
"city": "Tangmarg",
"climate": "Cold",
"code": 800009
},
{
"state": "Jammu & Kashmir",
"district": "Baramula",
"city": "Uri",
"climate": "Cold",
"code": 800007
},
{
"state": "Jammu & Kashmir",
"district": "Baramula",
"city": "Watra Gam",
"climate": "Cold",
"code": 800004
},
{
"state": "Jammu & Kashmir",
"district": "Doda",
"city": "Bhaderwah",
"climate": "Cold",
"code": 800050
},
{
"state": "Jammu & Kashmir",
"district": "Doda",
"city": "Doda",
"climate": "Cold",
"code": 800049
},
{
"state": "Jammu & Kashmir",
"district": "Doda",
"city": "Thathri",
"climate": "Cold",
"code": 900181
},
{
"state": "Jammu & Kashmir",
"district": "Ganderbal",
"city": "Ganderbal",
"climate": "Cold",
"code": 800015
},
{
"state": "Jammu & Kashmir",
"district": "Jammu",
"city": "Akhnoor",
"climate": "Cold",
"code": 800069
},
{
"state": "Jammu & Kashmir",
"district": "Jammu",
"city": "Arnia",
"climate": "Cold",
"code": 800076
},
{
"state": "Jammu & Kashmir",
"district": "Jammu",
"city": "Bishna",
"climate": "Cold",
"code": 800075
},
{
"state": "Jammu & Kashmir",
"district": "Jammu",
"city": "Ghomanhasan",
"climate": "Cold",
"code": 800073
},
{
"state": "Jammu & Kashmir",
"district": "Jammu",
"city": "Jammu",
"climate": "Cold",
"code": 800071
},
{
"state": "Jammu & Kashmir",
"district": "Jammu",
"city": "Jammu Cantonment",
"climate": "Cold",
"code": 800072
},
{
"state": "Jammu & Kashmir",
"district": "Jammu",
"city": "Jourian",
"climate": "Cold",
"code": 800068
},
{
"state": "Jammu & Kashmir",
"district": "Jammu",
"city": "Khore",
"climate": "Cold",
"code": 800070
},
{
"state": "Jammu & Kashmir",
"district": "Jammu",
"city": "R.S. Pora",
"climate": "Cold",
"code": 800074
},
{
"state": "Jammu & Kashmir",
"district": "Kathua",
"city": "Bashohli",
"climate": "Cold",
"code": 800082
},
{
"state": "Jammu & Kashmir",
"district": "Kathua",
"city": "Billawar",
"climate": "Cold",
"code": 800081
},
{
"state": "Jammu & Kashmir",
"district": "Kathua",
"city": "Hiranagar",
"climate": "Cold",
"code": 800086
},
{
"state": "Jammu & Kashmir",
"district": "Kathua",
"city": "Kathua",
"climate": "Cold",
"code": 800084
},
{
"state": "Jammu & Kashmir",
"district": "Kathua",
"city": "Lakhanpur",
"climate": "Cold",
"code": 800083
},
{
"state": "Jammu & Kashmir",
"district": "Kathua",
"city": "Parole",
"climate": "Cold",
"code": 800085
},
{
"state": "Jammu & Kashmir",
"district": "Kishtwar",
"city": "Kishtwar",
"climate": "Cold",
"code": 800054
},
{
"state": "Jammu & Kashmir",
"district": "Kulgam",
"city": "Devsar",
"climate": "Cold",
"code": 800046
},
{
"state": "Jammu & Kashmir",
"district": "Kulgam",
"city": "Frisal",
"climate": "Cold",
"code": 800042
},
{
"state": "Jammu & Kashmir",
"district": "Kulgam",
"city": "Kulgam",
"climate": "Cold",
"code": 800040
},
{
"state": "Jammu & Kashmir",
"district": "Kulgam",
"city": "Yari Pora",
"climate": "Cold",
"code": 800043
},
{
"state": "Jammu & Kashmir",
"district": "Kupwara",
"city": "Handwara",
"climate": "Cold",
"code": 800002
},
{
"state": "Jammu & Kashmir",
"district": "Kupwara",
"city": "Kupwara",
"climate": "Cold",
"code": 800001
},
{
"state": "Jammu & Kashmir",
"district": "Kupwara",
"city": "Langate",
"climate": "Cold",
"code": 900173
},
{
"state": "Jammu & Kashmir",
"district": "Pulwama",
"city": "Awantipora",
"climate": "Cold",
"code": 800024
},
{
"state": "Jammu & Kashmir",
"district": "Pulwama",
"city": "Khrew",
"climate": "Cold",
"code": 800023
},
{
"state": "Jammu & Kashmir",
"district": "Pulwama",
"city": "Pampore",
"climate": "Cold",
"code": 800022
},
{
"state": "Jammu & Kashmir",
"district": "Pulwama",
"city": "Pulwama",
"climate": "Cold",
"code": 800026
},
{
"state": "Jammu & Kashmir",
"district": "Pulwama",
"city": "Tral",
"climate": "Cold",
"code": 800025
},
{
"state": "Jammu & Kashmir",
"district": "Punch",
"city": "Punch",
"climate": "Cold",
"code": 800062
},
{
"state": "Jammu & Kashmir",
"district": "Punch",
"city": "Surankote",
"climate": "Cold",
"code": 800063
},
{
"state": "Jammu & Kashmir",
"district": "Rajouri",
"city": "Kalakote",
"climate": "Cold",
"code": 900150
},
{
"state": "Jammu & Kashmir",
"district": "Rajouri",
"city": "Nowshehra",
"climate": "Cold",
"code": 800066
},
{
"state": "Jammu & Kashmir",
"district": "Rajouri",
"city": "Rajauri",
"climate": "Cold",
"code": 800065
},
{
"state": "Jammu & Kashmir",
"district": "Rajouri",
"city": "Sunderbani",
"climate": "Cold",
"code": 800067
},
{
"state": "Jammu & Kashmir",
"district": "Rajouri",
"city": "Thanamandi",
"climate": "Cold",
"code": 800064
},
{
"state": "Jammu & Kashmir",
"district": "Ramban",
"city": "Banihal",
"climate": "Cold",
"code": 800051
},
{
"state": "Jammu & Kashmir",
"district": "Ramban",
"city": "Batote",
"climate": "Cold",
"code": 800053
},
{
"state": "Jammu & Kashmir",
"district": "Ramban",
"city": "Ramban",
"climate": "Cold",
"code": 800052
},
{
"state": "Jammu & Kashmir",
"district": "Reasi",
"city": "Katra",
"climate": "Cold",
"code": 800061
},
{
"state": "Jammu & Kashmir",
"district": "Reasi",
"city": "Reasi",
"climate": "Cold",
"code": 800059
},
{
"state": "Jammu & Kashmir",
"district": "Samba",
"city": "Bari Brahamana",
"climate": "Cold",
"code": 800077
},
{
"state": "Jammu & Kashmir",
"district": "Samba",
"city": "Ramgarh",
"climate": "Cold",
"code": 800080
},
{
"state": "Jammu & Kashmir",
"district": "Samba",
"city": "Samba",
"climate": "Cold",
"code": 800079
},
{
"state": "Jammu & Kashmir",
"district": "Samba",
"city": "Vijay Pur",
"climate": "Cold",
"code": 800078
},
{
"state": "Jammu & Kashmir",
"district": "Shupiyan",
"city": "Shupiyan",
"climate": "Cold",
"code": 800027
},
{
"state": "Jammu & Kashmir",
"district": "Srinagar",
"city": "Anantnag",
"climate": "Cold",
"code": 800033
},
{
"state": "Jammu & Kashmir",
"district": "Srinagar",
"city": "Badamibagh Cantonment",
"climate": "Cold",
"code": 800014
},
{
"state": "Jammu & Kashmir",
"district": "Udhampur",
"city": "Chenani",
"climate": "Cold",
"code": 800057
},
{
"state": "Jammu & Kashmir",
"district": "Udhampur",
"city": "Ram Nagar",
"climate": "Cold",
"code": 800058
},
{
"state": "Jammu & Kashmir",
"district": "Udhampur",
"city": "Udhampur",
"climate": "Cold",
"code": 800055
},
{
"state": "Jharkhand",
"district": "Bokaro",
"city": "Chas",
"climate": "Composite",
"code": 801778
},
{
"state": "Jharkhand",
"district": "Bokaro",
"city": "Phusro",
"climate": "Composite",
"code": 801777
},
{
"state": "Jharkhand",
"district": "Chatra",
"city": "Chatra",
"climate": "Composite",
"code": 801765
},
{
"state": "Jharkhand",
"district": "Deoghar",
"city": "Deoghar",
"climate": "Composite",
"code": 801769
},
{
"state": "Jharkhand",
"district": "Deoghar",
"city": "Madhupur",
"climate": "Composite",
"code": 801770
},
{
"state": "Jharkhand",
"district": "Dhanbad",
"city": "Chirkunda",
"climate": "Composite",
"code": 801776
},
{
"state": "Jharkhand",
"district": "Dhanbad",
"city": "Dhanbad",
"climate": "Composite",
"code": 801775
},
{
"state": "Jharkhand",
"district": "Dumka",
"city": "Basukinath",
"climate": "Warm & humid",
"code": 801790
},
{
"state": "Jharkhand",
"district": "Dumka",
"city": "Dumka",
"climate": "Warm & humid",
"code": 801791
},
{
"state": "Jharkhand",
"district": "East Singhbhum",
"city": "Chakulia",
"climate": "Warm & humid",
"code": 801783
},
{
"state": "Jharkhand",
"district": "East Singhbhum",
"city": "Jamshedpur",
"climate": "Warm & humid",
"code": 801781
},
{
"state": "Jharkhand",
"district": "East Singhbhum",
"city": "Jugsalai",
"climate": "Warm & humid",
"code": 801782
},
{
"state": "Jharkhand",
"district": "East Singhbhum",
"city": "Mango",
"climate": "Warm & humid",
"code": 801780
},
{
"state": "Jharkhand",
"district": "Garhwa",
"city": "Garhwa",
"climate": "Composite",
"code": 801764
},
{
"state": "Jharkhand",
"district": "Garhwa",
"city": "Majhion",
"climate": "Composite",
"code": 801763
},
{
"state": "Jharkhand",
"district": "Garhwa",
"city": "Nagar Untari",
"climate": "Composite",
"code": 900234
},
{
"state": "Jharkhand",
"district": "Garhwa",
"city": "S. B. Nagar",
"climate": "Composite"
},
{
"state": "Jharkhand",
"district": "Giridih",
"city": "Badaki Suriya",
"climate": "Composite",
"code": 900818
},
{
"state": "Jharkhand",
"district": "Giridih",
"city": "Dhanwar",
"climate": "Composite",
"code": 900821
},
{
"state": "Jharkhand",
"district": "Giridih",
"city": "Giridih",
"climate": "Composite",
"code": 801768
},
{
"state": "Jharkhand",
"district": "Godda",
"city": "Godda",
"climate": "Warm & humid",
"code": 801771
},
{
"state": "Jharkhand",
"district": "Godda",
"city": "Mahgama",
"climate": "Warm & humid",
"code": 900825
},
{
"state": "Jharkhand",
"district": "Gumla",
"city": "Gumla",
"climate": "Composite",
"code": 801797
},
{
"state": "Jharkhand",
"district": "Hazaribagh",
"city": "Hazaribag",
"climate": "Composite",
"code": 801788
},
{
"state": "Jharkhand",
"district": "Jamtara",
"city": "Jamtara",
"climate": "Composite",
"code": 801792
},
{
"state": "Jharkhand",
"district": "Jamtara",
"city": "Mihijam",
"climate": "Composite",
"code": 801793
},
{
"state": "Jharkhand",
"district": "Khunti",
"city": "Khunti",
"climate": "Composite",
"code": 801796
},
{
"state": "Jharkhand",
"district": "Kodarma",
"city": "Domchanch",
"climate": "Composite",
"code": 900822
},
{
"state": "Jharkhand",
"district": "Kodarma",
"city": "Jhumri Tilaiya",
"climate": "Composite",
"code": 801767
},
{
"state": "Jharkhand",
"district": "Kodarma",
"city": "Kodarma",
"climate": "Composite",
"code": 801766
},
{
"state": "Jharkhand",
"district": "Latehar",
"city": "Latehar",
"climate": "Composite",
"code": 801787
},
{
"state": "Jharkhand",
"district": "Lohardaga",
"city": "Lohardaga",
"climate": "Composite",
"code": 801779
},
{
"state": "Jharkhand",
"district": "Pakur",
"city": "Pakur",
"climate": "Warm & humid",
"code": 801774
},
{
"state": "Jharkhand",
"district": "Palamu",
"city": "Bishrampur",
"climate": "Composite",
"code": 801785
},
{
"state": "Jharkhand",
"district": "Palamu",
"city": "Chhatarpur",
"climate": "Composite",
"code": 900820
},
{
"state": "Jharkhand",
"district": "Palamu",
"city": "Hariharganj",
"climate": "Composite",
"code": 900823
},
{
"state": "Jharkhand",
"district": "Palamu",
"city": "Hussainabad",
"climate": "Composite",
"code": 801784
},
{
"state": "Jharkhand",
"district": "Palamu",
"city": "Medininagar",
"climate": "Composite",
"code": 801786
},
{
"state": "Jharkhand",
"district": "Ramgarh",
"city": "Ramgarh Cantonment",
"climate": "Composite",
"code": 900487
},
{
"state": "Jharkhand",
"district": "Ramgarh",
"city": "Ramgarh Nagar Parishad",
"climate": "Composite",
"code": 801789
},
{
"state": "Jharkhand",
"district": "Ranchi",
"city": "Bundu",
"climate": "Composite",
"code": 801795
},
{
"state": "Jharkhand",
"district": "Ranchi",
"city": "Ranchi",
"climate": "Composite",
"code": 801794
},
{
"state": "Jharkhand",
"district": "Sahebganj",
"city": "Barharwa",
"climate": "Warm & humid",
"code": 900819
},
{
"state": "Jharkhand",
"district": "Sahebganj",
"city": "Rajmahal",
"climate": "Warm & humid",
"code": 801773
},
{
"state": "Jharkhand",
"district": "Sahebganj",
"city": "Sahibganj",
"climate": "Warm & humid",
"code": 801772
},
{
"state": "Jharkhand",
"district": "Saraikela - Kharswan",
"city": "Adityapur",
"climate": "Composite",
"code": 801801
},
{
"state": "Jharkhand",
"district": "Saraikela - Kharswan",
"city": "Kapali",
"climate": "Composite",
"code": 900824
},
{
"state": "Jharkhand",
"district": "Saraikela - Kharswan",
"city": "Seraikela",
"climate": "Composite",
"code": 801802
},
{
"state": "Jharkhand",
"district": "Simdega",
"city": "Simdega",
"climate": "Warm & humid",
"code": 801798
},
{
"state": "Jharkhand",
"district": "West Singhbhum",
"city": "Chaibasa",
"climate": "Warm & humid",
"code": 801800
},
{
"state": "Jharkhand",
"district": "West Singhbhum",
"city": "Chakardharpur",
"climate": "Warm & humid",
"code": 801799
},
{
"state": "Karnataka",
"district": "Bagalkote",
"city": "Ameenagada",
"climate": "Warm & humid",
"code": 900419
},
{
"state": "Karnataka",
"district": "Bagalkote",
"city": "Badami",
"climate": "Warm & humid",
"code": 803046
},
{
"state": "Karnataka",
"district": "Bagalkote",
"city": "Bagalkot",
"climate": "Warm & humid",
"code": 803048
},
{
"state": "Karnataka",
"district": "Bagalkote",
"city": "Belagali",
"climate": "Warm & humid",
"code": 900420
},
{
"state": "Karnataka",
"district": "Bagalkote",
"city": "Bilgi",
"climate": "Warm & humid",
"code": 803043
},
{
"state": "Karnataka",
"district": "Bagalkote",
"city": "Guledgudda",
"climate": "Warm & humid",
"code": 803047
},
{
"state": "Karnataka",
"district": "Bagalkote",
"city": "Hungund",
"climate": "Warm & humid",
"code": 803049
},
{
"state": "Karnataka",
"district": "Bagalkote",
"city": "Ilkal",
"climate": "Warm & humid",
"code": 803050
},
{
"state": "Karnataka",
"district": "Bagalkote",
"city": "Jamkhandi",
"climate": "Warm & humid",
"code": 803041
},
{
"state": "Karnataka",
"district": "Bagalkote",
"city": "Kamatagi",
"climate": "Warm & humid",
"code": 900421
},
{
"state": "Karnataka",
"district": "Bagalkote",
"city": "Kerur",
"climate": "Warm & humid",
"code": 803045
},
{
"state": "Karnataka",
"district": "Bagalkote",
"city": "Lokapura",
"climate": "Warm & humid",
"code": 900765
},
{
"state": "Karnataka",
"district": "Bagalkote",
"city": "Mahalingpur",
"climate": "Warm & humid",
"code": 803039
},
{
"state": "Karnataka",
"district": "Bagalkote",
"city": "Mudhol",
"climate": "Warm & humid",
"code": 803044
},
{
"state": "Karnataka",
"district": "Bagalkote",
"city": "Rabkavi Banhatti",
"climate": "Warm & humid",
"code": 803042
},
{
"state": "Karnataka",
"district": "Bagalkote",
"city": "Shiruru",
"climate": "Warm & humid",
"code": 900669
},
{
"state": "Karnataka",
"district": "Bagalkote",
"city": "Terdal",
"climate": "Warm & humid",
"code": 803040
},
{
"state": "Karnataka",
"district": "Ballary",
"city": "Bellary",
"climate": "Warm & humid",
"code": 803114
},
{
"state": "Karnataka",
"district": "Ballary",
"city": "Hagaribommanahalli",
"climate": "Warm & humid",
"code": 900399
},
{
"state": "Karnataka",
"district": "Ballary",
"city": "Harapanahalli",
"climate": "Warm & humid",
"code": 803125
},
{
"state": "Karnataka",
"district": "Ballary",
"city": "Hoovina Hadagalli",
"climate": "Warm & humid",
"code": 803108
},
{
"state": "Karnataka",
"district": "Ballary",
"city": "Hospet",
"climate": "Warm & humid",
"code": 803109
},
{
"state": "Karnataka",
"district": "Ballary",
"city": "Kamalapuram",
"climate": "Warm & humid",
"code": 803110
},
{
"state": "Karnataka",
"district": "Ballary",
"city": "Kampli",
"climate": "Warm & humid",
"code": 803111
},
{
"state": "Karnataka",
"district": "Ballary",
"city": "Kotturu",
"climate": "Warm & humid",
"code": 803117
},
{
"state": "Karnataka",
"district": "Ballary",
"city": "Kudatini",
"climate": "Warm & humid",
"code": 900427
},
{
"state": "Karnataka",
"district": "Ballary",
"city": "Kudligi",
"climate": "Warm & humid",
"code": 803116
},
{
"state": "Karnataka",
"district": "Ballary",
"city": "Kurekuppa",
"climate": "Warm & humid",
"code": 900397
},
{
"state": "Karnataka",
"district": "Ballary",
"city": "Kurudugodu",
"climate": "Warm & humid",
"code": 900398
},
{
"state": "Karnataka",
"district": "Ballary",
"city": "Mariammanahalli",
"climate": "Warm & humid",
"code": 900428
},
{
"state": "Karnataka",
"district": "Ballary",
"city": "Sandur",
"climate": "Warm & humid",
"code": 803115
},
{
"state": "Karnataka",
"district": "Ballary",
"city": "Siruguppa",
"climate": "Warm & humid",
"code": 803112
},
{
"state": "Karnataka",
"district": "Ballary",
"city": "Tekkalakote",
"climate": "Warm & humid",
"code": 803113
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "Ainapur",
"climate": "Warm & humid",
"code": 900473
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "Ankalagi-Akkatangerahaala",
"climate": "Warm & humid",
"code": 900770
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "Arabhavi",
"climate": "Warm & humid",
"code": 900417
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "Athni",
"climate": "Warm & humid",
"code": 803024
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "Bail Hongal",
"climate": "Warm & humid",
"code": 803036
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "Belgaum",
"climate": "Warm & humid",
"code": 803033
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "Belgaum Cantonment",
"climate": "Warm & humid",
"code": 803034
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "Boragaon",
"climate": "Warm & humid",
"code": 900418
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "Channamma Kitturu",
"climate": "Warm & humid",
"code": 900412
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "Chikodi",
"climate": "Warm & humid",
"code": 803023
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "Chinchali",
"climate": "Warm & humid",
"code": 900409
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "Examba",
"climate": "Warm & humid",
"code": 900411
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "Gokak",
"climate": "Warm & humid",
"code": 803030
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "Harogeri",
"climate": "Warm & humid",
"code": 900394
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "Hukeri",
"climate": "Warm & humid",
"code": 803032
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "Kabbura",
"climate": "Warm & humid",
"code": 900416
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "Kagawada",
"climate": "Warm & humid",
"code": 900767
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "Kalloli",
"climate": "Warm & humid",
"code": 900413
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "Kankanavadi",
"climate": "Warm & humid",
"code": 900406
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "Khanapur",
"climate": "Warm & humid",
"code": 803035
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "Konnur",
"climate": "Warm & humid",
"code": 803028
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "Kudchi",
"climate": "Warm & humid",
"code": 803025
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "M.K Hubballi",
"climate": "Warm & humid",
"code": 900407
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "Macche",
"climate": "Warm & humid",
"code": 900768
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "Mallapura",
"climate": "Warm & humid",
"code": 900410
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "Manuvalli",
"climate": "Warm & humid",
"code": 900392
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "Mudalgi",
"climate": "Warm & humid",
"code": 803027
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "Mugalakoda",
"climate": "Warm & humid",
"code": 900391
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "Naaganura",
"climate": "Warm & humid",
"code": 900408
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "Nipani",
"climate": "Warm & humid",
"code": 803021
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "Peeranavaadi",
"climate": "Warm & humid",
"code": 900769
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "Ramdurg",
"climate": "Warm & humid",
"code": 803038
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "Raybag",
"climate": "Warm & humid",
"code": 803026
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "Sadalgi",
"climate": "Warm & humid",
"code": 803022
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "Sankeshwar",
"climate": "Warm & humid",
"code": 803031
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "Saundatti-Yellamma",
"climate": "Warm & humid",
"code": 803037
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "Shedbaala",
"climate": "Warm & humid",
"code": 900415
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "Ugar Khurda",
"climate": "Warm & humid",
"code": 900393
},
{
"state": "Karnataka",
"district": "Belagavi",
"city": "Yaragatti",
"climate": "Warm & humid",
"code": 900766
},
{
"state": "Karnataka",
"district": "Bengaluru Rural",
"city": "Bashettihalli",
"climate": "Temperate",
"code": 900666
},
{
"state": "Karnataka",
"district": "Bengaluru Rural",
"city": "Devanahalli",
"climate": "Temperate",
"code": 803235
},
{
"state": "Karnataka",
"district": "Bengaluru Rural",
"city": "Dod Ballapur",
"climate": "Temperate",
"code": 803233
},
{
"state": "Karnataka",
"district": "Bengaluru Rural",
"city": "Hosakote",
"climate": "Temperate",
"code": 803236
},
{
"state": "Karnataka",
"district": "Bengaluru Rural",
"city": "Nelamangala",
"climate": "Temperate",
"code": 803232
},
{
"state": "Karnataka",
"district": "Bengaluru Rural",
"city": "Vijayapura",
"climate": "Temperate",
"code": 803234
},
{
"state": "Karnataka",
"district": "Bengaluru Urban",
"city": "Anekal",
"climate": "Temperate",
"code": 803163
},
{
"state": "Karnataka",
"district": "Bengaluru Urban",
"city": "Attibele",
"climate": "Temperate",
"code": 900390
},
{
"state": "Karnataka",
"district": "Bengaluru Urban",
"city": "Bommasandra",
"climate": "Temperate",
"code": 900387
},
{
"state": "Karnataka",
"district": "Bengaluru Urban",
"city": "Bruhat Bengaluru Mahanagara Palike",
"climate": "Temperate",
"code": 803162
},
{
"state": "Karnataka",
"district": "Bengaluru Urban",
"city": "Chandapura",
"climate": "Temperate",
"code": 900388
},
{
"state": "Karnataka",
"district": "Bengaluru Urban",
"city": "Chikkabanavara",
"climate": "Temperate",
"code": 900772
},
{
"state": "Karnataka",
"district": "Bengaluru Urban",
"city": "Doddathoguru",
"climate": "Temperate"
},
{
"state": "Karnataka",
"district": "Bengaluru Urban",
"city": "Hebbagodi",
"climate": "Temperate",
"code": 900386
},
{
"state": "Karnataka",
"district": "Bengaluru Urban",
"city": "Hunasamaranahalli",
"climate": "Temperate",
"code": 900771
},
{
"state": "Karnataka",
"district": "Bengaluru Urban",
"city": "Jigani",
"climate": "Temperate",
"code": 900389
},
{
"state": "Karnataka",
"district": "Bengaluru Urban",
"city": "Konappana Agrahara",
"climate": "Temperate"
},
{
"state": "Karnataka",
"district": "Bengaluru Urban",
"city": "Madanayakanahalli",
"climate": "Temperate",
"code": 900606
},
{
"state": "Karnataka",
"district": "Bidar",
"city": "Aurad",
"climate": "Warm & humid",
"code": 803059
},
{
"state": "Karnataka",
"district": "Bidar",
"city": "Basavakalyan",
"climate": "Warm & humid",
"code": 803057
},
{
"state": "Karnataka",
"district": "Bidar",
"city": "Bhalki",
"climate": "Warm & humid",
"code": 803058
},
{
"state": "Karnataka",
"district": "Bidar",
"city": "Bidar",
"climate": "Warm & humid",
"code": 803060
},
{
"state": "Karnataka",
"district": "Bidar",
"city": "Chitgoppa",
"climate": "Warm & humid",
"code": 803062
},
{
"state": "Karnataka",
"district": "Bidar",
"city": "Halli Kheda",
"climate": "Warm & humid",
"code": 900403
},
{
"state": "Karnataka",
"district": "Bidar",
"city": "Homnabad",
"climate": "Warm & humid",
"code": 803061
},
{
"state": "Karnataka",
"district": "Chamarajanagara",
"city": "Chamarajanagar",
"climate": "Warm & humid",
"code": 803201
},
{
"state": "Karnataka",
"district": "Chamarajanagara",
"city": "Gundlupet",
"climate": "Warm & humid",
"code": 803200
},
{
"state": "Karnataka",
"district": "Chamarajanagara",
"city": "Hanur",
"climate": "Warm & humid",
"code": 803204
},
{
"state": "Karnataka",
"district": "Chamarajanagara",
"city": "Kollegal",
"climate": "Warm & humid",
"code": 803203
},
{
"state": "Karnataka",
"district": "Chamarajanagara",
"city": "Yelandur",
"climate": "Warm & humid",
"code": 803202
},
{
"state": "Karnataka",
"district": "Chikkaballapura",
"city": "Bagepalli",
"climate": "Temperate",
"code": 803229
},
{
"state": "Karnataka",
"district": "Chikkaballapura",
"city": "Chikkaballapura",
"climate": "Temperate",
"code": 803227
},
{
"state": "Karnataka",
"district": "Chikkaballapura",
"city": "Chintamani",
"climate": "Temperate",
"code": 803231
},
{
"state": "Karnataka",
"district": "Chikkaballapura",
"city": "Gauribidanur",
"climate": "Temperate",
"code": 803226
},
{
"state": "Karnataka",
"district": "Chikkaballapura",
"city": "Gudibanda",
"climate": "Temperate",
"code": 803228
},
{
"state": "Karnataka",
"district": "Chikkaballapura",
"city": "Sidlaghatta",
"climate": "Temperate",
"code": 803230
},
{
"state": "Karnataka",
"district": "Chikkamagaluru",
"city": "Ajjampura",
"climate": "Warm & humid",
"code": 900607
},
{
"state": "Karnataka",
"district": "Chikkamagaluru",
"city": "Birur",
"climate": "Warm & humid",
"code": 803147
},
{
"state": "Karnataka",
"district": "Chikkamagaluru",
"city": "Chikmagalur",
"climate": "Warm & humid",
"code": 803149
},
{
"state": "Karnataka",
"district": "Chikkamagaluru",
"city": "Kadur",
"climate": "Warm & humid",
"code": 803148
},
{
"state": "Karnataka",
"district": "Chikkamagaluru",
"city": "Koppa",
"climate": "Warm & humid",
"code": 803144
},
{
"state": "Karnataka",
"district": "Chikkamagaluru",
"city": "Kudremukh",
"climate": "Warm & humid",
"code": 803151
},
{
"state": "Karnataka",
"district": "Chikkamagaluru",
"city": "Mudigere",
"climate": "Warm & humid",
"code": 803150
},
{
"state": "Karnataka",
"district": "Chikkamagaluru",
"city": "Narasimharajapura",
"climate": "Warm & humid",
"code": 803145
},
{
"state": "Karnataka",
"district": "Chikkamagaluru",
"city": "Sringeri",
"climate": "Warm & humid",
"code": 803143
},
{
"state": "Karnataka",
"district": "Chikkamagaluru",
"city": "Tarikere",
"climate": "Warm & humid",
"code": 803146
},
{
"state": "Karnataka",
"district": "Chitradurga",
"city": "Challakere",
"climate": "Warm & humid",
"code": 803119
},
{
"state": "Karnataka",
"district": "Chitradurga",
"city": "Chitradurga",
"climate": "Warm & humid",
"code": 803120
},
{
"state": "Karnataka",
"district": "Chitradurga",
"city": "Hiriyur",
"climate": "Warm & humid",
"code": 803123
},
{
"state": "Karnataka",
"district": "Chitradurga",
"city": "Holalkere",
"climate": "Warm & humid",
"code": 803121
},
{
"state": "Karnataka",
"district": "Chitradurga",
"city": "Hosdurga",
"climate": "Warm & humid",
"code": 803122
},
{
"state": "Karnataka",
"district": "Chitradurga",
"city": "Molakalmuru",
"climate": "Warm & humid",
"code": 803118
},
{
"state": "Karnataka",
"district": "Chitradurga",
"city": "Nayakanahatti",
"climate": "Warm & humid",
"code": 900429
},
{
"state": "Karnataka",
"district": "Dakshina kannada",
"city": "Bajape",
"climate": "Warm & humid",
"code": 900774
},
{
"state": "Karnataka",
"district": "Dakshina kannada",
"city": "Bantval",
"climate": "Warm & humid",
"code": 803183
},
{
"state": "Karnataka",
"district": "Dakshina kannada",
"city": "Beltangadi",
"climate": "Warm & humid",
"code": 803184
},
{
"state": "Karnataka",
"district": "Dakshina kannada",
"city": "Kadaba",
"climate": "Warm & humid",
"code": 900773
},
{
"state": "Karnataka",
"district": "Dakshina kannada",
"city": "Kinnigoli",
"climate": "Warm & humid",
"code": 900775
},
{
"state": "Karnataka",
"district": "Dakshina kannada",
"city": "Kotekaar",
"climate": "Warm & humid",
"code": 900383
},
{
"state": "Karnataka",
"district": "Dakshina kannada",
"city": "Mangalore",
"climate": "Warm & humid",
"code": 803181
},
{
"state": "Karnataka",
"district": "Dakshina kannada",
"city": "Mudbidri",
"climate": "Warm & humid",
"code": 803180
},
{
"state": "Karnataka",
"district": "Dakshina kannada",
"city": "Mulki",
"climate": "Warm & humid",
"code": 803179
},
{
"state": "Karnataka",
"district": "Dakshina kannada",
"city": "Puttur",
"climate": "Warm & humid",
"code": 803185
},
{
"state": "Karnataka",
"district": "Dakshina kannada",
"city": "Someshwara",
"climate": "Warm & humid",
"code": 900608
},
{
"state": "Karnataka",
"district": "Dakshina kannada",
"city": "Sulya",
"climate": "Warm & humid",
"code": 803186
},
{
"state": "Karnataka",
"district": "Dakshina kannada",
"city": "Ullal",
"climate": "Warm & humid",
"code": 803182
},
{
"state": "Karnataka",
"district": "Dakshina kannada",
"city": "Vitla",
"climate": "Warm & humid",
"code": 900384
},
{
"state": "Karnataka",
"district": "Davangere",
"city": "Channagiri",
"climate": "Warm & humid",
"code": 803129
},
{
"state": "Karnataka",
"district": "Davangere",
"city": "Davanagere",
"climate": "Warm & humid",
"code": 803127
},
{
"state": "Karnataka",
"district": "Davangere",
"city": "Harihar",
"climate": "Warm & humid",
"code": 803124
},
{
"state": "Karnataka",
"district": "Davangere",
"city": "Honnali",
"climate": "Warm & humid",
"code": 803128
},
{
"state": "Karnataka",
"district": "Davangere",
"city": "Jagalur",
"climate": "Warm & humid",
"code": 803126
},
{
"state": "Karnataka",
"district": "Davangere",
"city": "Malebennuru",
"climate": "Warm & humid",
"code": 900400
},
{
"state": "Karnataka",
"district": "Davangere",
"city": "Nyamathi",
"climate": "Warm & humid",
"code": 900667
},
{
"state": "Karnataka",
"district": "Dharwada",
"city": "Alnavar",
"climate": "Warm & humid",
"code": 803084
},
{
"state": "Karnataka",
"district": "Dharwada",
"city": "Annigeri",
"climate": "Warm & humid",
"code": 803086
},
{
"state": "Karnataka",
"district": "Dharwada",
"city": "Hubli-Dharwad",
"climate": "Warm & humid",
"code": 803083
},
{
"state": "Karnataka",
"district": "Dharwada",
"city": "Kalghatgi",
"climate": "Warm & humid",
"code": 803087
},
{
"state": "Karnataka",
"district": "Dharwada",
"city": "Kundgol",
"climate": "Warm & humid",
"code": 803088
},
{
"state": "Karnataka",
"district": "Dharwada",
"city": "Navalgund",
"climate": "Warm & humid",
"code": 803085
},
{
"state": "Karnataka",
"district": "Gadaga",
"city": "Gadag-Betigeri",
"climate": "Warm & humid",
"code": 803078
},
{
"state": "Karnataka",
"district": "Gadaga",
"city": "Gajendragarh",
"climate": "Warm & humid",
"code": 803076
},
{
"state": "Karnataka",
"district": "Gadaga",
"city": "Lakshmeshwar",
"climate": "Warm & humid",
"code": 803081
},
{
"state": "Karnataka",
"district": "Gadaga",
"city": "Mulgund",
"climate": "Warm & humid",
"code": 803079
},
{
"state": "Karnataka",
"district": "Gadaga",
"city": "Mundargi",
"climate": "Warm & humid",
"code": 803082
},
{
"state": "Karnataka",
"district": "Gadaga",
"city": "Naregal",
"climate": "Warm & humid",
"code": 803077
},
{
"state": "Karnataka",
"district": "Gadaga",
"city": "Nargund",
"climate": "Warm & humid",
"code": 803074
},
{
"state": "Karnataka",
"district": "Gadaga",
"city": "Ron",
"climate": "Warm & humid",
"code": 803075
},
{
"state": "Karnataka",
"district": "Gadaga",
"city": "Shirhatti",
"climate": "Warm & humid",
"code": 803080
},
{
"state": "Karnataka",
"district": "Hassan",
"city": "Alur",
"climate": "Warm & humid",
"code": 803175
},
{
"state": "Karnataka",
"district": "Hassan",
"city": "Arkalgud",
"climate": "Warm & humid",
"code": 803176
},
{
"state": "Karnataka",
"district": "Hassan",
"city": "Arsikere",
"climate": "Warm & humid",
"code": 803173
},
{
"state": "Karnataka",
"district": "Hassan",
"city": "Belur",
"climate": "Warm & humid",
"code": 803172
},
{
"state": "Karnataka",
"district": "Hassan",
"city": "Channarayapatna",
"climate": "Warm & humid",
"code": 803178
},
{
"state": "Karnataka",
"district": "Hassan",
"city": "Hassan",
"climate": "Warm & humid",
"code": 803174
},
{
"state": "Karnataka",
"district": "Hassan",
"city": "Hole Narsipur",
"climate": "Warm & humid",
"code": 803177
},
{
"state": "Karnataka",
"district": "Hassan",
"city": "Sakleshpur",
"climate": "Warm & humid",
"code": 803171
},
{
"state": "Karnataka",
"district": "Haveri",
"city": "Bankapura",
"climate": "Warm & humid",
"code": 803101
},
{
"state": "Karnataka",
"district": "Haveri",
"city": "Byadgi",
"climate": "Warm & humid",
"code": 803105
},
{
"state": "Karnataka",
"district": "Haveri",
"city": "Guttala",
"climate": "Warm & humid",
"code": 900430
},
{
"state": "Karnataka",
"district": "Haveri",
"city": "Hangal",
"climate": "Warm & humid",
"code": 803103
},
{
"state": "Karnataka",
"district": "Haveri",
"city": "Haveri",
"climate": "Warm & humid",
"code": 803104
},
{
"state": "Karnataka",
"district": "Haveri",
"city": "Hirekerur",
"climate": "Warm & humid",
"code": 803106
},
{
"state": "Karnataka",
"district": "Haveri",
"city": "Ranibennur",
"climate": "Warm & humid",
"code": 803107
},
{
"state": "Karnataka",
"district": "Haveri",
"city": "Rattihalli",
"climate": "Warm & humid",
"code": 900611
},
{
"state": "Karnataka",
"district": "Haveri",
"city": "Savanur",
"climate": "Warm & humid",
"code": 803102
},
{
"state": "Karnataka",
"district": "Haveri",
"city": "Shiggaon",
"climate": "Warm & humid",
"code": 803100
},
{
"state": "Karnataka",
"district": "Kalaburagi",
"city": "Afzalpur",
"climate": "Warm & humid",
"code": 803206
},
{
"state": "Karnataka",
"district": "Kalaburagi",
"city": "Aland",
"climate": "Warm & humid",
"code": 803205
},
{
"state": "Karnataka",
"district": "Kalaburagi",
"city": "Chincholi",
"climate": "Warm & humid",
"code": 803208
},
{
"state": "Karnataka",
"district": "Kalaburagi",
"city": "Chitapur",
"climate": "Warm & humid",
"code": 803210
},
{
"state": "Karnataka",
"district": "Kalaburagi",
"city": "Gulbarga",
"climate": "Warm & humid",
"code": 803207
},
{
"state": "Karnataka",
"district": "Kalaburagi",
"city": "Jevargi",
"climate": "Warm & humid",
"code": 803214
},
{
"state": "Karnataka",
"district": "Kalaburagi",
"city": "Kalaburagi",
"climate": "Warm & humid"
},
{
"state": "Karnataka",
"district": "Kalaburagi",
"city": "Kalagi",
"climate": "Warm & humid",
"code": 900776
},
{
"state": "Karnataka",
"district": "Kalaburagi",
"city": "Kamalapura",
"climate": "Warm & humid",
"code": 900777
},
{
"state": "Karnataka",
"district": "Kalaburagi",
"city": "Sedam",
"climate": "Warm & humid",
"code": 803209
},
{
"state": "Karnataka",
"district": "Kalaburagi",
"city": "Shahabad",
"climate": "Warm & humid",
"code": 803212
},
{
"state": "Karnataka",
"district": "Kalaburagi",
"city": "Shahabad Acc",
"climate": "Warm & humid",
"code": 803211
},
{
"state": "Karnataka",
"district": "Kalaburagi",
"city": "Wadi",
"climate": "Warm & humid",
"code": 803213
},
{
"state": "Karnataka",
"district": "Kalaburagi",
"city": "Yadrami",
"climate": "Warm & humid",
"code": 900778
},
{
"state": "Karnataka",
"district": "Kodagu",
"city": "Kushalnagar",
"climate": "Cold",
"code": 803189
},
{
"state": "Karnataka",
"district": "Kodagu",
"city": "Madikeri",
"climate": "Cold",
"code": 803187
},
{
"state": "Karnataka",
"district": "Kodagu",
"city": "Somvarpet",
"climate": "Cold",
"code": 803188
},
{
"state": "Karnataka",
"district": "Kodagu",
"city": "Virajpet",
"climate": "Cold",
"code": 803190
},
{
"state": "Karnataka",
"district": "Kolar",
"city": "Bangarapet",
"climate": "Cold",
"code": 803223
},
{
"state": "Karnataka",
"district": "Kolar",
"city": "Kolar",
"climate": "Cold",
"code": 803221
},
{
"state": "Karnataka",
"district": "Kolar",
"city": "Malur",
"climate": "Cold",
"code": 803222
},
{
"state": "Karnataka",
"district": "Kolar",
"city": "Mulbagal",
"climate": "Cold",
"code": 803225
},
{
"state": "Karnataka",
"district": "Kolar",
"city": "Robertson Pet",
"climate": "Cold",
"code": 803224
},
{
"state": "Karnataka",
"district": "Kolar",
"city": "Srinivaspur",
"climate": "Cold",
"code": 803220
},
{
"state": "Karnataka",
"district": "Kolar",
"city": "Vemgal-Kurugal",
"climate": "Cold"
},
{
"state": "Karnataka",
"district": "Koppala",
"city": "Bhagyanagar",
"climate": "Cold",
"code": 900425
},
{
"state": "Karnataka",
"district": "Koppala",
"city": "Gangawati",
"climate": "Cold",
"code": 803072
},
{
"state": "Karnataka",
"district": "Koppala",
"city": "Kaaratagi",
"climate": "Cold",
"code": 900396
},
{
"state": "Karnataka",
"district": "Koppala",
"city": "Kanakagiri",
"climate": "Cold",
"code": 900422
},
{
"state": "Karnataka",
"district": "Koppala",
"city": "Koppal",
"climate": "Cold",
"code": 803073
},
{
"state": "Karnataka",
"district": "Koppala",
"city": "Kukanooru",
"climate": "Cold",
"code": 900423
},
{
"state": "Karnataka",
"district": "Koppala",
"city": "Kushtagi",
"climate": "Cold",
"code": 803071
},
{
"state": "Karnataka",
"district": "Koppala",
"city": "Tavaragera",
"climate": "Cold",
"code": 900424
},
{
"state": "Karnataka",
"district": "Koppala",
"city": "Yelbarga",
"climate": "Cold",
"code": 803070
},
{
"state": "Karnataka",
"district": "Mandya",
"city": "Belluru",
"climate": "Warm & humid",
"code": 900499
},
{
"state": "Karnataka",
"district": "Mandya",
"city": "Krishnarajpet",
"climate": "Warm & humid",
"code": 803164
},
{
"state": "Karnataka",
"district": "Mandya",
"city": "Maddur",
"climate": "Warm & humid",
"code": 803169
},
{
"state": "Karnataka",
"district": "Mandya",
"city": "Malavalli",
"climate": "Warm & humid",
"code": 803170
},
{
"state": "Karnataka",
"district": "Mandya",
"city": "Mandya",
"climate": "Warm & humid",
"code": 803168
},
{
"state": "Karnataka",
"district": "Mandya",
"city": "Nagamangala",
"climate": "Warm & humid",
"code": 803165
},
{
"state": "Karnataka",
"district": "Mandya",
"city": "Pandavapura",
"climate": "Warm & humid",
"code": 803166
},
{
"state": "Karnataka",
"district": "Mandya",
"city": "Shrirangapattana",
"climate": "Warm & humid",
"code": 803167
},
{
"state": "Karnataka",
"district": "Mysuru",
"city": "Bannur",
"climate": "Warm & humid",
"code": 803198
},
{
"state": "Karnataka",
"district": "Mysuru",
"city": "Bogadi",
"climate": "Warm & humid",
"code": 900783
},
{
"state": "Karnataka",
"district": "Mysuru",
"city": "Heggadadevankote",
"climate": "Warm & humid",
"code": 803195
},
{
"state": "Karnataka",
"district": "Mysuru",
"city": "Hootagalli",
"climate": "Warm & humid",
"code": 900779
},
{
"state": "Karnataka",
"district": "Mysuru",
"city": "Hunsur",
"climate": "Warm & humid",
"code": 803192
},
{
"state": "Karnataka",
"district": "Mysuru",
"city": "Kadakola",
"climate": "Warm & humid",
"code": 900781
},
{
"state": "Karnataka",
"district": "Mysuru",
"city": "Krishnarajanagara",
"climate": "Warm & humid",
"code": 803193
},
{
"state": "Karnataka",
"district": "Mysuru",
"city": "Mysore",
"climate": "Warm & humid",
"code": 803194
},
{
"state": "Karnataka",
"district": "Mysuru",
"city": "Nanjangud",
"climate": "Warm & humid",
"code": 803197
},
{
"state": "Karnataka",
"district": "Mysuru",
"city": "Piriyapatna",
"climate": "Warm & humid",
"code": 803191
},
{
"state": "Karnataka",
"district": "Mysuru",
"city": "Rammanahalli",
"climate": "Warm & humid",
"code": 900780
},
{
"state": "Karnataka",
"district": "Mysuru",
"city": "Saragur",
"climate": "Warm & humid",
"code": 803196
},
{
"state": "Karnataka",
"district": "Mysuru",
"city": "Srirampura",
"climate": "Warm & humid",
"code": 900782
},
{
"state": "Karnataka",
"district": "Mysuru",
"city": "Tirumakudal Narsipur",
"climate": "Warm & humid",
"code": 803199
},
{
"state": "Karnataka",
"district": "Raichuru",
"city": "Balaganur",
"climate": "Warm & humid",
"code": 900432
},
{
"state": "Karnataka",
"district": "Raichuru",
"city": "Devadurga",
"climate": "Warm & humid",
"code": 803066
},
{
"state": "Karnataka",
"district": "Raichuru",
"city": "Hatti",
"climate": "Warm & humid",
"code": 900497
},
{
"state": "Karnataka",
"district": "Raichuru",
"city": "Hatti Gold Mines",
"climate": "Warm & humid",
"code": 803065
},
{
"state": "Karnataka",
"district": "Raichuru",
"city": "Jalahalli",
"climate": "Warm & humid",
"code": 900784
},
{
"state": "Karnataka",
"district": "Raichuru",
"city": "Kowtal",
"climate": "Warm & humid",
"code": 900405
},
{
"state": "Karnataka",
"district": "Raichuru",
"city": "Lingsugur",
"climate": "Warm & humid",
"code": 803064
},
{
"state": "Karnataka",
"district": "Raichuru",
"city": "Manvi",
"climate": "Warm & humid",
"code": 803068
},
{
"state": "Karnataka",
"district": "Raichuru",
"city": "Maski",
"climate": "Warm & humid",
"code": 900395
},
{
"state": "Karnataka",
"district": "Raichuru",
"city": "Mudgal",
"climate": "Warm & humid",
"code": 803063
},
{
"state": "Karnataka",
"district": "Raichuru",
"city": "Raichur",
"climate": "Warm & humid",
"code": 803067
},
{
"state": "Karnataka",
"district": "Raichuru",
"city": "Sindhnur",
"climate": "Warm & humid",
"code": 803069
},
{
"state": "Karnataka",
"district": "Raichuru",
"city": "Siravara",
"climate": "Warm & humid",
"code": 900433
},
{
"state": "Karnataka",
"district": "Raichuru",
"city": "Turuvihaala",
"climate": "Warm & humid",
"code": 900431
},
{
"state": "Karnataka",
"district": "Ramanagara",
"city": "Bidadi",
"climate": "Warm & humid",
"code": 900401
},
{
"state": "Karnataka",
"district": "Ramanagara",
"city": "Channapatna",
"climate": "Warm & humid",
"code": 803239
},
{
"state": "Karnataka",
"district": "Ramanagara",
"city": "Harohalli",
"climate": "Warm & humid",
"code": 900785
},
{
"state": "Karnataka",
"district": "Ramanagara",
"city": "Kanakapura",
"climate": "Warm & humid",
"code": 803240
},
{
"state": "Karnataka",
"district": "Ramanagara",
"city": "Magadi",
"climate": "Warm & humid",
"code": 803237
},
{
"state": "Karnataka",
"district": "Ramanagara",
"city": "Ramanagara",
"climate": "Warm & humid",
"code": 803238
},
{
"state": "Karnataka",
"district": "Shivamogga",
"city": "Anavatthi",
"climate": "Warm & humid",
"code": 900786
},
{
"state": "Karnataka",
"district": "Shivamogga",
"city": "Babaleshwar",
"climate": "Warm & humid",
"code": 900787
},
{
"state": "Karnataka",
"district": "Shivamogga",
"city": "Bhadravati",
"climate": "Warm & humid",
"code": 803138
},
{
"state": "Karnataka",
"district": "Shivamogga",
"city": "Hollehunuru",
"climate": "Warm & humid",
"code": 900668
},
{
"state": "Karnataka",
"district": "Shivamogga",
"city": "Hosanagara",
"climate": "Warm & humid",
"code": 803135
},
{
"state": "Karnataka",
"district": "Shivamogga",
"city": "Jog Kargal",
"climate": "Warm & humid",
"code": 803130
},
{
"state": "Karnataka",
"district": "Shivamogga",
"city": "Sagar",
"climate": "Warm & humid",
"code": 803131
},
{
"state": "Karnataka",
"district": "Shivamogga",
"city": "Shikarpur",
"climate": "Warm & humid",
"code": 803134
},
{
"state": "Karnataka",
"district": "Shivamogga",
"city": "Shimoga",
"climate": "Warm & humid",
"code": 803137
},
{
"state": "Karnataka",
"district": "Shivamogga",
"city": "Siralkoppa",
"climate": "Warm & humid",
"code": 803133
},
{
"state": "Karnataka",
"district": "Shivamogga",
"city": "Sorab",
"climate": "Warm & humid",
"code": 803132
},
{
"state": "Karnataka",
"district": "Shivamogga",
"city": "Tirthahalli",
"climate": "Warm & humid",
"code": 803136
},
{
"state": "Karnataka",
"district": "Tumakuru",
"city": "Chiknayakanhalli",
"climate": "Warm & humid",
"code": 803152
},
{
"state": "Karnataka",
"district": "Tumakuru",
"city": "Gubbi",
"climate": "Warm & humid",
"code": 803158
},
{
"state": "Karnataka",
"district": "Tumakuru",
"city": "Huliyar",
"climate": "Warm & humid",
"code": 900503
},
{
"state": "Karnataka",
"district": "Tumakuru",
"city": "Koratagere",
"climate": "Warm & humid",
"code": 803156
},
{
"state": "Karnataka",
"district": "Tumakuru",
"city": "Kunigal",
"climate": "Warm & humid",
"code": 803161
},
{
"state": "Karnataka",
"district": "Tumakuru",
"city": "Madhugiri",
"climate": "Warm & humid",
"code": 803155
},
{
"state": "Karnataka",
"district": "Tumakuru",
"city": "Pavagada",
"climate": "Warm & humid",
"code": 803154
},
{
"state": "Karnataka",
"district": "Tumakuru",
"city": "Sira",
"climate": "Warm & humid",
"code": 803153
},
{
"state": "Karnataka",
"district": "Tumakuru",
"city": "Tiptur",
"climate": "Warm & humid",
"code": 803159
},
{
"state": "Karnataka",
"district": "Tumakuru",
"city": "Tumkur",
"climate": "Warm & humid",
"code": 803157
},
{
"state": "Karnataka",
"district": "Tumakuru",
"city": "Turuvekere",
"climate": "Warm & humid",
"code": 803160
},
{
"state": "Karnataka",
"district": "Udupi",
"city": "Bainduru",
"climate": "Warm & humid",
"code": 900609
},
{
"state": "Karnataka",
"district": "Udupi",
"city": "Karkal",
"climate": "Warm & humid",
"code": 803142
},
{
"state": "Karnataka",
"district": "Udupi",
"city": "Kaup",
"climate": "Warm & humid",
"code": 900402
},
{
"state": "Karnataka",
"district": "Udupi",
"city": "Kundapura",
"climate": "Warm & humid",
"code": 803139
},
{
"state": "Karnataka",
"district": "Udupi",
"city": "Saligram",
"climate": "Warm & humid",
"code": 803140
},
{
"state": "Karnataka",
"district": "Udupi",
"city": "Udupi",
"climate": "Warm & humid",
"code": 803141
},
{
"state": "Karnataka",
"district": "Uttara Kannada",
"city": "Ankola",
"climate": "Warm & humid",
"code": 803095
},
{
"state": "Karnataka",
"district": "Uttara Kannada",
"city": "Bhatkal",
"climate": "Warm & humid",
"code": 803099
},
{
"state": "Karnataka",
"district": "Uttara Kannada",
"city": "Dandeli",
"climate": "Warm & humid",
"code": 803089
},
{
"state": "Karnataka",
"district": "Uttara Kannada",
"city": "Haliyal",
"climate": "Warm & humid",
"code": 803091
},
{
"state": "Karnataka",
"district": "Uttara Kannada",
"city": "Honavar",
"climate": "Warm & humid",
"code": 803098
},
{
"state": "Karnataka",
"district": "Uttara Kannada",
"city": "Jaali",
"climate": "Warm & humid",
"code": 900426
},
{
"state": "Karnataka",
"district": "Uttara Kannada",
"city": "Karwar",
"climate": "Warm & humid",
"code": 803090
},
{
"state": "Karnataka",
"district": "Uttara Kannada",
"city": "Kumta",
"climate": "Warm & humid",
"code": 803096
},
{
"state": "Karnataka",
"district": "Uttara Kannada",
"city": "Manki",
"climate": "Warm & humid",
"code": 900788
},
{
"state": "Karnataka",
"district": "Uttara Kannada",
"city": "Mundgod",
"climate": "Warm & humid",
"code": 803093
},
{
"state": "Karnataka",
"district": "Uttara Kannada",
"city": "Siddapur",
"climate": "Warm & humid",
"code": 803097
},
{
"state": "Karnataka",
"district": "Uttara Kannada",
"city": "Sirsi",
"climate": "Warm & humid",
"code": 803094
},
{
"state": "Karnataka",
"district": "Uttara Kannada",
"city": "Yellapur",
"climate": "Warm & humid",
"code": 803092
},
{
"state": "Karnataka",
"district": "Vijayapura",
"city": "Alamela",
"climate": "Warm & humid",
"code": 900434
},
{
"state": "Karnataka",
"district": "Vijayapura",
"city": "Basavana Bagevadi",
"climate": "Warm & humid",
"code": 803054
},
{
"state": "Karnataka",
"district": "Vijayapura",
"city": "Bijapur",
"climate": "Warm & humid",
"code": 803051
},
{
"state": "Karnataka",
"district": "Vijayapura",
"city": "Chadachana",
"climate": "Warm & humid",
"code": 900375
},
{
"state": "Karnataka",
"district": "Vijayapura",
"city": "Devarahipparagi",
"climate": "Warm & humid",
"code": 900374
},
{
"state": "Karnataka",
"district": "Vijayapura",
"city": "Indi",
"climate": "Warm & humid",
"code": 803052
},
{
"state": "Karnataka",
"district": "Vijayapura",
"city": "Kolahara",
"climate": "Warm & humid",
"code": 900435
},
{
"state": "Karnataka",
"district": "Vijayapura",
"city": "Managuli",
"climate": "Warm & humid",
"code": 900368
},
{
"state": "Karnataka",
"district": "Vijayapura",
"city": "Muddebihal",
"climate": "Warm & humid",
"code": 803055
},
{
"state": "Karnataka",
"district": "Vijayapura",
"city": "Nalatavada",
"climate": "Warm & humid",
"code": 900436
},
{
"state": "Karnataka",
"district": "Vijayapura",
"city": "Nidagundi Tp",
"climate": "Warm & humid",
"code": 900376
},
{
"state": "Karnataka",
"district": "Vijayapura",
"city": "Sindgi",
"climate": "Warm & humid",
"code": 803053
},
{
"state": "Karnataka",
"district": "Vijayapura",
"city": "Talikota",
"climate": "Warm & humid",
"code": 803056
},
{
"state": "Karnataka",
"district": "Vijayapura",
"city": "Thikota",
"climate": "Warm & humid",
"code": 900610
},
{
"state": "Karnataka",
"district": "Vijayapura",
"city": "Vijayapura",
"climate": "Warm & humid"
},
{
"state": "Karnataka",
"district": "Yadgir",
"city": "Bhimarayanagudi",
"climate": "Warm & humid",
"code": 803216
},
{
"state": "Karnataka",
"district": "Yadgir",
"city": "Gurmatkal",
"climate": "Warm & humid",
"code": 803218
},
{
"state": "Karnataka",
"district": "Yadgir",
"city": "Hunasagi",
"climate": "Warm & humid",
"code": 900612
},
{
"state": "Karnataka",
"district": "Yadgir",
"city": "Kakkera",
"climate": "Warm & humid",
"code": 900361
},
{
"state": "Karnataka",
"district": "Yadgir",
"city": "Kembav",
"climate": "Warm & humid",
"code": 900360
},
{
"state": "Karnataka",
"district": "Yadgir",
"city": "Shahpur",
"climate": "Warm & humid",
"code": 803217
},
{
"state": "Karnataka",
"district": "Yadgir",
"city": "Shorapur",
"climate": "Warm & humid",
"code": 803215
},
{
"state": "Karnataka",
"district": "Yadgir",
"city": "Yadgir",
"climate": "Warm & humid",
"code": 803219
},
{
"state": "Kerala",
"district": "Alappuzha",
"city": "Alappuzha",
"climate": "Warm & humid",
"code": 803299
},
{
"state": "Kerala",
"district": "Alappuzha",
"city": "Chengannur",
"climate": "Warm & humid",
"code": 803301
},
{
"state": "Kerala",
"district": "Alappuzha",
"city": "Cherthala",
"climate": "Warm & humid",
"code": 803298
},
{
"state": "Kerala",
"district": "Alappuzha",
"city": "Haripad",
"climate": "Warm & humid",
"code": 900201
},
{
"state": "Kerala",
"district": "Alappuzha",
"city": "Kayamkulam",
"climate": "Warm & humid",
"code": 803300
},
{
"state": "Kerala",
"district": "Alappuzha",
"city": "Mavelikkara",
"climate": "Warm & humid",
"code": 803302
},
{
"state": "Kerala",
"district": "Ernakulam",
"city": "Aluva",
"climate": "Warm & humid",
"code": 803286
},
{
"state": "Kerala",
"district": "Ernakulam",
"city": "Angamaly",
"climate": "Warm & humid",
"code": 803285
},
{
"state": "Kerala",
"district": "Ernakulam",
"city": "Eloor",
"climate": "Warm & humid",
"code": 900011
},
{
"state": "Kerala",
"district": "Ernakulam",
"city": "Kalamassery",
"climate": "Warm & humid",
"code": 803289
},
{
"state": "Kerala",
"district": "Ernakulam",
"city": "Kochi",
"climate": "Warm & humid",
"code": 803288
},
{
"state": "Kerala",
"district": "Ernakulam",
"city": "Koothattukulam",
"climate": "Warm & humid",
"code": 900205
},
{
"state": "Kerala",
"district": "Ernakulam",
"city": "Kothamangalam",
"climate": "Warm & humid",
"code": 803292
},
{
"state": "Kerala",
"district": "Ernakulam",
"city": "Maradu",
"climate": "Warm & humid",
"code": 900010
},
{
"state": "Kerala",
"district": "Ernakulam",
"city": "Muvattupuzha",
"climate": "Warm & humid",
"code": 803291
},
{
"state": "Kerala",
"district": "Ernakulam",
"city": "Paravur",
"climate": "Warm & humid",
"code": 803287
},
{
"state": "Kerala",
"district": "Ernakulam",
"city": "Perumbavoor",
"climate": "Warm & humid",
"code": 803284
},
{
"state": "Kerala",
"district": "Ernakulam",
"city": "Piravom",
"climate": "Warm & humid",
"code": 900204
},
{
"state": "Kerala",
"district": "Ernakulam",
"city": "Thrikkakara",
"climate": "Warm & humid",
"code": 900009
},
{
"state": "Kerala",
"district": "Ernakulam",
"city": "Thrippunithura",
"climate": "Warm & humid",
"code": 803290
},
{
"state": "Kerala",
"district": "Idukki",
"city": "Kattappana",
"climate": "Warm & humid",
"code": 900203
},
{
"state": "Kerala",
"district": "Idukki",
"city": "Thodupuzha",
"climate": "Warm & humid",
"code": 803293
},
{
"state": "Kerala",
"district": "Kannur",
"city": "Anthoor",
"climate": "Warm & humid",
"code": 900212
},
{
"state": "Kerala",
"district": "Kannur",
"city": "Iritty",
"climate": "Warm & humid",
"code": 900213
},
{
"state": "Kerala",
"district": "Kannur",
"city": "Kannur",
"climate": "Warm & humid",
"code": 803259
},
{
"state": "Kerala",
"district": "Kannur",
"city": "Kannur Cantonment",
"climate": "Warm & humid",
"code": 803260
},
{
"state": "Kerala",
"district": "Kannur",
"city": "Koothuparamba",
"climate": "Warm & humid",
"code": 803262
},
{
"state": "Kerala",
"district": "Kannur",
"city": "Mattannur",
"climate": "Warm & humid",
"code": 803261
},
{
"state": "Kerala",
"district": "Kannur",
"city": "Panoor",
"climate": "Warm & humid",
"code": 900214
},
{
"state": "Kerala",
"district": "Kannur",
"city": "Payyannur",
"climate": "Warm & humid",
"code": 803257
},
{
"state": "Kerala",
"district": "Kannur",
"city": "Sreekandapuram",
"climate": "Warm & humid",
"code": 900215
},
{
"state": "Kerala",
"district": "Kannur",
"city": "Taliparamba",
"climate": "Warm & humid",
"code": 803258
},
{
"state": "Kerala",
"district": "Kannur",
"city": "Thalassery",
"climate": "Warm & humid",
"code": 803263
},
{
"state": "Kerala",
"district": "Kasaragod",
"city": "Kanhangad",
"climate": "Warm & humid",
"code": 803256
},
{
"state": "Kerala",
"district": "Kasaragod",
"city": "Kasaragod",
"climate": "Warm & humid",
"code": 803255
},
{
"state": "Kerala",
"district": "Kasaragod",
"city": "Neeleswaram",
"climate": "Warm & humid",
"code": 900174
},
{
"state": "Kerala",
"district": "Kollam",
"city": "Karunagapally",
"climate": "Warm & humid",
"code": 900175
},
{
"state": "Kerala",
"district": "Kollam",
"city": "Kollam",
"climate": "Warm & humid",
"code": 803306
},
{
"state": "Kerala",
"district": "Kollam",
"city": "Kottarakkara",
"climate": "Warm & humid",
"code": 900199
},
{
"state": "Kerala",
"district": "Kollam",
"city": "Paravoor",
"climate": "Warm & humid",
"code": 803308
},
{
"state": "Kerala",
"district": "Kollam",
"city": "Punalur",
"climate": "Warm & humid",
"code": 803307
},
{
"state": "Kerala",
"district": "Kottayam",
"city": "Changanassery",
"climate": "Warm & humid",
"code": 803297
},
{
"state": "Kerala",
"district": "Kottayam",
"city": "Erattupetta",
"climate": "Warm & humid",
"code": 900235
},
{
"state": "Kerala",
"district": "Kottayam",
"city": "Ettumanoor",
"climate": "Warm & humid",
"code": 900202
},
{
"state": "Kerala",
"district": "Kottayam",
"city": "Kottayam",
"climate": "Warm & humid",
"code": 803296
},
{
"state": "Kerala",
"district": "Kottayam",
"city": "Palai",
"climate": "Warm & humid",
"code": 803294
},
{
"state": "Kerala",
"district": "Kottayam",
"city": "Vaikom",
"climate": "Warm & humid",
"code": 803295
},
{
"state": "Kerala",
"district": "Kozhikode",
"city": "Feroke",
"climate": "Warm & humid",
"code": 900222
},
{
"state": "Kerala",
"district": "Kozhikode",
"city": "Koduvally",
"climate": "Warm & humid",
"code": 900224
},
{
"state": "Kerala",
"district": "Kozhikode",
"city": "Koyilandy Muncipality",
"climate": "Warm & humid",
"code": 803266
},
{
"state": "Kerala",
"district": "Kozhikode",
"city": "Kozhikode",
"climate": "Warm & humid",
"code": 803267
},
{
"state": "Kerala",
"district": "Kozhikode",
"city": "Mukkam",
"climate": "Warm & humid",
"code": 900225
},
{
"state": "Kerala",
"district": "Kozhikode",
"city": "Payyoli",
"climate": "Warm & humid",
"code": 900223
},
{
"state": "Kerala",
"district": "Kozhikode",
"city": "Ramanattukara",
"climate": "Warm & humid",
"code": 900221
},
{
"state": "Kerala",
"district": "Kozhikode",
"city": "Vadakara",
"climate": "Warm & humid",
"code": 803265
},
{
"state": "Kerala",
"district": "Malappuram",
"city": "Kondotty",
"climate": "Warm & humid",
"code": 900216
},
{
"state": "Kerala",
"district": "Malappuram",
"city": "Kottakkal",
"climate": "Warm & humid",
"code": 900130
},
{
"state": "Kerala",
"district": "Malappuram",
"city": "Malappuram",
"climate": "Warm & humid",
"code": 803269
},
{
"state": "Kerala",
"district": "Malappuram",
"city": "Manjeri",
"climate": "Warm & humid",
"code": 803268
},
{
"state": "Kerala",
"district": "Malappuram",
"city": "Nilambur",
"climate": "Warm & humid",
"code": 900151
},
{
"state": "Kerala",
"district": "Malappuram",
"city": "Parappananangadi",
"climate": "Warm & humid",
"code": 900219
},
{
"state": "Kerala",
"district": "Malappuram",
"city": "Perinthalmanna",
"climate": "Warm & humid",
"code": 803270
},
{
"state": "Kerala",
"district": "Malappuram",
"city": "Ponnani",
"climate": "Warm & humid",
"code": 803272
},
{
"state": "Kerala",
"district": "Malappuram",
"city": "Tanur",
"climate": "Warm & humid",
"code": 900218
},
{
"state": "Kerala",
"district": "Malappuram",
"city": "Tirur",
"climate": "Warm & humid",
"code": 803271
},
{
"state": "Kerala",
"district": "Malappuram",
"city": "Tirurangadi",
"climate": "Warm & humid",
"code": 900220
},
{
"state": "Kerala",
"district": "Malappuram",
"city": "Valancherry",
"climate": "Warm & humid",
"code": 900217
},
{
"state": "Kerala",
"district": "Palakkad",
"city": "Cherpulassery",
"climate": "Warm & humid",
"code": 900209
},
{
"state": "Kerala",
"district": "Palakkad",
"city": "Chittur-Thathamangalam",
"climate": "Warm & humid",
"code": 803276
},
{
"state": "Kerala",
"district": "Palakkad",
"city": "Mannarkkad",
"climate": "Warm & humid",
"code": 900207
},
{
"state": "Kerala",
"district": "Palakkad",
"city": "Ottappalam",
"climate": "Warm & humid",
"code": 803274
},
{
"state": "Kerala",
"district": "Palakkad",
"city": "Palakkad",
"climate": "Warm & humid",
"code": 803275
},
{
"state": "Kerala",
"district": "Palakkad",
"city": "Pattambi",
"climate": "Warm & humid",
"code": 900208
},
{
"state": "Kerala",
"district": "Palakkad",
"city": "Shoranur",
"climate": "Warm & humid",
"code": 803273
},
{
"state": "Kerala",
"district": "Pathanamthitta",
"city": "Adoor",
"climate": "Warm & humid",
"code": 803305
},
{
"state": "Kerala",
"district": "Pathanamthitta",
"city": "Pandalam",
"climate": "Warm & humid",
"code": 900200
},
{
"state": "Kerala",
"district": "Pathanamthitta",
"city": "Pathanamthitta",
"climate": "Warm & humid",
"code": 803304
},
{
"state": "Kerala",
"district": "Pathanamthitta",
"city": "Thiruvalla",
"climate": "Warm & humid",
"code": 803303
},
{
"state": "Kerala",
"district": "Thiruvananthapuram",
"city": "Attingal",
"climate": "Warm & humid",
"code": 803310
},
{
"state": "Kerala",
"district": "Thiruvananthapuram",
"city": "Nedumangad",
"climate": "Warm & humid",
"code": 803311
},
{
"state": "Kerala",
"district": "Thiruvananthapuram",
"city": "Neyyattinkara",
"climate": "Warm & humid",
"code": 803313
},
{
"state": "Kerala",
"district": "Thiruvananthapuram",
"city": "Thiruvananthapuram",
"climate": "Warm & humid",
"code": 803312
},
{
"state": "Kerala",
"district": "Thiruvananthapuram",
"city": "Varkala",
"climate": "Warm & humid",
"code": 803309
},
{
"state": "Kerala",
"district": "Thrissur",
"city": "Chalakudy",
"climate": "Warm & humid",
"code": 803283
},
{
"state": "Kerala",
"district": "Thrissur",
"city": "Chavakkad",
"climate": "Warm & humid",
"code": 803279
},
{
"state": "Kerala",
"district": "Thrissur",
"city": "Guruvayoor",
"climate": "Warm & humid",
"code": 803278
},
{
"state": "Kerala",
"district": "Thrissur",
"city": "Irinjalakuda",
"climate": "Warm & humid",
"code": 803282
},
{
"state": "Kerala",
"district": "Thrissur",
"city": "Kodungallur",
"climate": "Warm & humid",
"code": 803281
},
{
"state": "Kerala",
"district": "Thrissur",
"city": "Kunnamkulam",
"climate": "Warm & humid",
"code": 803277
},
{
"state": "Kerala",
"district": "Thrissur",
"city": "Thrissur",
"climate": "Warm & humid",
"code": 803280
},
{
"state": "Kerala",
"district": "Thrissur",
"city": "Wadakkancheri",
"climate": "Warm & humid",
"code": 900206
},
{
"state": "Kerala",
"district": "Wayanad",
"city": "Kalpetta",
"climate": "Warm & humid",
"code": 803264
},
{
"state": "Kerala",
"district": "Wayanad",
"city": "Mananthavadi",
"climate": "Warm & humid",
"code": 900210
},
{
"state": "Kerala",
"district": "Wayanad",
"city": "Sultan Bathery",
"climate": "Warm & humid",
"code": 900211
},
{
"state": "Ladakh",
"district": "Kargil",
"city": "Kargil",
"climate": "Cold",
"code": 800048
},
{
"state": "Ladakh",
"district": "Leh",
"city": "Leh Ladakh",
"climate": "Cold",
"code": 800047
},
{
"state": "Madhya Pradesh",
"district": "Agar Malwa",
"city": "Agar",
"climate": "Hot and Dry",
"code": 802237
},
{
"state": "Madhya Pradesh",
"district": "Agar Malwa",
"city": "Badagaon_A",
"climate": "Hot and Dry",
"code": 802235
},
{
"state": "Madhya Pradesh",
"district": "Agar Malwa",
"city": "Barode",
"climate": "Hot and Dry",
"code": 802236
},
{
"state": "Madhya Pradesh",
"district": "Agar Malwa",
"city": "Kanad",
"climate": "Hot and Dry",
"code": 802238
},
{
"state": "Madhya Pradesh",
"district": "Agar Malwa",
"city": "Nalkheda",
"climate": "Hot and Dry",
"code": 802234
},
{
"state": "Madhya Pradesh",
"district": "Agar Malwa",
"city": "Soyatkalan",
"climate": "Hot and Dry",
"code": 802232
},
{
"state": "Madhya Pradesh",
"district": "Agar Malwa",
"city": "Susner",
"climate": "Hot and Dry",
"code": 802233
},
{
"state": "Madhya Pradesh",
"district": "Alirajpur",
"city": "Alirajpur",
"climate": "Hot and Dry",
"code": 802433
},
{
"state": "Madhya Pradesh",
"district": "Alirajpur",
"city": "Bhavra",
"climate": "Hot and Dry",
"code": 802431
},
{
"state": "Madhya Pradesh",
"district": "Alirajpur",
"city": "Jobat",
"climate": "Hot and Dry",
"code": 802432
},
{
"state": "Madhya Pradesh",
"district": "Anuppur",
"city": "Amarkantak",
"climate": "Composite",
"code": 802421
},
{
"state": "Madhya Pradesh",
"district": "Anuppur",
"city": "Anuppur",
"climate": "Composite",
"code": 802419
},
{
"state": "Madhya Pradesh",
"district": "Anuppur",
"city": "BARGAON (Amlai)",
"climate": "Composite"
},
{
"state": "Madhya Pradesh",
"district": "Anuppur",
"city": "Bangawan",
"climate": "Composite",
"code": 900691
},
{
"state": "Madhya Pradesh",
"district": "Anuppur",
"city": "Bijuri",
"climate": "Composite",
"code": 802416
},
{
"state": "Madhya Pradesh",
"district": "Anuppur",
"city": "Dola",
"climate": "Composite",
"code": 900692
},
{
"state": "Madhya Pradesh",
"district": "Anuppur",
"city": "Dumarkachar",
"climate": "Composite",
"code": 900693
},
{
"state": "Madhya Pradesh",
"district": "Anuppur",
"city": "Jaithari",
"climate": "Composite",
"code": 802420
},
{
"state": "Madhya Pradesh",
"district": "Anuppur",
"city": "Kotma",
"climate": "Composite",
"code": 802417
},
{
"state": "Madhya Pradesh",
"district": "Anuppur",
"city": "Pasan",
"climate": "Composite",
"code": 802418
},
{
"state": "Madhya Pradesh",
"district": "Ashoknagar",
"city": "Ashoknagar",
"climate": "Composite",
"code": 802408
},
{
"state": "Madhya Pradesh",
"district": "Ashoknagar",
"city": "Chanderi",
"climate": "Composite",
"code": 802407
},
{
"state": "Madhya Pradesh",
"district": "Ashoknagar",
"city": "Esagarh",
"climate": "Composite",
"code": 802406
},
{
"state": "Madhya Pradesh",
"district": "Ashoknagar",
"city": "Mungaoli",
"climate": "Composite",
"code": 802409
},
{
"state": "Madhya Pradesh",
"district": "Ashoknagar",
"city": "Piparai",
"climate": "Composite",
"code": 900682
},
{
"state": "Madhya Pradesh",
"district": "Ashoknagar",
"city": "Shadora",
"climate": "Composite",
"code": 900156
},
{
"state": "Madhya Pradesh",
"district": "Balaghat",
"city": "Baihar",
"climate": "Composite",
"code": 802398
},
{
"state": "Madhya Pradesh",
"district": "Balaghat",
"city": "Balaghat",
"climate": "Composite",
"code": 802397
},
{
"state": "Madhya Pradesh",
"district": "Balaghat",
"city": "Katangi_B",
"climate": "Composite",
"code": 802395
},
{
"state": "Madhya Pradesh",
"district": "Balaghat",
"city": "Langi",
"climate": "Composite",
"code": 802400
},
{
"state": "Madhya Pradesh",
"district": "Balaghat",
"city": "Malajkhand",
"climate": "Composite",
"code": 802399
},
{
"state": "Madhya Pradesh",
"district": "Balaghat",
"city": "Waraseoni",
"climate": "Composite",
"code": 802396
},
{
"state": "Madhya Pradesh",
"district": "Barwani",
"city": "Anjad",
"climate": "Hot and Dry",
"code": 802286
},
{
"state": "Madhya Pradesh",
"district": "Barwani",
"city": "Badwani",
"climate": "Hot and Dry",
"code": 802285
},
{
"state": "Madhya Pradesh",
"district": "Barwani",
"city": "Khetia",
"climate": "Hot and Dry",
"code": 802290
},
{
"state": "Madhya Pradesh",
"district": "Barwani",
"city": "Niwali Burjurg",
"climate": "Hot and Dry",
"code": 900677
},
{
"state": "Madhya Pradesh",
"district": "Barwani",
"city": "Palsood",
"climate": "Hot and Dry",
"code": 802288
},
{
"state": "Madhya Pradesh",
"district": "Barwani",
"city": "Pansemal",
"climate": "Hot and Dry",
"code": 802289
},
{
"state": "Madhya Pradesh",
"district": "Barwani",
"city": "Rajpur_M",
"climate": "Hot and Dry",
"code": 802287
},
{
"state": "Madhya Pradesh",
"district": "Barwani",
"city": "Sendhwa",
"climate": "Hot and Dry",
"code": 802291
},
{
"state": "Madhya Pradesh",
"district": "Barwani",
"city": "Thikari",
"climate": "Hot and Dry",
"code": 900678
},
{
"state": "Madhya Pradesh",
"district": "Betul",
"city": "Amla",
"climate": "Composite",
"code": 802340
},
{
"state": "Madhya Pradesh",
"district": "Betul",
"city": "Athner",
"climate": "Composite",
"code": 802334
},
{
"state": "Madhya Pradesh",
"district": "Betul",
"city": "Betul",
"climate": "Composite",
"code": 802335
},
{
"state": "Madhya Pradesh",
"district": "Betul",
"city": "Betul Bazaar",
"climate": "Composite",
"code": 802336
},
{
"state": "Madhya Pradesh",
"district": "Betul",
"city": "Bhainsdehi",
"climate": "Composite",
"code": 802333
},
{
"state": "Madhya Pradesh",
"district": "Betul",
"city": "Chicholi",
"climate": "Composite",
"code": 802337
},
{
"state": "Madhya Pradesh",
"district": "Betul",
"city": "Ghodadogri",
"climate": "Composite",
"code": 900702
},
{
"state": "Madhya Pradesh",
"district": "Betul",
"city": "Multai",
"climate": "Composite",
"code": 802339
},
{
"state": "Madhya Pradesh",
"district": "Betul",
"city": "Sarni",
"climate": "Composite",
"code": 802338
},
{
"state": "Madhya Pradesh",
"district": "Betul",
"city": "Shahpur",
"climate": "Composite",
"code": 900703
},
{
"state": "Madhya Pradesh",
"district": "Bhind",
"city": "Akoda",
"climate": "Composite",
"code": 802091
},
{
"state": "Madhya Pradesh",
"district": "Bhind",
"city": "Alampur",
"climate": "Composite",
"code": 802098
},
{
"state": "Madhya Pradesh",
"district": "Bhind",
"city": "Bhind",
"climate": "Composite",
"code": 802090
},
{
"state": "Madhya Pradesh",
"district": "Bhind",
"city": "Daboh",
"climate": "Composite",
"code": 802099
},
{
"state": "Madhya Pradesh",
"district": "Bhind",
"city": "Gohad",
"climate": "Composite",
"code": 802094
},
{
"state": "Madhya Pradesh",
"district": "Bhind",
"city": "Gormi",
"climate": "Composite",
"code": 802093
},
{
"state": "Madhya Pradesh",
"district": "Bhind",
"city": "Lahar",
"climate": "Composite",
"code": 802097
},
{
"state": "Madhya Pradesh",
"district": "Bhind",
"city": "Malanpur",
"climate": "Composite",
"code": 900680
},
{
"state": "Madhya Pradesh",
"district": "Bhind",
"city": "Mau",
"climate": "Composite",
"code": 802095
},
{
"state": "Madhya Pradesh",
"district": "Bhind",
"city": "Mehgaon",
"climate": "Composite",
"code": 802092
},
{
"state": "Madhya Pradesh",
"district": "Bhind",
"city": "Mihona",
"climate": "Composite",
"code": 802096
},
{
"state": "Madhya Pradesh",
"district": "Bhind",
"city": "Phuphkalan",
"climate": "Composite",
"code": 802089
},
{
"state": "Madhya Pradesh",
"district": "Bhind",
"city": "Raun",
"climate": "Composite",
"code": 900681
},
{
"state": "Madhya Pradesh",
"district": "Bhopal",
"city": "Berasia",
"climate": "Composite",
"code": 802311
},
{
"state": "Madhya Pradesh",
"district": "Bhopal",
"city": "Bhopal",
"climate": "Composite",
"code": 802312
},
{
"state": "Madhya Pradesh",
"district": "Burhanpur",
"city": "Burhanpur",
"climate": "Hot and Dry",
"code": 802439
},
{
"state": "Madhya Pradesh",
"district": "Burhanpur",
"city": "Nepanagar",
"climate": "Hot and Dry",
"code": 802441
},
{
"state": "Madhya Pradesh",
"district": "Burhanpur",
"city": "Shahpur_B",
"climate": "Hot and Dry",
"code": 802440
},
{
"state": "Madhya Pradesh",
"district": "Chhatarpur",
"city": "Badalmalhera",
"climate": "Composite",
"code": 802142
},
{
"state": "Madhya Pradesh",
"district": "Chhatarpur",
"city": "Bijawar",
"climate": "Composite",
"code": 802145
},
{
"state": "Madhya Pradesh",
"district": "Chhatarpur",
"city": "Buxwaha",
"climate": "Composite",
"code": 802146
},
{
"state": "Madhya Pradesh",
"district": "Chhatarpur",
"city": "Chandala",
"climate": "Composite",
"code": 802134
},
{
"state": "Madhya Pradesh",
"district": "Chhatarpur",
"city": "Chhatarpur",
"climate": "Composite",
"code": 802139
},
{
"state": "Madhya Pradesh",
"district": "Chhatarpur",
"city": "Gadimalhara",
"climate": "Composite",
"code": 802137
},
{
"state": "Madhya Pradesh",
"district": "Chhatarpur",
"city": "Ghuwara",
"climate": "Composite",
"code": 802143
},
{
"state": "Madhya Pradesh",
"district": "Chhatarpur",
"city": "Harpalpur",
"climate": "Composite",
"code": 802135
},
{
"state": "Madhya Pradesh",
"district": "Chhatarpur",
"city": "Khajurao",
"climate": "Composite",
"code": 802141
},
{
"state": "Madhya Pradesh",
"district": "Chhatarpur",
"city": "Lavkush Nagar",
"climate": "Composite",
"code": 802133
},
{
"state": "Madhya Pradesh",
"district": "Chhatarpur",
"city": "Maharajpur",
"climate": "Composite",
"code": 802138
},
{
"state": "Madhya Pradesh",
"district": "Chhatarpur",
"city": "Nogaon",
"climate": "Composite",
"code": 802136
},
{
"state": "Madhya Pradesh",
"district": "Chhatarpur",
"city": "Rajnagar",
"climate": "Composite",
"code": 802140
},
{
"state": "Madhya Pradesh",
"district": "Chhatarpur",
"city": "Satai",
"climate": "Composite",
"code": 802144
},
{
"state": "Madhya Pradesh",
"district": "Chhatarpur",
"city": "Warigarh",
"climate": "Composite",
"code": 802132
},
{
"state": "Madhya Pradesh",
"district": "Chhindwara",
"city": "Amarwara",
"climate": "Composite",
"code": 802377
},
{
"state": "Madhya Pradesh",
"district": "Chhindwara",
"city": "Badkuhi",
"climate": "Composite",
"code": 802385
},
{
"state": "Madhya Pradesh",
"district": "Chhindwara",
"city": "Bichhuua",
"climate": "Composite",
"code": 900160
},
{
"state": "Madhya Pradesh",
"district": "Chhindwara",
"city": "Chand",
"climate": "Composite",
"code": 900161
},
{
"state": "Madhya Pradesh",
"district": "Chhindwara",
"city": "Chandameta Butaria",
"climate": "Composite",
"code": 802384
},
{
"state": "Madhya Pradesh",
"district": "Chhindwara",
"city": "Chhindwara",
"climate": "Composite",
"code": 802386
},
{
"state": "Madhya Pradesh",
"district": "Chhindwara",
"city": "Chorai",
"climate": "Composite",
"code": 802379
},
{
"state": "Madhya Pradesh",
"district": "Chhindwara",
"city": "Damua",
"climate": "Composite",
"code": 802381
},
{
"state": "Madhya Pradesh",
"district": "Chhindwara",
"city": "Dongar Parasiya",
"climate": "Composite",
"code": 802383
},
{
"state": "Madhya Pradesh",
"district": "Chhindwara",
"city": "Harrai",
"climate": "Composite",
"code": 802378
},
{
"state": "Madhya Pradesh",
"district": "Chhindwara",
"city": "Junnardeo",
"climate": "Composite",
"code": 802380
},
{
"state": "Madhya Pradesh",
"district": "Chhindwara",
"city": "Lodhikheda",
"climate": "Composite",
"code": 802389
},
{
"state": "Madhya Pradesh",
"district": "Chhindwara",
"city": "Mohgaon",
"climate": "Composite",
"code": 802388
},
{
"state": "Madhya Pradesh",
"district": "Chhindwara",
"city": "Newtonchikhli",
"climate": "Composite",
"code": 802382
},
{
"state": "Madhya Pradesh",
"district": "Chhindwara",
"city": "Pandhurna",
"climate": "Composite",
"code": 802391
},
{
"state": "Madhya Pradesh",
"district": "Chhindwara",
"city": "Piplanarayanwar",
"climate": "Composite",
"code": 802390
},
{
"state": "Madhya Pradesh",
"district": "Chhindwara",
"city": "Sausar",
"climate": "Composite",
"code": 802387
},
{
"state": "Madhya Pradesh",
"district": "Damoh",
"city": "Damoh",
"climate": "Composite",
"code": 802167
},
{
"state": "Madhya Pradesh",
"district": "Damoh",
"city": "Hatta",
"climate": "Composite",
"code": 802164
},
{
"state": "Madhya Pradesh",
"district": "Damoh",
"city": "Hindoriya",
"climate": "Composite",
"code": 802166
},
{
"state": "Madhya Pradesh",
"district": "Damoh",
"city": "Patera",
"climate": "Composite",
"code": 900165
},
{
"state": "Madhya Pradesh",
"district": "Damoh",
"city": "Pathariya",
"climate": "Composite",
"code": 802165
},
{
"state": "Madhya Pradesh",
"district": "Damoh",
"city": "Tendukheda_D",
"climate": "Composite",
"code": 802168
},
{
"state": "Madhya Pradesh",
"district": "Datia",
"city": "Badoni",
"climate": "Composite",
"code": 802110
},
{
"state": "Madhya Pradesh",
"district": "Datia",
"city": "Bhander",
"climate": "Composite",
"code": 802111
},
{
"state": "Madhya Pradesh",
"district": "Datia",
"city": "Datia",
"climate": "Composite",
"code": 802109
},
{
"state": "Madhya Pradesh",
"district": "Datia",
"city": "Indergarh_Mp",
"climate": "Composite",
"code": 802108
},
{
"state": "Madhya Pradesh",
"district": "Datia",
"city": "Seondha",
"climate": "Composite",
"code": 802107
},
{
"state": "Madhya Pradesh",
"district": "Dewas",
"city": "Bagli",
"climate": "Composite",
"code": 802254
},
{
"state": "Madhya Pradesh",
"district": "Dewas",
"city": "Bhaurasa",
"climate": "Composite",
"code": 802245
},
{
"state": "Madhya Pradesh",
"district": "Dewas",
"city": "Dewas",
"climate": "Composite",
"code": 802248
},
{
"state": "Madhya Pradesh",
"district": "Dewas",
"city": "Hatpipliya",
"climate": "Composite",
"code": 802255
},
{
"state": "Madhya Pradesh",
"district": "Dewas",
"city": "Kannod",
"climate": "Composite",
"code": 802249
},
{
"state": "Madhya Pradesh",
"district": "Dewas",
"city": "Kanthaphod",
"climate": "Composite",
"code": 802251
},
{
"state": "Madhya Pradesh",
"district": "Dewas",
"city": "Karnawad",
"climate": "Composite",
"code": 802253
},
{
"state": "Madhya Pradesh",
"district": "Dewas",
"city": "Khategaon",
"climate": "Composite",
"code": 802256
},
{
"state": "Madhya Pradesh",
"district": "Dewas",
"city": "Loharda",
"climate": "Composite",
"code": 802250
},
{
"state": "Madhya Pradesh",
"district": "Dewas",
"city": "Neemawar",
"climate": "Composite",
"code": 900166
},
{
"state": "Madhya Pradesh",
"district": "Dewas",
"city": "Pipalrawan",
"climate": "Composite",
"code": 802247
},
{
"state": "Madhya Pradesh",
"district": "Dewas",
"city": "Satwas",
"climate": "Composite",
"code": 802252
},
{
"state": "Madhya Pradesh",
"district": "Dewas",
"city": "Sonkatch",
"climate": "Composite",
"code": 802246
},
{
"state": "Madhya Pradesh",
"district": "Dewas",
"city": "Tonkhurd",
"climate": "Composite",
"code": 802244
},
{
"state": "Madhya Pradesh",
"district": "Dhar",
"city": "Badnawar",
"climate": "Hot and Dry",
"code": 802257
},
{
"state": "Madhya Pradesh",
"district": "Dhar",
"city": "Dahi",
"climate": "Hot and Dry",
"code": 802264
},
{
"state": "Madhya Pradesh",
"district": "Dhar",
"city": "Dhamnod_D",
"climate": "Hot and Dry",
"code": 802266
},
{
"state": "Madhya Pradesh",
"district": "Dhar",
"city": "Dhar",
"climate": "Hot and Dry",
"code": 802260
},
{
"state": "Madhya Pradesh",
"district": "Dhar",
"city": "Dharampuri",
"climate": "Hot and Dry",
"code": 802267
},
{
"state": "Madhya Pradesh",
"district": "Dhar",
"city": "Kukshi",
"climate": "Hot and Dry",
"code": 802263
},
{
"state": "Madhya Pradesh",
"district": "Dhar",
"city": "Manavar",
"climate": "Hot and Dry",
"code": 802265
},
{
"state": "Madhya Pradesh",
"district": "Dhar",
"city": "Mandav",
"climate": "Hot and Dry",
"code": 802262
},
{
"state": "Madhya Pradesh",
"district": "Dhar",
"city": "Pithampur",
"climate": "Hot and Dry",
"code": 802261
},
{
"state": "Madhya Pradesh",
"district": "Dhar",
"city": "Rajgarh_D",
"climate": "Hot and Dry",
"code": 802258
},
{
"state": "Madhya Pradesh",
"district": "Dhar",
"city": "Sardarpur",
"climate": "Hot and Dry",
"code": 802259
},
{
"state": "Madhya Pradesh",
"district": "Dindori",
"city": "Dindori_D",
"climate": "Composite",
"code": 802371
},
{
"state": "Madhya Pradesh",
"district": "Dindori",
"city": "Shahpura_D",
"climate": "Composite",
"code": 802370
},
{
"state": "Madhya Pradesh",
"district": "Guna",
"city": "Aron",
"climate": "Hot and Dry",
"code": 802404
},
{
"state": "Madhya Pradesh",
"district": "Guna",
"city": "Chachodabinaganj",
"climate": "Hot and Dry",
"code": 802405
},
{
"state": "Madhya Pradesh",
"district": "Guna",
"city": "Guna",
"climate": "Hot and Dry",
"code": 802401
},
{
"state": "Madhya Pradesh",
"district": "Guna",
"city": "Kumbhraj",
"climate": "Hot and Dry",
"code": 802403
},
{
"state": "Madhya Pradesh",
"district": "Guna",
"city": "Madhusudangarh",
"climate": "Hot and Dry",
"code": 900683
},
{
"state": "Madhya Pradesh",
"district": "Guna",
"city": "Radhogarh",
"climate": "Hot and Dry",
"code": 802402
},
{
"state": "Madhya Pradesh",
"district": "Gwalior",
"city": "Antri",
"climate": "Composite",
"code": 802106
},
{
"state": "Madhya Pradesh",
"district": "Gwalior",
"city": "Bilaua",
"climate": "Composite",
"code": 802102
},
{
"state": "Madhya Pradesh",
"district": "Gwalior",
"city": "Bitarwar",
"climate": "Composite",
"code": 802105
},
{
"state": "Madhya Pradesh",
"district": "Gwalior",
"city": "Dabra",
"climate": "Composite",
"code": 802104
},
{
"state": "Madhya Pradesh",
"district": "Gwalior",
"city": "Gwalior",
"climate": "Composite",
"code": 802100
},
{
"state": "Madhya Pradesh",
"district": "Gwalior",
"city": "Mohna",
"climate": "Composite",
"code": 900684
},
{
"state": "Madhya Pradesh",
"district": "Gwalior",
"city": "Morar Cantonment",
"climate": "Composite",
"code": 802101
},
{
"state": "Madhya Pradesh",
"district": "Gwalior",
"city": "Pichhore",
"climate": "Composite",
"code": 802103
},
{
"state": "Madhya Pradesh",
"district": "Harda",
"city": "Harda",
"climate": "Composite",
"code": 802342
},
{
"state": "Madhya Pradesh",
"district": "Harda",
"city": "Khirkiya",
"climate": "Composite",
"code": 802341
},
{
"state": "Madhya Pradesh",
"district": "Harda",
"city": "Sirali",
"climate": "Composite",
"code": 900704
},
{
"state": "Madhya Pradesh",
"district": "Harda",
"city": "Timarni",
"climate": "Composite",
"code": 802343
},
{
"state": "Madhya Pradesh",
"district": "Indore",
"city": "Betma",
"climate": "Composite",
"code": 802270
},
{
"state": "Madhya Pradesh",
"district": "Indore",
"city": "Depalpur",
"climate": "Composite",
"code": 802269
},
{
"state": "Madhya Pradesh",
"district": "Indore",
"city": "Gautampura",
"climate": "Composite",
"code": 802268
},
{
"state": "Madhya Pradesh",
"district": "Indore",
"city": "Hathod",
"climate": "Composite",
"code": 802271
},
{
"state": "Madhya Pradesh",
"district": "Indore",
"city": "Indore",
"climate": "Composite",
"code": 802273
},
{
"state": "Madhya Pradesh",
"district": "Indore",
"city": "Manpur",
"climate": "Composite",
"code": 802277
},
{
"state": "Madhya Pradesh",
"district": "Indore",
"city": "Mhow Cantonment",
"climate": "Composite",
"code": 802275
},
{
"state": "Madhya Pradesh",
"district": "Indore",
"city": "Mhowgaon",
"climate": "Composite",
"code": 802276
},
{
"state": "Madhya Pradesh",
"district": "Indore",
"city": "Rau",
"climate": "Composite",
"code": 802274
},
{
"state": "Madhya Pradesh",
"district": "Indore",
"city": "Sanwer",
"climate": "Composite",
"code": 802272
},
{
"state": "Madhya Pradesh",
"district": "Jabalpur",
"city": "Berala_M",
"climate": "Composite",
"code": 802363
},
{
"state": "Madhya Pradesh",
"district": "Jabalpur",
"city": "Bhedaghat",
"climate": "Composite",
"code": 802362
},
{
"state": "Madhya Pradesh",
"district": "Jabalpur",
"city": "Jabalpur",
"climate": "Composite",
"code": 802361
},
{
"state": "Madhya Pradesh",
"district": "Jabalpur",
"city": "Jabalpur Cantonment",
"climate": "Composite",
"code": 802360
},
{
"state": "Madhya Pradesh",
"district": "Jabalpur",
"city": "Katangi_J",
"climate": "Composite",
"code": 802357
},
{
"state": "Madhya Pradesh",
"district": "Jabalpur",
"city": "Manjholi_J",
"climate": "Composite",
"code": 802356
},
{
"state": "Madhya Pradesh",
"district": "Jabalpur",
"city": "Panagar",
"climate": "Composite",
"code": 802364
},
{
"state": "Madhya Pradesh",
"district": "Jabalpur",
"city": "Patan_Mp",
"climate": "Composite",
"code": 802358
},
{
"state": "Madhya Pradesh",
"district": "Jabalpur",
"city": "Shahpur Bhitoni",
"climate": "Composite",
"code": 802359
},
{
"state": "Madhya Pradesh",
"district": "Jabalpur",
"city": "Sihora",
"climate": "Composite",
"code": 802355
},
{
"state": "Madhya Pradesh",
"district": "Jhabua",
"city": "Jhabua",
"climate": "Hot and Dry",
"code": 802429
},
{
"state": "Madhya Pradesh",
"district": "Jhabua",
"city": "Meghnagar",
"climate": "Hot and Dry",
"code": 900157
},
{
"state": "Madhya Pradesh",
"district": "Jhabua",
"city": "Petlawad",
"climate": "Hot and Dry",
"code": 802428
},
{
"state": "Madhya Pradesh",
"district": "Jhabua",
"city": "Ranapur",
"climate": "Hot and Dry",
"code": 802430
},
{
"state": "Madhya Pradesh",
"district": "Jhabua",
"city": "Thandla",
"climate": "Hot and Dry",
"code": 802427
},
{
"state": "Madhya Pradesh",
"district": "Khandwa",
"city": "Chhanera",
"climate": "Composite",
"code": 802434
},
{
"state": "Madhya Pradesh",
"district": "Khandwa",
"city": "Khandwa",
"climate": "Composite",
"code": 802435
},
{
"state": "Madhya Pradesh",
"district": "Khandwa",
"city": "Mundi",
"climate": "Composite",
"code": 802437
},
{
"state": "Madhya Pradesh",
"district": "Khandwa",
"city": "Omkareshwar",
"climate": "Composite",
"code": 802436
},
{
"state": "Madhya Pradesh",
"district": "Khandwa",
"city": "Pandhana",
"climate": "Composite",
"code": 802438
},
{
"state": "Madhya Pradesh",
"district": "Khandwa",
"city": "Punasa",
"climate": "Composite"
},
{
"state": "Madhya Pradesh",
"district": "Khargaon",
"city": "Barwaha",
"climate": "Hot and Dry",
"code": 802278
},
{
"state": "Madhya Pradesh",
"district": "Khargaon",
"city": "Bhikangaon",
"climate": "Hot and Dry",
"code": 802283
},
{
"state": "Madhya Pradesh",
"district": "Khargaon",
"city": "Bistaan",
"climate": "Hot and Dry",
"code": 900679
},
{
"state": "Madhya Pradesh",
"district": "Khargaon",
"city": "Karhi Pandlya",
"climate": "Hot and Dry",
"code": 900158
},
{
"state": "Madhya Pradesh",
"district": "Khargaon",
"city": "Kasrawad",
"climate": "Hot and Dry",
"code": 802282
},
{
"state": "Madhya Pradesh",
"district": "Khargaon",
"city": "Khargone",
"climate": "Hot and Dry",
"code": 802284
},
{
"state": "Madhya Pradesh",
"district": "Khargaon",
"city": "Maheshwar",
"climate": "Hot and Dry",
"code": 802280
},
{
"state": "Madhya Pradesh",
"district": "Khargaon",
"city": "Mandleshwar",
"climate": "Hot and Dry",
"code": 802281
},
{
"state": "Madhya Pradesh",
"district": "Khargaon",
"city": "Sanawad",
"climate": "Hot and Dry",
"code": 802279
},
{
"state": "Madhya Pradesh",
"district": "Mandla",
"city": "Bamhani",
"climate": "Composite",
"code": 802374
},
{
"state": "Madhya Pradesh",
"district": "Mandla",
"city": "Bhua Bhichhia",
"climate": "Composite",
"code": 802375
},
{
"state": "Madhya Pradesh",
"district": "Mandla",
"city": "Mandla",
"climate": "Composite",
"code": 802373
},
{
"state": "Madhya Pradesh",
"district": "Mandla",
"city": "Nainpur",
"climate": "Composite",
"code": 802376
},
{
"state": "Madhya Pradesh",
"district": "Mandla",
"city": "Niwas",
"climate": "Composite",
"code": 802372
},
{
"state": "Madhya Pradesh",
"district": "Mandsaur",
"city": "Bhainsoda Mandi",
"climate": "Hot and Dry",
"code": 900701
},
{
"state": "Madhya Pradesh",
"district": "Mandsaur",
"city": "Bhanpura",
"climate": "Hot and Dry",
"code": 802205
},
{
"state": "Madhya Pradesh",
"district": "Mandsaur",
"city": "Garoth",
"climate": "Hot and Dry",
"code": 802209
},
{
"state": "Madhya Pradesh",
"district": "Mandsaur",
"city": "Malhargarh",
"climate": "Hot and Dry",
"code": 802206
},
{
"state": "Madhya Pradesh",
"district": "Mandsaur",
"city": "Mandsaur",
"climate": "Hot and Dry",
"code": 802211
},
{
"state": "Madhya Pradesh",
"district": "Mandsaur",
"city": "Nagri_M",
"climate": "Hot and Dry",
"code": 802212
},
{
"state": "Madhya Pradesh",
"district": "Mandsaur",
"city": "Narayangarh",
"climate": "Hot and Dry",
"code": 802207
},
{
"state": "Madhya Pradesh",
"district": "Mandsaur",
"city": "Pipalya Mandi",
"climate": "Hot and Dry",
"code": 802208
},
{
"state": "Madhya Pradesh",
"district": "Mandsaur",
"city": "Shyamgarh",
"climate": "Hot and Dry",
"code": 802210
},
{
"state": "Madhya Pradesh",
"district": "Mandsaur",
"city": "Sitamau",
"climate": "Hot and Dry",
"code": 802213
},
{
"state": "Madhya Pradesh",
"district": "Mandsaur",
"city": "Suwasra",
"climate": "Hot and Dry",
"code": 802214
},
{
"state": "Madhya Pradesh",
"district": "Morena",
"city": "Ambah",
"climate": "Composite",
"code": 802081
},
{
"state": "Madhya Pradesh",
"district": "Morena",
"city": "Bamore",
"climate": "Composite",
"code": 802084
},
{
"state": "Madhya Pradesh",
"district": "Morena",
"city": "Jaura",
"climate": "Composite",
"code": 802085
},
{
"state": "Madhya Pradesh",
"district": "Morena",
"city": "Jhundpura",
"climate": "Composite",
"code": 802087
},
{
"state": "Madhya Pradesh",
"district": "Morena",
"city": "Kailaras",
"climate": "Composite",
"code": 802086
},
{
"state": "Madhya Pradesh",
"district": "Morena",
"city": "Morena",
"climate": "Composite",
"code": 802083
},
{
"state": "Madhya Pradesh",
"district": "Morena",
"city": "Porsa",
"climate": "Composite",
"code": 802082
},
{
"state": "Madhya Pradesh",
"district": "Morena",
"city": "Sabalgarh",
"climate": "Composite",
"code": 802088
},
{
"state": "Madhya Pradesh",
"district": "Murwara (Katni)",
"city": "Barhi",
"climate": "Composite",
"code": 802352
},
{
"state": "Madhya Pradesh",
"district": "Murwara (Katni)",
"city": "Katni",
"climate": "Composite",
"code": 802351
},
{
"state": "Madhya Pradesh",
"district": "Murwara (Katni)",
"city": "Kymore",
"climate": "Composite",
"code": 802353
},
{
"state": "Madhya Pradesh",
"district": "Murwara (Katni)",
"city": "Vijay Radhogarh",
"climate": "Composite",
"code": 802354
},
{
"state": "Madhya Pradesh",
"district": "Narmadapuram",
"city": "Babai",
"climate": "Composite",
"code": 802347
},
{
"state": "Madhya Pradesh",
"district": "Narmadapuram",
"city": "Itarsi",
"climate": "Composite",
"code": 802345
},
{
"state": "Madhya Pradesh",
"district": "Narmadapuram",
"city": "Narmadapuram",
"climate": "Composite",
"code": 802346
},
{
"state": "Madhya Pradesh",
"district": "Narmadapuram",
"city": "Pachmarhi Cantonment",
"climate": "Composite",
"code": 802350
},
{
"state": "Madhya Pradesh",
"district": "Narmadapuram",
"city": "Pipariya",
"climate": "Composite",
"code": 802349
},
{
"state": "Madhya Pradesh",
"district": "Narmadapuram",
"city": "Seoni Malwa",
"climate": "Composite",
"code": 802344
},
{
"state": "Madhya Pradesh",
"district": "Narmadapuram",
"city": "Sohagpur",
"climate": "Composite",
"code": 802348
},
{
"state": "Madhya Pradesh",
"district": "Narmadapuram",
"city": "Vankhedi",
"climate": "Composite",
"code": 900171
},
{
"state": "Madhya Pradesh",
"district": "Narsimhapur",
"city": "Chichli",
"climate": "Composite",
"code": 900163
},
{
"state": "Madhya Pradesh",
"district": "Narsimhapur",
"city": "Gadarwara",
"climate": "Composite",
"code": 802366
},
{
"state": "Madhya Pradesh",
"district": "Narsimhapur",
"city": "Gotegaon",
"climate": "Composite",
"code": 802365
},
{
"state": "Madhya Pradesh",
"district": "Narsimhapur",
"city": "Kareli",
"climate": "Composite",
"code": 802368
},
{
"state": "Madhya Pradesh",
"district": "Narsimhapur",
"city": "Narsinghpur",
"climate": "Composite",
"code": 802367
},
{
"state": "Madhya Pradesh",
"district": "Narsimhapur",
"city": "Sainkheda",
"climate": "Composite",
"code": 900159
},
{
"state": "Madhya Pradesh",
"district": "Narsimhapur",
"city": "Salichoka",
"climate": "Composite",
"code": 900162
},
{
"state": "Madhya Pradesh",
"district": "Narsimhapur",
"city": "Tendukheda_N",
"climate": "Composite",
"code": 802369
},
{
"state": "Madhya Pradesh",
"district": "Neemuch",
"city": "Athana",
"climate": "Composite",
"code": 900167
},
{
"state": "Madhya Pradesh",
"district": "Neemuch",
"city": "Diken",
"climate": "Composite",
"code": 802196
},
{
"state": "Madhya Pradesh",
"district": "Neemuch",
"city": "Jawad",
"climate": "Composite",
"code": 802197
},
{
"state": "Madhya Pradesh",
"district": "Neemuch",
"city": "Jeeran",
"climate": "Composite",
"code": 802201
},
{
"state": "Madhya Pradesh",
"district": "Neemuch",
"city": "Kukdeshwar",
"climate": "Composite",
"code": 802204
},
{
"state": "Madhya Pradesh",
"district": "Neemuch",
"city": "Manasa",
"climate": "Composite",
"code": 802203
},
{
"state": "Madhya Pradesh",
"district": "Neemuch",
"city": "Nayagaon",
"climate": "Composite",
"code": 900168
},
{
"state": "Madhya Pradesh",
"district": "Neemuch",
"city": "Neemuch",
"climate": "Composite",
"code": 802200
},
{
"state": "Madhya Pradesh",
"district": "Neemuch",
"city": "Rampura",
"climate": "Composite",
"code": 802202
},
{
"state": "Madhya Pradesh",
"district": "Neemuch",
"city": "Ratangarh_N_M",
"climate": "Composite",
"code": 802199
},
{
"state": "Madhya Pradesh",
"district": "Neemuch",
"city": "Sarwania Maharaj",
"climate": "Composite",
"code": 900169
},
{
"state": "Madhya Pradesh",
"district": "Neemuch",
"city": "Singoli",
"climate": "Composite",
"code": 802198
},
{
"state": "Madhya Pradesh",
"district": "Niwari",
"city": "Jeron Khalsa",
"climate": "Composite",
"code": 802122
},
{
"state": "Madhya Pradesh",
"district": "Niwari",
"city": "Niwari",
"climate": "Composite",
"code": 802120
},
{
"state": "Madhya Pradesh",
"district": "Niwari",
"city": "Orchha",
"climate": "Composite",
"code": 802121
},
{
"state": "Madhya Pradesh",
"district": "Niwari",
"city": "Prithvipur",
"climate": "Composite",
"code": 802123
},
{
"state": "Madhya Pradesh",
"district": "Niwari",
"city": "Taricharkala",
"climate": "Composite",
"code": 802119
},
{
"state": "Madhya Pradesh",
"district": "Panna",
"city": "Ajaigarh",
"climate": "Composite",
"code": 802147
},
{
"state": "Madhya Pradesh",
"district": "Panna",
"city": "Amanganj",
"climate": "Composite",
"code": 802151
},
{
"state": "Madhya Pradesh",
"district": "Panna",
"city": "Devendra Nagar",
"climate": "Composite",
"code": 802149
},
{
"state": "Madhya Pradesh",
"district": "Panna",
"city": "Gunnor",
"climate": "Composite",
"code": 900696
},
{
"state": "Madhya Pradesh",
"district": "Panna",
"city": "Kikrathi",
"climate": "Composite",
"code": 802150
},
{
"state": "Madhya Pradesh",
"district": "Panna",
"city": "Panna",
"climate": "Composite",
"code": 802148
},
{
"state": "Madhya Pradesh",
"district": "Panna",
"city": "Pawai",
"climate": "Composite",
"code": 802152
},
{
"state": "Madhya Pradesh",
"district": "Raisen",
"city": "Baadi",
"climate": "Composite",
"code": 802330
},
{
"state": "Madhya Pradesh",
"district": "Raisen",
"city": "Bareli",
"climate": "Composite",
"code": 802329
},
{
"state": "Madhya Pradesh",
"district": "Raisen",
"city": "Begumganj",
"climate": "Composite",
"code": 802325
},
{
"state": "Madhya Pradesh",
"district": "Raisen",
"city": "Deori",
"climate": "Composite"
},
{
"state": "Madhya Pradesh",
"district": "Raisen",
"city": "Gairatganj",
"climate": "Composite",
"code": 802324
},
{
"state": "Madhya Pradesh",
"district": "Raisen",
"city": "Mandideep",
"climate": "Composite",
"code": 802327
},
{
"state": "Madhya Pradesh",
"district": "Raisen",
"city": "Obedullaganj",
"climate": "Composite",
"code": 802328
},
{
"state": "Madhya Pradesh",
"district": "Raisen",
"city": "Raisen",
"climate": "Composite",
"code": 802323
},
{
"state": "Madhya Pradesh",
"district": "Raisen",
"city": "Sanchi",
"climate": "Composite",
"code": 802322
},
{
"state": "Madhya Pradesh",
"district": "Raisen",
"city": "Silwani",
"climate": "Composite",
"code": 802331
},
{
"state": "Madhya Pradesh",
"district": "Raisen",
"city": "Sultanpur_R",
"climate": "Composite",
"code": 802326
},
{
"state": "Madhya Pradesh",
"district": "Raisen",
"city": "Udaipura",
"climate": "Composite",
"code": 802332
},
{
"state": "Madhya Pradesh",
"district": "Rajgarh",
"city": "Biaora",
"climate": "Composite",
"code": 802299
},
{
"state": "Madhya Pradesh",
"district": "Rajgarh",
"city": "Boda",
"climate": "Composite",
"code": 802302
},
{
"state": "Madhya Pradesh",
"district": "Rajgarh",
"city": "Chhapiheda",
"climate": "Composite",
"code": 802295
},
{
"state": "Madhya Pradesh",
"district": "Rajgarh",
"city": "Jeerapur",
"climate": "Composite",
"code": 802293
},
{
"state": "Madhya Pradesh",
"district": "Rajgarh",
"city": "Khilchipur",
"climate": "Composite",
"code": 802294
},
{
"state": "Madhya Pradesh",
"district": "Rajgarh",
"city": "Khujner",
"climate": "Composite",
"code": 802297
},
{
"state": "Madhya Pradesh",
"district": "Rajgarh",
"city": "Kurawar",
"climate": "Composite",
"code": 900154
},
{
"state": "Madhya Pradesh",
"district": "Rajgarh",
"city": "Machalpur",
"climate": "Composite",
"code": 802292
},
{
"state": "Madhya Pradesh",
"district": "Rajgarh",
"city": "Narsinghgarh",
"climate": "Composite",
"code": 802301
},
{
"state": "Madhya Pradesh",
"district": "Rajgarh",
"city": "Pachore",
"climate": "Composite",
"code": 802303
},
{
"state": "Madhya Pradesh",
"district": "Rajgarh",
"city": "Rajgarh_R",
"climate": "Composite",
"code": 802296
},
{
"state": "Madhya Pradesh",
"district": "Rajgarh",
"city": "Sarangpur",
"climate": "Composite",
"code": 802300
},
{
"state": "Madhya Pradesh",
"district": "Rajgarh",
"city": "Suthalia",
"climate": "Composite",
"code": 802298
},
{
"state": "Madhya Pradesh",
"district": "Rajgarh",
"city": "Talen",
"climate": "Composite",
"code": 802304
},
{
"state": "Madhya Pradesh",
"district": "Ratlam",
"city": "Alot",
"climate": "Hot and Dry",
"code": 802218
},
{
"state": "Madhya Pradesh",
"district": "Ratlam",
"city": "Badawada",
"climate": "Hot and Dry",
"code": 802217
},
{
"state": "Madhya Pradesh",
"district": "Ratlam",
"city": "Dhamnod_R",
"climate": "Hot and Dry",
"code": 802223
},
{
"state": "Madhya Pradesh",
"district": "Ratlam",
"city": "Jawara",
"climate": "Hot and Dry",
"code": 802216
},
{
"state": "Madhya Pradesh",
"district": "Ratlam",
"city": "Namli",
"climate": "Hot and Dry",
"code": 802221
},
{
"state": "Madhya Pradesh",
"district": "Ratlam",
"city": "Piplodha",
"climate": "Hot and Dry",
"code": 802215
},
{
"state": "Madhya Pradesh",
"district": "Ratlam",
"city": "Ratlam",
"climate": "Hot and Dry",
"code": 802222
},
{
"state": "Madhya Pradesh",
"district": "Ratlam",
"city": "Sailana",
"climate": "Hot and Dry",
"code": 802220
},
{
"state": "Madhya Pradesh",
"district": "Ratlam",
"city": "Tal",
"climate": "Hot and Dry",
"code": 802219
},
{
"state": "Madhya Pradesh",
"district": "Rewa",
"city": "Baikunthpur_M",
"climate": "Composite",
"code": 802183
},
{
"state": "Madhya Pradesh",
"district": "Rewa",
"city": "Chakghat",
"climate": "Composite",
"code": 802180
},
{
"state": "Madhya Pradesh",
"district": "Rewa",
"city": "Dabhoura",
"climate": "Composite",
"code": 900690
},
{
"state": "Madhya Pradesh",
"district": "Rewa",
"city": "Govindgarh",
"climate": "Composite",
"code": 802190
},
{
"state": "Madhya Pradesh",
"district": "Rewa",
"city": "Gurh",
"climate": "Composite",
"code": 802191
},
{
"state": "Madhya Pradesh",
"district": "Rewa",
"city": "Hanumana",
"climate": "Composite",
"code": 802186
},
{
"state": "Madhya Pradesh",
"district": "Rewa",
"city": "Mangava",
"climate": "Composite",
"code": 802184
},
{
"state": "Madhya Pradesh",
"district": "Rewa",
"city": "Mauganj",
"climate": "Composite",
"code": 802187
},
{
"state": "Madhya Pradesh",
"district": "Rewa",
"city": "Nai Garhi",
"climate": "Composite",
"code": 802188
},
{
"state": "Madhya Pradesh",
"district": "Rewa",
"city": "Rewa",
"climate": "Composite",
"code": 802189
},
{
"state": "Madhya Pradesh",
"district": "Rewa",
"city": "Semaria",
"climate": "Composite",
"code": 802185
},
{
"state": "Madhya Pradesh",
"district": "Rewa",
"city": "Sirmour",
"climate": "Composite",
"code": 802182
},
{
"state": "Madhya Pradesh",
"district": "Rewa",
"city": "Theothar",
"climate": "Composite",
"code": 802181
},
{
"state": "Madhya Pradesh",
"district": "Sagar",
"city": "Baandri",
"climate": "Composite",
"code": 900697
},
{
"state": "Madhya Pradesh",
"district": "Sagar",
"city": "Banda",
"climate": "Composite",
"code": 802155
},
{
"state": "Madhya Pradesh",
"district": "Sagar",
"city": "Barodiya kalan",
"climate": "Composite"
},
{
"state": "Madhya Pradesh",
"district": "Sagar",
"city": "Bilhara",
"climate": "Composite",
"code": 900698
},
{
"state": "Madhya Pradesh",
"district": "Sagar",
"city": "Bina Etawa",
"climate": "Composite",
"code": 802153
},
{
"state": "Madhya Pradesh",
"district": "Sagar",
"city": "Deori_S",
"climate": "Composite",
"code": 802163
},
{
"state": "Madhya Pradesh",
"district": "Sagar",
"city": "Garhakota",
"climate": "Composite",
"code": 802161
},
{
"state": "Madhya Pradesh",
"district": "Sagar",
"city": "Karrapur",
"climate": "Composite"
},
{
"state": "Madhya Pradesh",
"district": "Sagar",
"city": "Khurai",
"climate": "Composite",
"code": 802154
},
{
"state": "Madhya Pradesh",
"district": "Sagar",
"city": "Makronia",
"climate": "Composite",
"code": 900172
},
{
"state": "Madhya Pradesh",
"district": "Sagar",
"city": "Malthaun",
"climate": "Composite",
"code": 900699
},
{
"state": "Madhya Pradesh",
"district": "Sagar",
"city": "Rahatgarh",
"climate": "Composite",
"code": 802157
},
{
"state": "Madhya Pradesh",
"district": "Sagar",
"city": "Rehli",
"climate": "Composite",
"code": 802162
},
{
"state": "Madhya Pradesh",
"district": "Sagar",
"city": "Sagar",
"climate": "Composite",
"code": 802159
},
{
"state": "Madhya Pradesh",
"district": "Sagar",
"city": "Saugor Cantonment",
"climate": "Composite",
"code": 802160
},
{
"state": "Madhya Pradesh",
"district": "Sagar",
"city": "Shahgarh",
"climate": "Composite",
"code": 802156
},
{
"state": "Madhya Pradesh",
"district": "Sagar",
"city": "Shahpur_S",
"climate": "Composite",
"code": 802158
},
{
"state": "Madhya Pradesh",
"district": "Sagar",
"city": "Surakhi",
"climate": "Composite",
"code": 900700
},
{
"state": "Madhya Pradesh",
"district": "Satna",
"city": "Amarpatan",
"climate": "Composite",
"code": 802178
},
{
"state": "Madhya Pradesh",
"district": "Satna",
"city": "Birsinghpur",
"climate": "Composite",
"code": 802172
},
{
"state": "Madhya Pradesh",
"district": "Satna",
"city": "Chitrakoot",
"climate": "Composite",
"code": 802171
},
{
"state": "Madhya Pradesh",
"district": "Satna",
"city": "Jaitwara",
"climate": "Composite",
"code": 802173
},
{
"state": "Madhya Pradesh",
"district": "Satna",
"city": "Kotar",
"climate": "Composite",
"code": 802177
},
{
"state": "Madhya Pradesh",
"district": "Satna",
"city": "Kothi",
"climate": "Composite",
"code": 802169
},
{
"state": "Madhya Pradesh",
"district": "Satna",
"city": "Maihar",
"climate": "Composite",
"code": 802179
},
{
"state": "Madhya Pradesh",
"district": "Satna",
"city": "Nagod",
"climate": "Composite",
"code": 802174
},
{
"state": "Madhya Pradesh",
"district": "Satna",
"city": "New Ramnagar",
"climate": "Composite",
"code": 900164
},
{
"state": "Madhya Pradesh",
"district": "Satna",
"city": "Rampur Bhaghelan",
"climate": "Composite",
"code": 802176
},
{
"state": "Madhya Pradesh",
"district": "Satna",
"city": "Satna",
"climate": "Composite",
"code": 802170
},
{
"state": "Madhya Pradesh",
"district": "Satna",
"city": "Uchehra",
"climate": "Composite",
"code": 802175
},
{
"state": "Madhya Pradesh",
"district": "Sehore",
"city": "Ashta",
"climate": "Composite",
"code": 802315
},
{
"state": "Madhya Pradesh",
"district": "Sehore",
"city": "Budni",
"climate": "Composite",
"code": 802320
},
{
"state": "Madhya Pradesh",
"district": "Sehore",
"city": "Ichhawar",
"climate": "Composite",
"code": 802318
},
{
"state": "Madhya Pradesh",
"district": "Sehore",
"city": "Jawar",
"climate": "Composite",
"code": 802317
},
{
"state": "Madhya Pradesh",
"district": "Sehore",
"city": "Kothri",
"climate": "Composite",
"code": 802316
},
{
"state": "Madhya Pradesh",
"district": "Sehore",
"city": "Nasrullaganj",
"climate": "Composite",
"code": 802319
},
{
"state": "Madhya Pradesh",
"district": "Sehore",
"city": "Rehti",
"climate": "Composite",
"code": 802321
},
{
"state": "Madhya Pradesh",
"district": "Sehore",
"city": "Sehore",
"climate": "Composite",
"code": 802314
},
{
"state": "Madhya Pradesh",
"district": "Sehore",
"city": "Shahganj",
"climate": "Composite",
"code": 900127
},
{
"state": "Madhya Pradesh",
"district": "Seoni",
"city": "Barghat",
"climate": "Composite",
"code": 802394
},
{
"state": "Madhya Pradesh",
"district": "Seoni",
"city": "Chapara",
"climate": "Composite",
"code": 900688
},
{
"state": "Madhya Pradesh",
"district": "Seoni",
"city": "Kewlari",
"climate": "Composite",
"code": 900689
},
{
"state": "Madhya Pradesh",
"district": "Seoni",
"city": "Lakhnadoan",
"climate": "Composite",
"code": 802392
},
{
"state": "Madhya Pradesh",
"district": "Seoni",
"city": "Seoni_M",
"climate": "Composite",
"code": 802393
},
{
"state": "Madhya Pradesh",
"district": "Shahdol",
"city": "Bakho",
"climate": "Composite",
"code": 900694
},
{
"state": "Madhya Pradesh",
"district": "Shahdol",
"city": "Beohari",
"climate": "Composite",
"code": 802411
},
{
"state": "Madhya Pradesh",
"district": "Shahdol",
"city": "Burhar",
"climate": "Composite",
"code": 802414
},
{
"state": "Madhya Pradesh",
"district": "Shahdol",
"city": "Dhanpuri",
"climate": "Composite",
"code": 802415
},
{
"state": "Madhya Pradesh",
"district": "Shahdol",
"city": "Jaysingh Nagar",
"climate": "Composite",
"code": 802412
},
{
"state": "Madhya Pradesh",
"district": "Shahdol",
"city": "Khand",
"climate": "Composite",
"code": 802410
},
{
"state": "Madhya Pradesh",
"district": "Shahdol",
"city": "Shahdol",
"climate": "Composite",
"code": 802413
},
{
"state": "Madhya Pradesh",
"district": "Shajapur",
"city": "Akodia",
"climate": "Composite",
"code": 802242
},
{
"state": "Madhya Pradesh",
"district": "Shajapur",
"city": "Makshi",
"climate": "Composite",
"code": 802240
},
{
"state": "Madhya Pradesh",
"district": "Shajapur",
"city": "Palaykala",
"climate": "Composite",
"code": 802243
},
{
"state": "Madhya Pradesh",
"district": "Shajapur",
"city": "Pankhedi Kalapipal",
"climate": "Composite",
"code": 900170
},
{
"state": "Madhya Pradesh",
"district": "Shajapur",
"city": "Shajapur",
"climate": "Composite",
"code": 802239
},
{
"state": "Madhya Pradesh",
"district": "Shajapur",
"city": "Shujalpur",
"climate": "Composite",
"code": 802241
},
{
"state": "Madhya Pradesh",
"district": "Sheopur",
"city": "Badoda",
"climate": "Composite",
"code": 802080
},
{
"state": "Madhya Pradesh",
"district": "Sheopur",
"city": "Bijaypur",
"climate": "Composite",
"code": 802078
},
{
"state": "Madhya Pradesh",
"district": "Sheopur",
"city": "Sheopur",
"climate": "Composite",
"code": 802079
},
{
"state": "Madhya Pradesh",
"district": "Shivpuri",
"city": "Badarwas",
"climate": "Composite",
"code": 802116
},
{
"state": "Madhya Pradesh",
"district": "Shivpuri",
"city": "Bairad",
"climate": "Composite",
"code": 900155
},
{
"state": "Madhya Pradesh",
"district": "Shivpuri",
"city": "Karera",
"climate": "Composite",
"code": 802114
},
{
"state": "Madhya Pradesh",
"district": "Shivpuri",
"city": "Khaniadhana",
"climate": "Composite",
"code": 802118
},
{
"state": "Madhya Pradesh",
"district": "Shivpuri",
"city": "Kolaras",
"climate": "Composite",
"code": 802115
},
{
"state": "Madhya Pradesh",
"district": "Shivpuri",
"city": "Mangrauni",
"climate": "Composite",
"code": 900685
},
{
"state": "Madhya Pradesh",
"district": "Shivpuri",
"city": "Narwar",
"climate": "Composite",
"code": 802113
},
{
"state": "Madhya Pradesh",
"district": "Shivpuri",
"city": "Pichhor",
"climate": "Composite",
"code": 802117
},
{
"state": "Madhya Pradesh",
"district": "Shivpuri",
"city": "Pohari",
"climate": "Composite",
"code": 900686
},
{
"state": "Madhya Pradesh",
"district": "Shivpuri",
"city": "Rannod",
"climate": "Composite",
"code": 900687
},
{
"state": "Madhya Pradesh",
"district": "Shivpuri",
"city": "Shivpuri",
"climate": "Composite",
"code": 802112
},
{
"state": "Madhya Pradesh",
"district": "Sidhi",
"city": "Churhat",
"climate": "Composite",
"code": 802423
},
{
"state": "Madhya Pradesh",
"district": "Sidhi",
"city": "Manjholi_S",
"climate": "Composite",
"code": 802425
},
{
"state": "Madhya Pradesh",
"district": "Sidhi",
"city": "Rampurnekin",
"climate": "Composite",
"code": 802422
},
{
"state": "Madhya Pradesh",
"district": "Sidhi",
"city": "Siddhi",
"climate": "Composite",
"code": 802424
},
{
"state": "Madhya Pradesh",
"district": "Singrauli",
"city": "Bargaon",
"climate": "Composite"
},
{
"state": "Madhya Pradesh",
"district": "Singrauli",
"city": "Singrauli",
"climate": "Composite",
"code": 802426
},
{
"state": "Madhya Pradesh",
"district": "Singrauli",
"city": "sarai",
"climate": "Composite"
},
{
"state": "Madhya Pradesh",
"district": "Tikamgarh",
"city": "Badagaon_T",
"climate": "Composite",
"code": 802131
},
{
"state": "Madhya Pradesh",
"district": "Tikamgarh",
"city": "Baldevgarh",
"climate": "Composite",
"code": 802127
},
{
"state": "Madhya Pradesh",
"district": "Tikamgarh",
"city": "Jatara",
"climate": "Composite",
"code": 802125
},
{
"state": "Madhya Pradesh",
"district": "Tikamgarh",
"city": "Kari",
"climate": "Composite",
"code": 802129
},
{
"state": "Madhya Pradesh",
"district": "Tikamgarh",
"city": "Khargapur",
"climate": "Composite",
"code": 802128
},
{
"state": "Madhya Pradesh",
"district": "Tikamgarh",
"city": "Lidhorakhas",
"climate": "Composite",
"code": 802124
},
{
"state": "Madhya Pradesh",
"district": "Tikamgarh",
"city": "Palera",
"climate": "Composite",
"code": 802126
},
{
"state": "Madhya Pradesh",
"district": "Tikamgarh",
"city": "Tikamgarh",
"climate": "Composite",
"code": 802130
},
{
"state": "Madhya Pradesh",
"district": "Ujjain",
"city": "Badnagar",
"climate": "Composite",
"code": 802231
},
{
"state": "Madhya Pradesh",
"district": "Ujjain",
"city": "Khachrod",
"climate": "Composite",
"code": 802224
},
{
"state": "Madhya Pradesh",
"district": "Ujjain",
"city": "Mahidpur",
"climate": "Composite",
"code": 802227
},
{
"state": "Madhya Pradesh",
"district": "Ujjain",
"city": "Makdone",
"climate": "Composite",
"code": 802229
},
{
"state": "Madhya Pradesh",
"district": "Ujjain",
"city": "Nagda",
"climate": "Composite",
"code": 802225
},
{
"state": "Madhya Pradesh",
"district": "Ujjain",
"city": "Tarana",
"climate": "Composite",
"code": 802228
},
{
"state": "Madhya Pradesh",
"district": "Ujjain",
"city": "Ujjain",
"climate": "Composite",
"code": 802230
},
{
"state": "Madhya Pradesh",
"district": "Ujjain",
"city": "Unhel",
"climate": "Composite",
"code": 802226
},
{
"state": "Madhya Pradesh",
"district": "Umaria",
"city": "Chandia",
"climate": "Composite",
"code": 802193
},
{
"state": "Madhya Pradesh",
"district": "Umaria",
"city": "Manpur-U",
"climate": "Composite",
"code": 900695
},
{
"state": "Madhya Pradesh",
"district": "Umaria",
"city": "Nawrozabad",
"climate": "Composite",
"code": 802195
},
{
"state": "Madhya Pradesh",
"district": "Umaria",
"city": "Pali_M",
"climate": "Composite",
"code": 802194
},
{
"state": "Madhya Pradesh",
"district": "Umaria",
"city": "Umariya",
"climate": "Composite",
"code": 802192
},
{
"state": "Madhya Pradesh",
"district": "Vidisha",
"city": "Ganjbasoda",
"climate": "Composite",
"code": 802308
},
{
"state": "Madhya Pradesh",
"district": "Vidisha",
"city": "Kurwai",
"climate": "Composite",
"code": 802307
},
{
"state": "Madhya Pradesh",
"district": "Vidisha",
"city": "Lateri",
"climate": "Composite",
"code": 802305
},
{
"state": "Madhya Pradesh",
"district": "Vidisha",
"city": "Shamshabad",
"climate": "Composite",
"code": 802309
},
{
"state": "Madhya Pradesh",
"district": "Vidisha",
"city": "Sironj",
"climate": "Composite",
"code": 802306
},
{
"state": "Madhya Pradesh",
"district": "Vidisha",
"city": "Vidisha",
"climate": "Composite",
"code": 802310
},
{
"state": "Maharashtra",
"district": "Ahmednagar",
"city": "Ahmednagar",
"climate": "Hot and Dry",
"code": 802828
},
{
"state": "Maharashtra",
"district": "Ahmednagar",
"city": "AhmednagaraÂ Cantonment",
"climate": "Hot and Dry",
"code": 802829
},
{
"state": "Maharashtra",
"district": "Ahmednagar",
"city": "Akole",
"climate": "Hot and Dry",
"code": 900366
},
{
"state": "Maharashtra",
"district": "Ahmednagar",
"city": "Deolali Pravara",
"climate": "Hot and Dry",
"code": 802831
},
{
"state": "Maharashtra",
"district": "Ahmednagar",
"city": "Jamkhed",
"climate": "Hot and Dry",
"code": 900330
},
{
"state": "Maharashtra",
"district": "Ahmednagar",
"city": "Karjat_A",
"climate": "Hot and Dry",
"code": 900377
},
{
"state": "Maharashtra",
"district": "Ahmednagar",
"city": "Kopargaon",
"climate": "Hot and Dry",
"code": 802823
},
{
"state": "Maharashtra",
"district": "Ahmednagar",
"city": "Nevasa",
"climate": "Hot and Dry",
"code": 900461
},
{
"state": "Maharashtra",
"district": "Ahmednagar",
"city": "Parner",
"climate": "Hot and Dry",
"code": 900370
},
{
"state": "Maharashtra",
"district": "Ahmednagar",
"city": "Pathardi",
"climate": "Hot and Dry",
"code": 802827
},
{
"state": "Maharashtra",
"district": "Ahmednagar",
"city": "Rahta Pimplas",
"climate": "Hot and Dry",
"code": 802825
},
{
"state": "Maharashtra",
"district": "Ahmednagar",
"city": "Rahuri",
"climate": "Hot and Dry",
"code": 802830
},
{
"state": "Maharashtra",
"district": "Ahmednagar",
"city": "Sangamner",
"climate": "Hot and Dry",
"code": 802822
},
{
"state": "Maharashtra",
"district": "Ahmednagar",
"city": "Shevgaon",
"climate": "Hot and Dry",
"code": 900329
},
{
"state": "Maharashtra",
"district": "Ahmednagar",
"city": "Shirdi",
"climate": "Hot and Dry",
"code": 802824
},
{
"state": "Maharashtra",
"district": "Ahmednagar",
"city": "Shrigonda",
"climate": "Hot and Dry",
"code": 802832
},
{
"state": "Maharashtra",
"district": "Ahmednagar",
"city": "Shrirampur",
"climate": "Hot and Dry",
"code": 802826
},
{
"state": "Maharashtra",
"district": "Akola",
"city": "Akola",
"climate": "Hot and Dry",
"code": 802676
},
{
"state": "Maharashtra",
"district": "Akola",
"city": "Akot",
"climate": "Hot and Dry",
"code": 802674
},
{
"state": "Maharashtra",
"district": "Akola",
"city": "Balapur",
"climate": "Hot and Dry",
"code": 802675
},
{
"state": "Maharashtra",
"district": "Akola",
"city": "Barshi Taklii",
"climate": "Hot and Dry",
"code": 900331
},
{
"state": "Maharashtra",
"district": "Akola",
"city": "Murtizapur",
"climate": "Hot and Dry",
"code": 802677
},
{
"state": "Maharashtra",
"district": "Akola",
"city": "Patur",
"climate": "Hot and Dry",
"code": 802678
},
{
"state": "Maharashtra",
"district": "Akola",
"city": "Telhara",
"climate": "Hot and Dry",
"code": 802673
},
{
"state": "Maharashtra",
"district": "Amravati",
"city": "Achalpur",
"climate": "Hot and Dry",
"code": 802685
},
{
"state": "Maharashtra",
"district": "Amravati",
"city": "Amravati",
"climate": "Hot and Dry",
"code": 802690
},
{
"state": "Maharashtra",
"district": "Amravati",
"city": "Anjangaon Surji",
"climate": "Hot and Dry",
"code": 802684
},
{
"state": "Maharashtra",
"district": "Amravati",
"city": "Bhatakuli",
"climate": "Hot and Dry",
"code": 900256
},
{
"state": "Maharashtra",
"district": "Amravati",
"city": "Chandur Baazar",
"climate": "Hot and Dry",
"code": 802686
},
{
"state": "Maharashtra",
"district": "Amravati",
"city": "Chandur Railway",
"climate": "Hot and Dry",
"code": 802692
},
{
"state": "Maharashtra",
"district": "Amravati",
"city": "Chikhaldara",
"climate": "Hot and Dry",
"code": 802683
},
{
"state": "Maharashtra",
"district": "Amravati",
"city": "Daryapur",
"climate": "Hot and Dry",
"code": 802691
},
{
"state": "Maharashtra",
"district": "Amravati",
"city": "Dattapur Dhamangaon",
"climate": "Hot and Dry",
"code": 802693
},
{
"state": "Maharashtra",
"district": "Amravati",
"city": "Dharni",
"climate": "Hot and Dry",
"code": 900255
},
{
"state": "Maharashtra",
"district": "Amravati",
"city": "Morshi",
"climate": "Hot and Dry",
"code": 802687
},
{
"state": "Maharashtra",
"district": "Amravati",
"city": "Nandgaon Khandeshwar",
"climate": "Hot and Dry",
"code": 900260
},
{
"state": "Maharashtra",
"district": "Amravati",
"city": "Shendurjanaghat",
"climate": "Hot and Dry",
"code": 802689
},
{
"state": "Maharashtra",
"district": "Amravati",
"city": "Teosa",
"climate": "Hot and Dry",
"code": 900332
},
{
"state": "Maharashtra",
"district": "Amravati",
"city": "Warud",
"climate": "Hot and Dry",
"code": 802688
},
{
"state": "Maharashtra",
"district": "Aurangabad",
"city": "Aurangabad",
"climate": "Hot and Dry",
"code": 802765
},
{
"state": "Maharashtra",
"district": "Aurangabad",
"city": "Aurangabad Cantonment",
"climate": "Hot and Dry",
"code": 802766
},
{
"state": "Maharashtra",
"district": "Aurangabad",
"city": "Gangapur_A",
"climate": "Hot and Dry",
"code": 802769
},
{
"state": "Maharashtra",
"district": "Aurangabad",
"city": "Kannad",
"climate": "Hot and Dry",
"code": 802763
},
{
"state": "Maharashtra",
"district": "Aurangabad",
"city": "Khuldabad",
"climate": "Hot and Dry",
"code": 802767
},
{
"state": "Maharashtra",
"district": "Aurangabad",
"city": "Paithan",
"climate": "Hot and Dry",
"code": 802770
},
{
"state": "Maharashtra",
"district": "Aurangabad",
"city": "Phulambri",
"climate": "Hot and Dry",
"code": 900263
},
{
"state": "Maharashtra",
"district": "Aurangabad",
"city": "Sillod",
"climate": "Hot and Dry",
"code": 802764
},
{
"state": "Maharashtra",
"district": "Aurangabad",
"city": "Soygaon",
"climate": "Hot and Dry",
"code": 900264
},
{
"state": "Maharashtra",
"district": "Aurangabad",
"city": "Vaijapur",
"climate": "Hot and Dry",
"code": 802768
},
{
"state": "Maharashtra",
"district": "Beed",
"city": "Ambajogi",
"climate": "Hot and Dry",
"code": 802839
},
{
"state": "Maharashtra",
"district": "Beed",
"city": "Ashti_B",
"climate": "Hot and Dry",
"code": 900266
},
{
"state": "Maharashtra",
"district": "Beed",
"city": "Beed",
"climate": "Hot and Dry",
"code": 802835
},
{
"state": "Maharashtra",
"district": "Beed",
"city": "Dharur",
"climate": "Hot and Dry",
"code": 802837
},
{
"state": "Maharashtra",
"district": "Beed",
"city": "Georai",
"climate": "Hot and Dry",
"code": 802833
},
{
"state": "Maharashtra",
"district": "Beed",
"city": "Kaij",
"climate": "Hot and Dry",
"code": 802836
},
{
"state": "Maharashtra",
"district": "Beed",
"city": "Majalegaon",
"climate": "Hot and Dry",
"code": 802834
},
{
"state": "Maharashtra",
"district": "Beed",
"city": "Parli",
"climate": "Hot and Dry",
"code": 802838
},
{
"state": "Maharashtra",
"district": "Beed",
"city": "Patoda",
"climate": "Hot and Dry",
"code": 900254
},
{
"state": "Maharashtra",
"district": "Beed",
"city": "Shirur Kasar",
"climate": "Hot and Dry",
"code": 900267
},
{
"state": "Maharashtra",
"district": "Beed",
"city": "Wadavani",
"climate": "Hot and Dry",
"code": 900265
},
{
"state": "Maharashtra",
"district": "Bhandara",
"city": "Bhandara",
"climate": "Composite",
"code": 802713
},
{
"state": "Maharashtra",
"district": "Bhandara",
"city": "Lakhandur",
"climate": "Composite",
"code": 900291
},
{
"state": "Maharashtra",
"district": "Bhandara",
"city": "Lakhani",
"climate": "Composite",
"code": 900290
},
{
"state": "Maharashtra",
"district": "Bhandara",
"city": "Mohadi",
"climate": "Composite",
"code": 900292
},
{
"state": "Maharashtra",
"district": "Bhandara",
"city": "Pauni",
"climate": "Composite",
"code": 802714
},
{
"state": "Maharashtra",
"district": "Bhandara",
"city": "Sakoli",
"climate": "Composite",
"code": 900258
},
{
"state": "Maharashtra",
"district": "Bhandara",
"city": "Tumsar",
"climate": "Composite",
"code": 802712
},
{
"state": "Maharashtra",
"district": "Buldana",
"city": "Buldana",
"climate": "Hot and Dry",
"code": 802669
},
{
"state": "Maharashtra",
"district": "Buldana",
"city": "Chikhli",
"climate": "Hot and Dry",
"code": 802668
},
{
"state": "Maharashtra",
"district": "Buldana",
"city": "Deulgaon Raja",
"climate": "Hot and Dry",
"code": 802670
},
{
"state": "Maharashtra",
"district": "Buldana",
"city": "Jalgaon Jamod",
"climate": "Hot and Dry",
"code": 802662
},
{
"state": "Maharashtra",
"district": "Buldana",
"city": "Khamgaon",
"climate": "Hot and Dry",
"code": 802666
},
{
"state": "Maharashtra",
"district": "Buldana",
"city": "Lonar",
"climate": "Hot and Dry",
"code": 802672
},
{
"state": "Maharashtra",
"district": "Buldana",
"city": "Malkapur_B",
"climate": "Hot and Dry",
"code": 802665
},
{
"state": "Maharashtra",
"district": "Buldana",
"city": "Mehkar",
"climate": "Hot and Dry",
"code": 802667
},
{
"state": "Maharashtra",
"district": "Buldana",
"city": "Motala",
"climate": "Hot and Dry",
"code": 900321
},
{
"state": "Maharashtra",
"district": "Buldana",
"city": "Nandura",
"climate": "Hot and Dry",
"code": 802664
},
{
"state": "Maharashtra",
"district": "Buldana",
"city": "Sangrampur",
"climate": "Hot and Dry",
"code": 900226
},
{
"state": "Maharashtra",
"district": "Buldana",
"city": "Shegaon",
"climate": "Hot and Dry",
"code": 802663
},
{
"state": "Maharashtra",
"district": "Buldana",
"city": "Sindkhed Raja",
"climate": "Hot and Dry",
"code": 802671
},
{
"state": "Maharashtra",
"district": "Chandrapur",
"city": "Badravati",
"climate": "Warm & humid",
"code": 802721
},
{
"state": "Maharashtra",
"district": "Chandrapur",
"city": "Ballarpur",
"climate": "Warm & humid",
"code": 802724
},
{
"state": "Maharashtra",
"district": "Chandrapur",
"city": "Bhishi",
"climate": "Warm & humid",
"code": 900865
},
{
"state": "Maharashtra",
"district": "Chandrapur",
"city": "Brahmapuri",
"climate": "Warm & humid",
"code": 802720
},
{
"state": "Maharashtra",
"district": "Chandrapur",
"city": "Chandrapur_M",
"climate": "Warm & humid",
"code": 802722
},
{
"state": "Maharashtra",
"district": "Chandrapur",
"city": "Chimur",
"climate": "Warm & humid",
"code": 900178
},
{
"state": "Maharashtra",
"district": "Chandrapur",
"city": "Gadchandur",
"climate": "Warm & humid",
"code": 900182
},
{
"state": "Maharashtra",
"district": "Chandrapur",
"city": "Ghugghus",
"climate": "Warm & humid",
"code": 900751
},
{
"state": "Maharashtra",
"district": "Chandrapur",
"city": "Gond Pipari",
"climate": "Warm & humid",
"code": 900294
},
{
"state": "Maharashtra",
"district": "Chandrapur",
"city": "Jivati",
"climate": "Warm & humid",
"code": 900295
},
{
"state": "Maharashtra",
"district": "Chandrapur",
"city": "Korpana",
"climate": "Warm & humid",
"code": 900237
},
{
"state": "Maharashtra",
"district": "Chandrapur",
"city": "Mul",
"climate": "Warm & humid",
"code": 802723
},
{
"state": "Maharashtra",
"district": "Chandrapur",
"city": "Nagbhid",
"climate": "Warm & humid",
"code": 900259
},
{
"state": "Maharashtra",
"district": "Chandrapur",
"city": "Pombhurna",
"climate": "Warm & humid",
"code": 900236
},
{
"state": "Maharashtra",
"district": "Chandrapur",
"city": "Rajura",
"climate": "Warm & humid",
"code": 802725
},
{
"state": "Maharashtra",
"district": "Chandrapur",
"city": "Saoli",
"climate": "Warm & humid",
"code": 900252
},
{
"state": "Maharashtra",
"district": "Chandrapur",
"city": "Sindewahi",
"climate": "Warm & humid",
"code": 900293
},
{
"state": "Maharashtra",
"district": "Chandrapur",
"city": "Warora",
"climate": "Warm & humid",
"code": 802719
},
{
"state": "Maharashtra",
"district": "Dhule",
"city": "Dhule",
"climate": "Hot and Dry",
"code": 802646
},
{
"state": "Maharashtra",
"district": "Dhule",
"city": "Doundaicha Warwade",
"climate": "Hot and Dry",
"code": 802645
},
{
"state": "Maharashtra",
"district": "Dhule",
"city": "Sakri",
"climate": "Hot and Dry",
"code": 900328
},
{
"state": "Maharashtra",
"district": "Dhule",
"city": "Shirpur- Warwade",
"climate": "Hot and Dry",
"code": 802644
},
{
"state": "Maharashtra",
"district": "Dhule",
"city": "Sindhkheda",
"climate": "Hot and Dry",
"code": 900194
},
{
"state": "Maharashtra",
"district": "Gadchiroli",
"city": "Aheri",
"climate": "Warm & humid",
"code": 900298
},
{
"state": "Maharashtra",
"district": "Gadchiroli",
"city": "Armori",
"climate": "Warm & humid",
"code": 900296
},
{
"state": "Maharashtra",
"district": "Gadchiroli",
"city": "Bhamragad",
"climate": "Warm & humid",
"code": 900385
},
{
"state": "Maharashtra",
"district": "Gadchiroli",
"city": "Chamorsi",
"climate": "Warm & humid",
"code": 900297
},
{
"state": "Maharashtra",
"district": "Gadchiroli",
"city": "Desaiganj",
"climate": "Warm & humid",
"code": 802717
},
{
"state": "Maharashtra",
"district": "Gadchiroli",
"city": "Dhanora",
"climate": "Warm & humid",
"code": 900302
},
{
"state": "Maharashtra",
"district": "Gadchiroli",
"city": "Etapalli",
"climate": "Warm & humid",
"code": 900301
},
{
"state": "Maharashtra",
"district": "Gadchiroli",
"city": "Gadchiroli",
"climate": "Warm & humid",
"code": 802718
},
{
"state": "Maharashtra",
"district": "Gadchiroli",
"city": "Korchi",
"climate": "Warm & humid",
"code": 900303
},
{
"state": "Maharashtra",
"district": "Gadchiroli",
"city": "Kurkheda",
"climate": "Warm & humid",
"code": 900300
},
{
"state": "Maharashtra",
"district": "Gadchiroli",
"city": "Mulchera",
"climate": "Warm & humid",
"code": 900362
},
{
"state": "Maharashtra",
"district": "Gadchiroli",
"city": "Sironcha",
"climate": "Warm & humid",
"code": 900299
},
{
"state": "Maharashtra",
"district": "Gondiya",
"city": "Amgaon",
"climate": "Composite",
"code": 900585
},
{
"state": "Maharashtra",
"district": "Gondiya",
"city": "Arjuni",
"climate": "Composite",
"code": 900305
},
{
"state": "Maharashtra",
"district": "Gondiya",
"city": "Deori_G",
"climate": "Composite",
"code": 900306
},
{
"state": "Maharashtra",
"district": "Gondiya",
"city": "Gondiya",
"climate": "Composite",
"code": 802716
},
{
"state": "Maharashtra",
"district": "Gondiya",
"city": "Goregaon",
"climate": "Composite",
"code": 900304
},
{
"state": "Maharashtra",
"district": "Gondiya",
"city": "Sadak Arjuni",
"climate": "Composite",
"code": 900363
},
{
"state": "Maharashtra",
"district": "Gondiya",
"city": "Salekasa",
"climate": "Composite",
"code": 900378
},
{
"state": "Maharashtra",
"district": "Gondiya",
"city": "Tirora",
"climate": "Composite",
"code": 802715
},
{
"state": "Maharashtra",
"district": "Hingoli",
"city": "Aundha",
"climate": "Hot and Dry",
"code": 900268
},
{
"state": "Maharashtra",
"district": "Hingoli",
"city": "Basmat",
"climate": "Hot and Dry",
"code": 802750
},
{
"state": "Maharashtra",
"district": "Hingoli",
"city": "Hingoli",
"climate": "Hot and Dry",
"code": 802748
},
{
"state": "Maharashtra",
"district": "Hingoli",
"city": "Kalamnuri",
"climate": "Hot and Dry",
"code": 802749
},
{
"state": "Maharashtra",
"district": "Hingoli",
"city": "Sengaon",
"climate": "Hot and Dry",
"code": 900316
},
{
"state": "Maharashtra",
"district": "Jalgaon",
"city": "Amalner",
"climate": "Hot and Dry",
"code": 802656
},
{
"state": "Maharashtra",
"district": "Jalgaon",
"city": "Bhadgaon",
"climate": "Hot and Dry",
"code": 802658
},
{
"state": "Maharashtra",
"district": "Jalgaon",
"city": "Bhusawal",
"climate": "Hot and Dry",
"code": 802652
},
{
"state": "Maharashtra",
"district": "Jalgaon",
"city": "Bodwad",
"climate": "Hot and Dry",
"code": 900337
},
{
"state": "Maharashtra",
"district": "Jalgaon",
"city": "Chalisgaon",
"climate": "Hot and Dry",
"code": 802659
},
{
"state": "Maharashtra",
"district": "Jalgaon",
"city": "Chopada",
"climate": "Hot and Dry",
"code": 802647
},
{
"state": "Maharashtra",
"district": "Jalgaon",
"city": "Dharangaon",
"climate": "Hot and Dry",
"code": 802655
},
{
"state": "Maharashtra",
"district": "Jalgaon",
"city": "Erandol",
"climate": "Hot and Dry",
"code": 802654
},
{
"state": "Maharashtra",
"district": "Jalgaon",
"city": "Faizpur",
"climate": "Hot and Dry",
"code": 802649
},
{
"state": "Maharashtra",
"district": "Jalgaon",
"city": "Jalgaon",
"climate": "Hot and Dry",
"code": 802653
},
{
"state": "Maharashtra",
"district": "Jalgaon",
"city": "Jamner",
"climate": "Hot and Dry",
"code": 802661
},
{
"state": "Maharashtra",
"district": "Jalgaon",
"city": "Muktai Nagar",
"climate": "Hot and Dry",
"code": 900587
},
{
"state": "Maharashtra",
"district": "Jalgaon",
"city": "Nashirabad",
"climate": "Hot and Dry",
"code": 900868
},
{
"state": "Maharashtra",
"district": "Jalgaon",
"city": "Pachora",
"climate": "Hot and Dry",
"code": 802660
},
{
"state": "Maharashtra",
"district": "Jalgaon",
"city": "Parola",
"climate": "Hot and Dry",
"code": 802657
},
{
"state": "Maharashtra",
"district": "Jalgaon",
"city": "Raver",
"climate": "Hot and Dry",
"code": 802651
},
{
"state": "Maharashtra",
"district": "Jalgaon",
"city": "Savda",
"climate": "Hot and Dry",
"code": 802650
},
{
"state": "Maharashtra",
"district": "Jalgaon",
"city": "Shendurni",
"climate": "Hot and Dry",
"code": 900588
},
{
"state": "Maharashtra",
"district": "Jalgaon",
"city": "Varangaon",
"climate": "Hot and Dry",
"code": 900367
},
{
"state": "Maharashtra",
"district": "Jalgaon",
"city": "Yawal",
"climate": "Hot and Dry",
"code": 802648
},
{
"state": "Maharashtra",
"district": "Jalna",
"city": "Ambad",
"climate": "Hot and Dry",
"code": 802761
},
{
"state": "Maharashtra",
"district": "Jalna",
"city": "Badnapur",
"climate": "Hot and Dry",
"code": 900335
},
{
"state": "Maharashtra",
"district": "Jalna",
"city": "Bhokardan",
"climate": "Hot and Dry",
"code": 802759
},
{
"state": "Maharashtra",
"district": "Jalna",
"city": "Ghansawangi",
"climate": "Hot and Dry",
"code": 900336
},
{
"state": "Maharashtra",
"district": "Jalna",
"city": "Jafrabad",
"climate": "Hot and Dry",
"code": 900334
},
{
"state": "Maharashtra",
"district": "Jalna",
"city": "Jalna",
"climate": "Hot and Dry",
"code": 802760
},
{
"state": "Maharashtra",
"district": "Jalna",
"city": "Mantha",
"climate": "Hot and Dry",
"code": 900333
},
{
"state": "Maharashtra",
"district": "Jalna",
"city": "Partur",
"climate": "Hot and Dry",
"code": 802762
},
{
"state": "Maharashtra",
"district": "Jalna",
"city": "Tirthpuri",
"climate": "Hot and Dry",
"code": 900862
},
{
"state": "Maharashtra",
"district": "Kolhapur",
"city": "Ajara",
"climate": "Warm & humid",
"code": 900589
},
{
"state": "Maharashtra",
"district": "Kolhapur",
"city": "Chandgad",
"climate": "Warm & humid",
"code": 900590
},
{
"state": "Maharashtra",
"district": "Kolhapur",
"city": "Gadhinglaj",
"climate": "Warm & humid",
"code": 802890
},
{
"state": "Maharashtra",
"district": "Kolhapur",
"city": "Hatkangale",
"climate": "Warm & humid",
"code": 900591
},
{
"state": "Maharashtra",
"district": "Kolhapur",
"city": "Hupari",
"climate": "Warm & humid",
"code": 900592
},
{
"state": "Maharashtra",
"district": "Kolhapur",
"city": "Ichalkaranji",
"climate": "Warm & humid",
"code": 802884
},
{
"state": "Maharashtra",
"district": "Kolhapur",
"city": "Jaysingpur",
"climate": "Warm & humid",
"code": 802885
},
{
"state": "Maharashtra",
"district": "Kolhapur",
"city": "Kagal",
"climate": "Warm & humid",
"code": 802888
},
{
"state": "Maharashtra",
"district": "Kolhapur",
"city": "Kolhapur",
"climate": "Warm & humid",
"code": 802887
},
{
"state": "Maharashtra",
"district": "Kolhapur",
"city": "Kurundvad",
"climate": "Warm & humid",
"code": 802886
},
{
"state": "Maharashtra",
"district": "Kolhapur",
"city": "Malkapur_K",
"climate": "Warm & humid",
"code": 802881
},
{
"state": "Maharashtra",
"district": "Kolhapur",
"city": "Murgud",
"climate": "Warm & humid",
"code": 802889
},
{
"state": "Maharashtra",
"district": "Kolhapur",
"city": "Panhala",
"climate": "Warm & humid",
"code": 802882
},
{
"state": "Maharashtra",
"district": "Kolhapur",
"city": "Shirol",
"climate": "Warm & humid",
"code": 900593
},
{
"state": "Maharashtra",
"district": "Kolhapur",
"city": "Vadgaon",
"climate": "Warm & humid",
"code": 802883
},
{
"state": "Maharashtra",
"district": "Latur",
"city": "Ahmedpur",
"climate": "Hot and Dry",
"code": 802841
},
{
"state": "Maharashtra",
"district": "Latur",
"city": "Ausa",
"climate": "Hot and Dry",
"code": 802842
},
{
"state": "Maharashtra",
"district": "Latur",
"city": "Chakur",
"climate": "Hot and Dry",
"code": 900269
},
{
"state": "Maharashtra",
"district": "Latur",
"city": "Deoni",
"climate": "Hot and Dry",
"code": 900327
},
{
"state": "Maharashtra",
"district": "Latur",
"city": "Jalkot",
"climate": "Hot and Dry",
"code": 900257
},
{
"state": "Maharashtra",
"district": "Latur",
"city": "Latur",
"climate": "Hot and Dry",
"code": 802840
},
{
"state": "Maharashtra",
"district": "Latur",
"city": "Nilanga",
"climate": "Hot and Dry",
"code": 802843
},
{
"state": "Maharashtra",
"district": "Latur",
"city": "Renapur",
"climate": "Hot and Dry",
"code": 900271
},
{
"state": "Maharashtra",
"district": "Latur",
"city": "Shirur Anantpal",
"climate": "Hot and Dry",
"code": 900272
},
{
"state": "Maharashtra",
"district": "Latur",
"city": "Udgir",
"climate": "Hot and Dry",
"code": 802844
},
{
"state": "Maharashtra",
"district": "Mumbai",
"city": "Greater Mumbai",
"climate": "Warm & humid",
"code": 802794
},
{
"state": "Maharashtra",
"district": "Nagpur",
"city": "Bhiwapur",
"climate": "Composite",
"code": 900253
},
{
"state": "Maharashtra",
"district": "Nagpur",
"city": "Butibori",
"climate": "Composite",
"code": 900586
},
{
"state": "Maharashtra",
"district": "Nagpur",
"city": "Hingana",
"climate": "Composite",
"code": 900308
},
{
"state": "Maharashtra",
"district": "Nagpur",
"city": "Kalameshwar",
"climate": "Composite",
"code": 802703
},
{
"state": "Maharashtra",
"district": "Nagpur",
"city": "Kamptee",
"climate": "Composite",
"code": 802708
},
{
"state": "Maharashtra",
"district": "Nagpur",
"city": "Kamptee Cantonment",
"climate": "Composite",
"code": 802709
},
{
"state": "Maharashtra",
"district": "Nagpur",
"city": "Kanhan-Pipri",
"climate": "Composite",
"code": 900184
},
{
"state": "Maharashtra",
"district": "Nagpur",
"city": "Katol",
"climate": "Composite",
"code": 802702
},
{
"state": "Maharashtra",
"district": "Nagpur",
"city": "Khapa",
"climate": "Composite",
"code": 802706
},
{
"state": "Maharashtra",
"district": "Nagpur",
"city": "Kuhi",
"climate": "Composite",
"code": 900307
},
{
"state": "Maharashtra",
"district": "Nagpur",
"city": "Mahadula",
"climate": "Composite",
"code": 900131
},
{
"state": "Maharashtra",
"district": "Nagpur",
"city": "Mauda Ct",
"climate": "Composite",
"code": 900132
},
{
"state": "Maharashtra",
"district": "Nagpur",
"city": "Mohpa",
"climate": "Composite",
"code": 802704
},
{
"state": "Maharashtra",
"district": "Nagpur",
"city": "Mowad",
"climate": "Composite",
"code": 802700
},
{
"state": "Maharashtra",
"district": "Nagpur",
"city": "Nagpur",
"climate": "Composite",
"code": 802710
},
{
"state": "Maharashtra",
"district": "Nagpur",
"city": "Narkhed",
"climate": "Composite",
"code": 802701
},
{
"state": "Maharashtra",
"district": "Nagpur",
"city": "Parsivni",
"climate": "Composite",
"code": 900490
},
{
"state": "Maharashtra",
"district": "Nagpur",
"city": "Ramtek",
"climate": "Composite",
"code": 802707
},
{
"state": "Maharashtra",
"district": "Nagpur",
"city": "Savner",
"climate": "Composite",
"code": 802705
},
{
"state": "Maharashtra",
"district": "Nagpur",
"city": "Umred",
"climate": "Composite",
"code": 802711
},
{
"state": "Maharashtra",
"district": "Nagpur",
"city": "Wadi",
"climate": "Composite",
"code": 900185
},
{
"state": "Maharashtra",
"district": "Nagpur",
"city": "Wanadongri",
"climate": "Composite",
"code": 900379
},
{
"state": "Maharashtra",
"district": "Nanded Waghala",
"city": "Ardharpur",
"climate": "Hot and Dry",
"code": 900013
},
{
"state": "Maharashtra",
"district": "Nanded Waghala",
"city": "Bhokar",
"climate": "Hot and Dry",
"code": 802739
},
{
"state": "Maharashtra",
"district": "Nanded Waghala",
"city": "Biloli",
"climate": "Hot and Dry",
"code": 802743
},
{
"state": "Maharashtra",
"district": "Nanded Waghala",
"city": "Deglur",
"climate": "Hot and Dry",
"code": 802747
},
{
"state": "Maharashtra",
"district": "Nanded Waghala",
"city": "Dharmabad",
"climate": "Hot and Dry",
"code": 802741
},
{
"state": "Maharashtra",
"district": "Nanded Waghala",
"city": "Hadgaon",
"climate": "Hot and Dry",
"code": 802736
},
{
"state": "Maharashtra",
"district": "Nanded Waghala",
"city": "Himayatnagar",
"climate": "Hot and Dry",
"code": 900274
},
{
"state": "Maharashtra",
"district": "Nanded Waghala",
"city": "Kandhar",
"climate": "Hot and Dry",
"code": 802745
},
{
"state": "Maharashtra",
"district": "Nanded Waghala",
"city": "Kinwat",
"climate": "Hot and Dry",
"code": 802735
},
{
"state": "Maharashtra",
"district": "Nanded Waghala",
"city": "Kundalwadi",
"climate": "Hot and Dry",
"code": 802742
},
{
"state": "Maharashtra",
"district": "Nanded Waghala",
"city": "Loha",
"climate": "Hot and Dry",
"code": 802744
},
{
"state": "Maharashtra",
"district": "Nanded Waghala",
"city": "Mahur",
"climate": "Hot and Dry",
"code": 900133
},
{
"state": "Maharashtra",
"district": "Nanded Waghala",
"city": "Mudkhed",
"climate": "Hot and Dry",
"code": 802738
},
{
"state": "Maharashtra",
"district": "Nanded Waghala",
"city": "Mukhed",
"climate": "Hot and Dry",
"code": 802746
},
{
"state": "Maharashtra",
"district": "Nanded Waghala",
"city": "Naigaon",
"climate": "Hot and Dry",
"code": 900273
},
{
"state": "Maharashtra",
"district": "Nanded Waghala",
"city": "Nanded Waghala",
"climate": "Hot and Dry",
"code": 802737
},
{
"state": "Maharashtra",
"district": "Nanded Waghala",
"city": "Peth Umri_N",
"climate": "Hot and Dry",
"code": 802740
},
{
"state": "Maharashtra",
"district": "Nandurbar",
"city": "Dhadgaon Wadfalya",
"climate": "Hot and Dry",
"code": 900313
},
{
"state": "Maharashtra",
"district": "Nandurbar",
"city": "Nandurbar",
"climate": "Hot and Dry",
"code": 802642
},
{
"state": "Maharashtra",
"district": "Nandurbar",
"city": "Nawapur",
"climate": "Hot and Dry",
"code": 802643
},
{
"state": "Maharashtra",
"district": "Nandurbar",
"city": "Shahada",
"climate": "Hot and Dry",
"code": 802641
},
{
"state": "Maharashtra",
"district": "Nandurbar",
"city": "Talode",
"climate": "Hot and Dry",
"code": 802640
},
{
"state": "Maharashtra",
"district": "Nashik",
"city": "Bhagur",
"climate": "Hot and Dry",
"code": 802778
},
{
"state": "Maharashtra",
"district": "Nashik",
"city": "Chandwad",
"climate": "Hot and Dry",
"code": 900326
},
{
"state": "Maharashtra",
"district": "Nashik",
"city": "Deola",
"climate": "Hot and Dry",
"code": 900341
},
{
"state": "Maharashtra",
"district": "Nashik",
"city": "Deolali Cantonment",
"climate": "Hot and Dry",
"code": 802777
},
{
"state": "Maharashtra",
"district": "Nashik",
"city": "Dindori_N",
"climate": "Hot and Dry",
"code": 900338
},
{
"state": "Maharashtra",
"district": "Nashik",
"city": "Igatpuri",
"climate": "Hot and Dry",
"code": 802779
},
{
"state": "Maharashtra",
"district": "Nashik",
"city": "Kalwan",
"climate": "Hot and Dry",
"code": 900339
},
{
"state": "Maharashtra",
"district": "Nashik",
"city": "Malegaon",
"climate": "Hot and Dry",
"code": 802772
},
{
"state": "Maharashtra",
"district": "Nashik",
"city": "Manmad",
"climate": "Hot and Dry",
"code": 802774
},
{
"state": "Maharashtra",
"district": "Nashik",
"city": "Nandgaon",
"climate": "Hot and Dry",
"code": 802773
},
{
"state": "Maharashtra",
"district": "Nashik",
"city": "Nashik",
"climate": "Hot and Dry",
"code": 802776
},
{
"state": "Maharashtra",
"district": "Nashik",
"city": "Niphad",
"climate": "Hot and Dry",
"code": 900340
},
{
"state": "Maharashtra",
"district": "Nashik",
"city": "Ozar",
"climate": "Hot and Dry",
"code": 900861
},
{
"state": "Maharashtra",
"district": "Nashik",
"city": "Peth",
"climate": "Hot and Dry",
"code": 900342
},
{
"state": "Maharashtra",
"district": "Nashik",
"city": "Satana",
"climate": "Hot and Dry",
"code": 802771
},
{
"state": "Maharashtra",
"district": "Nashik",
"city": "Sinnar",
"climate": "Hot and Dry",
"code": 802780
},
{
"state": "Maharashtra",
"district": "Nashik",
"city": "Surgana",
"climate": "Hot and Dry",
"code": 900343
},
{
"state": "Maharashtra",
"district": "Nashik",
"city": "Trimbak",
"climate": "Hot and Dry",
"code": 802775
},
{
"state": "Maharashtra",
"district": "Nashik",
"city": "Yeola",
"climate": "Hot and Dry",
"code": 802781
},
{
"state": "Maharashtra",
"district": "Osmanabad",
"city": "Bhum",
"climate": "Hot and Dry",
"code": 802846
},
{
"state": "Maharashtra",
"district": "Osmanabad",
"city": "Kalamb_O",
"climate": "Hot and Dry",
"code": 802847
},
{
"state": "Maharashtra",
"district": "Osmanabad",
"city": "Lohara B.",
"climate": "Hot and Dry",
"code": 900276
},
{
"state": "Maharashtra",
"district": "Osmanabad",
"city": "Murum",
"climate": "Hot and Dry",
"code": 802851
},
{
"state": "Maharashtra",
"district": "Osmanabad",
"city": "Naldurg",
"climate": "Hot and Dry",
"code": 802850
},
{
"state": "Maharashtra",
"district": "Osmanabad",
"city": "Osmanabad",
"climate": "Hot and Dry",
"code": 802848
},
{
"state": "Maharashtra",
"district": "Osmanabad",
"city": "Paranda",
"climate": "Hot and Dry",
"code": 802845
},
{
"state": "Maharashtra",
"district": "Osmanabad",
"city": "Tuljapur",
"climate": "Hot and Dry",
"code": 802849
},
{
"state": "Maharashtra",
"district": "Osmanabad",
"city": "Umarga",
"climate": "Hot and Dry",
"code": 802852
},
{
"state": "Maharashtra",
"district": "Osmanabad",
"city": "Vashi",
"climate": "Hot and Dry",
"code": 900275
},
{
"state": "Maharashtra",
"district": "Palghar",
"city": "Dahanu",
"climate": "Composite",
"code": 802782
},
{
"state": "Maharashtra",
"district": "Palghar",
"city": "Jawhar",
"climate": "Composite",
"code": 802783
},
{
"state": "Maharashtra",
"district": "Palghar",
"city": "Mokhada",
"climate": "Composite",
"code": 900319
},
{
"state": "Maharashtra",
"district": "Palghar",
"city": "Palghar",
"climate": "Composite",
"code": 802784
},
{
"state": "Maharashtra",
"district": "Palghar",
"city": "Talasari",
"climate": "Composite",
"code": 900318
},
{
"state": "Maharashtra",
"district": "Palghar",
"city": "Vasai Virar",
"climate": "Composite",
"code": 802785
},
{
"state": "Maharashtra",
"district": "Palghar",
"city": "Vikramgad",
"climate": "Composite",
"code": 900320
},
{
"state": "Maharashtra",
"district": "Palghar",
"city": "Wada",
"climate": "Composite",
"code": 900584
},
{
"state": "Maharashtra",
"district": "Parbhani",
"city": "Gangakhed",
"climate": "Hot and Dry",
"code": 802757
},
{
"state": "Maharashtra",
"district": "Parbhani",
"city": "Jintur",
"climate": "Hot and Dry",
"code": 802752
},
{
"state": "Maharashtra",
"district": "Parbhani",
"city": "Manwat",
"climate": "Hot and Dry",
"code": 802754
},
{
"state": "Maharashtra",
"district": "Parbhani",
"city": "Palam",
"climate": "Hot and Dry",
"code": 900277
},
{
"state": "Maharashtra",
"district": "Parbhani",
"city": "Parbhani",
"climate": "Hot and Dry",
"code": 802753
},
{
"state": "Maharashtra",
"district": "Parbhani",
"city": "Pathri",
"climate": "Hot and Dry",
"code": 802755
},
{
"state": "Maharashtra",
"district": "Parbhani",
"city": "Purna",
"climate": "Hot and Dry",
"code": 802758
},
{
"state": "Maharashtra",
"district": "Parbhani",
"city": "Sailu",
"climate": "Hot and Dry",
"code": 802751
},
{
"state": "Maharashtra",
"district": "Parbhani",
"city": "Sonpeth",
"climate": "Hot and Dry",
"code": 802756
},
{
"state": "Maharashtra",
"district": "Pune",
"city": "Alandi",
"climate": "Warm & humid",
"code": 802808
},
{
"state": "Maharashtra",
"district": "Pune",
"city": "Baramati",
"climate": "Warm & humid",
"code": 802820
},
{
"state": "Maharashtra",
"district": "Pune",
"city": "Bhor",
"climate": "Warm & humid",
"code": 802819
},
{
"state": "Maharashtra",
"district": "Pune",
"city": "Chakan",
"climate": "Warm & humid",
"code": 900371
},
{
"state": "Maharashtra",
"district": "Pune",
"city": "Daund",
"climate": "Warm & humid",
"code": 802816
},
{
"state": "Maharashtra",
"district": "Pune",
"city": "Dehu",
"climate": "Warm & humid",
"code": 900753
},
{
"state": "Maharashtra",
"district": "Pune",
"city": "Dehuroad Cantonment",
"climate": "Warm & humid",
"code": 802812
},
{
"state": "Maharashtra",
"district": "Pune",
"city": "Indapur",
"climate": "Warm & humid",
"code": 802821
},
{
"state": "Maharashtra",
"district": "Pune",
"city": "Jejuri",
"climate": "Warm & humid",
"code": 802818
},
{
"state": "Maharashtra",
"district": "Pune",
"city": "Junnar",
"climate": "Warm & humid",
"code": 802806
},
{
"state": "Maharashtra",
"district": "Pune",
"city": "Kirkee Cantonment",
"climate": "Warm & humid",
"code": 802815
},
{
"state": "Maharashtra",
"district": "Pune",
"city": "Lonavala",
"climate": "Warm & humid",
"code": 802810
},
{
"state": "Maharashtra",
"district": "Pune",
"city": "MalegaonÃ¢Â",
"climate": "Warm & humid",
"code": 900752
},
{
"state": "Maharashtra",
"district": "Pune",
"city": "Manchar",
"climate": "Warm & humid",
"code": 900867
},
{
"state": "Maharashtra",
"district": "Pune",
"city": "Pimpri Chinchwad",
"climate": "Warm & humid",
"code": 802811
},
{
"state": "Maharashtra",
"district": "Pune",
"city": "Pune",
"climate": "Warm & humid",
"code": 802814
},
{
"state": "Maharashtra",
"district": "Pune",
"city": "Pune Cantonment",
"climate": "Warm & humid",
"code": 802813
},
{
"state": "Maharashtra",
"district": "Pune",
"city": "Rajguru Nagar",
"climate": "Warm & humid",
"code": 900233
},
{
"state": "Maharashtra",
"district": "Pune",
"city": "Sasvad",
"climate": "Warm & humid",
"code": 802817
},
{
"state": "Maharashtra",
"district": "Pune",
"city": "Shirur",
"climate": "Warm & humid",
"code": 802807
},
{
"state": "Maharashtra",
"district": "Pune",
"city": "Talegaon Dabhade",
"climate": "Warm & humid",
"code": 802809
},
{
"state": "Maharashtra",
"district": "Pune",
"city": "Vadgaon Maval",
"climate": "Warm & humid",
"code": 900594
},
{
"state": "Maharashtra",
"district": "Raigadh",
"city": "Alibag",
"climate": "Warm & humid",
"code": 802801
},
{
"state": "Maharashtra",
"district": "Raigadh",
"city": "Karjat_R",
"climate": "Warm & humid",
"code": 802798
},
{
"state": "Maharashtra",
"district": "Raigadh",
"city": "Khalapur",
"climate": "Warm & humid",
"code": 900280
},
{
"state": "Maharashtra",
"district": "Raigadh",
"city": "Khopoli",
"climate": "Warm & humid",
"code": 802799
},
{
"state": "Maharashtra",
"district": "Raigadh",
"city": "Mahad",
"climate": "Warm & humid",
"code": 802805
},
{
"state": "Maharashtra",
"district": "Raigadh",
"city": "Mangaon",
"climate": "Warm & humid",
"code": 900278
},
{
"state": "Maharashtra",
"district": "Raigadh",
"city": "Matheran",
"climate": "Warm & humid",
"code": 802797
},
{
"state": "Maharashtra",
"district": "Raigadh",
"city": "Mhasala",
"climate": "Warm & humid",
"code": 900282
},
{
"state": "Maharashtra",
"district": "Raigadh",
"city": "Murud-Janjira",
"climate": "Warm & humid",
"code": 802802
},
{
"state": "Maharashtra",
"district": "Raigadh",
"city": "Pali",
"climate": "Warm & humid",
"code": 900863
},
{
"state": "Maharashtra",
"district": "Raigadh",
"city": "Panvel",
"climate": "Warm & humid",
"code": 802796
},
{
"state": "Maharashtra",
"district": "Raigadh",
"city": "Pen",
"climate": "Warm & humid",
"code": 802800
},
{
"state": "Maharashtra",
"district": "Raigadh",
"city": "Poladpur",
"climate": "Warm & humid",
"code": 900281
},
{
"state": "Maharashtra",
"district": "Raigadh",
"city": "Roha Ashtami",
"climate": "Warm & humid",
"code": 802803
},
{
"state": "Maharashtra",
"district": "Raigadh",
"city": "Shriwardhan",
"climate": "Warm & humid",
"code": 802804
},
{
"state": "Maharashtra",
"district": "Raigadh",
"city": "Tala",
"climate": "Warm & humid",
"code": 900279
},
{
"state": "Maharashtra",
"district": "Raigadh",
"city": "Uran",
"climate": "Warm & humid",
"code": 802795
},
{
"state": "Maharashtra",
"district": "Ratnagiri",
"city": "Chiplun",
"climate": "Warm & humid",
"code": 802874
},
{
"state": "Maharashtra",
"district": "Ratnagiri",
"city": "Dapoli Camp",
"climate": "Warm & humid",
"code": 802872
},
{
"state": "Maharashtra",
"district": "Ratnagiri",
"city": "Devrukh",
"climate": "Warm & humid",
"code": 900026
},
{
"state": "Maharashtra",
"district": "Ratnagiri",
"city": "Guhagar",
"climate": "Warm & humid",
"code": 900025
},
{
"state": "Maharashtra",
"district": "Ratnagiri",
"city": "Khed",
"climate": "Warm & humid",
"code": 802873
},
{
"state": "Maharashtra",
"district": "Ratnagiri",
"city": "Lanja",
"climate": "Warm & humid",
"code": 900152
},
{
"state": "Maharashtra",
"district": "Ratnagiri",
"city": "Mandangad",
"climate": "Warm & humid",
"code": 900283
},
{
"state": "Maharashtra",
"district": "Ratnagiri",
"city": "Rajapur",
"climate": "Warm & humid",
"code": 802876
},
{
"state": "Maharashtra",
"district": "Ratnagiri",
"city": "Ratnagiri",
"climate": "Warm & humid",
"code": 802875
},
{
"state": "Maharashtra",
"district": "Sangli",
"city": "Ashta",
"climate": "Warm & humid",
"code": 802892
},
{
"state": "Maharashtra",
"district": "Sangli",
"city": "Atpadi",
"climate": "Warm & humid",
"code": 900864
},
{
"state": "Maharashtra",
"district": "Sangli",
"city": "Jath",
"climate": "Warm & humid",
"code": 900027
},
{
"state": "Maharashtra",
"district": "Sangli",
"city": "Kadegaon",
"climate": "Warm & humid",
"code": 900346
},
{
"state": "Maharashtra",
"district": "Sangli",
"city": "Kavathe Mahankal",
"climate": "Warm & humid",
"code": 900344
},
{
"state": "Maharashtra",
"district": "Sangli",
"city": "Khanapur_M",
"climate": "Warm & humid",
"code": 900372
},
{
"state": "Maharashtra",
"district": "Sangli",
"city": "Palus",
"climate": "Warm & humid",
"code": 900373
},
{
"state": "Maharashtra",
"district": "Sangli",
"city": "Sangli",
"climate": "Warm & humid",
"code": 802895
},
{
"state": "Maharashtra",
"district": "Sangli",
"city": "Shirala",
"climate": "Warm & humid",
"code": 900345
},
{
"state": "Maharashtra",
"district": "Sangli",
"city": "Tasgaon",
"climate": "Warm & humid",
"code": 802894
},
{
"state": "Maharashtra",
"district": "Sangli",
"city": "Uran Islampur",
"climate": "Warm & humid",
"code": 802891
},
{
"state": "Maharashtra",
"district": "Sangli",
"city": "Vita",
"climate": "Warm & humid",
"code": 802893
},
{
"state": "Maharashtra",
"district": "Satara",
"city": "Dahiwadi",
"climate": "Cold",
"code": 900351
},
{
"state": "Maharashtra",
"district": "Satara",
"city": "Karhad",
"climate": "Cold",
"code": 802870
},
{
"state": "Maharashtra",
"district": "Satara",
"city": "Khandala",
"climate": "Cold",
"code": 900352
},
{
"state": "Maharashtra",
"district": "Satara",
"city": "Koregaon",
"climate": "Cold",
"code": 900348
},
{
"state": "Maharashtra",
"district": "Satara",
"city": "Lonand",
"climate": "Cold",
"code": 900347
},
{
"state": "Maharashtra",
"district": "Satara",
"city": "Mahabaleshwar",
"climate": "Cold",
"code": 802863
},
{
"state": "Maharashtra",
"district": "Satara",
"city": "Malkapur_S",
"climate": "Cold",
"code": 802871
},
{
"state": "Maharashtra",
"district": "Satara",
"city": "Medha",
"climate": "Cold",
"code": 900353
},
{
"state": "Maharashtra",
"district": "Satara",
"city": "Mhaswad",
"climate": "Cold",
"code": 802867
},
{
"state": "Maharashtra",
"district": "Satara",
"city": "Panchgani",
"climate": "Cold",
"code": 802864
},
{
"state": "Maharashtra",
"district": "Satara",
"city": "Patan_Mh",
"climate": "Cold",
"code": 900350
},
{
"state": "Maharashtra",
"district": "Satara",
"city": "Phaltan",
"climate": "Cold",
"code": 802866
},
{
"state": "Maharashtra",
"district": "Satara",
"city": "Rahimatpur",
"climate": "Cold",
"code": 802868
},
{
"state": "Maharashtra",
"district": "Satara",
"city": "Satara",
"climate": "Cold",
"code": 802869
},
{
"state": "Maharashtra",
"district": "Satara",
"city": "Waduj",
"climate": "Cold",
"code": 900349
},
{
"state": "Maharashtra",
"district": "Satara",
"city": "Wai",
"climate": "Cold",
"code": 802865
},
{
"state": "Maharashtra",
"district": "Sindhudurga",
"city": "Devgad",
"climate": "Warm & humid",
"code": 900287
},
{
"state": "Maharashtra",
"district": "Sindhudurga",
"city": "Kankavli",
"climate": "Warm & humid",
"code": 802877
},
{
"state": "Maharashtra",
"district": "Sindhudurga",
"city": "Kasai Dodamarg",
"climate": "Warm & humid",
"code": 900286
},
{
"state": "Maharashtra",
"district": "Sindhudurga",
"city": "Kudal",
"climate": "Warm & humid",
"code": 900284
},
{
"state": "Maharashtra",
"district": "Sindhudurga",
"city": "Malwan",
"climate": "Warm & humid",
"code": 802878
},
{
"state": "Maharashtra",
"district": "Sindhudurga",
"city": "Sawantwadi",
"climate": "Warm & humid",
"code": 802880
},
{
"state": "Maharashtra",
"district": "Sindhudurga",
"city": "Vaibhavwadi",
"climate": "Warm & humid",
"code": 900285
},
{
"state": "Maharashtra",
"district": "Sindhudurga",
"city": "Vengurla",
"climate": "Warm & humid",
"code": 802879
},
{
"state": "Maharashtra",
"district": "Solapur",
"city": "Akkalkot",
"climate": "Hot and Dry",
"code": 802860
},
{
"state": "Maharashtra",
"district": "Solapur",
"city": "Akluj",
"climate": "Hot and Dry",
"code": 900858
},
{
"state": "Maharashtra",
"district": "Solapur",
"city": "Angar",
"climate": "Hot and Dry",
"code": 900866
},
{
"state": "Maharashtra",
"district": "Solapur",
"city": "Barshi",
"climate": "Hot and Dry",
"code": 802855
},
{
"state": "Maharashtra",
"district": "Solapur",
"city": "Dudhani",
"climate": "Hot and Dry",
"code": 802862
},
{
"state": "Maharashtra",
"district": "Solapur",
"city": "Karmala",
"climate": "Hot and Dry",
"code": 802853
},
{
"state": "Maharashtra",
"district": "Solapur",
"city": "Kurduvadi",
"climate": "Hot and Dry",
"code": 802854
},
{
"state": "Maharashtra",
"district": "Solapur",
"city": "Madha",
"climate": "Hot and Dry",
"code": 900315
},
{
"state": "Maharashtra",
"district": "Solapur",
"city": "Mahalung Shripur",
"climate": "Hot and Dry",
"code": 900750
},
{
"state": "Maharashtra",
"district": "Solapur",
"city": "Maindargi",
"climate": "Hot and Dry",
"code": 802861
},
{
"state": "Maharashtra",
"district": "Solapur",
"city": "Malshiras",
"climate": "Hot and Dry",
"code": 900314
},
{
"state": "Maharashtra",
"district": "Solapur",
"city": "Mangalvedhe",
"climate": "Hot and Dry",
"code": 802859
},
{
"state": "Maharashtra",
"district": "Solapur",
"city": "Mohol",
"climate": "Hot and Dry",
"code": 900317
},
{
"state": "Maharashtra",
"district": "Solapur",
"city": "Natepute",
"climate": "Hot and Dry",
"code": 900859
},
{
"state": "Maharashtra",
"district": "Solapur",
"city": "Pandharpur",
"climate": "Hot and Dry",
"code": 802857
},
{
"state": "Maharashtra",
"district": "Solapur",
"city": "Sangole",
"climate": "Hot and Dry",
"code": 802858
},
{
"state": "Maharashtra",
"district": "Solapur",
"city": "Solapur",
"climate": "Hot and Dry",
"code": 802856
},
{
"state": "Maharashtra",
"district": "Solapur",
"city": "Vairag",
"climate": "Hot and Dry",
"code": 900860
},
{
"state": "Maharashtra",
"district": "Thane",
"city": "Ambarnath",
"climate": "Warm & humid",
"code": 802793
},
{
"state": "Maharashtra",
"district": "Thane",
"city": "Bhiwandi Nizampur",
"climate": "Warm & humid",
"code": 802789
},
{
"state": "Maharashtra",
"district": "Thane",
"city": "Kalyan Dombivali",
"climate": "Warm & humid",
"code": 802790
},
{
"state": "Maharashtra",
"district": "Thane",
"city": "Kulgaon-Badlapur",
"climate": "Warm & humid",
"code": 802792
},
{
"state": "Maharashtra",
"district": "Thane",
"city": "Mira-Bhayandar",
"climate": "Warm & humid",
"code": 802786
},
{
"state": "Maharashtra",
"district": "Thane",
"city": "Murbad",
"climate": "Warm & humid",
"code": 900288
},
{
"state": "Maharashtra",
"district": "Thane",
"city": "Navi Mumbai",
"climate": "Warm & humid",
"code": 802788
},
{
"state": "Maharashtra",
"district": "Thane",
"city": "Shahpur_T",
"climate": "Warm & humid",
"code": 900289
},
{
"state": "Maharashtra",
"district": "Thane",
"city": "Thane",
"climate": "Warm & humid",
"code": 802787
},
{
"state": "Maharashtra",
"district": "Thane",
"city": "Ulhasnagar",
"climate": "Warm & humid",
"code": 802791
},
{
"state": "Maharashtra",
"district": "Wardha",
"city": "Arvi",
"climate": "Hot and Dry",
"code": 802694
},
{
"state": "Maharashtra",
"district": "Wardha",
"city": "Ashti_W",
"climate": "Hot and Dry",
"code": 900311
},
{
"state": "Maharashtra",
"district": "Wardha",
"city": "Deoli_W",
"climate": "Hot and Dry",
"code": 802698
},
{
"state": "Maharashtra",
"district": "Wardha",
"city": "Hinganghat",
"climate": "Hot and Dry",
"code": 802699
},
{
"state": "Maharashtra",
"district": "Wardha",
"city": "Karanja",
"climate": "Hot and Dry",
"code": 900312
},
{
"state": "Maharashtra",
"district": "Wardha",
"city": "Pulgaon",
"climate": "Hot and Dry",
"code": 802697
},
{
"state": "Maharashtra",
"district": "Wardha",
"city": "Samudrapur",
"climate": "Hot and Dry",
"code": 900309
},
{
"state": "Maharashtra",
"district": "Wardha",
"city": "Selu",
"climate": "Hot and Dry",
"code": 900310
},
{
"state": "Maharashtra",
"district": "Wardha",
"city": "Sindi",
"climate": "Hot and Dry",
"code": 802695
},
{
"state": "Maharashtra",
"district": "Wardha",
"city": "Wardha",
"climate": "Hot and Dry",
"code": 802696
},
{
"state": "Maharashtra",
"district": "Washim",
"city": "Karanja_Was",
"climate": "Hot and Dry",
"code": 802680
},
{
"state": "Maharashtra",
"district": "Washim",
"city": "Malegaon Zahangir",
"climate": "Hot and Dry",
"code": 900261
},
{
"state": "Maharashtra",
"district": "Washim",
"city": "Manglurpir",
"climate": "Hot and Dry",
"code": 802679
},
{
"state": "Maharashtra",
"district": "Washim",
"city": "Manora",
"climate": "Hot and Dry",
"code": 900262
},
{
"state": "Maharashtra",
"district": "Washim",
"city": "Risod",
"climate": "Hot and Dry",
"code": 802682
},
{
"state": "Maharashtra",
"district": "Washim",
"city": "Washim",
"climate": "Hot and Dry",
"code": 802681
},
{
"state": "Maharashtra",
"district": "Yavatmal",
"city": "Arni",
"climate": "Composite",
"code": 900143
},
{
"state": "Maharashtra",
"district": "Yavatmal",
"city": "Babhulgaon",
"climate": "Composite",
"code": 900358
},
{
"state": "Maharashtra",
"district": "Yavatmal",
"city": "Darwha",
"climate": "Composite",
"code": 802728
},
{
"state": "Maharashtra",
"district": "Yavatmal",
"city": "Dhanki",
"climate": "Composite",
"code": 900749
},
{
"state": "Maharashtra",
"district": "Yavatmal",
"city": "Digras",
"climate": "Composite",
"code": 802729
},
{
"state": "Maharashtra",
"district": "Yavatmal",
"city": "Ghatanji",
"climate": "Composite",
"code": 802732
},
{
"state": "Maharashtra",
"district": "Yavatmal",
"city": "Kalamb_Y",
"climate": "Composite",
"code": 900355
},
{
"state": "Maharashtra",
"district": "Yavatmal",
"city": "Mahagaon",
"climate": "Composite",
"code": 900356
},
{
"state": "Maharashtra",
"district": "Yavatmal",
"city": "Maregaon",
"climate": "Composite",
"code": 900357
},
{
"state": "Maharashtra",
"district": "Yavatmal",
"city": "Ner",
"climate": "Composite",
"code": 802726
},
{
"state": "Maharashtra",
"district": "Yavatmal",
"city": "Pandharkaoda",
"climate": "Composite",
"code": 802733
},
{
"state": "Maharashtra",
"district": "Yavatmal",
"city": "Pusad",
"climate": "Composite",
"code": 802730
},
{
"state": "Maharashtra",
"district": "Yavatmal",
"city": "Ralegaon",
"climate": "Composite",
"code": 900354
},
{
"state": "Maharashtra",
"district": "Yavatmal",
"city": "Umarkhed",
"climate": "Composite",
"code": 802731
},
{
"state": "Maharashtra",
"district": "Yavatmal",
"city": "Wani",
"climate": "Composite",
"code": 802734
},
{
"state": "Maharashtra",
"district": "Yavatmal",
"city": "Yavatmal",
"climate": "Composite",
"code": 802727
},
{
"state": "Maharashtra",
"district": "Yavatmal",
"city": "Zari",
"climate": "Composite",
"code": 900359
},
{
"state": "Manipur",
"district": "Bishnupur",
"city": "Bishnupur",
"climate": "Warm & humid",
"code": 801471
},
{
"state": "Manipur",
"district": "Bishnupur",
"city": "Kumbi",
"climate": "Warm & humid",
"code": 801475
},
{
"state": "Manipur",
"district": "Bishnupur",
"city": "Kwakta",
"climate": "Warm & humid",
"code": 801474
},
{
"state": "Manipur",
"district": "Bishnupur",
"city": "Moirang",
"climate": "Warm & humid",
"code": 801473
},
{
"state": "Manipur",
"district": "Bishnupur",
"city": "Ningthoukhong",
"climate": "Warm & humid",
"code": 801472
},
{
"state": "Manipur",
"district": "Bishnupur",
"city": "Oinam",
"climate": "Warm & humid",
"code": 801470
},
{
"state": "Manipur",
"district": "Imphal East",
"city": "Andro Nagar",
"climate": "Warm & humid",
"code": 801495
},
{
"state": "Manipur",
"district": "Imphal East",
"city": "Imphal",
"climate": "Warm & humid",
"code": 801487
},
{
"state": "Manipur",
"district": "Imphal East",
"city": "Jiribam",
"climate": "Warm & humid",
"code": 801493
},
{
"state": "Manipur",
"district": "Imphal East",
"city": "Lamlai",
"climate": "Warm & humid",
"code": 801494
},
{
"state": "Manipur",
"district": "Imphal West",
"city": "Lamshang",
"climate": "Warm & humid",
"code": 801485
},
{
"state": "Manipur",
"district": "Imphal West",
"city": "Lilong_I",
"climate": "Warm & humid",
"code": 801492
},
{
"state": "Manipur",
"district": "Imphal West",
"city": "Mayang Imphal",
"climate": "Warm & humid",
"code": 801489
},
{
"state": "Manipur",
"district": "Imphal West",
"city": "Nambol",
"climate": "Warm & humid",
"code": 801469
},
{
"state": "Manipur",
"district": "Imphal West",
"city": "Samurou",
"climate": "Warm & humid",
"code": 801488
},
{
"state": "Manipur",
"district": "Imphal West",
"city": "Sekmai Bazar",
"climate": "Warm & humid",
"code": 801486
},
{
"state": "Manipur",
"district": "Imphal West",
"city": "Thongkhong Laxmi",
"climate": "Warm & humid",
"code": 801490
},
{
"state": "Manipur",
"district": "Imphal West",
"city": "Wangoi",
"climate": "Warm & humid",
"code": 801491
},
{
"state": "Manipur",
"district": "Thoubal",
"city": "Heirok",
"climate": "Warm & humid",
"code": 801477
},
{
"state": "Manipur",
"district": "Thoubal",
"city": "Kakching",
"climate": "Warm & humid",
"code": 801484
},
{
"state": "Manipur",
"district": "Thoubal",
"city": "Kakching Khunou",
"climate": "Warm & humid",
"code": 801483
},
{
"state": "Manipur",
"district": "Thoubal",
"city": "Lilong_T",
"climate": "Warm & humid",
"code": 801476
},
{
"state": "Manipur",
"district": "Thoubal",
"city": "Sikhong Sekmai",
"climate": "Warm & humid",
"code": 801480
},
{
"state": "Manipur",
"district": "Thoubal",
"city": "Sugnu",
"climate": "Warm & humid",
"code": 801482
},
{
"state": "Manipur",
"district": "Thoubal",
"city": "Thoubal",
"climate": "Warm & humid",
"code": 801479
},
{
"state": "Manipur",
"district": "Thoubal",
"city": "Wangjing Lamding",
"climate": "Warm & humid",
"code": 801478
},
{
"state": "Manipur",
"district": "Thoubal",
"city": "Yairipok",
"climate": "Warm & humid",
"code": 801481
},
{
"state": "Meghalaya",
"district": "East Garo Hills",
"city": "Resubelpara",
"climate": "Warm & humid",
"code": 801537
},
{
"state": "Meghalaya",
"district": "East Garo Hills",
"city": "Williamnagar",
"climate": "Warm & humid",
"code": 801538
},
{
"state": "Meghalaya",
"district": "East Khasi",
"city": "Shillong",
"climate": "Warm & humid",
"code": 801544
},
{
"state": "Meghalaya",
"district": "East Khasi",
"city": "Shillong Cantonment",
"climate": "Warm & humid",
"code": 801543
},
{
"state": "Meghalaya",
"district": "Ribhoi",
"city": "Nongpoh",
"climate": "Cold",
"code": 801542
},
{
"state": "Meghalaya",
"district": "South Garo Hills",
"city": "Baghmara",
"climate": "Warm & humid",
"code": 801539
},
{
"state": "Meghalaya",
"district": "West Garo Hills",
"city": "Tura",
"climate": "Warm & humid",
"code": 801536
},
{
"state": "Meghalaya",
"district": "West Jaintia",
"city": "Jowai",
"climate": "Warm & humid",
"code": 801545
},
{
"state": "Meghalaya",
"district": "West Khasi",
"city": "Mairang",
"climate": "Warm & humid",
"code": 801541
},
{
"state": "Meghalaya",
"district": "West Khasi",
"city": "Nongstoin",
"climate": "Warm & humid",
"code": 801540
},
{
"state": "Mizoram",
"district": "Aizawl",
"city": "Aizawl",
"climate": "Warm & humid",
"code": 801506
},
{
"state": "Mizoram",
"district": "Aizawl",
"city": "Darlawn",
"climate": "Warm & humid",
"code": 801504
},
{
"state": "Mizoram",
"district": "Aizawl",
"city": "Sairang",
"climate": "Warm & humid",
"code": 801505
},
{
"state": "Mizoram",
"district": "Aizawl",
"city": "Saitual",
"climate": "Warm & humid",
"code": 801507
},
{
"state": "Mizoram",
"district": "Champhai",
"city": "Biate",
"climate": "Warm & humid",
"code": 801511
},
{
"state": "Mizoram",
"district": "Champhai",
"city": "Champhai",
"climate": "Warm & humid",
"code": 801510
},
{
"state": "Mizoram",
"district": "Champhai",
"city": "Farkawn",
"climate": "Warm & humid",
"code": 900812
},
{
"state": "Mizoram",
"district": "Champhai",
"city": "Khawhai",
"climate": "Warm & humid",
"code": 801509
},
{
"state": "Mizoram",
"district": "Champhai",
"city": "Khawzawl",
"climate": "Warm & humid",
"code": 801508
},
{
"state": "Mizoram",
"district": "Hnahthial",
"city": "Hnahthial",
"climate": "Warm & humid"
},
{
"state": "Mizoram",
"district": "Khawzawl",
"city": "Biate",
"climate": "Warm & humid"
},
{
"state": "Mizoram",
"district": "Khawzawl",
"city": "Khawzawl",
"climate": "Warm & humid"
},
{
"state": "Mizoram",
"district": "Kolasib",
"city": "Bairabi",
"climate": "Warm & humid",
"code": 801502
},
{
"state": "Mizoram",
"district": "Kolasib",
"city": "Kawnpui",
"climate": "Warm & humid",
"code": 801500
},
{
"state": "Mizoram",
"district": "Kolasib",
"city": "Kolasib",
"climate": "Warm & humid",
"code": 801503
},
{
"state": "Mizoram",
"district": "Kolasib",
"city": "Vairengte",
"climate": "Warm & humid",
"code": 801501
},
{
"state": "Mizoram",
"district": "Lawngtlai",
"city": "Lawngtlai",
"climate": "Warm & humid",
"code": 801518
},
{
"state": "Mizoram",
"district": "Lunglei",
"city": "Hnahthial Town",
"climate": "Warm & humid",
"code": 801517
},
{
"state": "Mizoram",
"district": "Lunglei",
"city": "Lunglei",
"climate": "Warm & humid",
"code": 801516
},
{
"state": "Mizoram",
"district": "Lunglei",
"city": "Tlabung",
"climate": "Warm & humid",
"code": 801515
},
{
"state": "Mizoram",
"district": "Mamit",
"city": "Kawrthah",
"climate": "Warm & humid",
"code": 900813
},
{
"state": "Mizoram",
"district": "Mamit",
"city": "Lengpui",
"climate": "Warm & humid",
"code": 801499
},
{
"state": "Mizoram",
"district": "Mamit",
"city": "Mamit",
"climate": "Warm & humid",
"code": 801498
},
{
"state": "Mizoram",
"district": "Mamit",
"city": "West Phaileng",
"climate": "Warm & humid",
"code": 900814
},
{
"state": "Mizoram",
"district": "Mamit",
"city": "Zawlnuam",
"climate": "Warm & humid",
"code": 801497
},
{
"state": "Mizoram",
"district": "Saiha",
"city": "Siaha",
"climate": "Warm & humid",
"code": 801519
},
{
"state": "Mizoram",
"district": "Saitual",
"city": "Ngopa",
"climate": "Warm & humid",
"code": 900815
},
{
"state": "Mizoram",
"district": "Saitual",
"city": "Phullen",
"climate": "Warm & humid",
"code": 900816
},
{
"state": "Mizoram",
"district": "Serchhip",
"city": "N. Vanlaiphai",
"climate": "Warm & humid",
"code": 801514
},
{
"state": "Mizoram",
"district": "Serchhip",
"city": "Serchhip",
"climate": "Warm & humid",
"code": 801512
},
{
"state": "Mizoram",
"district": "Serchhip",
"city": "Thenzawl",
"climate": "Warm & humid",
"code": 801513
},
{
"state": "Nagaland",
"district": "Dimapur",
"city": "Chumukedima",
"climate": "Warm & humid",
"code": 801458
},
{
"state": "Nagaland",
"district": "Dimapur",
"city": "Dimapur",
"climate": "Warm & humid",
"code": 801457
},
{
"state": "Nagaland",
"district": "Dimapur",
"city": "East Dimapur Town Council",
"climate": "Warm & humid",
"code": 900792
},
{
"state": "Nagaland",
"district": "Dimapur",
"city": "Medziphema",
"climate": "Warm & humid",
"code": 801459
},
{
"state": "Nagaland",
"district": "Dimapur",
"city": "Niuland Town Council",
"climate": "Warm & humid",
"code": 900793
},
{
"state": "Nagaland",
"district": "Kiphire",
"city": "Kiphire",
"climate": "Warm & humid",
"code": 801464
},
{
"state": "Nagaland",
"district": "Kiphire",
"city": "Pungro Town Council",
"climate": "Warm & humid",
"code": 900795
},
{
"state": "Nagaland",
"district": "Kiphire",
"city": "Seyochung Town Council",
"climate": "Warm & humid",
"code": 900794
},
{
"state": "Nagaland",
"district": "Kohima",
"city": "Chiephobozou Town Council",
"climate": "Warm & humid",
"code": 900799
},
{
"state": "Nagaland",
"district": "Kohima",
"city": "Kohima",
"climate": "Warm & humid",
"code": 801466
},
{
"state": "Nagaland",
"district": "Kohima",
"city": "Tseminyu",
"climate": "Warm & humid",
"code": 801465
},
{
"state": "Nagaland",
"district": "Longleng",
"city": "Longleng",
"climate": "Cold",
"code": 801463
},
{
"state": "Nagaland",
"district": "Longleng",
"city": "Tamlu Town Council",
"climate": "Cold",
"code": 900790
},
{
"state": "Nagaland",
"district": "Mokokchung",
"city": "Changtongya",
"climate": "Cold",
"code": 801453
},
{
"state": "Nagaland",
"district": "Mokokchung",
"city": "Mangkolemba Town Council",
"climate": "Cold",
"code": 900791
},
{
"state": "Nagaland",
"district": "Mokokchung",
"city": "Mokokchung",
"climate": "Cold",
"code": 801454
},
{
"state": "Nagaland",
"district": "Mokokchung",
"city": "Tuli",
"climate": "Cold",
"code": 801452
},
{
"state": "Nagaland",
"district": "Mon",
"city": "Aboi Town Council",
"climate": "Cold",
"code": 900229
},
{
"state": "Nagaland",
"district": "Mon",
"city": "Mon",
"climate": "Cold",
"code": 801451
},
{
"state": "Nagaland",
"district": "Mon",
"city": "Naginimora",
"climate": "Cold",
"code": 801450
},
{
"state": "Nagaland",
"district": "Mon",
"city": "Tizit Town Counicl",
"climate": "Cold",
"code": 900800
},
{
"state": "Nagaland",
"district": "Mon",
"city": "Tobu Town Council",
"climate": "Cold",
"code": 900801
},
{
"state": "Nagaland",
"district": "Peren",
"city": "Jalukie",
"climate": "Warm & humid",
"code": 801467
},
{
"state": "Nagaland",
"district": "Peren",
"city": "Peren",
"climate": "Warm & humid",
"code": 801468
},
{
"state": "Nagaland",
"district": "Peren",
"city": "Tening Town Council",
"climate": "Warm & humid",
"code": 900802
},
{
"state": "Nagaland",
"district": "Phek",
"city": "Chozuba Town Council",
"climate": "Warm & humid",
"code": 900789
},
{
"state": "Nagaland",
"district": "Phek",
"city": "Meluri Town Council",
"climate": "Warm & humid",
"code": 900230
},
{
"state": "Nagaland",
"district": "Phek",
"city": "Pfutsero",
"climate": "Warm & humid",
"code": 801461
},
{
"state": "Nagaland",
"district": "Phek",
"city": "Phek",
"climate": "Warm & humid",
"code": 801460
},
{
"state": "Nagaland",
"district": "Shamator",
"city": "Shamatore Town Council",
"climate": "Warm & humid",
"code": 900231
},
{
"state": "Nagaland",
"district": "Tuensang",
"city": "Longkhim Town Council",
"climate": "Warm & humid",
"code": 900804
},
{
"state": "Nagaland",
"district": "Tuensang",
"city": "Noklak Town Council",
"climate": "Warm & humid",
"code": 900232
},
{
"state": "Nagaland",
"district": "Tuensang",
"city": "Tuensang",
"climate": "Warm & humid",
"code": 801462
},
{
"state": "Nagaland",
"district": "Wokha",
"city": "Bhandari Town Council",
"climate": "Warm & humid",
"code": 900803
},
{
"state": "Nagaland",
"district": "Wokha",
"city": "Wokha",
"climate": "Warm & humid",
"code": 801456
},
{
"state": "Nagaland",
"district": "Zunheboto",
"city": "Aghunato Town Council",
"climate": "Warm & humid",
"code": 900797
},
{
"state": "Nagaland",
"district": "Zunheboto",
"city": "Atoizu Town Council",
"climate": "Warm & humid",
"code": 900796
},
{
"state": "Nagaland",
"district": "Zunheboto",
"city": "Satakha Town Council",
"climate": "Warm & humid",
"code": 900798
},
{
"state": "Nagaland",
"district": "Zunheboto",
"city": "Zunheboto",
"climate": "Warm & humid",
"code": 801455
},
{
"state": "Odisha",
"district": "Anugul",
"city": "Anugul",
"climate": "Warm & humid",
"code": 801851
},
{
"state": "Odisha",
"district": "Anugul",
"city": "Athmallik",
"climate": "Warm & humid",
"code": 801852
},
{
"state": "Odisha",
"district": "Anugul",
"city": "Talcher",
"climate": "Warm & humid",
"code": 801850
},
{
"state": "Odisha",
"district": "Balangir",
"city": "Balangir",
"climate": "Warm & humid",
"code": 801890
},
{
"state": "Odisha",
"district": "Balangir",
"city": "Kantabanji",
"climate": "Warm & humid",
"code": 801892
},
{
"state": "Odisha",
"district": "Balangir",
"city": "Patnagarh",
"climate": "Warm & humid",
"code": 801891
},
{
"state": "Odisha",
"district": "Balangir",
"city": "Titlagarh Town",
"climate": "Warm & humid",
"code": 801893
},
{
"state": "Odisha",
"district": "Balangir",
"city": "Tusura Nac",
"climate": "Warm & humid",
"code": 900180
},
{
"state": "Odisha",
"district": "Baleshwar",
"city": "Baleshwar Town",
"climate": "Warm & humid",
"code": 801833
},
{
"state": "Odisha",
"district": "Baleshwar",
"city": "Jaleshwar",
"climate": "Warm & humid",
"code": 801829
},
{
"state": "Odisha",
"district": "Baleshwar",
"city": "Nilagiri",
"climate": "Warm & humid",
"code": 801831
},
{
"state": "Odisha",
"district": "Baleshwar",
"city": "Soro",
"climate": "Warm & humid",
"code": 801832
},
{
"state": "Odisha",
"district": "Bargarh",
"city": "Attabira Nac",
"climate": "Composite",
"code": 900085
},
{
"state": "Odisha",
"district": "Bargarh",
"city": "Barapali",
"climate": "Composite",
"code": 801804
},
{
"state": "Odisha",
"district": "Bargarh",
"city": "Bargarh",
"climate": "Composite",
"code": 801805
},
{
"state": "Odisha",
"district": "Bargarh",
"city": "Bijepur",
"climate": "Composite",
"code": 900492
},
{
"state": "Odisha",
"district": "Bargarh",
"city": "Padmapur",
"climate": "Composite",
"code": 801803
},
{
"state": "Odisha",
"district": "Baudh",
"city": "Baudhgarh",
"climate": "Warm & humid",
"code": 801886
},
{
"state": "Odisha",
"district": "Bhadrak",
"city": "Basudebpur",
"climate": "Warm & humid",
"code": 801836
},
{
"state": "Odisha",
"district": "Bhadrak",
"city": "Bhadrak",
"climate": "Warm & humid",
"code": 801835
},
{
"state": "Odisha",
"district": "Bhadrak",
"city": "Chandbali",
"climate": "Warm & humid",
"code": 900493
},
{
"state": "Odisha",
"district": "Bhadrak",
"city": "Dhamanagar",
"climate": "Warm & humid",
"code": 801834
},
{
"state": "Odisha",
"district": "Cuttack",
"city": "Athagad",
"climate": "Warm & humid",
"code": 801842
},
{
"state": "Odisha",
"district": "Cuttack",
"city": "Banki",
"climate": "Warm & humid",
"code": 801841
},
{
"state": "Odisha",
"district": "Cuttack",
"city": "Choudwar",
"climate": "Warm & humid",
"code": 801843
},
{
"state": "Odisha",
"district": "Cuttack",
"city": "Cuttack",
"climate": "Warm & humid",
"code": 801844
},
{
"state": "Odisha",
"district": "Debagarh",
"city": "Debagarh",
"climate": "Warm & humid",
"code": 801814
},
{
"state": "Odisha",
"district": "Dhenkanal",
"city": "Bhuban",
"climate": "Warm & humid",
"code": 801848
},
{
"state": "Odisha",
"district": "Dhenkanal",
"city": "Dhenkanal",
"climate": "Warm & humid",
"code": 801849
},
{
"state": "Odisha",
"district": "Dhenkanal",
"city": "Hindol Nac",
"climate": "Warm & humid",
"code": 900083
},
{
"state": "Odisha",
"district": "Dhenkanal",
"city": "Kamakshyanagar",
"climate": "Warm & humid",
"code": 801847
},
{
"state": "Odisha",
"district": "Gajapati",
"city": "Kashinagar",
"climate": "Warm & humid",
"code": 801882
},
{
"state": "Odisha",
"district": "Gajapati",
"city": "Paralakhemundi",
"climate": "Warm & humid",
"code": 801883
},
{
"state": "Odisha",
"district": "Ganjam",
"city": "Asika",
"climate": "Warm & humid",
"code": 801868
},
{
"state": "Odisha",
"district": "Ganjam",
"city": "Bellaguntha",
"climate": "Warm & humid",
"code": 801866
},
{
"state": "Odisha",
"district": "Ganjam",
"city": "Bhanjanagar",
"climate": "Warm & humid",
"code": 801865
},
{
"state": "Odisha",
"district": "Ganjam",
"city": "Brahmapur",
"climate": "Warm & humid",
"code": 801881
},
{
"state": "Odisha",
"district": "Ganjam",
"city": "Buguda",
"climate": "Warm & humid",
"code": 801864
},
{
"state": "Odisha",
"district": "Ganjam",
"city": "Chhatrapur",
"climate": "Warm & humid",
"code": 801874
},
{
"state": "Odisha",
"district": "Ganjam",
"city": "Chikiti",
"climate": "Warm & humid",
"code": 801880
},
{
"state": "Odisha",
"district": "Ganjam",
"city": "Digapahandi",
"climate": "Warm & humid",
"code": 801879
},
{
"state": "Odisha",
"district": "Ganjam",
"city": "Ganjam",
"climate": "Warm & humid",
"code": 801875
},
{
"state": "Odisha",
"district": "Ganjam",
"city": "Gopalpur",
"climate": "Warm & humid",
"code": 801878
},
{
"state": "Odisha",
"district": "Ganjam",
"city": "Hinjilicut",
"climate": "Warm & humid",
"code": 801877
},
{
"state": "Odisha",
"district": "Ganjam",
"city": "Kabisurjyanagar",
"climate": "Warm & humid",
"code": 801869
},
{
"state": "Odisha",
"district": "Ganjam",
"city": "Khalikote",
"climate": "Warm & humid",
"code": 801872
},
{
"state": "Odisha",
"district": "Ganjam",
"city": "Kodala",
"climate": "Warm & humid",
"code": 801871
},
{
"state": "Odisha",
"district": "Ganjam",
"city": "Polasara",
"climate": "Warm & humid",
"code": 801870
},
{
"state": "Odisha",
"district": "Ganjam",
"city": "Purusottampur",
"climate": "Warm & humid",
"code": 801876
},
{
"state": "Odisha",
"district": "Ganjam",
"city": "Rambha",
"climate": "Warm & humid",
"code": 801873
},
{
"state": "Odisha",
"district": "Ganjam",
"city": "Surada",
"climate": "Warm & humid",
"code": 801867
},
{
"state": "Odisha",
"district": "Jagatsinghpur",
"city": "Jagatsinghapur",
"climate": "Warm & humid",
"code": 801840
},
{
"state": "Odisha",
"district": "Jagatsinghpur",
"city": "Paradip",
"climate": "Warm & humid",
"code": 801839
},
{
"state": "Odisha",
"district": "Jajapur",
"city": "Byasanagar Town",
"climate": "Warm & humid",
"code": 801845
},
{
"state": "Odisha",
"district": "Jajapur",
"city": "Jajapur",
"climate": "Warm & humid",
"code": 801846
},
{
"state": "Odisha",
"district": "Jharsuguda",
"city": "Belpahar",
"climate": "Composite",
"code": 801806
},
{
"state": "Odisha",
"district": "Jharsuguda",
"city": "Brajarajnagar",
"climate": "Composite",
"code": 801807
},
{
"state": "Odisha",
"district": "Jharsuguda",
"city": "Jharsuguda",
"climate": "Composite",
"code": 801808
},
{
"state": "Odisha",
"district": "Kalahandi",
"city": "Bhawanipatna",
"climate": "Warm & humid",
"code": 801897
},
{
"state": "Odisha",
"district": "Kalahandi",
"city": "Dharmagarh Nac",
"climate": "Warm & humid",
"code": 900191
},
{
"state": "Odisha",
"district": "Kalahandi",
"city": "Junagarh",
"climate": "Warm & humid",
"code": 801898
},
{
"state": "Odisha",
"district": "Kalahandi",
"city": "Kesinga",
"climate": "Warm & humid",
"code": 801896
},
{
"state": "Odisha",
"district": "Kandhamal",
"city": "Balliguda Nac",
"climate": "Warm & humid",
"code": 900187
},
{
"state": "Odisha",
"district": "Kandhamal",
"city": "G. Udayagiri",
"climate": "Warm & humid",
"code": 801885
},
{
"state": "Odisha",
"district": "Kandhamal",
"city": "Phulabani",
"climate": "Warm & humid",
"code": 801884
},
{
"state": "Odisha",
"district": "Kendrapara",
"city": "Kendrapara",
"climate": "Warm & humid",
"code": 801838
},
{
"state": "Odisha",
"district": "Kendrapara",
"city": "Pattamundai",
"climate": "Warm & humid",
"code": 801837
},
{
"state": "Odisha",
"district": "Keonjhar",
"city": "Anandpur",
"climate": "Warm & humid",
"code": 801824
},
{
"state": "Odisha",
"district": "Keonjhar",
"city": "Barbil",
"climate": "Warm & humid",
"code": 801821
},
{
"state": "Odisha",
"district": "Keonjhar",
"city": "Champua Nac",
"climate": "Warm & humid",
"code": 900190
},
{
"state": "Odisha",
"district": "Keonjhar",
"city": "Joda",
"climate": "Warm & humid",
"code": 801822
},
{
"state": "Odisha",
"district": "Keonjhar",
"city": "Kendujhar",
"climate": "Warm & humid",
"code": 801823
},
{
"state": "Odisha",
"district": "Khurda",
"city": "Balugaon",
"climate": "Warm & humid",
"code": 801857
},
{
"state": "Odisha",
"district": "Khurda",
"city": "Banapur",
"climate": "Warm & humid",
"code": 801858
},
{
"state": "Odisha",
"district": "Khurda",
"city": "Bhubaneswar",
"climate": "Warm & humid",
"code": 801859
},
{
"state": "Odisha",
"district": "Khurda",
"city": "Jatani Town",
"climate": "Warm & humid",
"code": 801856
},
{
"state": "Odisha",
"district": "Khurda",
"city": "Khordha",
"climate": "Warm & humid",
"code": 801855
},
{
"state": "Odisha",
"district": "Koraput",
"city": "Jeypur",
"climate": "Warm & humid",
"code": 801906
},
{
"state": "Odisha",
"district": "Koraput",
"city": "Koraput",
"climate": "Warm & humid",
"code": 801905
},
{
"state": "Odisha",
"district": "Koraput",
"city": "Kotpad",
"climate": "Warm & humid",
"code": 801904
},
{
"state": "Odisha",
"district": "Koraput",
"city": "Sunabeda",
"climate": "Warm & humid",
"code": 801907
},
{
"state": "Odisha",
"district": "Malkangiri",
"city": "Balimela",
"climate": "Warm & humid",
"code": 801909
},
{
"state": "Odisha",
"district": "Malkangiri",
"city": "Malkangiri",
"climate": "Warm & humid",
"code": 801908
},
{
"state": "Odisha",
"district": "Mayurbhanj",
"city": "Baripada Town",
"climate": "Warm & humid",
"code": 801828
},
{
"state": "Odisha",
"district": "Mayurbhanj",
"city": "Karanjia",
"climate": "Warm & humid",
"code": 801826
},
{
"state": "Odisha",
"district": "Mayurbhanj",
"city": "Rairangapur",
"climate": "Warm & humid",
"code": 801825
},
{
"state": "Odisha",
"district": "Mayurbhanj",
"city": "Udala",
"climate": "Warm & humid",
"code": 801827
},
{
"state": "Odisha",
"district": "Nabarangapur",
"city": "Nabarangapur",
"climate": "Warm & humid",
"code": 801903
},
{
"state": "Odisha",
"district": "Nabarangapur",
"city": "Umarkote",
"climate": "Warm & humid",
"code": 801902
},
{
"state": "Odisha",
"district": "Nayagarh",
"city": "Daspalla Nac",
"climate": "Warm & humid",
"code": 900179
},
{
"state": "Odisha",
"district": "Nayagarh",
"city": "Khandapada",
"climate": "Warm & humid",
"code": 801853
},
{
"state": "Odisha",
"district": "Nayagarh",
"city": "Nayagarh",
"climate": "Warm & humid",
"code": 801854
},
{
"state": "Odisha",
"district": "Nayagarh",
"city": "Odagaon",
"climate": "Warm & humid",
"code": 900495
},
{
"state": "Odisha",
"district": "Nayagarh",
"city": "Ranpur Nac",
"climate": "Warm & humid",
"code": 900186
},
{
"state": "Odisha",
"district": "Nuapada",
"city": "Khariar",
"climate": "Composite",
"code": 801895
},
{
"state": "Odisha",
"district": "Nuapada",
"city": "Khariar Road",
"climate": "Composite",
"code": 801894
},
{
"state": "Odisha",
"district": "Nuapada",
"city": "Nuapada Nac",
"climate": "Composite",
"code": 900079
},
{
"state": "Odisha",
"district": "Puri",
"city": "Konark",
"climate": "Warm & humid",
"code": 801862
},
{
"state": "Odisha",
"district": "Puri",
"city": "Nimapada",
"climate": "Warm & humid",
"code": 801861
},
{
"state": "Odisha",
"district": "Puri",
"city": "Pipili",
"climate": "Warm & humid",
"code": 801860
},
{
"state": "Odisha",
"district": "Puri",
"city": "Puri",
"climate": "Warm & humid",
"code": 801863
},
{
"state": "Odisha",
"district": "Rayagada",
"city": "Gudari",
"climate": "Warm & humid",
"code": 801901
},
{
"state": "Odisha",
"district": "Rayagada",
"city": "Gunupur Town",
"climate": "Warm & humid",
"code": 801900
},
{
"state": "Odisha",
"district": "Rayagada",
"city": "Rayagada",
"climate": "Warm & humid",
"code": 801899
},
{
"state": "Odisha",
"district": "Sambalpur",
"city": "Kochinda",
"climate": "Warm & humid",
"code": 801809
},
{
"state": "Odisha",
"district": "Sambalpur",
"city": "Redhakhol",
"climate": "Warm & humid",
"code": 801812
},
{
"state": "Odisha",
"district": "Sambalpur",
"city": "Sambalpur Town",
"climate": "Warm & humid",
"code": 801813
},
{
"state": "Odisha",
"district": "Sonepur",
"city": "Binika",
"climate": "Warm & humid",
"code": 801887
},
{
"state": "Odisha",
"district": "Sonepur",
"city": "Sonapur",
"climate": "Warm & humid",
"code": 801888
},
{
"state": "Odisha",
"district": "Sonepur",
"city": "Tarbha",
"climate": "Warm & humid",
"code": 801889
},
{
"state": "Odisha",
"district": "Sundergarh",
"city": "Biramitrapur",
"climate": "Warm & humid",
"code": 801818
},
{
"state": "Odisha",
"district": "Sundergarh",
"city": "Rajagangapur",
"climate": "Warm & humid",
"code": 801816
},
{
"state": "Odisha",
"district": "Sundergarh",
"city": "Raurkela Town",
"climate": "Warm & humid",
"code": 801819
},
{
"state": "Odisha",
"district": "Sundergarh",
"city": "Sundargarh",
"climate": "Warm & humid",
"code": 801815
},
{
"state": "Puducherry",
"district": "Karaikal",
"city": "Karaikal",
"climate": "Warm & humid",
"code": 804040
},
{
"state": "Puducherry",
"district": "Mahe",
"city": "Mahe",
"climate": "Warm & humid",
"code": 804039
},
{
"state": "Puducherry",
"district": "Puducherry",
"city": "Oulgaret -Ozhukarai",
"climate": "Warm & humid",
"code": 804037
},
{
"state": "Puducherry",
"district": "Puducherry",
"city": "Puducherry",
"climate": "Warm & humid",
"code": 804036
},
{
"state": "Puducherry",
"district": "Yanam",
"city": "Yanam",
"climate": "Warm & humid",
"code": 804035
},
{
"state": "Punjab",
"district": "Amritsar",
"city": "Ajnala",
"climate": "Composite",
"code": 800247
},
{
"state": "Punjab",
"district": "Amritsar",
"city": "Amritsar",
"climate": "Composite",
"code": 800252
},
{
"state": "Punjab",
"district": "Amritsar",
"city": "Amritsar Cantonment",
"climate": "Composite",
"code": 800250
},
{
"state": "Punjab",
"district": "Amritsar",
"city": "Baba Bakala",
"climate": "Composite",
"code": 900841
},
{
"state": "Punjab",
"district": "Amritsar",
"city": "Jandiala",
"climate": "Composite",
"code": 800251
},
{
"state": "Punjab",
"district": "Amritsar",
"city": "Majitha",
"climate": "Composite",
"code": 800249
},
{
"state": "Punjab",
"district": "Amritsar",
"city": "Raja Sansi",
"climate": "Composite",
"code": 800248
},
{
"state": "Punjab",
"district": "Amritsar",
"city": "Ramdas",
"climate": "Composite",
"code": 800246
},
{
"state": "Punjab",
"district": "Amritsar",
"city": "Rayya",
"climate": "Composite",
"code": 800253
},
{
"state": "Punjab",
"district": "Barnala",
"city": "Barnala",
"climate": "Composite",
"code": 800281
},
{
"state": "Punjab",
"district": "Barnala",
"city": "Bhadaur",
"climate": "Composite",
"code": 800285
},
{
"state": "Punjab",
"district": "Barnala",
"city": "Dhanaula",
"climate": "Composite",
"code": 800283
},
{
"state": "Punjab",
"district": "Barnala",
"city": "Handiaya",
"climate": "Composite",
"code": 800282
},
{
"state": "Punjab",
"district": "Barnala",
"city": "Tapa",
"climate": "Composite",
"code": 800284
},
{
"state": "Punjab",
"district": "Bathinda",
"city": "Bathinda",
"climate": "Composite",
"code": 800226
},
{
"state": "Punjab",
"district": "Bathinda",
"city": "Bhagta Bhai Ka",
"climate": "Composite",
"code": 800222
},
{
"state": "Punjab",
"district": "Bathinda",
"city": "Bhai Rupa",
"climate": "Composite",
"code": 900061
},
{
"state": "Punjab",
"district": "Bathinda",
"city": "Bhucho Mandi",
"climate": "Composite",
"code": 800224
},
{
"state": "Punjab",
"district": "Bathinda",
"city": "Goniana",
"climate": "Composite",
"code": 800225
},
{
"state": "Punjab",
"district": "Bathinda",
"city": "Kot Fatta",
"climate": "Composite",
"code": 800228
},
{
"state": "Punjab",
"district": "Bathinda",
"city": "Kot Shamir",
"climate": "Composite",
"code": 900047
},
{
"state": "Punjab",
"district": "Bathinda",
"city": "Kotha Guru",
"climate": "Composite",
"code": 900057
},
{
"state": "Punjab",
"district": "Bathinda",
"city": "Lehra Mohabbat",
"climate": "Composite",
"code": 900048
},
{
"state": "Punjab",
"district": "Bathinda",
"city": "Maluka",
"climate": "Composite",
"code": 900056
},
{
"state": "Punjab",
"district": "Bathinda",
"city": "Maur",
"climate": "Composite",
"code": 800231
},
{
"state": "Punjab",
"district": "Bathinda",
"city": "Mehraj",
"climate": "Composite",
"code": 900055
},
{
"state": "Punjab",
"district": "Bathinda",
"city": "Nathana",
"climate": "Composite",
"code": 900052
},
{
"state": "Punjab",
"district": "Bathinda",
"city": "Raman",
"climate": "Composite",
"code": 800229
},
{
"state": "Punjab",
"district": "Bathinda",
"city": "Rampura Phul",
"climate": "Composite",
"code": 800223
},
{
"state": "Punjab",
"district": "Bathinda",
"city": "Sangat",
"climate": "Composite",
"code": 800227
},
{
"state": "Punjab",
"district": "Bathinda",
"city": "Talwandi Sabo",
"climate": "Composite",
"code": 800230
},
{
"state": "Punjab",
"district": "Faridkot",
"city": "Faridkot",
"climate": "Composite",
"code": 800219
},
{
"state": "Punjab",
"district": "Faridkot",
"city": "Jaitu",
"climate": "Composite",
"code": 800221
},
{
"state": "Punjab",
"district": "Faridkot",
"city": "Kot Kapura",
"climate": "Composite",
"code": 800220
},
{
"state": "Punjab",
"district": "Fazilka",
"city": "Abohar",
"climate": "Composite",
"code": 800214
},
{
"state": "Punjab",
"district": "Fazilka",
"city": "Arniwala Sheikh Subhan",
"climate": "Composite",
"code": 900062
},
{
"state": "Punjab",
"district": "Fazilka",
"city": "Fazilka",
"climate": "Composite",
"code": 800213
},
{
"state": "Punjab",
"district": "Fazilka",
"city": "Jalalabad",
"climate": "Composite",
"code": 800212
},
{
"state": "Punjab",
"district": "Firozpur",
"city": "Ferozepur Cantonment",
"climate": "Composite",
"code": 800208
},
{
"state": "Punjab",
"district": "Firozpur",
"city": "Firozpur",
"climate": "Composite",
"code": 800207
},
{
"state": "Punjab",
"district": "Firozpur",
"city": "Guru Har Sahai",
"climate": "Composite",
"code": 800211
},
{
"state": "Punjab",
"district": "Firozpur",
"city": "Makhu",
"climate": "Composite",
"code": 800204
},
{
"state": "Punjab",
"district": "Firozpur",
"city": "Mallanwala Khass",
"climate": "Composite",
"code": 800206
},
{
"state": "Punjab",
"district": "Firozpur",
"city": "Mamdot",
"climate": "Composite",
"code": 900176
},
{
"state": "Punjab",
"district": "Firozpur",
"city": "Mudki",
"climate": "Composite",
"code": 800210
},
{
"state": "Punjab",
"district": "Firozpur",
"city": "Talwandi Bhai",
"climate": "Composite",
"code": 800209
},
{
"state": "Punjab",
"district": "Firozpur",
"city": "Zira",
"climate": "Composite",
"code": 800205
},
{
"state": "Punjab",
"district": "Gurdaspur",
"city": "Batala",
"climate": "Composite",
"code": 800149
},
{
"state": "Punjab",
"district": "Gurdaspur",
"city": "Dera Baba Nanak",
"climate": "Composite",
"code": 800152
},
{
"state": "Punjab",
"district": "Gurdaspur",
"city": "Dhariwal",
"climate": "Composite",
"code": 800147
},
{
"state": "Punjab",
"district": "Gurdaspur",
"city": "Dina Nagar",
"climate": "Composite",
"code": 800145
},
{
"state": "Punjab",
"district": "Gurdaspur",
"city": "Fatehgarh Churian",
"climate": "Composite",
"code": 800148
},
{
"state": "Punjab",
"district": "Gurdaspur",
"city": "Gurdaspur",
"climate": "Composite",
"code": 800146
},
{
"state": "Punjab",
"district": "Gurdaspur",
"city": "Qadian",
"climate": "Composite",
"code": 800150
},
{
"state": "Punjab",
"district": "Gurdaspur",
"city": "Sri Hargobindpur",
"climate": "Composite",
"code": 800151
},
{
"state": "Punjab",
"district": "Hoshiarpur",
"city": "Dasua",
"climate": "Composite",
"code": 800172
},
{
"state": "Punjab",
"district": "Hoshiarpur",
"city": "Gardhiwala",
"climate": "Composite",
"code": 800173
},
{
"state": "Punjab",
"district": "Hoshiarpur",
"city": "Garhshankar",
"climate": "Composite",
"code": 800179
},
{
"state": "Punjab",
"district": "Hoshiarpur",
"city": "Hariana",
"climate": "Composite",
"code": 800175
},
{
"state": "Punjab",
"district": "Hoshiarpur",
"city": "Hoshiarpur",
"climate": "Composite",
"code": 800176
},
{
"state": "Punjab",
"district": "Hoshiarpur",
"city": "Mahilpur",
"climate": "Composite",
"code": 800178
},
{
"state": "Punjab",
"district": "Hoshiarpur",
"city": "Mukerian",
"climate": "Composite",
"code": 800174
},
{
"state": "Punjab",
"district": "Hoshiarpur",
"city": "Sham Chaurasi",
"climate": "Composite",
"code": 800177
},
{
"state": "Punjab",
"district": "Hoshiarpur",
"city": "Talwara",
"climate": "Composite",
"code": 900024
},
{
"state": "Punjab",
"district": "Hoshiarpur",
"city": "Urmar Tanda",
"climate": "Composite",
"code": 800171
},
{
"state": "Punjab",
"district": "Jalandhar",
"city": "Adampur",
"climate": "Composite",
"code": 800168
},
{
"state": "Punjab",
"district": "Jalandhar",
"city": "Alawalpur",
"climate": "Composite",
"code": 800167
},
{
"state": "Punjab",
"district": "Jalandhar",
"city": "Bhogpur",
"climate": "Composite",
"code": 800170
},
{
"state": "Punjab",
"district": "Jalandhar",
"city": "Bilga",
"climate": "Composite",
"code": 900483
},
{
"state": "Punjab",
"district": "Jalandhar",
"city": "Goraya",
"climate": "Composite",
"code": 800162
},
{
"state": "Punjab",
"district": "Jalandhar",
"city": "Jalandhar",
"climate": "Composite",
"code": 800166
},
{
"state": "Punjab",
"district": "Jalandhar",
"city": "Jalandhar Cantonment",
"climate": "Composite",
"code": 800165
},
{
"state": "Punjab",
"district": "Jalandhar",
"city": "Kartarpur",
"climate": "Composite",
"code": 800169
},
{
"state": "Punjab",
"district": "Jalandhar",
"city": "Lohian Khass",
"climate": "Composite",
"code": 800159
},
{
"state": "Punjab",
"district": "Jalandhar",
"city": "Mehatpur",
"climate": "Composite",
"code": 900060
},
{
"state": "Punjab",
"district": "Jalandhar",
"city": "Nakodar",
"climate": "Composite",
"code": 800161
},
{
"state": "Punjab",
"district": "Jalandhar",
"city": "Nurmahal",
"climate": "Composite",
"code": 800164
},
{
"state": "Punjab",
"district": "Jalandhar",
"city": "Phillaur",
"climate": "Composite",
"code": 800163
},
{
"state": "Punjab",
"district": "Jalandhar",
"city": "Shahkot",
"climate": "Composite",
"code": 800160
},
{
"state": "Punjab",
"district": "Kapurthala",
"city": "Begowal",
"climate": "Composite",
"code": 800154
},
{
"state": "Punjab",
"district": "Kapurthala",
"city": "Bhulath",
"climate": "Composite",
"code": 800153
},
{
"state": "Punjab",
"district": "Kapurthala",
"city": "Dhilwan",
"climate": "Composite",
"code": 800156
},
{
"state": "Punjab",
"district": "Kapurthala",
"city": "Kapurthala",
"climate": "Composite",
"code": 800155
},
{
"state": "Punjab",
"district": "Kapurthala",
"city": "Nadala",
"climate": "Composite",
"code": 900054
},
{
"state": "Punjab",
"district": "Kapurthala",
"city": "Phagwara",
"climate": "Composite",
"code": 800158
},
{
"state": "Punjab",
"district": "Kapurthala",
"city": "Sultanpur",
"climate": "Composite",
"code": 800157
},
{
"state": "Punjab",
"district": "Ludhiana",
"city": "Doraha",
"climate": "Composite",
"code": 800194
},
{
"state": "Punjab",
"district": "Ludhiana",
"city": "Jagraon",
"climate": "Composite",
"code": 800199
},
{
"state": "Punjab",
"district": "Ludhiana",
"city": "Khanna",
"climate": "Composite",
"code": 800191
},
{
"state": "Punjab",
"district": "Ludhiana",
"city": "Ludhiana",
"climate": "Composite",
"code": 800196
},
{
"state": "Punjab",
"district": "Ludhiana",
"city": "Machhiwara",
"climate": "Composite",
"code": 800189
},
{
"state": "Punjab",
"district": "Ludhiana",
"city": "Maloud",
"climate": "Composite",
"code": 800193
},
{
"state": "Punjab",
"district": "Ludhiana",
"city": "Mullanpur Dakha",
"climate": "Composite",
"code": 800197
},
{
"state": "Punjab",
"district": "Ludhiana",
"city": "Payal",
"climate": "Composite",
"code": 800192
},
{
"state": "Punjab",
"district": "Ludhiana",
"city": "Raikot",
"climate": "Composite",
"code": 800198
},
{
"state": "Punjab",
"district": "Ludhiana",
"city": "Sahnewal",
"climate": "Composite",
"code": 800195
},
{
"state": "Punjab",
"district": "Ludhiana",
"city": "Samrala",
"climate": "Composite",
"code": 800190
},
{
"state": "Punjab",
"district": "Mansa",
"city": "Bareta",
"climate": "Composite",
"code": 800233
},
{
"state": "Punjab",
"district": "Mansa",
"city": "Bhikhi",
"climate": "Composite",
"code": 800235
},
{
"state": "Punjab",
"district": "Mansa",
"city": "Boha",
"climate": "Composite",
"code": 900053
},
{
"state": "Punjab",
"district": "Mansa",
"city": "Budhlada",
"climate": "Composite",
"code": 800234
},
{
"state": "Punjab",
"district": "Mansa",
"city": "Joga",
"climate": "Composite",
"code": 900058
},
{
"state": "Punjab",
"district": "Mansa",
"city": "Mansa",
"climate": "Composite",
"code": 800236
},
{
"state": "Punjab",
"district": "Mansa",
"city": "Sardulgarh",
"climate": "Composite",
"code": 800232
},
{
"state": "Punjab",
"district": "Moga",
"city": "Badhni Kalan",
"climate": "Composite",
"code": 800200
},
{
"state": "Punjab",
"district": "Moga",
"city": "Bagha Purana",
"climate": "Composite",
"code": 800201
},
{
"state": "Punjab",
"district": "Moga",
"city": "Dharamkot",
"climate": "Composite",
"code": 800203
},
{
"state": "Punjab",
"district": "Moga",
"city": "Fatehgarh Pajtur",
"climate": "Composite",
"code": 900482
},
{
"state": "Punjab",
"district": "Moga",
"city": "Kot Isse Khan",
"climate": "Composite",
"code": 900043
},
{
"state": "Punjab",
"district": "Moga",
"city": "Moga",
"climate": "Composite",
"code": 800202
},
{
"state": "Punjab",
"district": "Moga",
"city": "Nihal Singh Wala",
"climate": "Composite",
"code": 900044
},
{
"state": "Punjab",
"district": "Muktsar",
"city": "Bariwala",
"climate": "Composite",
"code": 800218
},
{
"state": "Punjab",
"district": "Muktsar",
"city": "Gidderbaha",
"climate": "Composite",
"code": 800216
},
{
"state": "Punjab",
"district": "Muktsar",
"city": "Malout",
"climate": "Composite",
"code": 800215
},
{
"state": "Punjab",
"district": "Muktsar",
"city": "Muktsar",
"climate": "Composite",
"code": 800217
},
{
"state": "Punjab",
"district": "Pathankot",
"city": "Narot Jaimal Singh",
"climate": "Composite",
"code": 900485
},
{
"state": "Punjab",
"district": "Pathankot",
"city": "Pathankot",
"climate": "Composite",
"code": 800144
},
{
"state": "Punjab",
"district": "Pathankot",
"city": "Sujanpur",
"climate": "Composite",
"code": 800143
},
{
"state": "Punjab",
"district": "Patiala",
"city": "Adda Devigarh",
"climate": "Composite",
"code": 900842
},
{
"state": "Punjab",
"district": "Patiala",
"city": "Bhadson",
"climate": "Composite",
"code": 800241
},
{
"state": "Punjab",
"district": "Patiala",
"city": "Ghagga",
"climate": "Composite",
"code": 800239
},
{
"state": "Punjab",
"district": "Patiala",
"city": "Ghanaur",
"climate": "Composite",
"code": 800244
},
{
"state": "Punjab",
"district": "Patiala",
"city": "Nabha",
"climate": "Composite",
"code": 800240
},
{
"state": "Punjab",
"district": "Patiala",
"city": "Patiala",
"climate": "Composite",
"code": 800242
},
{
"state": "Punjab",
"district": "Patiala",
"city": "Patran",
"climate": "Composite",
"code": 800238
},
{
"state": "Punjab",
"district": "Patiala",
"city": "Rajpura",
"climate": "Composite",
"code": 800245
},
{
"state": "Punjab",
"district": "Patiala",
"city": "Samana",
"climate": "Composite",
"code": 800237
},
{
"state": "Punjab",
"district": "Patiala",
"city": "Sanaur",
"climate": "Composite",
"code": 800243
},
{
"state": "Punjab",
"district": "Rupnagar",
"city": "Anandpur Sahib",
"climate": "Composite",
"code": 800257
},
{
"state": "Punjab",
"district": "Rupnagar",
"city": "Chamkaur Sahib",
"climate": "Composite",
"code": 800260
},
{
"state": "Punjab",
"district": "Rupnagar",
"city": "Kiratpur Sahib",
"climate": "Composite",
"code": 900107
},
{
"state": "Punjab",
"district": "Rupnagar",
"city": "Morinda",
"climate": "Composite",
"code": 800261
},
{
"state": "Punjab",
"district": "Rupnagar",
"city": "Nangal",
"climate": "Composite",
"code": 800258
},
{
"state": "Punjab",
"district": "Rupnagar",
"city": "Rupnagar",
"climate": "Composite",
"code": 800259
},
{
"state": "Punjab",
"district": "S.A.S. Nagar (Mohali)",
"city": "Banur",
"climate": "Composite",
"code": 800265
},
{
"state": "Punjab",
"district": "S.A.S. Nagar (Mohali)",
"city": "Dera Bassi",
"climate": "Composite",
"code": 800268
},
{
"state": "Punjab",
"district": "S.A.S. Nagar (Mohali)",
"city": "Ghaduan",
"climate": "Composite",
"code": 900843
},
{
"state": "Punjab",
"district": "S.A.S. Nagar (Mohali)",
"city": "Kharar",
"climate": "Composite",
"code": 800263
},
{
"state": "Punjab",
"district": "S.A.S. Nagar (Mohali)",
"city": "Kurali",
"climate": "Composite",
"code": 800262
},
{
"state": "Punjab",
"district": "S.A.S. Nagar (Mohali)",
"city": "Lalru",
"climate": "Composite",
"code": 900059
},
{
"state": "Punjab",
"district": "S.A.S. Nagar (Mohali)",
"city": "Mohali",
"climate": "Composite",
"code": 800266
},
{
"state": "Punjab",
"district": "S.A.S. Nagar (Mohali)",
"city": "Naya Gaon",
"climate": "Composite",
"code": 800264
},
{
"state": "Punjab",
"district": "S.A.S. Nagar (Mohali)",
"city": "Zirakpur",
"climate": "Composite",
"code": 800267
},
{
"state": "Punjab",
"district": "Sahid Bhgat Singh Nagar",
"city": "Balachaur",
"climate": "Composite",
"code": 800183
},
{
"state": "Punjab",
"district": "Sahid Bhgat Singh Nagar",
"city": "Banga",
"climate": "Composite",
"code": 800180
},
{
"state": "Punjab",
"district": "Sahid Bhgat Singh Nagar",
"city": "Nawanshahr",
"climate": "Composite",
"code": 800181
},
{
"state": "Punjab",
"district": "Sahid Bhgat Singh Nagar",
"city": "Rahon",
"climate": "Composite",
"code": 800182
},
{
"state": "Punjab",
"district": "Sangrur",
"city": "Ahmedgarh",
"climate": "Composite",
"code": 800269
},
{
"state": "Punjab",
"district": "Sangrur",
"city": "Amargarh",
"climate": "Composite",
"code": 900046
},
{
"state": "Punjab",
"district": "Sangrur",
"city": "Bhawanigarh",
"climate": "Composite",
"code": 800272
},
{
"state": "Punjab",
"district": "Sangrur",
"city": "Cheema",
"climate": "Composite",
"code": 800275
},
{
"state": "Punjab",
"district": "Sangrur",
"city": "Dhuri",
"climate": "Composite",
"code": 800271
},
{
"state": "Punjab",
"district": "Sangrur",
"city": "Dirba",
"climate": "Composite",
"code": 800277
},
{
"state": "Punjab",
"district": "Sangrur",
"city": "Khanauri",
"climate": "Composite",
"code": 800280
},
{
"state": "Punjab",
"district": "Sangrur",
"city": "Lehragaga",
"climate": "Composite",
"code": 800278
},
{
"state": "Punjab",
"district": "Sangrur",
"city": "Longowal",
"climate": "Composite",
"code": 800274
},
{
"state": "Punjab",
"district": "Sangrur",
"city": "Malerkotla",
"climate": "Composite",
"code": 800270
},
{
"state": "Punjab",
"district": "Sangrur",
"city": "Moonak",
"climate": "Composite",
"code": 800279
},
{
"state": "Punjab",
"district": "Sangrur",
"city": "Sangrur",
"climate": "Composite",
"code": 800273
},
{
"state": "Punjab",
"district": "Sangrur",
"city": "Sunam Udham Singh Wala",
"climate": "Composite",
"code": 800276
},
{
"state": "Punjab",
"district": "Sirhind Fatehgarh Sahib",
"city": "Amloh",
"climate": "Composite",
"code": 800186
},
{
"state": "Punjab",
"district": "Sirhind Fatehgarh Sahib",
"city": "Bassi Pathana",
"climate": "Composite",
"code": 800184
},
{
"state": "Punjab",
"district": "Sirhind Fatehgarh Sahib",
"city": "Gobindgarh",
"climate": "Composite",
"code": 800187
},
{
"state": "Punjab",
"district": "Sirhind Fatehgarh Sahib",
"city": "Khamanon",
"climate": "Composite",
"code": 800188
},
{
"state": "Punjab",
"district": "Sirhind Fatehgarh Sahib",
"city": "Sirhind Fatehgarh Sahib",
"climate": "Composite",
"code": 800185
},
{
"state": "Punjab",
"district": "Tarn Taran",
"city": "Bhikhiwind",
"climate": "Composite",
"code": 900045
},
{
"state": "Punjab",
"district": "Tarn Taran",
"city": "Khem Karan",
"climate": "Composite",
"code": 800256
},
{
"state": "Punjab",
"district": "Tarn Taran",
"city": "Patti",
"climate": "Composite",
"code": 800255
},
{
"state": "Punjab",
"district": "Tarn Taran",
"city": "Tarn Taran",
"climate": "Composite",
"code": 800254
},
{
"state": "Rajasthan",
"district": "Ajmer",
"city": "Ajmer",
"climate": "Composite",
"code": 800570
},
{
"state": "Rajasthan",
"district": "Ajmer",
"city": "Ajmer Cantonment",
"climate": "Composite",
"code": 900486
},
{
"state": "Rajasthan",
"district": "Ajmer",
"city": "Beawar",
"climate": "Composite",
"code": 800571
},
{
"state": "Rajasthan",
"district": "Ajmer",
"city": "Bijainagar",
"climate": "Composite",
"code": 800572
},
{
"state": "Rajasthan",
"district": "Ajmer",
"city": "Kekri",
"climate": "Composite",
"code": 800575
},
{
"state": "Rajasthan",
"district": "Ajmer",
"city": "Kishangarh",
"climate": "Composite",
"code": 800568
},
{
"state": "Rajasthan",
"district": "Ajmer",
"city": "Nasirabad",
"climate": "Composite",
"code": 800573
},
{
"state": "Rajasthan",
"district": "Ajmer",
"city": "Nasirabad Cantonment",
"climate": "Composite",
"code": 900496
},
{
"state": "Rajasthan",
"district": "Ajmer",
"city": "Pushkar",
"climate": "Composite",
"code": 800569
},
{
"state": "Rajasthan",
"district": "Ajmer",
"city": "Sarwar",
"climate": "Composite",
"code": 800574
},
{
"state": "Rajasthan",
"district": "Alwar",
"city": "Alwar",
"climate": "Composite",
"code": 800490
},
{
"state": "Rajasthan",
"district": "Alwar",
"city": "BAHADURPUR",
"climate": "Composite"
},
{
"state": "Rajasthan",
"district": "Alwar",
"city": "BARDOD",
"climate": "Composite"
},
{
"state": "Rajasthan",
"district": "Alwar",
"city": "Bansur",
"climate": "Composite",
"code": 900709
},
{
"state": "Rajasthan",
"district": "Alwar",
"city": "Behror",
"climate": "Composite",
"code": 800486
},
{
"state": "Rajasthan",
"district": "Alwar",
"city": "Bhiwadi",
"climate": "Composite",
"code": 800487
},
{
"state": "Rajasthan",
"district": "Alwar",
"city": "GOVINDGARH",
"climate": "Composite"
},
{
"state": "Rajasthan",
"district": "Alwar",
"city": "KOTKASIM",
"climate": "Composite"
},
{
"state": "Rajasthan",
"district": "Alwar",
"city": "Khairthal",
"climate": "Composite",
"code": 800489
},
{
"state": "Rajasthan",
"district": "Alwar",
"city": "Kherli",
"climate": "Composite",
"code": 800492
},
{
"state": "Rajasthan",
"district": "Alwar",
"city": "Kishangarhbas Mb",
"climate": "Composite",
"code": 900192
},
{
"state": "Rajasthan",
"district": "Alwar",
"city": "Laxmangarh",
"climate": "Composite",
"code": 900706
},
{
"state": "Rajasthan",
"district": "Alwar",
"city": "NEEMRANA",
"climate": "Composite"
},
{
"state": "Rajasthan",
"district": "Alwar",
"city": "Rajgarh_Al",
"climate": "Composite",
"code": 800491
},
{
"state": "Rajasthan",
"district": "Alwar",
"city": "Ramgarh",
"climate": "Composite",
"code": 800524
},
{
"state": "Rajasthan",
"district": "Alwar",
"city": "Ramgrah",
"climate": "Composite",
"code": 900707
},
{
"state": "Rajasthan",
"district": "Alwar",
"city": "TAPOOKRA",
"climate": "Composite"
},
{
"state": "Rajasthan",
"district": "Alwar",
"city": "Thanagazi",
"climate": "Composite",
"code": 900597
},
{
"state": "Rajasthan",
"district": "Alwar",
"city": "Tijara",
"climate": "Composite",
"code": 800488
},
{
"state": "Rajasthan",
"district": "Banswara",
"city": "Banswara",
"climate": "Hot and Dry",
"code": 800601
},
{
"state": "Rajasthan",
"district": "Banswara",
"city": "Kushalgarh",
"climate": "Hot and Dry",
"code": 800602
},
{
"state": "Rajasthan",
"district": "Banswara",
"city": "Partapur Garhi",
"climate": "Hot and Dry",
"code": 900599
},
{
"state": "Rajasthan",
"district": "Baran",
"city": "Antah",
"climate": "Hot and Dry",
"code": 800614
},
{
"state": "Rajasthan",
"district": "Baran",
"city": "Atru",
"climate": "Hot and Dry",
"code": 900717
},
{
"state": "Rajasthan",
"district": "Baran",
"city": "Baran",
"climate": "Hot and Dry",
"code": 800615
},
{
"state": "Rajasthan",
"district": "Baran",
"city": "Chhabra",
"climate": "Hot and Dry",
"code": 800616
},
{
"state": "Rajasthan",
"district": "Baran",
"city": "Mangrol",
"climate": "Hot and Dry",
"code": 800613
},
{
"state": "Rajasthan",
"district": "Barmer",
"city": "Balotra",
"climate": "Hot and Dry",
"code": 800549
},
{
"state": "Rajasthan",
"district": "Barmer",
"city": "Barmer",
"climate": "Hot and Dry",
"code": 800550
},
{
"state": "Rajasthan",
"district": "Barmer",
"city": "SIWANA",
"climate": "Hot and Dry"
},
{
"state": "Rajasthan",
"district": "Bharatpur",
"city": "Bayana",
"climate": "Composite",
"code": 800501
},
{
"state": "Rajasthan",
"district": "Bharatpur",
"city": "Bharatpur",
"climate": "Composite",
"code": 800498
},
{
"state": "Rajasthan",
"district": "Bharatpur",
"city": "Bhusawar",
"climate": "Composite",
"code": 800499
},
{
"state": "Rajasthan",
"district": "Bharatpur",
"city": "Deeg",
"climate": "Composite",
"code": 800495
},
{
"state": "Rajasthan",
"district": "Bharatpur",
"city": "Kaman",
"climate": "Composite",
"code": 800493
},
{
"state": "Rajasthan",
"district": "Bharatpur",
"city": "Kumher",
"climate": "Composite",
"code": 800497
},
{
"state": "Rajasthan",
"district": "Bharatpur",
"city": "Nadbai",
"climate": "Composite",
"code": 800496
},
{
"state": "Rajasthan",
"district": "Bharatpur",
"city": "Nagar",
"climate": "Composite",
"code": 800494
},
{
"state": "Rajasthan",
"district": "Bharatpur",
"city": "Rupbas",
"climate": "Composite",
"code": 900380
},
{
"state": "Rajasthan",
"district": "Bharatpur",
"city": "SIKARI",
"climate": "Composite"
},
{
"state": "Rajasthan",
"district": "Bharatpur",
"city": "Sikri",
"climate": "Composite",
"code": 900721
},
{
"state": "Rajasthan",
"district": "Bharatpur",
"city": "Ucchain",
"climate": "Composite",
"code": 900720
},
{
"state": "Rajasthan",
"district": "Bharatpur",
"city": "Weir",
"climate": "Composite",
"code": 800500
},
{
"state": "Rajasthan",
"district": "Bhilwara",
"city": "Asind",
"climate": "Hot and Dry",
"code": 800588
},
{
"state": "Rajasthan",
"district": "Bhilwara",
"city": "Bhilwara",
"climate": "Hot and Dry",
"code": 800592
},
{
"state": "Rajasthan",
"district": "Bhilwara",
"city": "Gangapur",
"climate": "Hot and Dry",
"code": 800591
},
{
"state": "Rajasthan",
"district": "Bhilwara",
"city": "Gulabpura",
"climate": "Hot and Dry",
"code": 800589
},
{
"state": "Rajasthan",
"district": "Bhilwara",
"city": "HAMEERGARH",
"climate": "Hot and Dry"
},
{
"state": "Rajasthan",
"district": "Bhilwara",
"city": "Jahazpur",
"climate": "Hot and Dry",
"code": 800593
},
{
"state": "Rajasthan",
"district": "Bhilwara",
"city": "Mandalgarh",
"climate": "Hot and Dry",
"code": 800594
},
{
"state": "Rajasthan",
"district": "Bhilwara",
"city": "Shahpura_Bh",
"climate": "Hot and Dry",
"code": 800590
},
{
"state": "Rajasthan",
"district": "Bikaner",
"city": "Bikaner",
"climate": "Hot and Dry",
"code": 800460
},
{
"state": "Rajasthan",
"district": "Bikaner",
"city": "Deshnoke",
"climate": "Hot and Dry",
"code": 800461
},
{
"state": "Rajasthan",
"district": "Bikaner",
"city": "Dungargarh",
"climate": "Hot and Dry",
"code": 800463
},
{
"state": "Rajasthan",
"district": "Bikaner",
"city": "KHAJUWALA",
"climate": "Hot and Dry"
},
{
"state": "Rajasthan",
"district": "Bikaner",
"city": "Nokha",
"climate": "Hot and Dry",
"code": 800462
},
{
"state": "Rajasthan",
"district": "Bundi",
"city": "Bundi",
"climate": "Hot and Dry",
"code": 800587
},
{
"state": "Rajasthan",
"district": "Bundi",
"city": "Indragarh",
"climate": "Hot and Dry",
"code": 800583
},
{
"state": "Rajasthan",
"district": "Bundi",
"city": "Kaprain",
"climate": "Hot and Dry",
"code": 800586
},
{
"state": "Rajasthan",
"district": "Bundi",
"city": "Keshoraipatan",
"climate": "Hot and Dry",
"code": 800585
},
{
"state": "Rajasthan",
"district": "Bundi",
"city": "Lakheri",
"climate": "Hot and Dry",
"code": 800584
},
{
"state": "Rajasthan",
"district": "Bundi",
"city": "Nainwa",
"climate": "Hot and Dry",
"code": 800582
},
{
"state": "Rajasthan",
"district": "Chittaurgarh",
"city": "Bari Sadri",
"climate": "Hot and Dry",
"code": 800608
},
{
"state": "Rajasthan",
"district": "Chittaurgarh",
"city": "Begun",
"climate": "Hot and Dry",
"code": 800603
},
{
"state": "Rajasthan",
"district": "Chittaurgarh",
"city": "Chittaurgarh",
"climate": "Hot and Dry",
"code": 800605
},
{
"state": "Rajasthan",
"district": "Chittaurgarh",
"city": "Kapasan",
"climate": "Hot and Dry",
"code": 800606
},
{
"state": "Rajasthan",
"district": "Chittaurgarh",
"city": "Nimbahera",
"climate": "Hot and Dry",
"code": 800607
},
{
"state": "Rajasthan",
"district": "Chittaurgarh",
"city": "Rawatbhata",
"climate": "Hot and Dry",
"code": 800604
},
{
"state": "Rajasthan",
"district": "Churu",
"city": "Bidasar",
"climate": "Composite",
"code": 800471
},
{
"state": "Rajasthan",
"district": "Churu",
"city": "Chhapar",
"climate": "Composite",
"code": 800472
},
{
"state": "Rajasthan",
"district": "Churu",
"city": "Churu",
"climate": "Composite",
"code": 800468
},
{
"state": "Rajasthan",
"district": "Churu",
"city": "Rajaldesar",
"climate": "Composite",
"code": 800470
},
{
"state": "Rajasthan",
"district": "Churu",
"city": "Rajgarh_Ch",
"climate": "Composite",
"code": 800465
},
{
"state": "Rajasthan",
"district": "Churu",
"city": "Ratangarh",
"climate": "Composite",
"code": 800469
},
{
"state": "Rajasthan",
"district": "Churu",
"city": "Ratannagar",
"climate": "Composite",
"code": 800467
},
{
"state": "Rajasthan",
"district": "Churu",
"city": "Sardarshahar",
"climate": "Composite",
"code": 800466
},
{
"state": "Rajasthan",
"district": "Churu",
"city": "Sujangarh",
"climate": "Composite",
"code": 800473
},
{
"state": "Rajasthan",
"district": "Churu",
"city": "Taranagar",
"climate": "Composite",
"code": 800464
},
{
"state": "Rajasthan",
"district": "Dausa",
"city": "Bandikui",
"climate": "Composite",
"code": 800510
},
{
"state": "Rajasthan",
"district": "Dausa",
"city": "Dausa",
"climate": "Composite",
"code": 800511
},
{
"state": "Rajasthan",
"district": "Dausa",
"city": "Lalsot",
"climate": "Composite",
"code": 800512
},
{
"state": "Rajasthan",
"district": "Dausa",
"city": "MANDAWAR",
"climate": "Composite"
},
{
"state": "Rajasthan",
"district": "Dausa",
"city": "Mahwa",
"climate": "Composite",
"code": 900382
},
{
"state": "Rajasthan",
"district": "Dausa",
"city": "Mandawari",
"climate": "Composite",
"code": 900712
},
{
"state": "Rajasthan",
"district": "Dhaulpur",
"city": "Bari",
"climate": "Composite",
"code": 800502
},
{
"state": "Rajasthan",
"district": "Dhaulpur",
"city": "Baseri",
"climate": "Composite",
"code": 900715
},
{
"state": "Rajasthan",
"district": "Dhaulpur",
"city": "Dhaulpur",
"climate": "Composite",
"code": 800503
},
{
"state": "Rajasthan",
"district": "Dhaulpur",
"city": "Rajakhera",
"climate": "Composite",
"code": 800504
},
{
"state": "Rajasthan",
"district": "Dhaulpur",
"city": "SARMATHURA",
"climate": "Composite"
},
{
"state": "Rajasthan",
"district": "Dhaulpur",
"city": "Sarmathpura",
"climate": "Composite",
"code": 900714
},
{
"state": "Rajasthan",
"district": "Dungarpur",
"city": "Dungarpur",
"climate": "Hot and Dry",
"code": 800599
},
{
"state": "Rajasthan",
"district": "Dungarpur",
"city": "Sagwara",
"climate": "Hot and Dry",
"code": 800600
},
{
"state": "Rajasthan",
"district": "Ganganagar",
"city": "Anupgarh",
"climate": "Composite",
"code": 800451
},
{
"state": "Rajasthan",
"district": "Ganganagar",
"city": "Gajsinghpur",
"climate": "Composite",
"code": 800448
},
{
"state": "Rajasthan",
"district": "Ganganagar",
"city": "Ganganagar",
"climate": "Composite",
"code": 800446
},
{
"state": "Rajasthan",
"district": "Ganganagar",
"city": "Karanpur",
"climate": "Composite",
"code": 800445
},
{
"state": "Rajasthan",
"district": "Ganganagar",
"city": "Kesrisinghpur",
"climate": "Composite",
"code": 800444
},
{
"state": "Rajasthan",
"district": "Ganganagar",
"city": "Lalgarh Jattan",
"climate": "Composite",
"code": 900718
},
{
"state": "Rajasthan",
"district": "Ganganagar",
"city": "Padampur",
"climate": "Composite",
"code": 800449
},
{
"state": "Rajasthan",
"district": "Ganganagar",
"city": "Raisinghnagar",
"climate": "Composite",
"code": 800450
},
{
"state": "Rajasthan",
"district": "Ganganagar",
"city": "Sadulshahar",
"climate": "Composite",
"code": 800447
},
{
"state": "Rajasthan",
"district": "Ganganagar",
"city": "Suratgarh",
"climate": "Composite",
"code": 800453
},
{
"state": "Rajasthan",
"district": "Ganganagar",
"city": "Vijainagar",
"climate": "Composite",
"code": 800452
},
{
"state": "Rajasthan",
"district": "Hanumangarh",
"city": "Bhadra",
"climate": "Composite",
"code": 800459
},
{
"state": "Rajasthan",
"district": "Hanumangarh",
"city": "Hanumangarh",
"climate": "Composite",
"code": 800455
},
{
"state": "Rajasthan",
"district": "Hanumangarh",
"city": "Nohar",
"climate": "Composite",
"code": 800458
},
{
"state": "Rajasthan",
"district": "Hanumangarh",
"city": "Pilibanga",
"climate": "Composite",
"code": 800456
},
{
"state": "Rajasthan",
"district": "Hanumangarh",
"city": "Rawatsar",
"climate": "Composite",
"code": 800457
},
{
"state": "Rajasthan",
"district": "Hanumangarh",
"city": "Sangaria",
"climate": "Composite",
"code": 800454
},
{
"state": "Rajasthan",
"district": "Hanumangarh",
"city": "TIBBI",
"climate": "Composite"
},
{
"state": "Rajasthan",
"district": "Jaipur",
"city": "Bagru",
"climate": "Composite",
"code": 800521
},
{
"state": "Rajasthan",
"district": "Jaipur",
"city": "Bassi",
"climate": "Composite",
"code": 900711
},
{
"state": "Rajasthan",
"district": "Jaipur",
"city": "Chaksu",
"climate": "Composite",
"code": 800523
},
{
"state": "Rajasthan",
"district": "Jaipur",
"city": "Chomu",
"climate": "Composite",
"code": 800516
},
{
"state": "Rajasthan",
"district": "Jaipur",
"city": "Jaipur Greater",
"climate": "Composite",
"code": 900600
},
{
"state": "Rajasthan",
"district": "Jaipur",
"city": "Jaipur Heritage",
"climate": "Composite",
"code": 800522
},
{
"state": "Rajasthan",
"district": "Jaipur",
"city": "Jobner",
"climate": "Composite",
"code": 800520
},
{
"state": "Rajasthan",
"district": "Jaipur",
"city": "KISHANGARHBAS",
"climate": "Composite"
},
{
"state": "Rajasthan",
"district": "Jaipur",
"city": "Khatushyamji",
"climate": "Composite",
"code": 900598
},
{
"state": "Rajasthan",
"district": "Jaipur",
"city": "Kishangarh Renwal",
"climate": "Composite",
"code": 800517
},
{
"state": "Rajasthan",
"district": "Jaipur",
"city": "Kotputli",
"climate": "Composite",
"code": 800513
},
{
"state": "Rajasthan",
"district": "Jaipur",
"city": "MANOHARPUR",
"climate": "Composite"
},
{
"state": "Rajasthan",
"district": "Jaipur",
"city": "NARAYANA",
"climate": "Composite"
},
{
"state": "Rajasthan",
"district": "Jaipur",
"city": "Pavata Pragpura",
"climate": "Composite",
"code": 900708
},
{
"state": "Rajasthan",
"district": "Jaipur",
"city": "Phulera",
"climate": "Composite",
"code": 800519
},
{
"state": "Rajasthan",
"district": "Jaipur",
"city": "Sambhar",
"climate": "Composite",
"code": 800518
},
{
"state": "Rajasthan",
"district": "Jaipur",
"city": "Shahpura_J",
"climate": "Composite",
"code": 800515
},
{
"state": "Rajasthan",
"district": "Jaipur",
"city": "Viratnagar",
"climate": "Composite",
"code": 800514
},
{
"state": "Rajasthan",
"district": "Jaisalmer",
"city": "Jaisalmer",
"climate": "Hot and Dry",
"code": 800547
},
{
"state": "Rajasthan",
"district": "Jaisalmer",
"city": "Pokaran",
"climate": "Hot and Dry",
"code": 800548
},
{
"state": "Rajasthan",
"district": "Jalor",
"city": "Bhinmal",
"climate": "Hot and Dry",
"code": 800552
},
{
"state": "Rajasthan",
"district": "Jalor",
"city": "Jalor",
"climate": "Hot and Dry",
"code": 800551
},
{
"state": "Rajasthan",
"district": "Jalor",
"city": "RANIWADA",
"climate": "Hot and Dry"
},
{
"state": "Rajasthan",
"district": "Jalor",
"city": "Raniwara",
"climate": "Hot and Dry"
},
{
"state": "Rajasthan",
"district": "Jalor",
"city": "Sanchore",
"climate": "Hot and Dry",
"code": 800553
},
{
"state": "Rajasthan",
"district": "Jhalawar",
"city": "Aklera",
"climate": "Hot and Dry",
"code": 800619
},
{
"state": "Rajasthan",
"district": "Jhalawar",
"city": "BARODAMEV",
"climate": "Hot and Dry"
},
{
"state": "Rajasthan",
"district": "Jhalawar",
"city": "Bhawani Mandi",
"climate": "Hot and Dry",
"code": 800620
},
{
"state": "Rajasthan",
"district": "Jhalawar",
"city": "Jhalawar",
"climate": "Hot and Dry",
"code": 800617
},
{
"state": "Rajasthan",
"district": "Jhalawar",
"city": "Jhalrapatan",
"climate": "Hot and Dry",
"code": 800618
},
{
"state": "Rajasthan",
"district": "Jhalawar",
"city": "Pirawa",
"climate": "Hot and Dry",
"code": 800621
},
{
"state": "Rajasthan",
"district": "Jhunjhunun",
"city": "Baggar",
"climate": "Composite",
"code": 800477
},
{
"state": "Rajasthan",
"district": "Jhunjhunun",
"city": "Bissau",
"climate": "Composite",
"code": 800474
},
{
"state": "Rajasthan",
"district": "Jhunjhunun",
"city": "Chirawa",
"climate": "Composite",
"code": 800481
},
{
"state": "Rajasthan",
"district": "Jhunjhunun",
"city": "GUDHAGORJI",
"climate": "Composite"
},
{
"state": "Rajasthan",
"district": "Jhunjhunun",
"city": "Jhunjhunun",
"climate": "Composite",
"code": 800476
},
{
"state": "Rajasthan",
"district": "Jhunjhunun",
"city": "Khetri",
"climate": "Composite",
"code": 800482
},
{
"state": "Rajasthan",
"district": "Jhunjhunun",
"city": "Mandawa",
"climate": "Composite",
"code": 800475
},
{
"state": "Rajasthan",
"district": "Jhunjhunun",
"city": "Mukandgarh",
"climate": "Composite",
"code": 800483
},
{
"state": "Rajasthan",
"district": "Jhunjhunun",
"city": "Nawalgarh",
"climate": "Composite",
"code": 800484
},
{
"state": "Rajasthan",
"district": "Jhunjhunun",
"city": "Pilani",
"climate": "Composite",
"code": 800478
},
{
"state": "Rajasthan",
"district": "Jhunjhunun",
"city": "Surajgarh",
"climate": "Composite",
"code": 800480
},
{
"state": "Rajasthan",
"district": "Jhunjhunun",
"city": "Udaipurwati",
"climate": "Composite",
"code": 800485
},
{
"state": "Rajasthan",
"district": "Jhunjhunun",
"city": "Vidyavihar",
"climate": "Composite",
"code": 800479
},
{
"state": "Rajasthan",
"district": "Jodhpur",
"city": "BALESAR SATTA",
"climate": "Hot and Dry"
},
{
"state": "Rajasthan",
"district": "Jodhpur",
"city": "Bhopalgarh",
"climate": "Hot and Dry",
"code": 900710
},
{
"state": "Rajasthan",
"district": "Jodhpur",
"city": "Bilara",
"climate": "Hot and Dry",
"code": 800546
},
{
"state": "Rajasthan",
"district": "Jodhpur",
"city": "Jodhpur North",
"climate": "Hot and Dry",
"code": 900595
},
{
"state": "Rajasthan",
"district": "Jodhpur",
"city": "Jodhpur South",
"climate": "Hot and Dry",
"code": 800544
},
{
"state": "Rajasthan",
"district": "Jodhpur",
"city": "Phalodi",
"climate": "Hot and Dry",
"code": 800543
},
{
"state": "Rajasthan",
"district": "Jodhpur",
"city": "Pipar City",
"climate": "Hot and Dry",
"code": 800545
},
{
"state": "Rajasthan",
"district": "Karauli",
"city": "Hindaun",
"climate": "Composite",
"code": 800506
},
{
"state": "Rajasthan",
"district": "Karauli",
"city": "Karauli",
"climate": "Composite",
"code": 800507
},
{
"state": "Rajasthan",
"district": "Karauli",
"city": "Sapotra",
"climate": "Composite",
"code": 900705
},
{
"state": "Rajasthan",
"district": "Karauli",
"city": "Todabhim",
"climate": "Composite",
"code": 800505
},
{
"state": "Rajasthan",
"district": "Kota",
"city": "Itawa",
"climate": "Hot and Dry",
"code": 900137
},
{
"state": "Rajasthan",
"district": "Kota",
"city": "Kaithoon",
"climate": "Hot and Dry",
"code": 800610
},
{
"state": "Rajasthan",
"district": "Kota",
"city": "Kota North",
"climate": "Hot and Dry",
"code": 900596
},
{
"state": "Rajasthan",
"district": "Kota",
"city": "Kota South",
"climate": "Hot and Dry",
"code": 800609
},
{
"state": "Rajasthan",
"district": "Kota",
"city": "Ramganj Mandi",
"climate": "Hot and Dry",
"code": 800611
},
{
"state": "Rajasthan",
"district": "Kota",
"city": "Sangod",
"climate": "Hot and Dry",
"code": 800612
},
{
"state": "Rajasthan",
"district": "Kota",
"city": "Sultanpur",
"climate": "Hot and Dry",
"code": 900716
},
{
"state": "Rajasthan",
"district": "Nagaur",
"city": "BASNI",
"climate": "Hot and Dry"
},
{
"state": "Rajasthan",
"district": "Nagaur",
"city": "BORAWAR",
"climate": "Hot and Dry"
},
{
"state": "Rajasthan",
"district": "Nagaur",
"city": "Degana",
"climate": "Hot and Dry",
"code": 900189
},
{
"state": "Rajasthan",
"district": "Nagaur",
"city": "Didwana",
"climate": "Hot and Dry",
"code": 800534
},
{
"state": "Rajasthan",
"district": "Nagaur",
"city": "JAYAL",
"climate": "Hot and Dry"
},
{
"state": "Rajasthan",
"district": "Nagaur",
"city": "Kuchaman City",
"climate": "Hot and Dry",
"code": 800541
},
{
"state": "Rajasthan",
"district": "Nagaur",
"city": "Kuchera",
"climate": "Hot and Dry",
"code": 800537
},
{
"state": "Rajasthan",
"district": "Nagaur",
"city": "Ladnu",
"climate": "Hot and Dry",
"code": 800533
},
{
"state": "Rajasthan",
"district": "Nagaur",
"city": "Makrana",
"climate": "Hot and Dry",
"code": 800540
},
{
"state": "Rajasthan",
"district": "Nagaur",
"city": "Merta City",
"climate": "Hot and Dry",
"code": 800538
},
{
"state": "Rajasthan",
"district": "Nagaur",
"city": "Mundwa",
"climate": "Hot and Dry",
"code": 800536
},
{
"state": "Rajasthan",
"district": "Nagaur",
"city": "Nagaur",
"climate": "Hot and Dry",
"code": 800535
},
{
"state": "Rajasthan",
"district": "Nagaur",
"city": "Nawa",
"climate": "Hot and Dry",
"code": 800542
},
{
"state": "Rajasthan",
"district": "Nagaur",
"city": "Parbatsar",
"climate": "Hot and Dry",
"code": 800539
},
{
"state": "Rajasthan",
"district": "Pali",
"city": "Bali",
"climate": "Hot and Dry",
"code": 800567
},
{
"state": "Rajasthan",
"district": "Pali",
"city": "Falna",
"climate": "Hot and Dry",
"code": 800566
},
{
"state": "Rajasthan",
"district": "Pali",
"city": "Jaitaran",
"climate": "Hot and Dry",
"code": 800559
},
{
"state": "Rajasthan",
"district": "Pali",
"city": "MARWARJUNCTION",
"climate": "Hot and Dry"
},
{
"state": "Rajasthan",
"district": "Pali",
"city": "Pali",
"climate": "Hot and Dry",
"code": 800561
},
{
"state": "Rajasthan",
"district": "Pali",
"city": "Rani",
"climate": "Hot and Dry",
"code": 800562
},
{
"state": "Rajasthan",
"district": "Pali",
"city": "Sadri",
"climate": "Hot and Dry",
"code": 800563
},
{
"state": "Rajasthan",
"district": "Pali",
"city": "Sojat",
"climate": "Hot and Dry",
"code": 800560
},
{
"state": "Rajasthan",
"district": "Pali",
"city": "Sumerpur",
"climate": "Hot and Dry",
"code": 800565
},
{
"state": "Rajasthan",
"district": "Pali",
"city": "Takhatgarh",
"climate": "Hot and Dry",
"code": 800564
},
{
"state": "Rajasthan",
"district": "Pratapgarh",
"city": "Chhoti Sadri",
"climate": "Hot and Dry",
"code": 800627
},
{
"state": "Rajasthan",
"district": "Pratapgarh",
"city": "DHARIAWAD",
"climate": "Hot and Dry"
},
{
"state": "Rajasthan",
"district": "Pratapgarh",
"city": "Pratapgarh",
"climate": "Hot and Dry",
"code": 800628
},
{
"state": "Rajasthan",
"district": "Rajsamand",
"city": "Amet",
"climate": "Hot and Dry",
"code": 800596
},
{
"state": "Rajasthan",
"district": "Rajsamand",
"city": "Deogarh",
"climate": "Hot and Dry",
"code": 800595
},
{
"state": "Rajasthan",
"district": "Rajsamand",
"city": "Nathdwara",
"climate": "Hot and Dry",
"code": 800598
},
{
"state": "Rajasthan",
"district": "Rajsamand",
"city": "Rajsamand",
"climate": "Hot and Dry",
"code": 800597
},
{
"state": "Rajasthan",
"district": "Sawai Madhopur",
"city": "BONLI",
"climate": "Composite"
},
{
"state": "Rajasthan",
"district": "Sawai Madhopur",
"city": "Bamanwas",
"climate": "Composite",
"code": 900719
},
{
"state": "Rajasthan",
"district": "Sawai Madhopur",
"city": "Gangapur City",
"climate": "Composite",
"code": 800508
},
{
"state": "Rajasthan",
"district": "Sawai Madhopur",
"city": "Sawai Madhopur",
"climate": "Composite",
"code": 800509
},
{
"state": "Rajasthan",
"district": "Sikar",
"city": "AJEETGARH",
"climate": "Composite"
},
{
"state": "Rajasthan",
"district": "Sikar",
"city": "DANTARAMGARH",
"climate": "Composite"
},
{
"state": "Rajasthan",
"district": "Sikar",
"city": "Fatehpur",
"climate": "Composite",
"code": 800525
},
{
"state": "Rajasthan",
"district": "Sikar",
"city": "Khandela",
"climate": "Composite",
"code": 800529
},
{
"state": "Rajasthan",
"district": "Sikar",
"city": "Lachhmangarh",
"climate": "Composite",
"code": 800526
},
{
"state": "Rajasthan",
"district": "Sikar",
"city": "Losal",
"climate": "Composite",
"code": 800528
},
{
"state": "Rajasthan",
"district": "Sikar",
"city": "Neem-Ka-Thana",
"climate": "Composite",
"code": 800532
},
{
"state": "Rajasthan",
"district": "Sikar",
"city": "Reengus",
"climate": "Composite",
"code": 800531
},
{
"state": "Rajasthan",
"district": "Sikar",
"city": "Sikar",
"climate": "Composite",
"code": 800527
},
{
"state": "Rajasthan",
"district": "Sikar",
"city": "Sri Madhopur",
"climate": "Composite",
"code": 800530
},
{
"state": "Rajasthan",
"district": "Sirohi",
"city": "Abu Road",
"climate": "Cold",
"code": 800558
},
{
"state": "Rajasthan",
"district": "Sirohi",
"city": "Jawal",
"climate": "Cold",
"code": 900713
},
{
"state": "Rajasthan",
"district": "Sirohi",
"city": "Mount Abu",
"climate": "Cold",
"code": 800557
},
{
"state": "Rajasthan",
"district": "Sirohi",
"city": "Pindwara",
"climate": "Cold",
"code": 800556
},
{
"state": "Rajasthan",
"district": "Sirohi",
"city": "Sheoganj",
"climate": "Cold",
"code": 800554
},
{
"state": "Rajasthan",
"district": "Sirohi",
"city": "Sirohi",
"climate": "Cold",
"code": 800555
},
{
"state": "Rajasthan",
"district": "Tonk",
"city": "Deoli",
"climate": "Composite",
"code": 800580
},
{
"state": "Rajasthan",
"district": "Tonk",
"city": "Malpura",
"climate": "Composite",
"code": 800576
},
{
"state": "Rajasthan",
"district": "Tonk",
"city": "Niwai",
"climate": "Composite",
"code": 800577
},
{
"state": "Rajasthan",
"district": "Tonk",
"city": "Todaraisingh",
"climate": "Composite",
"code": 800579
},
{
"state": "Rajasthan",
"district": "Tonk",
"city": "Tonk",
"climate": "Composite",
"code": 800578
},
{
"state": "Rajasthan",
"district": "Tonk",
"city": "Uniara",
"climate": "Composite",
"code": 800581
},
{
"state": "Rajasthan",
"district": "Udaipur",
"city": "Bhinder",
"climate": "Composite",
"code": 800624
},
{
"state": "Rajasthan",
"district": "Udaipur",
"city": "Fatehnagar",
"climate": "Composite",
"code": 800622
},
{
"state": "Rajasthan",
"district": "Udaipur",
"city": "Kanor",
"climate": "Composite",
"code": 800625
},
{
"state": "Rajasthan",
"district": "Udaipur",
"city": "RISHABHDEO",
"climate": "Composite"
},
{
"state": "Rajasthan",
"district": "Udaipur",
"city": "SEMARI",
"climate": "Composite"
},
{
"state": "Rajasthan",
"district": "Udaipur",
"city": "Salumbar",
"climate": "Composite",
"code": 800626
},
{
"state": "Rajasthan",
"district": "Udaipur",
"city": "Udaipur",
"climate": "Composite",
"code": 800623
},
{
"state": "Sikkim",
"district": "Gangtok",
"city": "Gangtok",
"climate": "Cold",
"code": 801421
},
{
"state": "Sikkim",
"district": "Gangtok",
"city": "Singtam",
"climate": "Cold",
"code": 801422
},
{
"state": "Sikkim",
"district": "Gyalshing",
"city": "Gyalshing",
"climate": "Cold",
"code": 801417
},
{
"state": "Sikkim",
"district": "Mangan",
"city": "Mangan",
"climate": "Cold",
"code": 801416
},
{
"state": "Sikkim",
"district": "Namchi",
"city": "Jorethang",
"climate": "Cold",
"code": 801420
},
{
"state": "Sikkim",
"district": "Namchi",
"city": "Namchi",
"climate": "Cold",
"code": 801419
},
{
"state": "Sikkim",
"district": "Pakyong",
"city": "Rangpo",
"climate": "Cold",
"code": 801423
},
{
"state": "Tamil Nadu",
"district": "Ariyalur",
"city": "Ariyalur",
"climate": "Warm & humid",
"code": 803645
},
{
"state": "Tamil Nadu",
"district": "Ariyalur",
"city": "Jayamkondan",
"climate": "Warm & humid",
"code": 803643
},
{
"state": "Tamil Nadu",
"district": "Ariyalur",
"city": "Udaiyar Palayam",
"climate": "Warm & humid",
"code": 803644
},
{
"state": "Tamil Nadu",
"district": "Ariyalur",
"city": "Varatharajanpettai",
"climate": "Warm & humid",
"code": 803642
},
{
"state": "Tamil Nadu",
"district": "Chengalpattu",
"city": "Acharapakkam",
"climate": "Warm & humid",
"code": 803373
},
{
"state": "Tamil Nadu",
"district": "Chengalpattu",
"city": "Chengalpattu",
"climate": "Warm & humid",
"code": 803364
},
{
"state": "Tamil Nadu",
"district": "Chengalpattu",
"city": "Edaikalinadu",
"climate": "Warm & humid",
"code": 803374
},
{
"state": "Tamil Nadu",
"district": "Chengalpattu",
"city": "Guduvancherry",
"climate": "Warm & humid",
"code": 803361
},
{
"state": "Tamil Nadu",
"district": "Chengalpattu",
"city": "Karunkuzhi",
"climate": "Warm & humid",
"code": 803371
},
{
"state": "Tamil Nadu",
"district": "Chengalpattu",
"city": "Madhuranthagam",
"climate": "Warm & humid",
"code": 803372
},
{
"state": "Tamil Nadu",
"district": "Chengalpattu",
"city": "Mamallapuram",
"climate": "Warm & humid",
"code": 803369
},
{
"state": "Tamil Nadu",
"district": "Chengalpattu",
"city": "Maraimalainagar",
"climate": "Warm & humid",
"code": 803362
},
{
"state": "Tamil Nadu",
"district": "Chengalpattu",
"city": "Tambaram",
"climate": "Warm & humid",
"code": 803345
},
{
"state": "Tamil Nadu",
"district": "Chengalpattu",
"city": "Thirukalukundram",
"climate": "Warm & humid",
"code": 803370
},
{
"state": "Tamil Nadu",
"district": "Chengalpattu",
"city": "Thiruporur",
"climate": "Warm & humid",
"code": 803363
},
{
"state": "Tamil Nadu",
"district": "Chennai",
"city": "Chennai",
"climate": "Warm & humid",
"code": 803339
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "Alanthurai",
"climate": "Warm & humid",
"code": 803994
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "Anamalai",
"climate": "Warm & humid",
"code": 804006
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "Annur",
"climate": "Warm & humid",
"code": 803969
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "Chettipalayam",
"climate": "Warm & humid",
"code": 803995
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "Coimbatore",
"climate": "Warm & humid",
"code": 803984
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "Dhaliyur",
"climate": "Warm & humid",
"code": 803986
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "Ettimadai",
"climate": "Warm & humid",
"code": 803997
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "Gudalur_C",
"climate": "Warm & humid",
"code": 803971
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "Idigarai",
"climate": "Warm & humid",
"code": 803973
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "Irugur",
"climate": "Warm & humid",
"code": 803965
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "Kannampalyam",
"climate": "Warm & humid",
"code": 803968
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "Karamadai",
"climate": "Warm & humid",
"code": 803962
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "Karumathampatti",
"climate": "Warm & humid",
"code": 803964
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "Kinathukadavu",
"climate": "Warm & humid",
"code": 804000
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "Kottur",
"climate": "Warm & humid",
"code": 804009
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "Madhukkarai",
"climate": "Warm & humid",
"code": 803996
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "Mettupalayam_C",
"climate": "Warm & humid",
"code": 803961
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "Mopperipalayam",
"climate": "Warm & humid",
"code": 803963
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "Narasimhanaickenpalayam",
"climate": "Warm & humid",
"code": 803975
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "No.4 Veerapandi",
"climate": "Warm & humid",
"code": 803970
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "O.K.Mandapam",
"climate": "Warm & humid",
"code": 803998
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "Odayakulam",
"climate": "Warm & humid",
"code": 804007
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "Pallapalayam_C",
"climate": "Warm & humid",
"code": 803967
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "Periya Negamam",
"climate": "Warm & humid",
"code": 804001
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "Periyanaickenpalayam",
"climate": "Warm & humid",
"code": 803972
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "Perur",
"climate": "Warm & humid",
"code": 803991
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "Pollachi",
"climate": "Warm & humid",
"code": 804002
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "Pooluvapatti",
"climate": "Warm & humid",
"code": 803993
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "Samathur",
"climate": "Warm & humid",
"code": 804005
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "Sarcarsamakulam",
"climate": "Warm & humid",
"code": 803974
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "Sirumugai",
"climate": "Warm & humid",
"code": 803960
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "Suleswaranpatti",
"climate": "Warm & humid",
"code": 804004
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "Sulur",
"climate": "Warm & humid",
"code": 803966
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "T.M.Palayam",
"climate": "Warm & humid",
"code": 803999
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "Thenkarai_C",
"climate": "Warm & humid",
"code": 803992
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "Thondamuthur",
"climate": "Warm & humid",
"code": 803985
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "Valparai",
"climate": "Warm & humid",
"code": 804010
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "Vedapatti",
"climate": "Warm & humid",
"code": 803987
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "Vellalore",
"climate": "Warm & humid",
"code": 803988
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "Vettaikaranpudur",
"climate": "Warm & humid",
"code": 804008
},
{
"state": "Tamil Nadu",
"district": "Coimbatore",
"city": "Zaminuthukuli",
"climate": "Warm & humid",
"code": 804003
},
{
"state": "Tamil Nadu",
"district": "Cuddalore",
"city": "Annamalai Nagar",
"climate": "Warm & humid",
"code": 803658
},
{
"state": "Tamil Nadu",
"district": "Cuddalore",
"city": "Bhuvanagiri",
"climate": "Warm & humid",
"code": 803655
},
{
"state": "Tamil Nadu",
"district": "Cuddalore",
"city": "Chidambaram",
"climate": "Warm & humid",
"code": 803657
},
{
"state": "Tamil Nadu",
"district": "Cuddalore",
"city": "Cuddalore",
"climate": "Warm & humid",
"code": 803650
},
{
"state": "Tamil Nadu",
"district": "Cuddalore",
"city": "Gangaikondan",
"climate": "Warm & humid",
"code": 803663
},
{
"state": "Tamil Nadu",
"district": "Cuddalore",
"city": "Kattumannarkoil",
"climate": "Warm & humid",
"code": 803661
},
{
"state": "Tamil Nadu",
"district": "Cuddalore",
"city": "Killai",
"climate": "Warm & humid",
"code": 803656
},
{
"state": "Tamil Nadu",
"district": "Cuddalore",
"city": "Kurinjipadi",
"climate": "Warm & humid",
"code": 803651
},
{
"state": "Tamil Nadu",
"district": "Cuddalore",
"city": "Lalpet",
"climate": "Warm & humid",
"code": 803660
},
{
"state": "Tamil Nadu",
"district": "Cuddalore",
"city": "Mangalampet",
"climate": "Warm & humid",
"code": 803662
},
{
"state": "Tamil Nadu",
"district": "Cuddalore",
"city": "Melpattampakkam",
"climate": "Warm & humid",
"code": 803647
},
{
"state": "Tamil Nadu",
"district": "Cuddalore",
"city": "Nellikuppam",
"climate": "Warm & humid",
"code": 803648
},
{
"state": "Tamil Nadu",
"district": "Cuddalore",
"city": "Panruti",
"climate": "Warm & humid",
"code": 803649
},
{
"state": "Tamil Nadu",
"district": "Cuddalore",
"city": "Parangipettai",
"climate": "Warm & humid",
"code": 803653
},
{
"state": "Tamil Nadu",
"district": "Cuddalore",
"city": "Pennadam",
"climate": "Warm & humid",
"code": 803665
},
{
"state": "Tamil Nadu",
"district": "Cuddalore",
"city": "Sethiyathope",
"climate": "Warm & humid",
"code": 803654
},
{
"state": "Tamil Nadu",
"district": "Cuddalore",
"city": "Srimushnam",
"climate": "Warm & humid",
"code": 803659
},
{
"state": "Tamil Nadu",
"district": "Cuddalore",
"city": "Thittagudi",
"climate": "Warm & humid",
"code": 803666
},
{
"state": "Tamil Nadu",
"district": "Cuddalore",
"city": "Thorapadi",
"climate": "Warm & humid",
"code": 803646
},
{
"state": "Tamil Nadu",
"district": "Cuddalore",
"city": "Vadalur",
"climate": "Warm & humid",
"code": 803652
},
{
"state": "Tamil Nadu",
"district": "Cuddalore",
"city": "Virudhachalam",
"climate": "Warm & humid",
"code": 803664
},
{
"state": "Tamil Nadu",
"district": "Dharmapuri",
"city": "B. Mallapuram",
"climate": "Warm & humid",
"code": 803946
},
{
"state": "Tamil Nadu",
"district": "Dharmapuri",
"city": "Dharmapuri",
"climate": "Warm & humid",
"code": 803948
},
{
"state": "Tamil Nadu",
"district": "Dharmapuri",
"city": "Harur",
"climate": "Warm & humid",
"code": 803944
},
{
"state": "Tamil Nadu",
"district": "Dharmapuri",
"city": "Kadathur",
"climate": "Warm & humid",
"code": 803945
},
{
"state": "Tamil Nadu",
"district": "Dharmapuri",
"city": "Kambainallur",
"climate": "Warm & humid",
"code": 803943
},
{
"state": "Tamil Nadu",
"district": "Dharmapuri",
"city": "Karimangalama",
"climate": "Warm & humid",
"code": 803941
},
{
"state": "Tamil Nadu",
"district": "Dharmapuri",
"city": "Marandahalli",
"climate": "Warm & humid",
"code": 803940
},
{
"state": "Tamil Nadu",
"district": "Dharmapuri",
"city": "Palakkodu",
"climate": "Warm & humid",
"code": 803942
},
{
"state": "Tamil Nadu",
"district": "Dharmapuri",
"city": "Papparapatti",
"climate": "Warm & humid",
"code": 803949
},
{
"state": "Tamil Nadu",
"district": "Dharmapuri",
"city": "Pappireddipatti",
"climate": "Warm & humid",
"code": 803947
},
{
"state": "Tamil Nadu",
"district": "Dharmapuri",
"city": "Pennagaram",
"climate": "Warm & humid",
"code": 803950
},
{
"state": "Tamil Nadu",
"district": "Dindigul",
"city": "Agaram",
"climate": "Cold",
"code": 803587
},
{
"state": "Tamil Nadu",
"district": "Dindigul",
"city": "Ammayan Aickanur",
"climate": "Cold",
"code": 803597
},
{
"state": "Tamil Nadu",
"district": "Dindigul",
"city": "Ayakudi",
"climate": "Cold",
"code": 803577
},
{
"state": "Tamil Nadu",
"district": "Dindigul",
"city": "Ayyalur",
"climate": "Cold",
"code": 803583
},
{
"state": "Tamil Nadu",
"district": "Dindigul",
"city": "Ayyampalayam",
"climate": "Cold",
"code": 803593
},
{
"state": "Tamil Nadu",
"district": "Dindigul",
"city": "Balasamudram",
"climate": "Cold",
"code": 803578
},
{
"state": "Tamil Nadu",
"district": "Dindigul",
"city": "Bathalaguntu",
"climate": "Cold",
"code": 803600
},
{
"state": "Tamil Nadu",
"district": "Dindigul",
"city": "Chinnalapatti",
"climate": "Cold",
"code": 803592
},
{
"state": "Tamil Nadu",
"district": "Dindigul",
"city": "Dindigul",
"climate": "Cold",
"code": 803589
},
{
"state": "Tamil Nadu",
"district": "Dindigul",
"city": "Eriodu",
"climate": "Cold",
"code": 803582
},
{
"state": "Tamil Nadu",
"district": "Dindigul",
"city": "Kannivadi_D",
"climate": "Cold",
"code": 803590
},
{
"state": "Tamil Nadu",
"district": "Dindigul",
"city": "Keeranur_D",
"climate": "Cold",
"code": 803574
},
{
"state": "Tamil Nadu",
"district": "Dindigul",
"city": "Kodaikanal",
"climate": "Cold",
"code": 803595
},
{
"state": "Tamil Nadu",
"district": "Dindigul",
"city": "Natham",
"climate": "Cold",
"code": 803585
},
{
"state": "Tamil Nadu",
"district": "Dindigul",
"city": "Neikkarapatti",
"climate": "Cold",
"code": 803575
},
{
"state": "Tamil Nadu",
"district": "Dindigul",
"city": "Nillakottai",
"climate": "Cold",
"code": 803598
},
{
"state": "Tamil Nadu",
"district": "Dindigul",
"city": "Ottanchatram",
"climate": "Cold",
"code": 803579
},
{
"state": "Tamil Nadu",
"district": "Dindigul",
"city": "Palani",
"climate": "Cold",
"code": 803576
},
{
"state": "Tamil Nadu",
"district": "Dindigul",
"city": "Palayam",
"climate": "Cold",
"code": 803580
},
{
"state": "Tamil Nadu",
"district": "Dindigul",
"city": "Pannaikadu",
"climate": "Cold",
"code": 803594
},
{
"state": "Tamil Nadu",
"district": "Dindigul",
"city": "Pattiveeranpatti",
"climate": "Cold",
"code": 803599
},
{
"state": "Tamil Nadu",
"district": "Dindigul",
"city": "Sevugampatti",
"climate": "Cold",
"code": 803596
},
{
"state": "Tamil Nadu",
"district": "Dindigul",
"city": "Sithayankottai",
"climate": "Cold",
"code": 803591
},
{
"state": "Tamil Nadu",
"district": "Dindigul",
"city": "Sriramapuram",
"climate": "Cold",
"code": 803586
},
{
"state": "Tamil Nadu",
"district": "Dindigul",
"city": "Thadicombu",
"climate": "Cold",
"code": 803588
},
{
"state": "Tamil Nadu",
"district": "Dindigul",
"city": "Vadamadurai",
"climate": "Cold",
"code": 803584
},
{
"state": "Tamil Nadu",
"district": "Dindigul",
"city": "Vedasandur",
"climate": "Cold",
"code": 803581
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Ammapettai_E",
"climate": "Warm & humid",
"code": 803511
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Anthiyur",
"climate": "Warm & humid",
"code": 803512
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Appakdual",
"climate": "Warm & humid",
"code": 803516
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Arachalur",
"climate": "Warm & humid",
"code": 803551
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Ariyappampalyam",
"climate": "Warm & humid",
"code": 803507
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Athani",
"climate": "Warm & humid",
"code": 803514
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Avalpoondurai",
"climate": "Warm & humid",
"code": 803545
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Bhavani",
"climate": "Warm & humid",
"code": 803517
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Bhavanisagar",
"climate": "Warm & humid",
"code": 803508
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Chennasamudram",
"climate": "Warm & humid",
"code": 803557
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Chennimalai",
"climate": "Warm & humid",
"code": 803535
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Chithode",
"climate": "Warm & humid",
"code": 803537
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Elathur",
"climate": "Warm & humid",
"code": 803526
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Erode",
"climate": "Warm & humid",
"code": 803542
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Gobichettipalayam",
"climate": "Warm & humid",
"code": 803523
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Jambai",
"climate": "Warm & humid",
"code": 803515
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Kanjikovil",
"climate": "Warm & humid",
"code": 803530
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Karumandi Chellipalayam",
"climate": "Warm & humid",
"code": 803533
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Kasipalayam",
"climate": "Warm & humid",
"code": 803522
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Kembanaickenpalayam",
"climate": "Warm & humid",
"code": 803506
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Kilampadi",
"climate": "Warm & humid",
"code": 803548
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Kodumudi",
"climate": "Warm & humid",
"code": 803556
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Kolappalur",
"climate": "Warm & humid",
"code": 803527
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Kollankovil",
"climate": "Warm & humid",
"code": 803554
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Kugalur",
"climate": "Warm & humid",
"code": 803524
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Lakampatti",
"climate": "Warm & humid",
"code": 803521
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Modakkurrichi",
"climate": "Warm & humid",
"code": 803546
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Nalampatti",
"climate": "Warm & humid",
"code": 803531
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Nambiyur",
"climate": "Warm & humid",
"code": 803528
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Nasiyanur",
"climate": "Warm & humid",
"code": 803540
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Nerinjipettai",
"climate": "Warm & humid",
"code": 803510
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Olagadam",
"climate": "Warm & humid",
"code": 803513
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "P.Mettupalayam",
"climate": "Warm & humid",
"code": 803525
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Pallapalayam_E",
"climate": "Warm & humid",
"code": 803529
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Pasur",
"climate": "Warm & humid",
"code": 803547
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Periyakodiveri",
"climate": "Warm & humid",
"code": 803519
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Perundurai",
"climate": "Warm & humid",
"code": 803534
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Pethampalavam",
"climate": "Warm & humid",
"code": 803532
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Punjaipuliyampatti",
"climate": "Warm & humid",
"code": 803509
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Salangapalayam",
"climate": "Warm & humid",
"code": 803518
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Sathyamangalam",
"climate": "Warm & humid",
"code": 803505
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Sivagiri_E",
"climate": "Warm & humid",
"code": 803552
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Unjalur",
"climate": "Warm & humid",
"code": 803553
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Vadugapatti_E",
"climate": "Warm & humid",
"code": 803550
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Vaniputhur",
"climate": "Warm & humid",
"code": 803520
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Vellottamparappu",
"climate": "Warm & humid",
"code": 803549
},
{
"state": "Tamil Nadu",
"district": "Erode",
"city": "Vengambur",
"climate": "Warm & humid",
"code": 803555
},
{
"state": "Tamil Nadu",
"district": "Kallakurichi",
"city": "Chinnasalem",
"climate": "Warm & humid",
"code": 803441
},
{
"state": "Tamil Nadu",
"district": "Kallakurichi",
"city": "Kallakurichi",
"climate": "Warm & humid",
"code": 803440
},
{
"state": "Tamil Nadu",
"district": "Kallakurichi",
"city": "Manalurpet",
"climate": "Warm & humid",
"code": 803433
},
{
"state": "Tamil Nadu",
"district": "Kallakurichi",
"city": "Sankarapuram",
"climate": "Warm & humid",
"code": 803437
},
{
"state": "Tamil Nadu",
"district": "Kallakurichi",
"city": "Thiagadurgam",
"climate": "Warm & humid",
"code": 803439
},
{
"state": "Tamil Nadu",
"district": "Kallakurichi",
"city": "Thirukoilur",
"climate": "Warm & humid",
"code": 803435
},
{
"state": "Tamil Nadu",
"district": "Kallakurichi",
"city": "Ulundurpettai",
"climate": "Warm & humid",
"code": 803442
},
{
"state": "Tamil Nadu",
"district": "Kallakurichi",
"city": "Vadakkanandal",
"climate": "Warm & humid",
"code": 803438
},
{
"state": "Tamil Nadu",
"district": "Kancheepuram",
"city": "Kancheepuram",
"climate": "Warm & humid",
"code": 803365
},
{
"state": "Tamil Nadu",
"district": "Kancheepuram",
"city": "Kundrathur",
"climate": "Warm & humid",
"code": 803341
},
{
"state": "Tamil Nadu",
"district": "Kancheepuram",
"city": "Mangadu",
"climate": "Warm & humid",
"code": 803340
},
{
"state": "Tamil Nadu",
"district": "Kancheepuram",
"city": "Sriperumbudur",
"climate": "Warm & humid",
"code": 803342
},
{
"state": "Tamil Nadu",
"district": "Kancheepuram",
"city": "St Thomas Mount Cantonment",
"climate": "Warm & humid",
"code": 803350
},
{
"state": "Tamil Nadu",
"district": "Kancheepuram",
"city": "Uthiramerur",
"climate": "Warm & humid",
"code": 803368
},
{
"state": "Tamil Nadu",
"district": "Kancheepuram",
"city": "Walajabad",
"climate": "Warm & humid",
"code": 803367
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Agasteeswaram",
"climate": "Warm & humid",
"code": 803937
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Anjugramam",
"climate": "Warm & humid",
"code": 803933
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Aralvoimozhi Town",
"climate": "Warm & humid",
"code": 803923
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Arumanai",
"climate": "Warm & humid",
"code": 803881
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Attoor",
"climate": "Warm & humid",
"code": 803900
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Azhagappapuram",
"climate": "Warm & humid",
"code": 803932
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Azhagiapandipuram",
"climate": "Warm & humid",
"code": 803921
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Boothapandi",
"climate": "Warm & humid",
"code": 803922
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Colachel",
"climate": "Warm & humid",
"code": 803917
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Edaicode",
"climate": "Warm & humid",
"code": 803882
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Eraniel",
"climate": "Warm & humid",
"code": 803910
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Ganapathipuram",
"climate": "Warm & humid",
"code": 803930
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Kadayal",
"climate": "Warm & humid",
"code": 803880
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Kaliyakkavilai",
"climate": "Warm & humid",
"code": 803884
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Kallukoottam",
"climate": "Warm & humid",
"code": 803914
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Kanyakumari",
"climate": "Warm & humid",
"code": 803939
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Kappiyarai",
"climate": "Warm & humid",
"code": 803909
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Karungal",
"climate": "Warm & humid",
"code": 803894
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Keezhkulam",
"climate": "Warm & humid",
"code": 803893
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Killiyur",
"climate": "Warm & humid",
"code": 803892
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Kollancode",
"climate": "Warm & humid",
"code": 803889
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Koothanallur_K",
"climate": "Warm & humid",
"code": 803903
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Kotttaram",
"climate": "Warm & humid",
"code": 803934
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Kulasekaram",
"climate": "Warm & humid",
"code": 803898
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Kumarapuram",
"climate": "Warm & humid",
"code": 803902
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Kuzhithurai",
"climate": "Warm & humid",
"code": 803886
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Manavalakurichy",
"climate": "Warm & humid",
"code": 803919
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Mandaikadu",
"climate": "Warm & humid",
"code": 803918
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Marungur",
"climate": "Warm & humid",
"code": 803925
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Mulagumoodu",
"climate": "Warm & humid",
"code": 803905
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Myladi",
"climate": "Warm & humid",
"code": 803931
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Nagarcoil",
"climate": "Warm & humid",
"code": 803927
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Nallur",
"climate": "Warm & humid",
"code": 803888
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Neyyoor",
"climate": "Warm & humid",
"code": 803912
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Pacode",
"climate": "Warm & humid",
"code": 803885
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Padbanabapuram",
"climate": "Warm & humid",
"code": 803907
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Palapallam",
"climate": "Warm & humid",
"code": 803895
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Palukal",
"climate": "Warm & humid",
"code": 803883
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Ponmanai",
"climate": "Warm & humid",
"code": 803897
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Puthalam",
"climate": "Warm & humid",
"code": 803936
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Puthukkadai",
"climate": "Warm & humid",
"code": 803891
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Reethapuram",
"climate": "Warm & humid",
"code": 803913
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Suchindrum",
"climate": "Warm & humid",
"code": 803929
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Thazhakudy",
"climate": "Warm & humid",
"code": 803924
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Thenthamarikulam",
"climate": "Warm & humid",
"code": 803938
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Therur",
"climate": "Warm & humid",
"code": 803926
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Thingalnagar",
"climate": "Warm & humid",
"code": 803915
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Thirparappu",
"climate": "Warm & humid",
"code": 803896
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Thiruvattar",
"climate": "Warm & humid",
"code": 803899
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Thiruvithancode",
"climate": "Warm & humid",
"code": 803908
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Unnamalaikadai",
"climate": "Warm & humid",
"code": 803887
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Valvachagostam",
"climate": "Warm & humid",
"code": 803904
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Vellimalai",
"climate": "Warm & humid",
"code": 803920
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Verkilambi",
"climate": "Warm & humid",
"code": 803901
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Vilavoor",
"climate": "Warm & humid",
"code": 803906
},
{
"state": "Tamil Nadu",
"district": "Kanniyakumari",
"city": "Villukuri",
"climate": "Warm & humid",
"code": 803911
},
{
"state": "Tamil Nadu",
"district": "Karur",
"city": "Aravakurichi",
"climate": "Warm & humid",
"code": 803601
},
{
"state": "Tamil Nadu",
"district": "Karur",
"city": "Karur",
"climate": "Warm & humid",
"code": 803607
},
{
"state": "Tamil Nadu",
"district": "Karur",
"city": "Krishnaraya Puram",
"climate": "Warm & humid",
"code": 803611
},
{
"state": "Tamil Nadu",
"district": "Karur",
"city": "Kulithalai",
"climate": "Warm & humid",
"code": 803613
},
{
"state": "Tamil Nadu",
"district": "Karur",
"city": "Marudur",
"climate": "Warm & humid",
"code": 803614
},
{
"state": "Tamil Nadu",
"district": "Karur",
"city": "Nangavaram",
"climate": "Warm & humid",
"code": 803615
},
{
"state": "Tamil Nadu",
"district": "Karur",
"city": "P.J. Cholapuram",
"climate": "Warm & humid",
"code": 803612
},
{
"state": "Tamil Nadu",
"district": "Karur",
"city": "Pallappatty",
"climate": "Warm & humid",
"code": 803602
},
{
"state": "Tamil Nadu",
"district": "Karur",
"city": "Puliyur",
"climate": "Warm & humid",
"code": 803608
},
{
"state": "Tamil Nadu",
"district": "Karur",
"city": "Punjaipugalur",
"climate": "Warm & humid",
"code": 803604
},
{
"state": "Tamil Nadu",
"district": "Karur",
"city": "Punjaithotta Kurichi",
"climate": "Warm & humid",
"code": 803605
},
{
"state": "Tamil Nadu",
"district": "Karur",
"city": "Uppidamangalam",
"climate": "Warm & humid",
"code": 803610
},
{
"state": "Tamil Nadu",
"district": "Krishnagiri",
"city": "Bargur",
"climate": "Warm & humid",
"code": 803953
},
{
"state": "Tamil Nadu",
"district": "Krishnagiri",
"city": "Denkanikottai",
"climate": "Warm & humid",
"code": 803957
},
{
"state": "Tamil Nadu",
"district": "Krishnagiri",
"city": "Hossur",
"climate": "Warm & humid",
"code": 803951
},
{
"state": "Tamil Nadu",
"district": "Krishnagiri",
"city": "Kaveripattinam",
"climate": "Warm & humid",
"code": 803955
},
{
"state": "Tamil Nadu",
"district": "Krishnagiri",
"city": "Kelamangalam",
"climate": "Warm & humid",
"code": 803956
},
{
"state": "Tamil Nadu",
"district": "Krishnagiri",
"city": "Krishnagiri",
"climate": "Warm & humid",
"code": 803954
},
{
"state": "Tamil Nadu",
"district": "Krishnagiri",
"city": "Nagojanahalli",
"climate": "Warm & humid",
"code": 803958
},
{
"state": "Tamil Nadu",
"district": "Krishnagiri",
"city": "Uthangaral",
"climate": "Warm & humid",
"code": 803959
},
{
"state": "Tamil Nadu",
"district": "Madurai",
"city": "A.Vellalapatti",
"climate": "Warm & humid",
"code": 803740
},
{
"state": "Tamil Nadu",
"district": "Madurai",
"city": "Allanganallur",
"climate": "Warm & humid",
"code": 803748
},
{
"state": "Tamil Nadu",
"district": "Madurai",
"city": "Elumalai",
"climate": "Warm & humid",
"code": 803750
},
{
"state": "Tamil Nadu",
"district": "Madurai",
"city": "Madurai",
"climate": "Warm & humid",
"code": 803754
},
{
"state": "Tamil Nadu",
"district": "Madurai",
"city": "Melur",
"climate": "Warm & humid",
"code": 803741
},
{
"state": "Tamil Nadu",
"district": "Madurai",
"city": "Palamedu",
"climate": "Warm & humid",
"code": 803746
},
{
"state": "Tamil Nadu",
"district": "Madurai",
"city": "Paravai",
"climate": "Warm & humid",
"code": 803743
},
{
"state": "Tamil Nadu",
"district": "Madurai",
"city": "Periyur",
"climate": "Warm & humid",
"code": 803752
},
{
"state": "Tamil Nadu",
"district": "Madurai",
"city": "Sozhavandhan",
"climate": "Warm & humid",
"code": 803747
},
{
"state": "Tamil Nadu",
"district": "Madurai",
"city": "T.Kallupatii",
"climate": "Warm & humid",
"code": 803751
},
{
"state": "Tamil Nadu",
"district": "Madurai",
"city": "Thirumangalam",
"climate": "Warm & humid",
"code": 803753
},
{
"state": "Tamil Nadu",
"district": "Madurai",
"city": "Usilampatti",
"climate": "Warm & humid",
"code": 803749
},
{
"state": "Tamil Nadu",
"district": "Madurai",
"city": "Vadipatti",
"climate": "Warm & humid",
"code": 803745
},
{
"state": "Tamil Nadu",
"district": "Mayiladuthurai",
"city": "Kuthalam",
"climate": "Warm & humid",
"code": 803671
},
{
"state": "Tamil Nadu",
"district": "Mayiladuthurai",
"city": "Manalmedu",
"climate": "Warm & humid",
"code": 803669
},
{
"state": "Tamil Nadu",
"district": "Mayiladuthurai",
"city": "Mayiladuthurai",
"climate": "Warm & humid",
"code": 803670
},
{
"state": "Tamil Nadu",
"district": "Mayiladuthurai",
"city": "Sirkali",
"climate": "Warm & humid",
"code": 803667
},
{
"state": "Tamil Nadu",
"district": "Mayiladuthurai",
"city": "Tharangampadi",
"climate": "Warm & humid",
"code": 803672
},
{
"state": "Tamil Nadu",
"district": "Mayiladuthurai",
"city": "Vaithieswarankoil",
"climate": "Warm & humid",
"code": 803668
},
{
"state": "Tamil Nadu",
"district": "Nagapattinam",
"city": "Kilvelur",
"climate": "Warm & humid",
"code": 803675
},
{
"state": "Tamil Nadu",
"district": "Nagapattinam",
"city": "Nagapattinam",
"climate": "Warm & humid",
"code": 803674
},
{
"state": "Tamil Nadu",
"district": "Nagapattinam",
"city": "Thalanayar",
"climate": "Warm & humid",
"code": 803677
},
{
"state": "Tamil Nadu",
"district": "Nagapattinam",
"city": "Thittachery",
"climate": "Warm & humid",
"code": 803673
},
{
"state": "Tamil Nadu",
"district": "Nagapattinam",
"city": "Vedharanyam",
"climate": "Warm & humid",
"code": 803678
},
{
"state": "Tamil Nadu",
"district": "Nagapattinam",
"city": "Velankanni",
"climate": "Warm & humid",
"code": 803676
},
{
"state": "Tamil Nadu",
"district": "Namakkal",
"city": "Alampalayam_N_T",
"climate": "Warm & humid",
"code": 803485
},
{
"state": "Tamil Nadu",
"district": "Namakkal",
"city": "Athanur",
"climate": "Warm & humid",
"code": 803488
},
{
"state": "Tamil Nadu",
"district": "Namakkal",
"city": "Erumapatty",
"climate": "Warm & humid",
"code": 803498
},
{
"state": "Tamil Nadu",
"district": "Namakkal",
"city": "Kalappanaickenpatti",
"climate": "Warm & humid",
"code": 803495
},
{
"state": "Tamil Nadu",
"district": "Namakkal",
"city": "Kumarapalayam",
"climate": "Warm & humid",
"code": 803482
},
{
"state": "Tamil Nadu",
"district": "Namakkal",
"city": "Mallasamudram",
"climate": "Warm & humid",
"code": 803481
},
{
"state": "Tamil Nadu",
"district": "Namakkal",
"city": "Mohanur",
"climate": "Warm & humid",
"code": 803499
},
{
"state": "Tamil Nadu",
"district": "Namakkal",
"city": "Namagiripettai",
"climate": "Warm & humid",
"code": 803490
},
{
"state": "Tamil Nadu",
"district": "Namakkal",
"city": "Namakkal",
"climate": "Warm & humid",
"code": 803497
},
{
"state": "Tamil Nadu",
"district": "Namakkal",
"city": "Padaiveedu",
"climate": "Warm & humid",
"code": 803483
},
{
"state": "Tamil Nadu",
"district": "Namakkal",
"city": "Pallipalayam",
"climate": "Warm & humid",
"code": 803486
},
{
"state": "Tamil Nadu",
"district": "Namakkal",
"city": "Pandamangalam",
"climate": "Warm & humid",
"code": 803504
},
{
"state": "Tamil Nadu",
"district": "Namakkal",
"city": "Paramathy",
"climate": "Warm & humid",
"code": 803500
},
{
"state": "Tamil Nadu",
"district": "Namakkal",
"city": "Pattinam",
"climate": "Warm & humid",
"code": 803492
},
{
"state": "Tamil Nadu",
"district": "Namakkal",
"city": "Pillanallur",
"climate": "Warm & humid",
"code": 803494
},
{
"state": "Tamil Nadu",
"district": "Namakkal",
"city": "Pothanur",
"climate": "Warm & humid",
"code": 803502
},
{
"state": "Tamil Nadu",
"district": "Namakkal",
"city": "R. Pudupatty",
"climate": "Warm & humid",
"code": 803489
},
{
"state": "Tamil Nadu",
"district": "Namakkal",
"city": "Rasipuram",
"climate": "Warm & humid",
"code": 803493
},
{
"state": "Tamil Nadu",
"district": "Namakkal",
"city": "Seerapalli",
"climate": "Warm & humid",
"code": 803491
},
{
"state": "Tamil Nadu",
"district": "Namakkal",
"city": "Sendamangalam",
"climate": "Warm & humid",
"code": 803496
},
{
"state": "Tamil Nadu",
"district": "Namakkal",
"city": "Tiruchengode",
"climate": "Warm & humid",
"code": 803484
},
{
"state": "Tamil Nadu",
"district": "Namakkal",
"city": "Velur",
"climate": "Warm & humid",
"code": 803501
},
{
"state": "Tamil Nadu",
"district": "Namakkal",
"city": "Vengarai",
"climate": "Warm & humid",
"code": 803503
},
{
"state": "Tamil Nadu",
"district": "Namakkal",
"city": "Vennadur",
"climate": "Warm & humid",
"code": 803487
},
{
"state": "Tamil Nadu",
"district": "Perambalur",
"city": "Arumbavur",
"climate": "Warm & humid",
"code": 803638
},
{
"state": "Tamil Nadu",
"district": "Perambalur",
"city": "Kurumbalur",
"climate": "Warm & humid",
"code": 803640
},
{
"state": "Tamil Nadu",
"district": "Perambalur",
"city": "Labbaikudikadu",
"climate": "Warm & humid",
"code": 803641
},
{
"state": "Tamil Nadu",
"district": "Perambalur",
"city": "Perambalur",
"climate": "Warm & humid",
"code": 803639
},
{
"state": "Tamil Nadu",
"district": "Perambalur",
"city": "Poolambadi",
"climate": "Warm & humid",
"code": 803637
},
{
"state": "Tamil Nadu",
"district": "Pudukottai",
"city": "Alangudi",
"climate": "Warm & humid",
"code": 803721
},
{
"state": "Tamil Nadu",
"district": "Pudukottai",
"city": "Annavasal",
"climate": "Warm & humid",
"code": 803716
},
{
"state": "Tamil Nadu",
"district": "Pudukottai",
"city": "Aranthangi",
"climate": "Warm & humid",
"code": 803724
},
{
"state": "Tamil Nadu",
"district": "Pudukottai",
"city": "Arimalam",
"climate": "Warm & humid",
"code": 803719
},
{
"state": "Tamil Nadu",
"district": "Pudukottai",
"city": "Iluppur",
"climate": "Warm & humid",
"code": 803715
},
{
"state": "Tamil Nadu",
"district": "Pudukottai",
"city": "Karambakudi",
"climate": "Warm & humid",
"code": 803723
},
{
"state": "Tamil Nadu",
"district": "Pudukottai",
"city": "Keeramangalam",
"climate": "Warm & humid",
"code": 803722
},
{
"state": "Tamil Nadu",
"district": "Pudukottai",
"city": "Keeranur_P",
"climate": "Warm & humid",
"code": 803717
},
{
"state": "Tamil Nadu",
"district": "Pudukottai",
"city": "Ponnamaravathi",
"climate": "Warm & humid",
"code": 803720
},
{
"state": "Tamil Nadu",
"district": "Pudukottai",
"city": "Pudukottai",
"climate": "Warm & humid",
"code": 803718
},
{
"state": "Tamil Nadu",
"district": "Ramanathapuram",
"city": "Abiramam",
"climate": "Warm & humid",
"code": 803807
},
{
"state": "Tamil Nadu",
"district": "Ramanathapuram",
"city": "Kamuthi",
"climate": "Warm & humid",
"code": 803808
},
{
"state": "Tamil Nadu",
"district": "Ramanathapuram",
"city": "Keelakarai",
"climate": "Warm & humid",
"code": 803812
},
{
"state": "Tamil Nadu",
"district": "Ramanathapuram",
"city": "Mandapam",
"climate": "Warm & humid",
"code": 803811
},
{
"state": "Tamil Nadu",
"district": "Ramanathapuram",
"city": "Mudukulathur",
"climate": "Warm & humid",
"code": 803806
},
{
"state": "Tamil Nadu",
"district": "Ramanathapuram",
"city": "Paramakudi",
"climate": "Warm & humid",
"code": 803805
},
{
"state": "Tamil Nadu",
"district": "Ramanathapuram",
"city": "R.S. Mangalam",
"climate": "Warm & humid",
"code": 803804
},
{
"state": "Tamil Nadu",
"district": "Ramanathapuram",
"city": "Ramanathapuram",
"climate": "Warm & humid",
"code": 803810
},
{
"state": "Tamil Nadu",
"district": "Ramanathapuram",
"city": "Rameswaram",
"climate": "Warm & humid",
"code": 803813
},
{
"state": "Tamil Nadu",
"district": "Ramanathapuram",
"city": "Sayalgudi",
"climate": "Warm & humid",
"code": 803809
},
{
"state": "Tamil Nadu",
"district": "Ramanathapuram",
"city": "Thondi",
"climate": "Warm & humid",
"code": 803803
},
{
"state": "Tamil Nadu",
"district": "Ranipet",
"city": "Ammoor",
"climate": "Warm & humid",
"code": 803383
},
{
"state": "Tamil Nadu",
"district": "Ranipet",
"city": "Arakkonam",
"climate": "Warm & humid",
"code": 803387
},
{
"state": "Tamil Nadu",
"district": "Ranipet",
"city": "Arcot",
"climate": "Warm & humid",
"code": 803392
},
{
"state": "Tamil Nadu",
"district": "Ranipet",
"city": "Kalavai",
"climate": "Warm & humid",
"code": 803395
},
{
"state": "Tamil Nadu",
"district": "Ranipet",
"city": "Kaveripakkam",
"climate": "Warm & humid",
"code": 803390
},
{
"state": "Tamil Nadu",
"district": "Ranipet",
"city": "Melvisharam",
"climate": "Warm & humid",
"code": 803386
},
{
"state": "Tamil Nadu",
"district": "Ranipet",
"city": "Nemili",
"climate": "Warm & humid",
"code": 803389
},
{
"state": "Tamil Nadu",
"district": "Ranipet",
"city": "Panapakkam",
"climate": "Warm & humid",
"code": 803391
},
{
"state": "Tamil Nadu",
"district": "Ranipet",
"city": "Ranipet",
"climate": "Warm & humid",
"code": 803385
},
{
"state": "Tamil Nadu",
"district": "Ranipet",
"city": "Sholingur",
"climate": "Warm & humid",
"code": 803382
},
{
"state": "Tamil Nadu",
"district": "Ranipet",
"city": "Thakkolam",
"climate": "Warm & humid",
"code": 803388
},
{
"state": "Tamil Nadu",
"district": "Ranipet",
"city": "Thimiri",
"climate": "Warm & humid",
"code": 803394
},
{
"state": "Tamil Nadu",
"district": "Ranipet",
"city": "Vilapakkam",
"climate": "Warm & humid",
"code": 803393
},
{
"state": "Tamil Nadu",
"district": "Ranipet",
"city": "Wallajapet",
"climate": "Warm & humid",
"code": 803384
},
{
"state": "Tamil Nadu",
"district": "Salem",
"city": "Aattayampatty",
"climate": "Warm & humid",
"code": 803467
},
{
"state": "Tamil Nadu",
"district": "Salem",
"city": "Arasiramani",
"climate": "Warm & humid",
"code": 803459
},
{
"state": "Tamil Nadu",
"district": "Salem",
"city": "Attur",
"climate": "Warm & humid",
"code": 803473
},
{
"state": "Tamil Nadu",
"district": "Salem",
"city": "Ayothiapattinam",
"climate": "Warm & humid",
"code": 803470
},
{
"state": "Tamil Nadu",
"district": "Salem",
"city": "Belur_T",
"climate": "Warm & humid",
"code": 803468
},
{
"state": "Tamil Nadu",
"district": "Salem",
"city": "Edangansalai",
"climate": "Warm & humid",
"code": 803458
},
{
"state": "Tamil Nadu",
"district": "Salem",
"city": "Elampillai",
"climate": "Warm & humid",
"code": 803464
},
{
"state": "Tamil Nadu",
"district": "Salem",
"city": "Ethapur",
"climate": "Warm & humid",
"code": 803472
},
{
"state": "Tamil Nadu",
"district": "Salem",
"city": "Gangavalli",
"climate": "Warm & humid",
"code": 803478
},
{
"state": "Tamil Nadu",
"district": "Salem",
"city": "Idapaddi",
"climate": "Warm & humid",
"code": 803456
},
{
"state": "Tamil Nadu",
"district": "Salem",
"city": "Jalagandapuram",
"climate": "Warm & humid",
"code": 803450
},
{
"state": "Tamil Nadu",
"district": "Salem",
"city": "Kadayampatti",
"climate": "Warm & humid",
"code": 803451
},
{
"state": "Tamil Nadu",
"district": "Salem",
"city": "Kannankurichi",
"climate": "Warm & humid",
"code": 803462
},
{
"state": "Tamil Nadu",
"district": "Salem",
"city": "Karuppur",
"climate": "Warm & humid",
"code": 803453
},
{
"state": "Tamil Nadu",
"district": "Salem",
"city": "Keeripatti",
"climate": "Warm & humid",
"code": 803475
},
{
"state": "Tamil Nadu",
"district": "Salem",
"city": "Kolathur",
"climate": "Warm & humid",
"code": 803443
},
{
"state": "Tamil Nadu",
"district": "Salem",
"city": "Konganapuram",
"climate": "Warm & humid",
"code": 803457
},
{
"state": "Tamil Nadu",
"district": "Salem",
"city": "Mallur",
"climate": "Warm & humid",
"code": 803466
},
{
"state": "Tamil Nadu",
"district": "Salem",
"city": "Mecheri",
"climate": "Warm & humid",
"code": 803444
},
{
"state": "Tamil Nadu",
"district": "Salem",
"city": "Mettur",
"climate": "Warm & humid",
"code": 803446
},
{
"state": "Tamil Nadu",
"district": "Salem",
"city": "Nangavalli",
"climate": "Warm & humid",
"code": 803448
},
{
"state": "Tamil Nadu",
"district": "Salem",
"city": "Narasingapuram",
"climate": "Warm & humid",
"code": 803474
},
{
"state": "Tamil Nadu",
"district": "Salem",
"city": "Omalur",
"climate": "Warm & humid",
"code": 803452
},
{
"state": "Tamil Nadu",
"district": "Salem",
"city": "P.N.Patti",
"climate": "Warm & humid",
"code": 803447
},
{
"state": "Tamil Nadu",
"district": "Salem",
"city": "Panaimarathupatty",
"climate": "Warm & humid",
"code": 803465
},
{
"state": "Tamil Nadu",
"district": "Salem",
"city": "Pethanaickenpalayam",
"climate": "Warm & humid",
"code": 803471
},
{
"state": "Tamil Nadu",
"district": "Salem",
"city": "Poolampatti",
"climate": "Warm & humid",
"code": 803455
},
{
"state": "Tamil Nadu",
"district": "Salem",
"city": "Salem",
"climate": "Warm & humid",
"code": 803463
},
{
"state": "Tamil Nadu",
"district": "Salem",
"city": "Sangagiri",
"climate": "Warm & humid",
"code": 803461
},
{
"state": "Tamil Nadu",
"district": "Salem",
"city": "Sentharapatti",
"climate": "Warm & humid",
"code": 803480
},
{
"state": "Tamil Nadu",
"district": "Salem",
"city": "Thammampatti",
"climate": "Warm & humid",
"code": 803479
},
{
"state": "Tamil Nadu",
"district": "Salem",
"city": "Tharamangalam",
"climate": "Warm & humid",
"code": 803454
},
{
"state": "Tamil Nadu",
"district": "Salem",
"city": "Thedavur",
"climate": "Warm & humid",
"code": 803477
},
{
"state": "Tamil Nadu",
"district": "Salem",
"city": "Thevur",
"climate": "Warm & humid",
"code": 803460
},
{
"state": "Tamil Nadu",
"district": "Salem",
"city": "Vanavasi",
"climate": "Warm & humid",
"code": 803449
},
{
"state": "Tamil Nadu",
"district": "Salem",
"city": "Vazhapadi",
"climate": "Warm & humid",
"code": 803469
},
{
"state": "Tamil Nadu",
"district": "Salem",
"city": "Veeraganur",
"climate": "Warm & humid",
"code": 803476
},
{
"state": "Tamil Nadu",
"district": "Salem",
"city": "Veerakkalpudur",
"climate": "Warm & humid",
"code": 803445
},
{
"state": "Tamil Nadu",
"district": "Sivaganga",
"city": "Devakottai",
"climate": "Warm & humid",
"code": 803734
},
{
"state": "Tamil Nadu",
"district": "Sivaganga",
"city": "Ilayangudi",
"climate": "Warm & humid",
"code": 803739
},
{
"state": "Tamil Nadu",
"district": "Sivaganga",
"city": "Kanadukathan",
"climate": "Warm & humid",
"code": 803728
},
{
"state": "Tamil Nadu",
"district": "Sivaganga",
"city": "Kandanur",
"climate": "Warm & humid",
"code": 803731
},
{
"state": "Tamil Nadu",
"district": "Sivaganga",
"city": "Karaikudi",
"climate": "Warm & humid",
"code": 803733
},
{
"state": "Tamil Nadu",
"district": "Sivaganga",
"city": "Kottaiyur",
"climate": "Warm & humid",
"code": 803730
},
{
"state": "Tamil Nadu",
"district": "Sivaganga",
"city": "Manamadurai",
"climate": "Warm & humid",
"code": 803738
},
{
"state": "Tamil Nadu",
"district": "Sivaganga",
"city": "Nattarasankottai",
"climate": "Warm & humid",
"code": 803735
},
{
"state": "Tamil Nadu",
"district": "Sivaganga",
"city": "Nerkuppai",
"climate": "Warm & humid",
"code": 803725
},
{
"state": "Tamil Nadu",
"district": "Sivaganga",
"city": "Pallathur",
"climate": "Warm & humid",
"code": 803729
},
{
"state": "Tamil Nadu",
"district": "Sivaganga",
"city": "Puduvayal",
"climate": "Warm & humid",
"code": 803732
},
{
"state": "Tamil Nadu",
"district": "Sivaganga",
"city": "Singampuneri",
"climate": "Warm & humid",
"code": 803726
},
{
"state": "Tamil Nadu",
"district": "Sivaganga",
"city": "Sivagangai",
"climate": "Warm & humid",
"code": 803736
},
{
"state": "Tamil Nadu",
"district": "Sivaganga",
"city": "Thiruppathur",
"climate": "Warm & humid",
"code": 803727
},
{
"state": "Tamil Nadu",
"district": "Sivaganga",
"city": "Thiruppuvanam",
"climate": "Warm & humid",
"code": 803737
},
{
"state": "Tamil Nadu",
"district": "Tenkasi",
"city": "Achanpudur",
"climate": "Warm & humid",
"code": 803851
},
{
"state": "Tamil Nadu",
"district": "Tenkasi",
"city": "Alangulam",
"climate": "Warm & humid",
"code": 803857
},
{
"state": "Tamil Nadu",
"district": "Tenkasi",
"city": "Alwarkurichi",
"climate": "Warm & humid",
"code": 803861
},
{
"state": "Tamil Nadu",
"district": "Tenkasi",
"city": "Ayikudi",
"climate": "Warm & humid",
"code": 803845
},
{
"state": "Tamil Nadu",
"district": "Tenkasi",
"city": "Courtalam",
"climate": "Warm & humid",
"code": 803849
},
{
"state": "Tamil Nadu",
"district": "Tenkasi",
"city": "Ilanji",
"climate": "Warm & humid",
"code": 803848
},
{
"state": "Tamil Nadu",
"district": "Tenkasi",
"city": "Kadayanallur",
"climate": "Warm & humid",
"code": 803843
},
{
"state": "Tamil Nadu",
"district": "Tenkasi",
"city": "Kilapavoor",
"climate": "Warm & humid",
"code": 803856
},
{
"state": "Tamil Nadu",
"district": "Tenkasi",
"city": "Melagaram",
"climate": "Warm & humid",
"code": 803850
},
{
"state": "Tamil Nadu",
"district": "Tenkasi",
"city": "Panpoli",
"climate": "Warm & humid",
"code": 803853
},
{
"state": "Tamil Nadu",
"district": "Tenkasi",
"city": "Pudur",
"climate": "Warm & humid",
"code": 803854
},
{
"state": "Tamil Nadu",
"district": "Tenkasi",
"city": "Puliankudi",
"climate": "Warm & humid",
"code": 803839
},
{
"state": "Tamil Nadu",
"district": "Tenkasi",
"city": "Rayagiri",
"climate": "Warm & humid",
"code": 803837
},
{
"state": "Tamil Nadu",
"district": "Tenkasi",
"city": "Sambavar Vadagarai",
"climate": "Warm & humid",
"code": 803844
},
{
"state": "Tamil Nadu",
"district": "Tenkasi",
"city": "Sankarankoil",
"climate": "Warm & humid",
"code": 803841
},
{
"state": "Tamil Nadu",
"district": "Tenkasi",
"city": "Sivagiri_T",
"climate": "Warm & humid",
"code": 803836
},
{
"state": "Tamil Nadu",
"district": "Tenkasi",
"city": "Sundarapandiapuram",
"climate": "Warm & humid",
"code": 803847
},
{
"state": "Tamil Nadu",
"district": "Tenkasi",
"city": "Surandai",
"climate": "Warm & humid",
"code": 803842
},
{
"state": "Tamil Nadu",
"district": "Tenkasi",
"city": "Tenkasi",
"climate": "Warm & humid",
"code": 803846
},
{
"state": "Tamil Nadu",
"district": "Tenkasi",
"city": "Thiruvenkadam",
"climate": "Warm & humid",
"code": 803840
},
{
"state": "Tamil Nadu",
"district": "Tenkasi",
"city": "Vadakarai Keelpdiagai",
"climate": "Warm & humid",
"code": 803852
},
{
"state": "Tamil Nadu",
"district": "Tenkasi",
"city": "Vasudevanallur",
"climate": "Warm & humid",
"code": 803838
},
{
"state": "Tamil Nadu",
"district": "Thanjavur",
"city": "Adirampattinam",
"climate": "Warm & humid",
"code": 803712
},
{
"state": "Tamil Nadu",
"district": "Thanjavur",
"city": "Aduthurai",
"climate": "Warm & humid",
"code": 803691
},
{
"state": "Tamil Nadu",
"district": "Thanjavur",
"city": "Ammapettai_T",
"climate": "Warm & humid",
"code": 803703
},
{
"state": "Tamil Nadu",
"district": "Thanjavur",
"city": "Ayyampettai",
"climate": "Warm & humid",
"code": 803701
},
{
"state": "Tamil Nadu",
"district": "Thanjavur",
"city": "Cholapuram",
"climate": "Warm & humid",
"code": 803695
},
{
"state": "Tamil Nadu",
"district": "Thanjavur",
"city": "Kumbakonam",
"climate": "Warm & humid",
"code": 803697
},
{
"state": "Tamil Nadu",
"district": "Thanjavur",
"city": "Madukkur",
"climate": "Warm & humid",
"code": 803710
},
{
"state": "Tamil Nadu",
"district": "Thanjavur",
"city": "Melathiruppanthruthi",
"climate": "Warm & humid",
"code": 803705
},
{
"state": "Tamil Nadu",
"district": "Thanjavur",
"city": "Melattur",
"climate": "Warm & humid",
"code": 803702
},
{
"state": "Tamil Nadu",
"district": "Thanjavur",
"city": "Orthanadu",
"climate": "Warm & humid",
"code": 803709
},
{
"state": "Tamil Nadu",
"district": "Thanjavur",
"city": "Papanasam",
"climate": "Warm & humid",
"code": 803700
},
{
"state": "Tamil Nadu",
"district": "Thanjavur",
"city": "Pattukottai",
"climate": "Warm & humid",
"code": 803711
},
{
"state": "Tamil Nadu",
"district": "Thanjavur",
"city": "Peravurani",
"climate": "Warm & humid",
"code": 803713
},
{
"state": "Tamil Nadu",
"district": "Thanjavur",
"city": "Perumagalur",
"climate": "Warm & humid",
"code": 803714
},
{
"state": "Tamil Nadu",
"district": "Thanjavur",
"city": "Swamimalai",
"climate": "Warm & humid",
"code": 803698
},
{
"state": "Tamil Nadu",
"district": "Thanjavur",
"city": "Thanjavur",
"climate": "Warm & humid",
"code": 803707
},
{
"state": "Tamil Nadu",
"district": "Thanjavur",
"city": "Thirubuvanam",
"climate": "Warm & humid",
"code": 803693
},
{
"state": "Tamil Nadu",
"district": "Thanjavur",
"city": "Thirukattupalli",
"climate": "Warm & humid",
"code": 803706
},
{
"state": "Tamil Nadu",
"district": "Thanjavur",
"city": "Thirunageswaram",
"climate": "Warm & humid",
"code": 803696
},
{
"state": "Tamil Nadu",
"district": "Thanjavur",
"city": "Thiruppananthal",
"climate": "Warm & humid",
"code": 803690
},
{
"state": "Tamil Nadu",
"district": "Thanjavur",
"city": "Thiruvadaimaruthur",
"climate": "Warm & humid",
"code": 803694
},
{
"state": "Tamil Nadu",
"district": "Thanjavur",
"city": "Thiruvaiyaru",
"climate": "Warm & humid",
"code": 803704
},
{
"state": "Tamil Nadu",
"district": "Thanjavur",
"city": "Vallam",
"climate": "Warm & humid",
"code": 803708
},
{
"state": "Tamil Nadu",
"district": "Thanjavur",
"city": "Veppathur",
"climate": "Warm & humid",
"code": 803692
},
{
"state": "Tamil Nadu",
"district": "The Nilgiris",
"city": "Adigaratty",
"climate": "Cold",
"code": 803569
},
{
"state": "Tamil Nadu",
"district": "The Nilgiris",
"city": "Bikkatty",
"climate": "Cold",
"code": 803572
},
{
"state": "Tamil Nadu",
"district": "The Nilgiris",
"city": "Coonoor",
"climate": "Cold",
"code": 803570
},
{
"state": "Tamil Nadu",
"district": "The Nilgiris",
"city": "Devarshola",
"climate": "Cold",
"code": 803559
},
{
"state": "Tamil Nadu",
"district": "The Nilgiris",
"city": "Gudalur_N",
"climate": "Cold",
"code": 803560
},
{
"state": "Tamil Nadu",
"district": "The Nilgiris",
"city": "Hulical",
"climate": "Cold",
"code": 803571
},
{
"state": "Tamil Nadu",
"district": "The Nilgiris",
"city": "Jegathala",
"climate": "Cold",
"code": 803566
},
{
"state": "Tamil Nadu",
"district": "The Nilgiris",
"city": "Ketti",
"climate": "Cold",
"code": 803568
},
{
"state": "Tamil Nadu",
"district": "The Nilgiris",
"city": "Kil Kundah",
"climate": "Cold",
"code": 803573
},
{
"state": "Tamil Nadu",
"district": "The Nilgiris",
"city": "Kotagiri",
"climate": "Cold",
"code": 803565
},
{
"state": "Tamil Nadu",
"district": "The Nilgiris",
"city": "Naduvattam",
"climate": "Cold",
"code": 803563
},
{
"state": "Tamil Nadu",
"district": "The Nilgiris",
"city": "Nelliyalam",
"climate": "Cold",
"code": 803558
},
{
"state": "Tamil Nadu",
"district": "The Nilgiris",
"city": "O'Valley",
"climate": "Cold",
"code": 803561
},
{
"state": "Tamil Nadu",
"district": "The Nilgiris",
"city": "Sholur",
"climate": "Cold",
"code": 803562
},
{
"state": "Tamil Nadu",
"district": "The Nilgiris",
"city": "Udagamandalam",
"climate": "Cold",
"code": 803564
},
{
"state": "Tamil Nadu",
"district": "The Nilgiris",
"city": "Wellington Cantonment",
"climate": "Cold",
"code": 803567
},
{
"state": "Tamil Nadu",
"district": "Theni",
"city": "Andipatti",
"climate": "Warm & humid",
"code": 803786
},
{
"state": "Tamil Nadu",
"district": "Theni",
"city": "B. Meenakshipuram",
"climate": "Warm & humid",
"code": 803762
},
{
"state": "Tamil Nadu",
"district": "Theni",
"city": "Bodinayakanur",
"climate": "Warm & humid",
"code": 803760
},
{
"state": "Tamil Nadu",
"district": "Theni",
"city": "Boothipuram",
"climate": "Warm & humid",
"code": 803759
},
{
"state": "Tamil Nadu",
"district": "Theni",
"city": "C.Pudupatti",
"climate": "Warm & humid",
"code": 803781
},
{
"state": "Tamil Nadu",
"district": "Theni",
"city": "Chinnamanur",
"climate": "Warm & humid",
"code": 803777
},
{
"state": "Tamil Nadu",
"district": "Theni",
"city": "Cumbum",
"climate": "Warm & humid",
"code": 803783
},
{
"state": "Tamil Nadu",
"district": "Theni",
"city": "Devadanapatti",
"climate": "Warm & humid",
"code": 803764
},
{
"state": "Tamil Nadu",
"district": "Theni",
"city": "Ganguvarpatti",
"climate": "Warm & humid",
"code": 803763
},
{
"state": "Tamil Nadu",
"district": "Theni",
"city": "Gudalur_T",
"climate": "Warm & humid",
"code": 803784
},
{
"state": "Tamil Nadu",
"district": "Theni",
"city": "Hanumanthampatti",
"climate": "Warm & humid",
"code": 803780
},
{
"state": "Tamil Nadu",
"district": "Theni",
"city": "Highwavys",
"climate": "Warm & humid",
"code": 803785
},
{
"state": "Tamil Nadu",
"district": "Theni",
"city": "Kamayagoundanpatti",
"climate": "Warm & humid",
"code": 803782
},
{
"state": "Tamil Nadu",
"district": "Theni",
"city": "Kombai",
"climate": "Warm & humid",
"code": 803776
},
{
"state": "Tamil Nadu",
"district": "Theni",
"city": "Kuchanur",
"climate": "Warm & humid",
"code": 803773
},
{
"state": "Tamil Nadu",
"district": "Theni",
"city": "Markayankottai",
"climate": "Warm & humid",
"code": 803774
},
{
"state": "Tamil Nadu",
"district": "Theni",
"city": "Melachokkanathapuram",
"climate": "Warm & humid",
"code": 803761
},
{
"state": "Tamil Nadu",
"district": "Theni",
"city": "Odaipatti",
"climate": "Warm & humid",
"code": 803778
},
{
"state": "Tamil Nadu",
"district": "Theni",
"city": "Palani Chettipatti",
"climate": "Warm & humid",
"code": 803770
},
{
"state": "Tamil Nadu",
"district": "Theni",
"city": "Pannaipuram",
"climate": "Warm & humid",
"code": 803775
},
{
"state": "Tamil Nadu",
"district": "Theni",
"city": "Periyakulam",
"climate": "Warm & humid",
"code": 803767
},
{
"state": "Tamil Nadu",
"district": "Theni",
"city": "Thamaraikulam",
"climate": "Warm & humid",
"code": 803766
},
{
"state": "Tamil Nadu",
"district": "Theni",
"city": "Theni Alinagaram",
"climate": "Warm & humid",
"code": 803769
},
{
"state": "Tamil Nadu",
"district": "Theni",
"city": "Thenkarai_T",
"climate": "Warm & humid",
"code": 803768
},
{
"state": "Tamil Nadu",
"district": "Theni",
"city": "Thevaram",
"climate": "Warm & humid",
"code": 803772
},
{
"state": "Tamil Nadu",
"district": "Theni",
"city": "Uthamapalayam",
"climate": "Warm & humid",
"code": 803779
},
{
"state": "Tamil Nadu",
"district": "Theni",
"city": "Vadugapatti_T",
"climate": "Warm & humid",
"code": 803765
},
{
"state": "Tamil Nadu",
"district": "Theni",
"city": "Veerapandi",
"climate": "Warm & humid",
"code": 803771
},
{
"state": "Tamil Nadu",
"district": "Thirupathur",
"city": "Alangayam",
"climate": "Warm & humid",
"code": 803405
},
{
"state": "Tamil Nadu",
"district": "Thirupathur",
"city": "Ambur",
"climate": "Warm & humid",
"code": 803406
},
{
"state": "Tamil Nadu",
"district": "Thirupathur",
"city": "Jolarpet",
"climate": "Warm & humid",
"code": 803409
},
{
"state": "Tamil Nadu",
"district": "Thirupathur",
"city": "Natrampalli",
"climate": "Warm & humid",
"code": 803408
},
{
"state": "Tamil Nadu",
"district": "Thirupathur",
"city": "Tirupathur",
"climate": "Warm & humid",
"code": 803410
},
{
"state": "Tamil Nadu",
"district": "Thirupathur",
"city": "Uthayendram",
"climate": "Warm & humid",
"code": 803407
},
{
"state": "Tamil Nadu",
"district": "Thirupathur",
"city": "Vaniyambadi",
"climate": "Warm & humid",
"code": 803404
},
{
"state": "Tamil Nadu",
"district": "Thiruvallur",
"city": "Arani_Tr",
"climate": "Warm & humid",
"code": 803316
},
{
"state": "Tamil Nadu",
"district": "Thiruvallur",
"city": "Avadi",
"climate": "Warm & humid",
"code": 803323
},
{
"state": "Tamil Nadu",
"district": "Thiruvallur",
"city": "Gummidipoondi",
"climate": "Warm & humid",
"code": 803314
},
{
"state": "Tamil Nadu",
"district": "Thiruvallur",
"city": "Minjur",
"climate": "Warm & humid",
"code": 803317
},
{
"state": "Tamil Nadu",
"district": "Thiruvallur",
"city": "Naravarikuppam",
"climate": "Warm & humid",
"code": 803335
},
{
"state": "Tamil Nadu",
"district": "Thiruvallur",
"city": "Pallipet",
"climate": "Warm & humid",
"code": 803320
},
{
"state": "Tamil Nadu",
"district": "Thiruvallur",
"city": "Podhaturpet",
"climate": "Warm & humid",
"code": 803321
},
{
"state": "Tamil Nadu",
"district": "Thiruvallur",
"city": "Ponneri",
"climate": "Warm & humid",
"code": 803315
},
{
"state": "Tamil Nadu",
"district": "Thiruvallur",
"city": "Poonamallee",
"climate": "Warm & humid",
"code": 803327
},
{
"state": "Tamil Nadu",
"district": "Thiruvallur",
"city": "Thirumazhsai",
"climate": "Warm & humid",
"code": 803326
},
{
"state": "Tamil Nadu",
"district": "Thiruvallur",
"city": "Thiruninravur",
"climate": "Warm & humid",
"code": 803324
},
{
"state": "Tamil Nadu",
"district": "Thiruvallur",
"city": "Thirutani",
"climate": "Warm & humid",
"code": 803319
},
{
"state": "Tamil Nadu",
"district": "Thiruvallur",
"city": "Tiruvallur",
"climate": "Warm & humid",
"code": 803322
},
{
"state": "Tamil Nadu",
"district": "Thiruvallur",
"city": "Tiruverkadu",
"climate": "Warm & humid",
"code": 803325
},
{
"state": "Tamil Nadu",
"district": "Thiruvallur",
"city": "Uthukottai",
"climate": "Warm & humid",
"code": 803318
},
{
"state": "Tamil Nadu",
"district": "Thoothukkudi",
"city": "Alwarthirunagiri",
"climate": "Warm & humid",
"code": 803829
},
{
"state": "Tamil Nadu",
"district": "Thoothukkudi",
"city": "Arumuganeri",
"climate": "Warm & humid",
"code": 803831
},
{
"state": "Tamil Nadu",
"district": "Thoothukkudi",
"city": "Athur",
"climate": "Warm & humid",
"code": 803827
},
{
"state": "Tamil Nadu",
"district": "Thoothukkudi",
"city": "Eral",
"climate": "Warm & humid",
"code": 803825
},
{
"state": "Tamil Nadu",
"district": "Thoothukkudi",
"city": "Ettayapuram",
"climate": "Warm & humid",
"code": 803818
},
{
"state": "Tamil Nadu",
"district": "Thoothukkudi",
"city": "Kadambur",
"climate": "Warm & humid",
"code": 803816
},
{
"state": "Tamil Nadu",
"district": "Thoothukkudi",
"city": "Kalugumalai",
"climate": "Warm & humid",
"code": 803815
},
{
"state": "Tamil Nadu",
"district": "Thoothukkudi",
"city": "Kanam",
"climate": "Warm & humid",
"code": 803832
},
{
"state": "Tamil Nadu",
"district": "Thoothukkudi",
"city": "Kayalpattinam",
"climate": "Warm & humid",
"code": 803826
},
{
"state": "Tamil Nadu",
"district": "Thoothukkudi",
"city": "Kayathar",
"climate": "Warm & humid",
"code": 803817
},
{
"state": "Tamil Nadu",
"district": "Thoothukkudi",
"city": "Kovilpatti",
"climate": "Warm & humid",
"code": 803814
},
{
"state": "Tamil Nadu",
"district": "Thoothukkudi",
"city": "Nazareth",
"climate": "Warm & humid",
"code": 803830
},
{
"state": "Tamil Nadu",
"district": "Thoothukkudi",
"city": "Perungulam",
"climate": "Warm & humid",
"code": 803823
},
{
"state": "Tamil Nadu",
"district": "Thoothukkudi",
"city": "Pudur",
"climate": "Warm & humid",
"code": 803819
},
{
"state": "Tamil Nadu",
"district": "Thoothukkudi",
"city": "Sathankulam",
"climate": "Warm & humid",
"code": 803835
},
{
"state": "Tamil Nadu",
"district": "Thoothukkudi",
"city": "Sawyerpuram",
"climate": "Warm & humid",
"code": 803822
},
{
"state": "Tamil Nadu",
"district": "Thoothukkudi",
"city": "Srivaikuntam",
"climate": "Warm & humid",
"code": 803824
},
{
"state": "Tamil Nadu",
"district": "Thoothukkudi",
"city": "Thenthiruperai",
"climate": "Warm & humid",
"code": 803828
},
{
"state": "Tamil Nadu",
"district": "Thoothukkudi",
"city": "Thoothukudi Corporation",
"climate": "Warm & humid",
"code": 803821
},
{
"state": "Tamil Nadu",
"district": "Thoothukkudi",
"city": "Tiruchedur",
"climate": "Warm & humid",
"code": 803833
},
{
"state": "Tamil Nadu",
"district": "Thoothukkudi",
"city": "Udangudi",
"climate": "Warm & humid",
"code": 803834
},
{
"state": "Tamil Nadu",
"district": "Thoothukkudi",
"city": "Vilathikulam",
"climate": "Warm & humid",
"code": 803820
},
{
"state": "Tamil Nadu",
"district": "Tirunelveli",
"city": "Ambasamudram",
"climate": "Warm & humid",
"code": 803864
},
{
"state": "Tamil Nadu",
"district": "Tirunelveli",
"city": "Cheranmadevi",
"climate": "Warm & humid",
"code": 803865
},
{
"state": "Tamil Nadu",
"district": "Tirunelveli",
"city": "Eruvadi",
"climate": "Warm & humid",
"code": 803875
},
{
"state": "Tamil Nadu",
"district": "Tirunelveli",
"city": "Gopalasamudram",
"climate": "Warm & humid",
"code": 803871
},
{
"state": "Tamil Nadu",
"district": "Tirunelveli",
"city": "Kalakad",
"climate": "Warm & humid",
"code": 803873
},
{
"state": "Tamil Nadu",
"district": "Tirunelveli",
"city": "Kalladaikurichi",
"climate": "Warm & humid",
"code": 803867
},
{
"state": "Tamil Nadu",
"district": "Tirunelveli",
"city": "Manimuthar",
"climate": "Warm & humid",
"code": 803868
},
{
"state": "Tamil Nadu",
"district": "Tirunelveli",
"city": "Melasevai",
"climate": "Warm & humid",
"code": 803870
},
{
"state": "Tamil Nadu",
"district": "Tirunelveli",
"city": "Moolakaraipatti",
"climate": "Warm & humid",
"code": 803872
},
{
"state": "Tamil Nadu",
"district": "Tirunelveli",
"city": "Mukkudal",
"climate": "Warm & humid",
"code": 803862
},
{
"state": "Tamil Nadu",
"district": "Tirunelveli",
"city": "Nanguneri",
"climate": "Warm & humid",
"code": 803874
},
{
"state": "Tamil Nadu",
"district": "Tirunelveli",
"city": "Naranammalpuram",
"climate": "Warm & humid",
"code": 803859
},
{
"state": "Tamil Nadu",
"district": "Tirunelveli",
"city": "Panagudi",
"climate": "Warm & humid",
"code": 803878
},
{
"state": "Tamil Nadu",
"district": "Tirunelveli",
"city": "Pathamadai",
"climate": "Warm & humid",
"code": 803869
},
{
"state": "Tamil Nadu",
"district": "Tirunelveli",
"city": "Sankar Nagar",
"climate": "Warm & humid",
"code": 803858
},
{
"state": "Tamil Nadu",
"district": "Tirunelveli",
"city": "Sengottai",
"climate": "Warm & humid",
"code": 803855
},
{
"state": "Tamil Nadu",
"district": "Tirunelveli",
"city": "Thirukarungudi",
"climate": "Warm & humid",
"code": 803876
},
{
"state": "Tamil Nadu",
"district": "Tirunelveli",
"city": "Thisayanvilai",
"climate": "Warm & humid",
"code": 803879
},
{
"state": "Tamil Nadu",
"district": "Tirunelveli",
"city": "Tirunelveli",
"climate": "Warm & humid",
"code": 803860
},
{
"state": "Tamil Nadu",
"district": "Tirunelveli",
"city": "Vadakku Vallioor",
"climate": "Warm & humid",
"code": 803877
},
{
"state": "Tamil Nadu",
"district": "Tirunelveli",
"city": "Veeravanallur",
"climate": "Warm & humid",
"code": 803866
},
{
"state": "Tamil Nadu",
"district": "Tirunelveli",
"city": "Vikramasingapuram",
"climate": "Warm & humid",
"code": 803863
},
{
"state": "Tamil Nadu",
"district": "Tiruppur",
"city": "Avinashi",
"climate": "Warm & humid",
"code": 804021
},
{
"state": "Tamil Nadu",
"district": "Tiruppur",
"city": "Chhinnakkampalayam",
"climate": "Warm & humid",
"code": 804019
},
{
"state": "Tamil Nadu",
"district": "Tiruppur",
"city": "Dhali",
"climate": "Warm & humid",
"code": 804030
},
{
"state": "Tamil Nadu",
"district": "Tiruppur",
"city": "Dharapuram",
"climate": "Warm & humid",
"code": 804018
},
{
"state": "Tamil Nadu",
"district": "Tiruppur",
"city": "Kangayam",
"climate": "Warm & humid",
"code": 804012
},
{
"state": "Tamil Nadu",
"district": "Tiruppur",
"city": "Kaniyur",
"climate": "Warm & humid",
"code": 804031
},
{
"state": "Tamil Nadu",
"district": "Tiruppur",
"city": "Kannivadi_T",
"climate": "Warm & humid",
"code": 804015
},
{
"state": "Tamil Nadu",
"district": "Tiruppur",
"city": "Kolathupalayam",
"climate": "Warm & humid",
"code": 804017
},
{
"state": "Tamil Nadu",
"district": "Tiruppur",
"city": "Komaralingam",
"climate": "Warm & humid",
"code": 804033
},
{
"state": "Tamil Nadu",
"district": "Tiruppur",
"city": "Kunnathur",
"climate": "Warm & humid",
"code": 804020
},
{
"state": "Tamil Nadu",
"district": "Tiruppur",
"city": "Madathukulam",
"climate": "Warm & humid",
"code": 804032
},
{
"state": "Tamil Nadu",
"district": "Tiruppur",
"city": "Mulanur",
"climate": "Warm & humid",
"code": 804016
},
{
"state": "Tamil Nadu",
"district": "Tiruppur",
"city": "Muthur",
"climate": "Warm & humid",
"code": 804011
},
{
"state": "Tamil Nadu",
"district": "Tiruppur",
"city": "Palladam",
"climate": "Warm & humid",
"code": 804028
},
{
"state": "Tamil Nadu",
"district": "Tiruppur",
"city": "Rudrawathi",
"climate": "Warm & humid",
"code": 804014
},
{
"state": "Tamil Nadu",
"district": "Tiruppur",
"city": "Samalapuram",
"climate": "Warm & humid",
"code": 804027
},
{
"state": "Tamil Nadu",
"district": "Tiruppur",
"city": "Sangaramanallur",
"climate": "Warm & humid",
"code": 804034
},
{
"state": "Tamil Nadu",
"district": "Tiruppur",
"city": "Thirumuruganpoondi",
"climate": "Warm & humid",
"code": 804022
},
{
"state": "Tamil Nadu",
"district": "Tiruppur",
"city": "Tiruppur",
"climate": "Warm & humid",
"code": 804026
},
{
"state": "Tamil Nadu",
"district": "Tiruppur",
"city": "Udumalaipettai",
"climate": "Warm & humid",
"code": 804029
},
{
"state": "Tamil Nadu",
"district": "Tiruppur",
"city": "Uthukuli",
"climate": "Warm & humid",
"code": 804023
},
{
"state": "Tamil Nadu",
"district": "Tiruppur",
"city": "Vellakoil",
"climate": "Warm & humid",
"code": 804013
},
{
"state": "Tamil Nadu",
"district": "Tiruvannamalai",
"city": "Arani_Ti",
"climate": "Warm & humid",
"code": 803412
},
{
"state": "Tamil Nadu",
"district": "Tiruvannamalai",
"city": "Chengam",
"climate": "Warm & humid",
"code": 803421
},
{
"state": "Tamil Nadu",
"district": "Tiruvannamalai",
"city": "Chetpet",
"climate": "Warm & humid",
"code": 803419
},
{
"state": "Tamil Nadu",
"district": "Tiruvannamalai",
"city": "Desur",
"climate": "Warm & humid",
"code": 803416
},
{
"state": "Tamil Nadu",
"district": "Tiruvannamalai",
"city": "Kalambur",
"climate": "Warm & humid",
"code": 803417
},
{
"state": "Tamil Nadu",
"district": "Tiruvannamalai",
"city": "Kannamangalam",
"climate": "Warm & humid",
"code": 803411
},
{
"state": "Tamil Nadu",
"district": "Tiruvannamalai",
"city": "Kilpennathur",
"climate": "Warm & humid",
"code": 803423
},
{
"state": "Tamil Nadu",
"district": "Tiruvannamalai",
"city": "Pernamallur",
"climate": "Warm & humid",
"code": 803414
},
{
"state": "Tamil Nadu",
"district": "Tiruvannamalai",
"city": "Polur",
"climate": "Warm & humid",
"code": 803418
},
{
"state": "Tamil Nadu",
"district": "Tiruvannamalai",
"city": "Pudupalayam",
"climate": "Warm & humid",
"code": 803420
},
{
"state": "Tamil Nadu",
"district": "Tiruvannamalai",
"city": "Thiruvathipuram",
"climate": "Warm & humid",
"code": 803413
},
{
"state": "Tamil Nadu",
"district": "Tiruvannamalai",
"city": "Tiruvannamalai",
"climate": "Warm & humid",
"code": 803422
},
{
"state": "Tamil Nadu",
"district": "Tiruvannamalai",
"city": "Vandavasi",
"climate": "Warm & humid",
"code": 803415
},
{
"state": "Tamil Nadu",
"district": "Tiruvannamalai",
"city": "Vettavalam",
"climate": "Warm & humid",
"code": 803424
},
{
"state": "Tamil Nadu",
"district": "Tiruvarur",
"city": "Kodavasal",
"climate": "Warm & humid",
"code": 803680
},
{
"state": "Tamil Nadu",
"district": "Tiruvarur",
"city": "Koothanallur_T",
"climate": "Warm & humid",
"code": 803686
},
{
"state": "Tamil Nadu",
"district": "Tiruvarur",
"city": "Koradachery",
"climate": "Warm & humid",
"code": 803681
},
{
"state": "Tamil Nadu",
"district": "Tiruvarur",
"city": "Mannargudi",
"climate": "Warm & humid",
"code": 803687
},
{
"state": "Tamil Nadu",
"district": "Tiruvarur",
"city": "Muthupettai",
"climate": "Warm & humid",
"code": 803689
},
{
"state": "Tamil Nadu",
"district": "Tiruvarur",
"city": "Nannilam",
"climate": "Warm & humid",
"code": 803683
},
{
"state": "Tamil Nadu",
"district": "Tiruvarur",
"city": "Needamangalam",
"climate": "Warm & humid",
"code": 803685
},
{
"state": "Tamil Nadu",
"district": "Tiruvarur",
"city": "Peralam",
"climate": "Warm & humid",
"code": 803682
},
{
"state": "Tamil Nadu",
"district": "Tiruvarur",
"city": "Thiruthuraipoondi",
"climate": "Warm & humid",
"code": 803688
},
{
"state": "Tamil Nadu",
"district": "Tiruvarur",
"city": "Thiruvarur",
"climate": "Warm & humid",
"code": 803684
},
{
"state": "Tamil Nadu",
"district": "Tiruvarur",
"city": "Valangaiman",
"climate": "Warm & humid",
"code": 803679
},
{
"state": "Tamil Nadu",
"district": "Trichy",
"city": "Balakrishnanpatti",
"climate": "Warm & humid",
"code": 803622
},
{
"state": "Tamil Nadu",
"district": "Trichy",
"city": "Kallakudi",
"climate": "Warm & humid",
"code": 803626
},
{
"state": "Tamil Nadu",
"district": "Trichy",
"city": "Kattuputhur",
"climate": "Warm & humid",
"code": 803616
},
{
"state": "Tamil Nadu",
"district": "Trichy",
"city": "Koothapar",
"climate": "Warm & humid",
"code": 803632
},
{
"state": "Tamil Nadu",
"district": "Trichy",
"city": "Lalgudi",
"climate": "Warm & humid",
"code": 803629
},
{
"state": "Tamil Nadu",
"district": "Trichy",
"city": "Manaparai",
"climate": "Warm & humid",
"code": 803635
},
{
"state": "Tamil Nadu",
"district": "Trichy",
"city": "Mannachanallur",
"climate": "Warm & humid",
"code": 803625
},
{
"state": "Tamil Nadu",
"district": "Trichy",
"city": "Mettupalayam_T",
"climate": "Warm & humid",
"code": 803618
},
{
"state": "Tamil Nadu",
"district": "Trichy",
"city": "Musiri",
"climate": "Warm & humid",
"code": 803620
},
{
"state": "Tamil Nadu",
"district": "Trichy",
"city": "Ponnampatti",
"climate": "Warm & humid",
"code": 803636
},
{
"state": "Tamil Nadu",
"district": "Trichy",
"city": "Poovalur",
"climate": "Warm & humid",
"code": 803628
},
{
"state": "Tamil Nadu",
"district": "Trichy",
"city": "Pullambadi",
"climate": "Warm & humid",
"code": 803627
},
{
"state": "Tamil Nadu",
"district": "Trichy",
"city": "S.Kannanur",
"climate": "Warm & humid",
"code": 803624
},
{
"state": "Tamil Nadu",
"district": "Trichy",
"city": "Sirugamani",
"climate": "Warm & humid",
"code": 803630
},
{
"state": "Tamil Nadu",
"district": "Trichy",
"city": "Thathaiyangarpettai",
"climate": "Warm & humid",
"code": 803619
},
{
"state": "Tamil Nadu",
"district": "Trichy",
"city": "Thottiyam",
"climate": "Warm & humid",
"code": 803617
},
{
"state": "Tamil Nadu",
"district": "Trichy",
"city": "Thuraiyur",
"climate": "Warm & humid",
"code": 803623
},
{
"state": "Tamil Nadu",
"district": "Trichy",
"city": "Thuvakudi",
"climate": "Warm & humid",
"code": 803634
},
{
"state": "Tamil Nadu",
"district": "Trichy",
"city": "Tiruchirappalli",
"climate": "Warm & humid",
"code": 803631
},
{
"state": "Tamil Nadu",
"district": "Trichy",
"city": "Uppiliapuram",
"climate": "Warm & humid",
"code": 803621
},
{
"state": "Tamil Nadu",
"district": "Vellore",
"city": "Gudiyatham",
"climate": "Warm & humid",
"code": 803375
},
{
"state": "Tamil Nadu",
"district": "Vellore",
"city": "Odugathur",
"climate": "Warm & humid",
"code": 803403
},
{
"state": "Tamil Nadu",
"district": "Vellore",
"city": "Pallikonda",
"climate": "Warm & humid",
"code": 803399
},
{
"state": "Tamil Nadu",
"district": "Vellore",
"city": "Pennathur",
"climate": "Warm & humid",
"code": 803402
},
{
"state": "Tamil Nadu",
"district": "Vellore",
"city": "Pernambut",
"climate": "Warm & humid",
"code": 803376
},
{
"state": "Tamil Nadu",
"district": "Vellore",
"city": "Thiruvalam",
"climate": "Warm & humid",
"code": 803377
},
{
"state": "Tamil Nadu",
"district": "Vellore",
"city": "Vellore",
"climate": "Warm & humid",
"code": 803398
},
{
"state": "Tamil Nadu",
"district": "Viluppuram",
"city": "Ananthapuram_V",
"climate": "Warm & humid",
"code": 803426
},
{
"state": "Tamil Nadu",
"district": "Viluppuram",
"city": "Arakandanallur",
"climate": "Warm & humid",
"code": 803434
},
{
"state": "Tamil Nadu",
"district": "Viluppuram",
"city": "Gingee",
"climate": "Warm & humid",
"code": 803425
},
{
"state": "Tamil Nadu",
"district": "Viluppuram",
"city": "Kottakuppam",
"climate": "Warm & humid",
"code": 803429
},
{
"state": "Tamil Nadu",
"district": "Viluppuram",
"city": "Marakkanam",
"climate": "Warm & humid",
"code": 803428
},
{
"state": "Tamil Nadu",
"district": "Viluppuram",
"city": "Thiruvennainallur",
"climate": "Warm & humid",
"code": 803436
},
{
"state": "Tamil Nadu",
"district": "Viluppuram",
"city": "Tindivanam",
"climate": "Warm & humid",
"code": 803427
},
{
"state": "Tamil Nadu",
"district": "Viluppuram",
"city": "Valavanur",
"climate": "Warm & humid",
"code": 803432
},
{
"state": "Tamil Nadu",
"district": "Viluppuram",
"city": "Vikkiravandi",
"climate": "Warm & humid",
"code": 803430
},
{
"state": "Tamil Nadu",
"district": "Viluppuram",
"city": "Villupuram",
"climate": "Warm & humid",
"code": 803431
},
{
"state": "Tamil Nadu",
"district": "Virudhunagar",
"city": "Aruppukottai",
"climate": "Warm & humid",
"code": 803801
},
{
"state": "Tamil Nadu",
"district": "Virudhunagar",
"city": "Chettiarpatti",
"climate": "Warm & humid",
"code": 803789
},
{
"state": "Tamil Nadu",
"district": "Virudhunagar",
"city": "Kariapatti",
"climate": "Warm & humid",
"code": 803799
},
{
"state": "Tamil Nadu",
"district": "Virudhunagar",
"city": "Mallanginaru",
"climate": "Warm & humid",
"code": 900028
},
{
"state": "Tamil Nadu",
"district": "Virudhunagar",
"city": "Mamspuram",
"climate": "Warm & humid",
"code": 803795
},
{
"state": "Tamil Nadu",
"district": "Virudhunagar",
"city": "Rajapalayam",
"climate": "Warm & humid",
"code": 803787
},
{
"state": "Tamil Nadu",
"district": "Virudhunagar",
"city": "S.Kodikulam",
"climate": "Warm & humid",
"code": 803790
},
{
"state": "Tamil Nadu",
"district": "Virudhunagar",
"city": "Sattur",
"climate": "Warm & humid",
"code": 803802
},
{
"state": "Tamil Nadu",
"district": "Virudhunagar",
"city": "Seithur",
"climate": "Warm & humid",
"code": 803788
},
{
"state": "Tamil Nadu",
"district": "Virudhunagar",
"city": "Sivakasi",
"climate": "Warm & humid",
"code": 803797
},
{
"state": "Tamil Nadu",
"district": "Virudhunagar",
"city": "Srivilliputhur",
"climate": "Warm & humid",
"code": 803794
},
{
"state": "Tamil Nadu",
"district": "Virudhunagar",
"city": "Sundarapandiyam",
"climate": "Warm & humid",
"code": 803793
},
{
"state": "Tamil Nadu",
"district": "Virudhunagar",
"city": "Virudhunagar",
"climate": "Warm & humid",
"code": 803798
},
{
"state": "Tamil Nadu",
"district": "Virudhunagar",
"city": "W.Pudupatti",
"climate": "Warm & humid",
"code": 803792
},
{
"state": "Tamil Nadu",
"district": "Virudhunagar",
"city": "Watrap",
"climate": "Warm & humid",
"code": 900029
},
{
"state": "Telangana",
"district": "Adilabad",
"city": "Adilabad",
"climate": "Warm & humid",
"code": 802896
},
{
"state": "Telangana",
"district": "Bhadradri Kothagudem",
"city": "Kothagudem",
"climate": "Warm & humid",
"code": 802934
},
{
"state": "Telangana",
"district": "Bhadradri Kothagudem",
"city": "Manuguru",
"climate": "Warm & humid",
"code": 802932
},
{
"state": "Telangana",
"district": "Bhadradri Kothagudem",
"city": "Palwancha",
"climate": "Warm & humid",
"code": 802933
},
{
"state": "Telangana",
"district": "Bhadradri Kothagudem",
"city": "Yellandu",
"climate": "Warm & humid",
"code": 802935
},
{
"state": "Telangana",
"district": "Hanumakonda",
"city": "Parkala",
"climate": "Warm & humid",
"code": 900023
},
{
"state": "Telangana",
"district": "Hanumakonda",
"city": "Warangal",
"climate": "Warm & humid",
"code": 802930
},
{
"state": "Telangana",
"district": "Hyderabad",
"city": "Greater Hyderabad",
"climate": "Composite",
"code": 802918
},
{
"state": "Telangana",
"district": "Hyderabad",
"city": "Secunderabad Cantonment",
"climate": "Composite",
"code": 802919
},
{
"state": "Telangana",
"district": "Jagitial",
"city": "Dharmapuri",
"climate": "Composite",
"code": 900533
},
{
"state": "Telangana",
"district": "Jagitial",
"city": "Jagitial",
"climate": "Composite",
"code": 802908
},
{
"state": "Telangana",
"district": "Jagitial",
"city": "Korutla",
"climate": "Composite",
"code": 802909
},
{
"state": "Telangana",
"district": "Jagitial",
"city": "Metpally",
"climate": "Composite",
"code": 802910
},
{
"state": "Telangana",
"district": "Jagitial",
"city": "Raikal",
"climate": "Composite",
"code": 900565
},
{
"state": "Telangana",
"district": "Jangaon",
"city": "Jangaon",
"climate": "Composite",
"code": 802931
},
{
"state": "Telangana",
"district": "Jayashanker Bhupapally",
"city": "Bhupalpally",
"climate": "Warm & humid",
"code": 900020
},
{
"state": "Telangana",
"district": "Jogulamba Gadwal",
"city": "Alampur",
"climate": "Composite",
"code": 900516
},
{
"state": "Telangana",
"district": "Jogulamba Gadwal",
"city": "Gadwal",
"climate": "Composite",
"code": 802925
},
{
"state": "Telangana",
"district": "Jogulamba Gadwal",
"city": "Ieeja",
"climate": "Composite",
"code": 900039
},
{
"state": "Telangana",
"district": "Jogulamba Gadwal",
"city": "Waddepalle",
"climate": "Composite",
"code": 900577
},
{
"state": "Telangana",
"district": "Kamareddy",
"city": "Banswada",
"climate": "Composite",
"code": 900522
},
{
"state": "Telangana",
"district": "Kamareddy",
"city": "Kamareddy",
"climate": "Composite",
"code": 802906
},
{
"state": "Telangana",
"district": "Kamareddy",
"city": "Yellareddy",
"climate": "Composite",
"code": 900581
},
{
"state": "Telangana",
"district": "Karimnagar",
"city": "Choppandandi",
"climate": "Composite",
"code": 900530
},
{
"state": "Telangana",
"district": "Karimnagar",
"city": "Huzurabad",
"climate": "Composite",
"code": 900015
},
{
"state": "Telangana",
"district": "Karimnagar",
"city": "Jammikunta",
"climate": "Composite",
"code": 900016
},
{
"state": "Telangana",
"district": "Karimnagar",
"city": "Karimnagar",
"climate": "Composite",
"code": 802911
},
{
"state": "Telangana",
"district": "Karimnagar",
"city": "Kothapally",
"climate": "Composite",
"code": 900545
},
{
"state": "Telangana",
"district": "Khammam",
"city": "Khammam",
"climate": "Warm & humid",
"code": 802937
},
{
"state": "Telangana",
"district": "Khammam",
"city": "Madhira",
"climate": "Warm & humid",
"code": 900019
},
{
"state": "Telangana",
"district": "Khammam",
"city": "Sathupally",
"climate": "Warm & humid",
"code": 802936
},
{
"state": "Telangana",
"district": "Khammam",
"city": "Wyra",
"climate": "Warm & humid",
"code": 900579
},
{
"state": "Telangana",
"district": "Komaram Bheem Asifabad",
"city": "Khagaznagar",
"climate": "Warm & humid",
"code": 802897
},
{
"state": "Telangana",
"district": "Mahabubabad",
"city": "Dornakal",
"climate": "Composite",
"code": 900534
},
{
"state": "Telangana",
"district": "Mahabubabad",
"city": "Mahaboobabad",
"climate": "Composite",
"code": 900021
},
{
"state": "Telangana",
"district": "Mahabubabad",
"city": "Maripeda",
"climate": "Composite",
"code": 900551
},
{
"state": "Telangana",
"district": "Mahabubabad",
"city": "Thorrur",
"climate": "Composite",
"code": 900572
},
{
"state": "Telangana",
"district": "Mahabubnagar",
"city": "Bhoothpur",
"climate": "Composite",
"code": 900524
},
{
"state": "Telangana",
"district": "Mahabubnagar",
"city": "Jadcherla",
"climate": "Composite",
"code": 900147
},
{
"state": "Telangana",
"district": "Mahabubnagar",
"city": "Mahaboobnagar",
"climate": "Composite",
"code": 802922
},
{
"state": "Telangana",
"district": "Mancherial",
"city": "Bellampally",
"climate": "Warm & humid",
"code": 802900
},
{
"state": "Telangana",
"district": "Mancherial",
"city": "Chennur",
"climate": "Warm & humid",
"code": 900527
},
{
"state": "Telangana",
"district": "Mancherial",
"city": "Kyathanpally",
"climate": "Warm & humid",
"code": 900546
},
{
"state": "Telangana",
"district": "Mancherial",
"city": "Luxettipet",
"climate": "Warm & humid",
"code": 900547
},
{
"state": "Telangana",
"district": "Mancherial",
"city": "Mancherial",
"climate": "Warm & humid",
"code": 802902
},
{
"state": "Telangana",
"district": "Mancherial",
"city": "Mandamarri",
"climate": "Warm & humid",
"code": 802901
},
{
"state": "Telangana",
"district": "Mancherial",
"city": "Naspur",
"climate": "Warm & humid",
"code": 900558
},
{
"state": "Telangana",
"district": "Medak",
"city": "Medak",
"climate": "Composite",
"code": 802913
},
{
"state": "Telangana",
"district": "Medak",
"city": "Narsapur",
"climate": "Composite",
"code": 900556
},
{
"state": "Telangana",
"district": "Medak",
"city": "Ramayampet",
"climate": "Composite",
"code": 900566
},
{
"state": "Telangana",
"district": "Medak",
"city": "Toopran",
"climate": "Composite",
"code": 900571
},
{
"state": "Telangana",
"district": "Medchal-Malkajgiri",
"city": "Bod Uppal",
"climate": "Composite",
"code": 900475
},
{
"state": "Telangana",
"district": "Medchal-Malkajgiri",
"city": "Dammaiguda",
"climate": "Composite",
"code": 900532
},
{
"state": "Telangana",
"district": "Medchal-Malkajgiri",
"city": "Dundigal",
"climate": "Composite",
"code": 900535
},
{
"state": "Telangana",
"district": "Medchal-Malkajgiri",
"city": "Ghatkesar",
"climate": "Composite",
"code": 900536
},
{
"state": "Telangana",
"district": "Medchal-Malkajgiri",
"city": "Gundlapochampally",
"climate": "Composite",
"code": 900537
},
{
"state": "Telangana",
"district": "Medchal-Malkajgiri",
"city": "Jawahar Nagar",
"climate": "Composite",
"code": 900539
},
{
"state": "Telangana",
"district": "Medchal-Malkajgiri",
"city": "Kompally",
"climate": "Composite",
"code": 900542
},
{
"state": "Telangana",
"district": "Medchal-Malkajgiri",
"city": "Medchal",
"climate": "Composite",
"code": 900012
},
{
"state": "Telangana",
"district": "Medchal-Malkajgiri",
"city": "Nagaram",
"climate": "Composite",
"code": 900553
},
{
"state": "Telangana",
"district": "Medchal-Malkajgiri",
"city": "Nizampet",
"climate": "Composite",
"code": 900560
},
{
"state": "Telangana",
"district": "Medchal-Malkajgiri",
"city": "Peerzadiguda",
"climate": "Composite",
"code": 900476
},
{
"state": "Telangana",
"district": "Medchal-Malkajgiri",
"city": "Pocharam",
"climate": "Composite",
"code": 900564
},
{
"state": "Telangana",
"district": "Medchal-Malkajgiri",
"city": "Thumkunta",
"climate": "Composite",
"code": 900574
},
{
"state": "Telangana",
"district": "Nagarkurnool",
"city": "Achampet",
"climate": "Composite",
"code": 900106
},
{
"state": "Telangana",
"district": "Nagarkurnool",
"city": "Kalwakurthy",
"climate": "Composite",
"code": 900040
},
{
"state": "Telangana",
"district": "Nagarkurnool",
"city": "Kollapur",
"climate": "Composite",
"code": 900103
},
{
"state": "Telangana",
"district": "Nagarkurnool",
"city": "Nagarkurnool",
"climate": "Composite",
"code": 900041
},
{
"state": "Telangana",
"district": "Nalgonda",
"city": "Chandur",
"climate": "Composite",
"code": 900526
},
{
"state": "Telangana",
"district": "Nalgonda",
"city": "Chityal",
"climate": "Composite",
"code": 900529
},
{
"state": "Telangana",
"district": "Nalgonda",
"city": "Devarakonda",
"climate": "Composite",
"code": 900067
},
{
"state": "Telangana",
"district": "Nalgonda",
"city": "Haliya",
"climate": "Composite",
"code": 900538
},
{
"state": "Telangana",
"district": "Nalgonda",
"city": "Miryalguda",
"climate": "Composite",
"code": 802929
},
{
"state": "Telangana",
"district": "Nalgonda",
"city": "Nakrekal",
"climate": "Composite",
"code": 900732
},
{
"state": "Telangana",
"district": "Nalgonda",
"city": "Nalgonda",
"climate": "Composite",
"code": 802928
},
{
"state": "Telangana",
"district": "Nalgonda",
"city": "Nandikonda",
"climate": "Composite",
"code": 900554
},
{
"state": "Telangana",
"district": "Narayanpet",
"city": "Kosgi",
"climate": "Composite",
"code": 900543
},
{
"state": "Telangana",
"district": "Narayanpet",
"city": "Makthal",
"climate": "Composite",
"code": 900548
},
{
"state": "Telangana",
"district": "Narayanpet",
"city": "Narayanpet",
"climate": "Composite",
"code": 802923
},
{
"state": "Telangana",
"district": "Nirmal",
"city": "Bhainsa",
"climate": "Composite",
"code": 802898
},
{
"state": "Telangana",
"district": "Nirmal",
"city": "Khanapur",
"climate": "Composite",
"code": 900540
},
{
"state": "Telangana",
"district": "Nirmal",
"city": "Nirmal",
"climate": "Composite",
"code": 802899
},
{
"state": "Telangana",
"district": "Nizamabad",
"city": "Armoor",
"climate": "Composite",
"code": 802903
},
{
"state": "Telangana",
"district": "Nizamabad",
"city": "Bheemgal",
"climate": "Composite",
"code": 900523
},
{
"state": "Telangana",
"district": "Nizamabad",
"city": "Bodhan",
"climate": "Composite",
"code": 802905
},
{
"state": "Telangana",
"district": "Nizamabad",
"city": "Nizamabad",
"climate": "Composite",
"code": 802904
},
{
"state": "Telangana",
"district": "Peddapally",
"city": "Manthani",
"climate": "Composite",
"code": 900550
},
{
"state": "Telangana",
"district": "Peddapally",
"city": "Peddapalli",
"climate": "Composite",
"code": 900017
},
{
"state": "Telangana",
"district": "Peddapally",
"city": "Ramagundam",
"climate": "Composite",
"code": 802907
},
{
"state": "Telangana",
"district": "Peddapally",
"city": "Sultanabad",
"climate": "Composite",
"code": 900569
},
{
"state": "Telangana",
"district": "Rajanna Sircilla",
"city": "Sircilla",
"climate": "Composite",
"code": 802912
},
{
"state": "Telangana",
"district": "Rajanna Sircilla",
"city": "Vemulawada",
"climate": "Composite",
"code": 900018
},
{
"state": "Telangana",
"district": "Ranga Reddy",
"city": "Adibatla",
"climate": "Composite",
"code": 900514
},
{
"state": "Telangana",
"district": "Ranga Reddy",
"city": "Amangal",
"climate": "Composite",
"code": 900517
},
{
"state": "Telangana",
"district": "Ranga Reddy",
"city": "Badangpet",
"climate": "Composite",
"code": 900070
},
{
"state": "Telangana",
"district": "Ranga Reddy",
"city": "Badlaguda Jagir",
"climate": "Composite",
"code": 900521
},
{
"state": "Telangana",
"district": "Ranga Reddy",
"city": "Ibrahimpatnam",
"climate": "Composite",
"code": 900071
},
{
"state": "Telangana",
"district": "Ranga Reddy",
"city": "Jallpally",
"climate": "Composite",
"code": 900477
},
{
"state": "Telangana",
"district": "Ranga Reddy",
"city": "Kothur",
"climate": "Composite",
"code": 900733
},
{
"state": "Telangana",
"district": "Ranga Reddy",
"city": "Manikonda",
"climate": "Composite",
"code": 900549
},
{
"state": "Telangana",
"district": "Ranga Reddy",
"city": "Meerpet",
"climate": "Composite",
"code": 900479
},
{
"state": "Telangana",
"district": "Ranga Reddy",
"city": "Narsingi",
"climate": "Composite",
"code": 900557
},
{
"state": "Telangana",
"district": "Ranga Reddy",
"city": "Pedda Amberpet",
"climate": "Composite",
"code": 900072
},
{
"state": "Telangana",
"district": "Ranga Reddy",
"city": "Shadnagar",
"climate": "Composite",
"code": 900042
},
{
"state": "Telangana",
"district": "Ranga Reddy",
"city": "Shamshabad",
"climate": "Composite",
"code": 900567
},
{
"state": "Telangana",
"district": "Ranga Reddy",
"city": "Shankarpally",
"climate": "Composite",
"code": 900568
},
{
"state": "Telangana",
"district": "Ranga Reddy",
"city": "Thukkuguda",
"climate": "Composite",
"code": 900573
},
{
"state": "Telangana",
"district": "Ranga Reddy",
"city": "Turkayamjal",
"climate": "Composite",
"code": 900576
},
{
"state": "Telangana",
"district": "Sangareddy",
"city": "Ameenpur",
"climate": "Composite",
"code": 900519
},
{
"state": "Telangana",
"district": "Sangareddy",
"city": "Andole-Jogipet",
"climate": "Composite",
"code": 900065
},
{
"state": "Telangana",
"district": "Sangareddy",
"city": "Bollaram",
"climate": "Composite",
"code": 900525
},
{
"state": "Telangana",
"district": "Sangareddy",
"city": "Narayankhed",
"climate": "Composite",
"code": 900555
},
{
"state": "Telangana",
"district": "Sangareddy",
"city": "Sadasivpet",
"climate": "Composite",
"code": 802916
},
{
"state": "Telangana",
"district": "Sangareddy",
"city": "Sangareddy",
"climate": "Composite",
"code": 802917
},
{
"state": "Telangana",
"district": "Sangareddy",
"city": "Tellapur",
"climate": "Composite",
"code": 900570
},
{
"state": "Telangana",
"district": "Sangareddy",
"city": "Zaheerabad",
"climate": "Composite",
"code": 802915
},
{
"state": "Telangana",
"district": "Siddipet",
"city": "Cherial",
"climate": "Composite",
"code": 900528
},
{
"state": "Telangana",
"district": "Siddipet",
"city": "Dubbaka",
"climate": "Composite",
"code": 900086
},
{
"state": "Telangana",
"district": "Siddipet",
"city": "Gajwel",
"climate": "Composite",
"code": 900066
},
{
"state": "Telangana",
"district": "Siddipet",
"city": "Husnabad",
"climate": "Composite",
"code": 900014
},
{
"state": "Telangana",
"district": "Siddipet",
"city": "Siddipet",
"climate": "Composite",
"code": 802914
},
{
"state": "Telangana",
"district": "Suryapet",
"city": "Huzurnagar",
"climate": "Composite",
"code": 900068
},
{
"state": "Telangana",
"district": "Suryapet",
"city": "Kodada",
"climate": "Composite",
"code": 900069
},
{
"state": "Telangana",
"district": "Suryapet",
"city": "Neredcherla",
"climate": "Composite",
"code": 900559
},
{
"state": "Telangana",
"district": "Suryapet",
"city": "Suryapet",
"climate": "Composite",
"code": 802927
},
{
"state": "Telangana",
"district": "Suryapet",
"city": "Tirumalagiri",
"climate": "Composite",
"code": 900575
},
{
"state": "Telangana",
"district": "Vikarabad",
"city": "Kodangal",
"climate": "Composite",
"code": 900541
},
{
"state": "Telangana",
"district": "Vikarabad",
"city": "Parigi",
"climate": "Composite",
"code": 900561
},
{
"state": "Telangana",
"district": "Vikarabad",
"city": "Tandur",
"climate": "Composite",
"code": 802921
},
{
"state": "Telangana",
"district": "Vikarabad",
"city": "Vikarabad",
"climate": "Composite",
"code": 802920
},
{
"state": "Telangana",
"district": "Wanaparthy",
"city": "Amarchinta",
"climate": "Composite",
"code": 900518
},
{
"state": "Telangana",
"district": "Wanaparthy",
"city": "Atmakur",
"climate": "Composite",
"code": 900520
},
{
"state": "Telangana",
"district": "Wanaparthy",
"city": "Kothakota",
"climate": "Composite",
"code": 900544
},
{
"state": "Telangana",
"district": "Wanaparthy",
"city": "Pebbair",
"climate": "Composite",
"code": 900562
},
{
"state": "Telangana",
"district": "Wanaparthy",
"city": "Wanaparthy",
"climate": "Composite",
"code": 802924
},
{
"state": "Telangana",
"district": "Warangal",
"city": "Narsampet",
"climate": "Composite",
"code": 900022
},
{
"state": "Telangana",
"district": "Warangal",
"city": "Wardhannapet",
"climate": "Composite",
"code": 900578
},
{
"state": "Telangana",
"district": "Yadadri Bhuvanagiri",
"city": "Alair",
"climate": "Composite",
"code": 900515
},
{
"state": "Telangana",
"district": "Yadadri Bhuvanagiri",
"city": "Bhongir",
"climate": "Composite",
"code": 802926
},
{
"state": "Telangana",
"district": "Yadadri Bhuvanagiri",
"city": "Choutuppal",
"climate": "Composite",
"code": 900531
},
{
"state": "Telangana",
"district": "Yadadri Bhuvanagiri",
"city": "Mothkur",
"climate": "Composite",
"code": 900552
},
{
"state": "Telangana",
"district": "Yadadri Bhuvanagiri",
"city": "Pochampally",
"climate": "Composite",
"code": 900563
},
{
"state": "Telangana",
"district": "Yadadri Bhuvanagiri",
"city": "Yadagirigutta",
"climate": "Composite",
"code": 900580
},
{
"state": "Tripura",
"district": "Dhalai",
"city": "Ambassa",
"climate": "Warm & humid",
"code": 801532
},
{
"state": "Tripura",
"district": "Dhalai",
"city": "Kamalpur",
"climate": "Warm & humid",
"code": 801531
},
{
"state": "Tripura",
"district": "Gomati",
"city": "Amarpur",
"climate": "Warm & humid",
"code": 801527
},
{
"state": "Tripura",
"district": "Gomati",
"city": "Udaipur",
"climate": "Warm & humid",
"code": 801526
},
{
"state": "Tripura",
"district": "Khowai",
"city": "Khowai",
"climate": "Warm & humid",
"code": 801520
},
{
"state": "Tripura",
"district": "Khowai",
"city": "Teliamura",
"climate": "Warm & humid",
"code": 801521
},
{
"state": "Tripura",
"district": "North Tripura",
"city": "Dharmanagar",
"climate": "Warm & humid",
"code": 801534
},
{
"state": "Tripura",
"district": "North Tripura",
"city": "Panisagar",
"climate": "Warm & humid",
"code": 900005
},
{
"state": "Tripura",
"district": "Sipahijala",
"city": "Bishalgarh",
"climate": "Warm & humid",
"code": 801524
},
{
"state": "Tripura",
"district": "Sipahijala",
"city": "Melagarh",
"climate": "Warm & humid",
"code": 900003
},
{
"state": "Tripura",
"district": "Sipahijala",
"city": "Sonamura",
"climate": "Warm & humid",
"code": 801525
},
{
"state": "Tripura",
"district": "South Tripura",
"city": "Belonia",
"climate": "Warm & humid",
"code": 801529
},
{
"state": "Tripura",
"district": "South Tripura",
"city": "Sabroom",
"climate": "Warm & humid",
"code": 801530
},
{
"state": "Tripura",
"district": "South Tripura",
"city": "Santir Bazar",
"climate": "Warm & humid",
"code": 801528
},
{
"state": "Tripura",
"district": "Unakoti",
"city": "Kailasahar",
"climate": "Warm & humid",
"code": 801533
},
{
"state": "Tripura",
"district": "Unakoti",
"city": "Kumarghat",
"climate": "Warm & humid",
"code": 801535
},
{
"state": "Tripura",
"district": "West Tripura",
"city": "Agartala",
"climate": "Warm & humid",
"code": 801523
},
{
"state": "Tripura",
"district": "West Tripura",
"city": "Jiraniya",
"climate": "Warm & humid",
"code": 900002
},
{
"state": "Tripura",
"district": "West Tripura",
"city": "Mohanpur",
"climate": "Warm & humid",
"code": 900004
},
{
"state": "Tripura",
"district": "West Tripura",
"city": "Ranirbazar",
"climate": "Warm & humid",
"code": 801522
},
{
"state": "Uttar Pradesh",
"district": "Agra",
"city": "Achhnera",
"climate": "Composite",
"code": 800806
},
{
"state": "Uttar Pradesh",
"district": "Agra",
"city": "Agra",
"climate": "Composite",
"code": 800804
},
{
"state": "Uttar Pradesh",
"district": "Agra",
"city": "Agra Cantonment",
"climate": "Composite",
"code": 800805
},
{
"state": "Uttar Pradesh",
"district": "Agra",
"city": "Bah",
"climate": "Composite",
"code": 800814
},
{
"state": "Uttar Pradesh",
"district": "Agra",
"city": "Dayalbagh",
"climate": "Composite",
"code": 800802
},
{
"state": "Uttar Pradesh",
"district": "Agra",
"city": "Etmadpur",
"climate": "Composite",
"code": 800801
},
{
"state": "Uttar Pradesh",
"district": "Agra",
"city": "Fatehabad",
"climate": "Composite",
"code": 800812
},
{
"state": "Uttar Pradesh",
"district": "Agra",
"city": "Fatehpur Sikri",
"climate": "Composite",
"code": 800808
},
{
"state": "Uttar Pradesh",
"district": "Agra",
"city": "Jagner",
"climate": "Composite",
"code": 800809
},
{
"state": "Uttar Pradesh",
"district": "Agra",
"city": "Kheragarh",
"climate": "Composite",
"code": 800810
},
{
"state": "Uttar Pradesh",
"district": "Agra",
"city": "Kiraoali",
"climate": "Composite",
"code": 800807
},
{
"state": "Uttar Pradesh",
"district": "Agra",
"city": "Pinahat",
"climate": "Composite",
"code": 800813
},
{
"state": "Uttar Pradesh",
"district": "Agra",
"city": "Shamsabad",
"climate": "Composite",
"code": 800811
},
{
"state": "Uttar Pradesh",
"district": "Agra",
"city": "Swamibagh",
"climate": "Composite",
"code": 800803
},
{
"state": "Uttar Pradesh",
"district": "Aligarh",
"city": "Aligarh",
"climate": "Composite",
"code": 800768
},
{
"state": "Uttar Pradesh",
"district": "Aligarh",
"city": "Atrauli",
"climate": "Composite",
"code": 800765
},
{
"state": "Uttar Pradesh",
"district": "Aligarh",
"city": "Barauli",
"climate": "Composite",
"code": 900737
},
{
"state": "Uttar Pradesh",
"district": "Aligarh",
"city": "Beswan",
"climate": "Composite",
"code": 800774
},
{
"state": "Uttar Pradesh",
"district": "Aligarh",
"city": "Chandaus",
"climate": "Composite",
"code": 900613
},
{
"state": "Uttar Pradesh",
"district": "Aligarh",
"city": "Chharra Rafatpur",
"climate": "Composite",
"code": 800766
},
{
"state": "Uttar Pradesh",
"district": "Aligarh",
"city": "Gabhana",
"climate": "Composite",
"code": 900736
},
{
"state": "Uttar Pradesh",
"district": "Aligarh",
"city": "Harduaganj",
"climate": "Composite",
"code": 800767
},
{
"state": "Uttar Pradesh",
"district": "Aligarh",
"city": "Iglas",
"climate": "Composite",
"code": 800773
},
{
"state": "Uttar Pradesh",
"district": "Aligarh",
"city": "Jalali",
"climate": "Composite",
"code": 800769
},
{
"state": "Uttar Pradesh",
"district": "Aligarh",
"city": "Jatari",
"climate": "Composite",
"code": 800763
},
{
"state": "Uttar Pradesh",
"district": "Aligarh",
"city": "Jawan Sikandarpur",
"climate": "Composite",
"code": 900735
},
{
"state": "Uttar Pradesh",
"district": "Aligarh",
"city": "Kauriaganj",
"climate": "Composite",
"code": 800770
},
{
"state": "Uttar Pradesh",
"district": "Aligarh",
"city": "Khair",
"climate": "Composite",
"code": 800764
},
{
"state": "Uttar Pradesh",
"district": "Aligarh",
"city": "Madrak",
"climate": "Composite",
"code": 900615
},
{
"state": "Uttar Pradesh",
"district": "Aligarh",
"city": "Pilkhana",
"climate": "Composite",
"code": 800771
},
{
"state": "Uttar Pradesh",
"district": "Aligarh",
"city": "Pisawa",
"climate": "Composite",
"code": 900614
},
{
"state": "Uttar Pradesh",
"district": "Aligarh",
"city": "Tappal",
"climate": "Composite",
"code": 900734
},
{
"state": "Uttar Pradesh",
"district": "Aligarh",
"city": "Vijaigarh",
"climate": "Composite",
"code": 800772
},
{
"state": "Uttar Pradesh",
"district": "Ambedkar Nagar",
"city": "Akbarpur",
"climate": "Composite",
"code": 801116
},
{
"state": "Uttar Pradesh",
"district": "Ambedkar Nagar",
"city": "Ashrafpur Kichhauchha",
"climate": "Composite",
"code": 801114
},
{
"state": "Uttar Pradesh",
"district": "Ambedkar Nagar",
"city": "Iltifatganj Bazar",
"climate": "Composite",
"code": 801112
},
{
"state": "Uttar Pradesh",
"district": "Ambedkar Nagar",
"city": "Jahangirganj",
"climate": "Composite",
"code": 900738
},
{
"state": "Uttar Pradesh",
"district": "Ambedkar Nagar",
"city": "Jalalpur",
"climate": "Composite",
"code": 801115
},
{
"state": "Uttar Pradesh",
"district": "Ambedkar Nagar",
"city": "Rajesultanpur",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Ambedkar Nagar",
"city": "Tanda_An",
"climate": "Composite",
"code": 801113
},
{
"state": "Uttar Pradesh",
"district": "Amethi",
"city": "Amethi_A",
"climate": "Composite",
"code": 801118
},
{
"state": "Uttar Pradesh",
"district": "Amethi",
"city": "Gauriganj",
"climate": "Composite",
"code": 900145
},
{
"state": "Uttar Pradesh",
"district": "Amethi",
"city": "Jais",
"climate": "Composite",
"code": 800958
},
{
"state": "Uttar Pradesh",
"district": "Amethi",
"city": "Musafirkhana",
"climate": "Composite",
"code": 801117
},
{
"state": "Uttar Pradesh",
"district": "Amroha",
"city": "Amroha",
"climate": "Composite",
"code": 800702
},
{
"state": "Uttar Pradesh",
"district": "Amroha",
"city": "Bachhraon",
"climate": "Composite",
"code": 800699
},
{
"state": "Uttar Pradesh",
"district": "Amroha",
"city": "Dhanaura",
"climate": "Composite",
"code": 800698
},
{
"state": "Uttar Pradesh",
"district": "Amroha",
"city": "Gajraula",
"climate": "Composite",
"code": 800700
},
{
"state": "Uttar Pradesh",
"district": "Amroha",
"city": "Hasanpur",
"climate": "Composite",
"code": 800704
},
{
"state": "Uttar Pradesh",
"district": "Amroha",
"city": "Joya",
"climate": "Composite",
"code": 800703
},
{
"state": "Uttar Pradesh",
"district": "Amroha",
"city": "Naugawan Sadat",
"climate": "Composite",
"code": 800701
},
{
"state": "Uttar Pradesh",
"district": "Amroha",
"city": "Saidnagli",
"climate": "Composite",
"code": 900739
},
{
"state": "Uttar Pradesh",
"district": "Amroha",
"city": "Ujhari",
"climate": "Composite",
"code": 800705
},
{
"state": "Uttar Pradesh",
"district": "Auraiya",
"city": "Achhalda",
"climate": "Composite",
"code": 800987
},
{
"state": "Uttar Pradesh",
"district": "Auraiya",
"city": "Atasu",
"climate": "Composite",
"code": 800989
},
{
"state": "Uttar Pradesh",
"district": "Auraiya",
"city": "Auraiya",
"climate": "Composite",
"code": 800992
},
{
"state": "Uttar Pradesh",
"district": "Auraiya",
"city": "Babarpur Ajitmal",
"climate": "Composite",
"code": 800988
},
{
"state": "Uttar Pradesh",
"district": "Auraiya",
"city": "Bidhuna",
"climate": "Composite",
"code": 800986
},
{
"state": "Uttar Pradesh",
"district": "Auraiya",
"city": "Dibiyapur",
"climate": "Composite",
"code": 800991
},
{
"state": "Uttar Pradesh",
"district": "Auraiya",
"city": "Phaphund",
"climate": "Composite",
"code": 800990
},
{
"state": "Uttar Pradesh",
"district": "Ayodhya",
"city": "Ayodhya",
"climate": "Composite",
"code": 801109
},
{
"state": "Uttar Pradesh",
"district": "Ayodhya",
"city": "Bhadarsa",
"climate": "Composite",
"code": 801106
},
{
"state": "Uttar Pradesh",
"district": "Ayodhya",
"city": "Bikapur",
"climate": "Composite",
"code": 801111
},
{
"state": "Uttar Pradesh",
"district": "Ayodhya",
"city": "Faizabad Cantonment",
"climate": "Composite",
"code": 801107
},
{
"state": "Uttar Pradesh",
"district": "Ayodhya",
"city": "Gosainganj_A",
"climate": "Composite",
"code": 801110
},
{
"state": "Uttar Pradesh",
"district": "Ayodhya",
"city": "Khirauni",
"climate": "Composite",
"code": 900741
},
{
"state": "Uttar Pradesh",
"district": "Ayodhya",
"city": "Kumarganj",
"climate": "Composite",
"code": 900740
},
{
"state": "Uttar Pradesh",
"district": "Ayodhya",
"city": "Maa Kamakhya",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Ayodhya",
"city": "Rudauli",
"climate": "Composite",
"code": 801105
},
{
"state": "Uttar Pradesh",
"district": "Ayodhya",
"city": "Suchittaganj",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Ayodhya",
"city": "Tarkulwa",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Azamgarh",
"city": "Atrauliya",
"climate": "Composite",
"code": 801183
},
{
"state": "Uttar Pradesh",
"district": "Azamgarh",
"city": "Azamgarh",
"climate": "Composite",
"code": 801189
},
{
"state": "Uttar Pradesh",
"district": "Azamgarh",
"city": "Azmatgarh",
"climate": "Composite",
"code": 801187
},
{
"state": "Uttar Pradesh",
"district": "Azamgarh",
"city": "Bilariaganj",
"climate": "Composite",
"code": 801185
},
{
"state": "Uttar Pradesh",
"district": "Azamgarh",
"city": "Budhanpur",
"climate": "Composite",
"code": 900616
},
{
"state": "Uttar Pradesh",
"district": "Azamgarh",
"city": "Jahanaganj",
"climate": "Composite",
"code": 900617
},
{
"state": "Uttar Pradesh",
"district": "Azamgarh",
"city": "Jiyanpur",
"climate": "Composite",
"code": 801186
},
{
"state": "Uttar Pradesh",
"district": "Azamgarh",
"city": "Katghar Lalganj",
"climate": "Composite",
"code": 801193
},
{
"state": "Uttar Pradesh",
"district": "Azamgarh",
"city": "Mahrajganj",
"climate": "Composite",
"code": 801184
},
{
"state": "Uttar Pradesh",
"district": "Azamgarh",
"city": "Mahul",
"climate": "Composite",
"code": 900193
},
{
"state": "Uttar Pradesh",
"district": "Azamgarh",
"city": "Martinganj",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Azamgarh",
"city": "Mehnagar",
"climate": "Composite",
"code": 801194
},
{
"state": "Uttar Pradesh",
"district": "Azamgarh",
"city": "Mubarakpur",
"climate": "Composite",
"code": 801188
},
{
"state": "Uttar Pradesh",
"district": "Azamgarh",
"city": "Nizamabad",
"climate": "Composite",
"code": 801190
},
{
"state": "Uttar Pradesh",
"district": "Azamgarh",
"city": "Phulpur_Az",
"climate": "Composite",
"code": 801192
},
{
"state": "Uttar Pradesh",
"district": "Azamgarh",
"city": "Sarai Mir",
"climate": "Composite",
"code": 801191
},
{
"state": "Uttar Pradesh",
"district": "Baghpat",
"city": "Agarwal Mandi",
"climate": "Composite",
"code": 800725
},
{
"state": "Uttar Pradesh",
"district": "Baghpat",
"city": "Aminagar Sarai",
"climate": "Composite",
"code": 800726
},
{
"state": "Uttar Pradesh",
"district": "Baghpat",
"city": "Baghpat",
"climate": "Composite",
"code": 800724
},
{
"state": "Uttar Pradesh",
"district": "Baghpat",
"city": "Baraut",
"climate": "Composite",
"code": 800723
},
{
"state": "Uttar Pradesh",
"district": "Baghpat",
"city": "Chhaprauli",
"climate": "Composite",
"code": 800720
},
{
"state": "Uttar Pradesh",
"district": "Baghpat",
"city": "Doghat",
"climate": "Composite",
"code": 800722
},
{
"state": "Uttar Pradesh",
"district": "Baghpat",
"city": "Khekada",
"climate": "Composite",
"code": 800727
},
{
"state": "Uttar Pradesh",
"district": "Baghpat",
"city": "Rataul",
"climate": "Composite",
"code": 900742
},
{
"state": "Uttar Pradesh",
"district": "Baghpat",
"city": "Tikri",
"climate": "Composite",
"code": 800721
},
{
"state": "Uttar Pradesh",
"district": "Bahraich",
"city": "Bahraich",
"climate": "Composite",
"code": 801125
},
{
"state": "Uttar Pradesh",
"district": "Bahraich",
"city": "Jarwal",
"climate": "Composite",
"code": 801126
},
{
"state": "Uttar Pradesh",
"district": "Bahraich",
"city": "Kaisarganj",
"climate": "Composite",
"code": 900743
},
{
"state": "Uttar Pradesh",
"district": "Bahraich",
"city": "Mihinpurwa",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Bahraich",
"city": "Nanpara",
"climate": "Composite",
"code": 801123
},
{
"state": "Uttar Pradesh",
"district": "Bahraich",
"city": "Payagpur",
"climate": "Composite",
"code": 900618
},
{
"state": "Uttar Pradesh",
"district": "Bahraich",
"city": "Risiya Bazar",
"climate": "Composite",
"code": 801124
},
{
"state": "Uttar Pradesh",
"district": "Bahraich",
"city": "Rupaidiha",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Ballia",
"city": "Ballia",
"climate": "Composite",
"code": 801206
},
{
"state": "Uttar Pradesh",
"district": "Ballia",
"city": "Bansdih",
"climate": "Composite",
"code": 801208
},
{
"state": "Uttar Pradesh",
"district": "Ballia",
"city": "Bariya",
"climate": "Composite",
"code": 900456
},
{
"state": "Uttar Pradesh",
"district": "Ballia",
"city": "Belthara Road",
"climate": "Composite",
"code": 801202
},
{
"state": "Uttar Pradesh",
"district": "Ballia",
"city": "Chitbara Gaon",
"climate": "Composite",
"code": 801205
},
{
"state": "Uttar Pradesh",
"district": "Ballia",
"city": "Maniyar",
"climate": "Composite",
"code": 801207
},
{
"state": "Uttar Pradesh",
"district": "Ballia",
"city": "Nagra",
"climate": "Composite",
"code": 900619
},
{
"state": "Uttar Pradesh",
"district": "Ballia",
"city": "Rasra",
"climate": "Composite",
"code": 801204
},
{
"state": "Uttar Pradesh",
"district": "Ballia",
"city": "Ratsarkalan",
"climate": "Composite",
"code": 900744
},
{
"state": "Uttar Pradesh",
"district": "Ballia",
"city": "Reoti",
"climate": "Composite",
"code": 801210
},
{
"state": "Uttar Pradesh",
"district": "Ballia",
"city": "Sahatwar",
"climate": "Composite",
"code": 801209
},
{
"state": "Uttar Pradesh",
"district": "Ballia",
"city": "Sikanderpur_B",
"climate": "Composite",
"code": 801203
},
{
"state": "Uttar Pradesh",
"district": "Balrampur",
"city": "Balrampur",
"climate": "Composite",
"code": 801129
},
{
"state": "Uttar Pradesh",
"district": "Balrampur",
"city": "Gainsari",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Balrampur",
"city": "Pachperwa",
"climate": "Composite",
"code": 801131
},
{
"state": "Uttar Pradesh",
"district": "Balrampur",
"city": "Tulsipur",
"climate": "Composite",
"code": 801130
},
{
"state": "Uttar Pradesh",
"district": "Balrampur",
"city": "Utraula",
"climate": "Composite",
"code": 801132
},
{
"state": "Uttar Pradesh",
"district": "Banda",
"city": "Atarra",
"climate": "Composite",
"code": 801056
},
{
"state": "Uttar Pradesh",
"district": "Banda",
"city": "Baberu",
"climate": "Composite",
"code": 801053
},
{
"state": "Uttar Pradesh",
"district": "Banda",
"city": "Banda",
"climate": "Composite",
"code": 801051
},
{
"state": "Uttar Pradesh",
"district": "Banda",
"city": "Bisanda Buzurg",
"climate": "Composite",
"code": 801055
},
{
"state": "Uttar Pradesh",
"district": "Banda",
"city": "Mataundh",
"climate": "Composite",
"code": 801050
},
{
"state": "Uttar Pradesh",
"district": "Banda",
"city": "Naraini",
"climate": "Composite",
"code": 801057
},
{
"state": "Uttar Pradesh",
"district": "Banda",
"city": "Oran",
"climate": "Composite",
"code": 801054
},
{
"state": "Uttar Pradesh",
"district": "Banda",
"city": "Tindwari",
"climate": "Composite",
"code": 801052
},
{
"state": "Uttar Pradesh",
"district": "Barabanki",
"city": "Banki",
"climate": "Composite",
"code": 801097
},
{
"state": "Uttar Pradesh",
"district": "Barabanki",
"city": "Belhara",
"climate": "Composite",
"code": 900452
},
{
"state": "Uttar Pradesh",
"district": "Barabanki",
"city": "Dariyabad",
"climate": "Composite",
"code": 801101
},
{
"state": "Uttar Pradesh",
"district": "Barabanki",
"city": "Dewa",
"climate": "Composite",
"code": 801095
},
{
"state": "Uttar Pradesh",
"district": "Barabanki",
"city": "Fatehpur",
"climate": "Composite",
"code": 801093
},
{
"state": "Uttar Pradesh",
"district": "Barabanki",
"city": "Haidergarh",
"climate": "Composite",
"code": 801103
},
{
"state": "Uttar Pradesh",
"district": "Barabanki",
"city": "Nawabganj_Bb",
"climate": "Composite",
"code": 801096
},
{
"state": "Uttar Pradesh",
"district": "Barabanki",
"city": "Ramnagar",
"climate": "Composite",
"code": 801094
},
{
"state": "Uttar Pradesh",
"district": "Barabanki",
"city": "Ramsanehi Ghat",
"climate": "Composite",
"code": 900745
},
{
"state": "Uttar Pradesh",
"district": "Barabanki",
"city": "Satrikh",
"climate": "Composite",
"code": 801098
},
{
"state": "Uttar Pradesh",
"district": "Barabanki",
"city": "Siddhaur",
"climate": "Composite",
"code": 801102
},
{
"state": "Uttar Pradesh",
"district": "Barabanki",
"city": "Subeha",
"climate": "Composite",
"code": 801104
},
{
"state": "Uttar Pradesh",
"district": "Barabanki",
"city": "Tikait Nagar",
"climate": "Composite",
"code": 801100
},
{
"state": "Uttar Pradesh",
"district": "Barabanki",
"city": "Zaidpur",
"climate": "Composite",
"code": 801099
},
{
"state": "Uttar Pradesh",
"district": "Bareilly",
"city": "Aonla",
"climate": "Composite",
"code": 800863
},
{
"state": "Uttar Pradesh",
"district": "Bareilly",
"city": "Baheri",
"climate": "Composite",
"code": 800853
},
{
"state": "Uttar Pradesh",
"district": "Bareilly",
"city": "Bareilly",
"climate": "Composite",
"code": 800866
},
{
"state": "Uttar Pradesh",
"district": "Bareilly",
"city": "Bareilly Cantonment",
"climate": "Composite",
"code": 800867
},
{
"state": "Uttar Pradesh",
"district": "Bareilly",
"city": "Bisharatganj",
"climate": "Composite",
"code": 800862
},
{
"state": "Uttar Pradesh",
"district": "Bareilly",
"city": "Deoranian",
"climate": "Composite",
"code": 800856
},
{
"state": "Uttar Pradesh",
"district": "Bareilly",
"city": "Dhaura Tanda",
"climate": "Composite",
"code": 800865
},
{
"state": "Uttar Pradesh",
"district": "Bareilly",
"city": "Faridpur",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Bareilly",
"city": "Faridpur(NPP)",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Bareilly",
"city": "Fatehganj Pashchimi",
"climate": "Composite",
"code": 800860
},
{
"state": "Uttar Pradesh",
"district": "Bareilly",
"city": "Fatehganj Purvi",
"climate": "Composite",
"code": 800872
},
{
"state": "Uttar Pradesh",
"district": "Bareilly",
"city": "Mirganj_B",
"climate": "Composite",
"code": 800859
},
{
"state": "Uttar Pradesh",
"district": "Bareilly",
"city": "Nawabganj_B",
"climate": "Composite",
"code": 800871
},
{
"state": "Uttar Pradesh",
"district": "Bareilly",
"city": "Richha",
"climate": "Composite",
"code": 800855
},
{
"state": "Uttar Pradesh",
"district": "Bareilly",
"city": "Rithora",
"climate": "Composite",
"code": 800869
},
{
"state": "Uttar Pradesh",
"district": "Bareilly",
"city": "Sainthal",
"climate": "Composite",
"code": 800870
},
{
"state": "Uttar Pradesh",
"district": "Bareilly",
"city": "Shahi",
"climate": "Composite",
"code": 800861
},
{
"state": "Uttar Pradesh",
"district": "Bareilly",
"city": "Shergarh",
"climate": "Composite",
"code": 800857
},
{
"state": "Uttar Pradesh",
"district": "Bareilly",
"city": "Shishgarh",
"climate": "Composite",
"code": 800858
},
{
"state": "Uttar Pradesh",
"district": "Bareilly",
"city": "Sirauli",
"climate": "Composite",
"code": 800864
},
{
"state": "Uttar Pradesh",
"district": "Bareilly",
"city": "Thiriya Nizamat Khan",
"climate": "Composite",
"code": 800868
},
{
"state": "Uttar Pradesh",
"district": "Basti",
"city": "Bankati",
"climate": "Composite",
"code": 900454
},
{
"state": "Uttar Pradesh",
"district": "Basti",
"city": "Basti",
"climate": "Composite",
"code": 801147
},
{
"state": "Uttar Pradesh",
"district": "Basti",
"city": "Bhabnan Bazar",
"climate": "Composite",
"code": 801146
},
{
"state": "Uttar Pradesh",
"district": "Basti",
"city": "Bhanpur Kaswa",
"climate": "Composite",
"code": 900621
},
{
"state": "Uttar Pradesh",
"district": "Basti",
"city": "Gaayghat",
"climate": "Composite",
"code": 900620
},
{
"state": "Uttar Pradesh",
"district": "Basti",
"city": "Ganeshpur",
"climate": "Composite",
"code": 900748
},
{
"state": "Uttar Pradesh",
"district": "Basti",
"city": "Harraiya",
"climate": "Composite",
"code": 801145
},
{
"state": "Uttar Pradesh",
"district": "Basti",
"city": "Kaptanganj",
"climate": "Composite",
"code": 900763
},
{
"state": "Uttar Pradesh",
"district": "Basti",
"city": "Mundervan",
"climate": "Composite",
"code": 900747
},
{
"state": "Uttar Pradesh",
"district": "Basti",
"city": "Nagar Bazar",
"climate": "Composite",
"code": 900746
},
{
"state": "Uttar Pradesh",
"district": "Basti",
"city": "Rudhauli Bazar",
"climate": "Composite",
"code": 900188
},
{
"state": "Uttar Pradesh",
"district": "Bhadohi",
"city": "Bhadohi",
"climate": "Composite",
"code": 801239
},
{
"state": "Uttar Pradesh",
"district": "Bhadohi",
"city": "Ghosia Bazar",
"climate": "Composite",
"code": 801243
},
{
"state": "Uttar Pradesh",
"district": "Bhadohi",
"city": "Gopiganj",
"climate": "Composite",
"code": 801241
},
{
"state": "Uttar Pradesh",
"district": "Bhadohi",
"city": "Gyanpur",
"climate": "Composite",
"code": 801240
},
{
"state": "Uttar Pradesh",
"district": "Bhadohi",
"city": "Khamaria",
"climate": "Composite",
"code": 801242
},
{
"state": "Uttar Pradesh",
"district": "Bhadohi",
"city": "Nai Bazar",
"climate": "Composite",
"code": 801238
},
{
"state": "Uttar Pradesh",
"district": "Bhadohi",
"city": "Suriyawan",
"climate": "Composite",
"code": 801237
},
{
"state": "Uttar Pradesh",
"district": "Bijnor",
"city": "Afzalgarh",
"climate": "Composite",
"code": 800670
},
{
"state": "Uttar Pradesh",
"district": "Bijnor",
"city": "Bijnor",
"climate": "Composite",
"code": 800665
},
{
"state": "Uttar Pradesh",
"district": "Bijnor",
"city": "Chandpur",
"climate": "Composite",
"code": 800677
},
{
"state": "Uttar Pradesh",
"district": "Bijnor",
"city": "Dhampur",
"climate": "Composite",
"code": 800672
},
{
"state": "Uttar Pradesh",
"district": "Bijnor",
"city": "Haldaur",
"climate": "Composite",
"code": 800667
},
{
"state": "Uttar Pradesh",
"district": "Bijnor",
"city": "Jalalabad_Bij",
"climate": "Composite",
"code": 800662
},
{
"state": "Uttar Pradesh",
"district": "Bijnor",
"city": "Jhalu",
"climate": "Composite",
"code": 800666
},
{
"state": "Uttar Pradesh",
"district": "Bijnor",
"city": "Kiratpur",
"climate": "Composite",
"code": 800663
},
{
"state": "Uttar Pradesh",
"district": "Bijnor",
"city": "Mandawar",
"climate": "Composite",
"code": 800664
},
{
"state": "Uttar Pradesh",
"district": "Bijnor",
"city": "Nagina",
"climate": "Composite",
"code": 800668
},
{
"state": "Uttar Pradesh",
"district": "Bijnor",
"city": "Najibabad",
"climate": "Composite",
"code": 800661
},
{
"state": "Uttar Pradesh",
"district": "Bijnor",
"city": "Nehtaur",
"climate": "Composite",
"code": 800673
},
{
"state": "Uttar Pradesh",
"district": "Bijnor",
"city": "Noorpur",
"climate": "Composite",
"code": 800676
},
{
"state": "Uttar Pradesh",
"district": "Bijnor",
"city": "Sahanpur",
"climate": "Composite",
"code": 800660
},
{
"state": "Uttar Pradesh",
"district": "Bijnor",
"city": "Sahaspur",
"climate": "Composite",
"code": 800675
},
{
"state": "Uttar Pradesh",
"district": "Bijnor",
"city": "Seohara",
"climate": "Composite",
"code": 800674
},
{
"state": "Uttar Pradesh",
"district": "Bijnor",
"city": "Sherkot",
"climate": "Composite",
"code": 800671
},
{
"state": "Uttar Pradesh",
"district": "Bijnor",
"city": "Warhapur",
"climate": "Composite",
"code": 800669
},
{
"state": "Uttar Pradesh",
"district": "Budaun",
"city": "Allapur",
"climate": "Composite",
"code": 800849
},
{
"state": "Uttar Pradesh",
"district": "Budaun",
"city": "Bilsi",
"climate": "Composite",
"code": 800840
},
{
"state": "Uttar Pradesh",
"district": "Budaun",
"city": "Bisauli",
"climate": "Composite",
"code": 800836
},
{
"state": "Uttar Pradesh",
"district": "Budaun",
"city": "Budaun",
"climate": "Composite",
"code": 800844
},
{
"state": "Uttar Pradesh",
"district": "Budaun",
"city": "Dahgawan",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Budaun",
"city": "Dataganj",
"climate": "Composite",
"code": 800850
},
{
"state": "Uttar Pradesh",
"district": "Budaun",
"city": "Faizganj",
"climate": "Composite",
"code": 800834
},
{
"state": "Uttar Pradesh",
"district": "Budaun",
"city": "Gulariya",
"climate": "Composite",
"code": 800846
},
{
"state": "Uttar Pradesh",
"district": "Budaun",
"city": "Islamnagar",
"climate": "Composite",
"code": 800833
},
{
"state": "Uttar Pradesh",
"district": "Budaun",
"city": "Kachhla",
"climate": "Composite",
"code": 800842
},
{
"state": "Uttar Pradesh",
"district": "Budaun",
"city": "Kakrala",
"climate": "Composite",
"code": 800848
},
{
"state": "Uttar Pradesh",
"district": "Budaun",
"city": "Kunwargaon",
"climate": "Composite",
"code": 800845
},
{
"state": "Uttar Pradesh",
"district": "Budaun",
"city": "Mundiya",
"climate": "Composite",
"code": 800835
},
{
"state": "Uttar Pradesh",
"district": "Budaun",
"city": "Rudayan",
"climate": "Composite",
"code": 800839
},
{
"state": "Uttar Pradesh",
"district": "Budaun",
"city": "Sahaswan",
"climate": "Composite",
"code": 800841
},
{
"state": "Uttar Pradesh",
"district": "Budaun",
"city": "Saidpur_B",
"climate": "Composite",
"code": 800837
},
{
"state": "Uttar Pradesh",
"district": "Budaun",
"city": "Sakhanu",
"climate": "Composite",
"code": 800847
},
{
"state": "Uttar Pradesh",
"district": "Budaun",
"city": "Ujhani",
"climate": "Composite",
"code": 800843
},
{
"state": "Uttar Pradesh",
"district": "Budaun",
"city": "Usawan",
"climate": "Composite",
"code": 800851
},
{
"state": "Uttar Pradesh",
"district": "Budaun",
"city": "Usehat",
"climate": "Composite",
"code": 800852
},
{
"state": "Uttar Pradesh",
"district": "Budaun",
"city": "Wazirganj",
"climate": "Composite",
"code": 800838
},
{
"state": "Uttar Pradesh",
"district": "Bulandshahar",
"city": "Anupshahr",
"climate": "Composite",
"code": 800755
},
{
"state": "Uttar Pradesh",
"district": "Bulandshahar",
"city": "Aurangabad",
"climate": "Composite",
"code": 800748
},
{
"state": "Uttar Pradesh",
"district": "Bulandshahar",
"city": "Bhawan Bahadur Nagar",
"climate": "Composite",
"code": 800751
},
{
"state": "Uttar Pradesh",
"district": "Bulandshahar",
"city": "Bugrasi",
"climate": "Composite",
"code": 800753
},
{
"state": "Uttar Pradesh",
"district": "Bulandshahar",
"city": "Bulandshahr",
"climate": "Composite",
"code": 800749
},
{
"state": "Uttar Pradesh",
"district": "Bulandshahar",
"city": "Chhatari",
"climate": "Composite",
"code": 800761
},
{
"state": "Uttar Pradesh",
"district": "Bulandshahar",
"city": "Dibai",
"climate": "Composite",
"code": 800757
},
{
"state": "Uttar Pradesh",
"district": "Bulandshahar",
"city": "Gulaothi",
"climate": "Composite",
"code": 800750
},
{
"state": "Uttar Pradesh",
"district": "Bulandshahar",
"city": "Jahangirabad",
"climate": "Composite",
"code": 800756
},
{
"state": "Uttar Pradesh",
"district": "Bulandshahar",
"city": "Kakod",
"climate": "Composite",
"code": 800747
},
{
"state": "Uttar Pradesh",
"district": "Bulandshahar",
"city": "Khanpur",
"climate": "Composite",
"code": 800754
},
{
"state": "Uttar Pradesh",
"district": "Bulandshahar",
"city": "Khurja",
"climate": "Composite",
"code": 800762
},
{
"state": "Uttar Pradesh",
"district": "Bulandshahar",
"city": "Naraura",
"climate": "Composite",
"code": 800758
},
{
"state": "Uttar Pradesh",
"district": "Bulandshahar",
"city": "Pahasu",
"climate": "Composite",
"code": 800760
},
{
"state": "Uttar Pradesh",
"district": "Bulandshahar",
"city": "Shikarpur",
"climate": "Composite",
"code": 800759
},
{
"state": "Uttar Pradesh",
"district": "Bulandshahar",
"city": "Siana",
"climate": "Composite",
"code": 800752
},
{
"state": "Uttar Pradesh",
"district": "Bulandshahar",
"city": "Sikandrabad",
"climate": "Composite",
"code": 800746
},
{
"state": "Uttar Pradesh",
"district": "Chandauli",
"city": "Chakia",
"climate": "Composite",
"code": 801231
},
{
"state": "Uttar Pradesh",
"district": "Chandauli",
"city": "Chandauli",
"climate": "Composite",
"code": 801229
},
{
"state": "Uttar Pradesh",
"district": "Chandauli",
"city": "Pandit Deendayal Upadhyay",
"climate": "Composite",
"code": 801227
},
{
"state": "Uttar Pradesh",
"district": "Chandauli",
"city": "Pt. Deendayal Upadhyay Nagar",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Chandauli",
"city": "Saiyad Raza",
"climate": "Composite",
"code": 801230
},
{
"state": "Uttar Pradesh",
"district": "Chitrakoot",
"city": "Chitrakoot Dham",
"climate": "Composite",
"code": 801059
},
{
"state": "Uttar Pradesh",
"district": "Chitrakoot",
"city": "Manikpur Sarhat",
"climate": "Composite",
"code": 801058
},
{
"state": "Uttar Pradesh",
"district": "Chitrakoot",
"city": "Mau",
"climate": "Composite",
"code": 900764
},
{
"state": "Uttar Pradesh",
"district": "Chitrakoot",
"city": "Rajapur",
"climate": "Composite",
"code": 801060
},
{
"state": "Uttar Pradesh",
"district": "Deoria",
"city": "Baitalpur",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Deoria",
"city": "Baluani Bazar",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Deoria",
"city": "Bariyarpur",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Deoria",
"city": "Bhatni Bazar",
"climate": "Composite",
"code": 801178
},
{
"state": "Uttar Pradesh",
"district": "Deoria",
"city": "Bhatpar Rani",
"climate": "Composite",
"code": 801182
},
{
"state": "Uttar Pradesh",
"district": "Deoria",
"city": "Deoria",
"climate": "Composite",
"code": 801175
},
{
"state": "Uttar Pradesh",
"district": "Deoria",
"city": "Gaura Barhaj",
"climate": "Composite",
"code": 801177
},
{
"state": "Uttar Pradesh",
"district": "Deoria",
"city": "Gauri Bazar",
"climate": "Composite",
"code": 801173
},
{
"state": "Uttar Pradesh",
"district": "Deoria",
"city": "Hetimpur",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Deoria",
"city": "Lar",
"climate": "Composite",
"code": 801181
},
{
"state": "Uttar Pradesh",
"district": "Deoria",
"city": "Madanpur",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Deoria",
"city": "Majhauliraj",
"climate": "Composite",
"code": 801179
},
{
"state": "Uttar Pradesh",
"district": "Deoria",
"city": "Patherdewa",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Deoria",
"city": "Rampur Karkhana",
"climate": "Composite",
"code": 801174
},
{
"state": "Uttar Pradesh",
"district": "Deoria",
"city": "Rudrapur",
"climate": "Composite",
"code": 801176
},
{
"state": "Uttar Pradesh",
"district": "Deoria",
"city": "Salempur",
"climate": "Composite",
"code": 801180
},
{
"state": "Uttar Pradesh",
"district": "Deoria",
"city": "Tarku Lavash",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Etah",
"city": "Aliganj",
"climate": "Composite",
"code": 801259
},
{
"state": "Uttar Pradesh",
"district": "Etah",
"city": "Awagarh",
"climate": "Composite",
"code": 801266
},
{
"state": "Uttar Pradesh",
"district": "Etah",
"city": "Etah",
"climate": "Composite",
"code": 801262
},
{
"state": "Uttar Pradesh",
"district": "Etah",
"city": "Jaithara",
"climate": "Composite",
"code": 801260
},
{
"state": "Uttar Pradesh",
"district": "Etah",
"city": "Jalesar",
"climate": "Composite",
"code": 801265
},
{
"state": "Uttar Pradesh",
"district": "Etah",
"city": "Marehra",
"climate": "Composite",
"code": 801263
},
{
"state": "Uttar Pradesh",
"district": "Etah",
"city": "Mirhachi",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Etah",
"city": "Nidhauli Kalan",
"climate": "Composite",
"code": 801264
},
{
"state": "Uttar Pradesh",
"district": "Etah",
"city": "Raja Ka Rampur",
"climate": "Composite",
"code": 801258
},
{
"state": "Uttar Pradesh",
"district": "Etah",
"city": "Sakit",
"climate": "Composite",
"code": 801261
},
{
"state": "Uttar Pradesh",
"district": "Etawah",
"city": "Bakewar",
"climate": "Composite",
"code": 800984
},
{
"state": "Uttar Pradesh",
"district": "Etawah",
"city": "Bharthana",
"climate": "Composite",
"code": 800983
},
{
"state": "Uttar Pradesh",
"district": "Etawah",
"city": "Ekdil",
"climate": "Composite",
"code": 800982
},
{
"state": "Uttar Pradesh",
"district": "Etawah",
"city": "Etawah",
"climate": "Composite",
"code": 800981
},
{
"state": "Uttar Pradesh",
"district": "Etawah",
"city": "Jaswantnagar",
"climate": "Composite",
"code": 800980
},
{
"state": "Uttar Pradesh",
"district": "Etawah",
"city": "Lakhna",
"climate": "Composite",
"code": 800985
},
{
"state": "Uttar Pradesh",
"district": "Farrukhabad",
"city": "Farrukhabad-Cum-Fatehgarh",
"climate": "Composite",
"code": 800968
},
{
"state": "Uttar Pradesh",
"district": "Farrukhabad",
"city": "Fatehgarh Cantonment",
"climate": "Composite",
"code": 800969
},
{
"state": "Uttar Pradesh",
"district": "Farrukhabad",
"city": "Kaimganj",
"climate": "Composite",
"code": 800966
},
{
"state": "Uttar Pradesh",
"district": "Farrukhabad",
"city": "Kamalganj",
"climate": "Composite",
"code": 800971
},
{
"state": "Uttar Pradesh",
"district": "Farrukhabad",
"city": "Kampil",
"climate": "Composite",
"code": 800965
},
{
"state": "Uttar Pradesh",
"district": "Farrukhabad",
"city": "Khimsepur",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Farrukhabad",
"city": "Mohammadabad",
"climate": "Composite",
"code": 800970
},
{
"state": "Uttar Pradesh",
"district": "Farrukhabad",
"city": "Nawabganj",
"climate": "Composite",
"code": 900623
},
{
"state": "Uttar Pradesh",
"district": "Farrukhabad",
"city": "Sankisa Basantpur",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Farrukhabad",
"city": "Shamsabad",
"climate": "Composite",
"code": 800967
},
{
"state": "Uttar Pradesh",
"district": "Fatehpur",
"city": "Asother",
"climate": "Composite",
"code": 900754
},
{
"state": "Uttar Pradesh",
"district": "Fatehpur",
"city": "Bahuwa",
"climate": "Composite",
"code": 801063
},
{
"state": "Uttar Pradesh",
"district": "Fatehpur",
"city": "Bindki",
"climate": "Composite",
"code": 801062
},
{
"state": "Uttar Pradesh",
"district": "Fatehpur",
"city": "Fatehpur",
"climate": "Composite",
"code": 801064
},
{
"state": "Uttar Pradesh",
"district": "Fatehpur",
"city": "Hathgram",
"climate": "Composite",
"code": 801067
},
{
"state": "Uttar Pradesh",
"district": "Fatehpur",
"city": "Kakhreru",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Fatehpur",
"city": "Karikandhata",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Fatehpur",
"city": "Khaga",
"climate": "Composite",
"code": 801065
},
{
"state": "Uttar Pradesh",
"district": "Fatehpur",
"city": "Kishunpur",
"climate": "Composite",
"code": 801066
},
{
"state": "Uttar Pradesh",
"district": "Fatehpur",
"city": "Kora Jahanabad",
"climate": "Composite",
"code": 801061
},
{
"state": "Uttar Pradesh",
"district": "Firozabad",
"city": "Eka",
"climate": "Composite",
"code": 900450
},
{
"state": "Uttar Pradesh",
"district": "Firozabad",
"city": "Fariha",
"climate": "Composite",
"code": 800817
},
{
"state": "Uttar Pradesh",
"district": "Firozabad",
"city": "Firozabad",
"climate": "Composite",
"code": 800816
},
{
"state": "Uttar Pradesh",
"district": "Firozabad",
"city": "Jasrana",
"climate": "Composite",
"code": 800818
},
{
"state": "Uttar Pradesh",
"district": "Firozabad",
"city": "Makkhanpur",
"climate": "Composite",
"code": 900624
},
{
"state": "Uttar Pradesh",
"district": "Firozabad",
"city": "Shikohabad",
"climate": "Composite",
"code": 800819
},
{
"state": "Uttar Pradesh",
"district": "Firozabad",
"city": "Sirsaganj",
"climate": "Composite",
"code": 800820
},
{
"state": "Uttar Pradesh",
"district": "Firozabad",
"city": "Tundla",
"climate": "Composite",
"code": 800815
},
{
"state": "Uttar Pradesh",
"district": "Gautam Buddha Nagar",
"city": "Bilaspur",
"climate": "Composite",
"code": 800741
},
{
"state": "Uttar Pradesh",
"district": "Gautam Buddha Nagar",
"city": "Dadri",
"climate": "Composite",
"code": 800740
},
{
"state": "Uttar Pradesh",
"district": "Gautam Buddha Nagar",
"city": "Dankaur",
"climate": "Composite",
"code": 800742
},
{
"state": "Uttar Pradesh",
"district": "Gautam Buddha Nagar",
"city": "Greater Noida",
"climate": "Composite",
"code": 900506
},
{
"state": "Uttar Pradesh",
"district": "Gautam Buddha Nagar",
"city": "Jahangirpur",
"climate": "Composite",
"code": 800744
},
{
"state": "Uttar Pradesh",
"district": "Gautam Buddha Nagar",
"city": "Jewar",
"climate": "Composite",
"code": 800745
},
{
"state": "Uttar Pradesh",
"district": "Gautam Buddha Nagar",
"city": "Noida",
"climate": "Composite",
"code": 900364
},
{
"state": "Uttar Pradesh",
"district": "Gautam Buddha Nagar",
"city": "Rabupura",
"climate": "Composite",
"code": 800743
},
{
"state": "Uttar Pradesh",
"district": "Ghaziabad",
"city": "Dasna",
"climate": "Composite",
"code": 800735
},
{
"state": "Uttar Pradesh",
"district": "Ghaziabad",
"city": "Faridnagar",
"climate": "Composite",
"code": 800731
},
{
"state": "Uttar Pradesh",
"district": "Ghaziabad",
"city": "Ghaziabad",
"climate": "Composite",
"code": 800734
},
{
"state": "Uttar Pradesh",
"district": "Ghaziabad",
"city": "Khoda Makanpur",
"climate": "Composite",
"code": 900441
},
{
"state": "Uttar Pradesh",
"district": "Ghaziabad",
"city": "Loni",
"climate": "Composite",
"code": 800733
},
{
"state": "Uttar Pradesh",
"district": "Ghaziabad",
"city": "Modinagar",
"climate": "Composite",
"code": 800730
},
{
"state": "Uttar Pradesh",
"district": "Ghaziabad",
"city": "Muradnagar",
"climate": "Composite",
"code": 800732
},
{
"state": "Uttar Pradesh",
"district": "Ghaziabad",
"city": "Niwari",
"climate": "Composite",
"code": 800729
},
{
"state": "Uttar Pradesh",
"district": "Ghaziabad",
"city": "Patala",
"climate": "Composite",
"code": 800728
},
{
"state": "Uttar Pradesh",
"district": "Ghazipur",
"city": "Bahadurganj",
"climate": "Composite",
"code": 801223
},
{
"state": "Uttar Pradesh",
"district": "Ghazipur",
"city": "Dildarnagar Fatehpur Bazar",
"climate": "Composite",
"code": 801225
},
{
"state": "Uttar Pradesh",
"district": "Ghazipur",
"city": "Ghazipur",
"climate": "Composite",
"code": 801222
},
{
"state": "Uttar Pradesh",
"district": "Ghazipur",
"city": "Jangipur",
"climate": "Composite",
"code": 801221
},
{
"state": "Uttar Pradesh",
"district": "Ghazipur",
"city": "Mohammadabad",
"climate": "Composite",
"code": 801224
},
{
"state": "Uttar Pradesh",
"district": "Ghazipur",
"city": "Sadat",
"climate": "Composite",
"code": 801219
},
{
"state": "Uttar Pradesh",
"district": "Ghazipur",
"city": "Saidpur_Gh",
"climate": "Composite",
"code": 801220
},
{
"state": "Uttar Pradesh",
"district": "Ghazipur",
"city": "Zamania",
"climate": "Composite",
"code": 801226
},
{
"state": "Uttar Pradesh",
"district": "Gonda",
"city": "Belsar",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Gonda",
"city": "Colonelganj",
"climate": "Composite",
"code": 801136
},
{
"state": "Uttar Pradesh",
"district": "Gonda",
"city": "Dhanepur",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Gonda",
"city": "Gonda",
"climate": "Composite",
"code": 801134
},
{
"state": "Uttar Pradesh",
"district": "Gonda",
"city": "Katra_G",
"climate": "Composite",
"code": 801135
},
{
"state": "Uttar Pradesh",
"district": "Gonda",
"city": "Khargupur",
"climate": "Composite",
"code": 801133
},
{
"state": "Uttar Pradesh",
"district": "Gonda",
"city": "Mankapur",
"climate": "Composite",
"code": 801138
},
{
"state": "Uttar Pradesh",
"district": "Gonda",
"city": "Nawabganj_G",
"climate": "Composite",
"code": 801137
},
{
"state": "Uttar Pradesh",
"district": "Gonda",
"city": "Paraspur",
"climate": "Composite",
"code": 900453
},
{
"state": "Uttar Pradesh",
"district": "Gonda",
"city": "Tarabganj",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Gorakhpur",
"city": "Bansgaon",
"climate": "Composite",
"code": 801163
},
{
"state": "Uttar Pradesh",
"district": "Gorakhpur",
"city": "Barhalganj",
"climate": "Composite",
"code": 801165
},
{
"state": "Uttar Pradesh",
"district": "Gorakhpur",
"city": "Campierganj",
"climate": "Composite",
"code": 900670
},
{
"state": "Uttar Pradesh",
"district": "Gorakhpur",
"city": "Chaumukha",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Gorakhpur",
"city": "Ghaghsara Bazaar",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Gorakhpur",
"city": "Gola Bazar",
"climate": "Composite",
"code": 801164
},
{
"state": "Uttar Pradesh",
"district": "Gorakhpur",
"city": "Gorakhpur",
"climate": "Composite",
"code": 801160
},
{
"state": "Uttar Pradesh",
"district": "Gorakhpur",
"city": "Mundera Bazar",
"climate": "Composite",
"code": 801162
},
{
"state": "Uttar Pradesh",
"district": "Gorakhpur",
"city": "Pipiganj",
"climate": "Composite",
"code": 801158
},
{
"state": "Uttar Pradesh",
"district": "Gorakhpur",
"city": "Pipraich",
"climate": "Composite",
"code": 801161
},
{
"state": "Uttar Pradesh",
"district": "Gorakhpur",
"city": "Sahjanwan",
"climate": "Composite",
"code": 801159
},
{
"state": "Uttar Pradesh",
"district": "Gorakhpur",
"city": "Unwal Kasba Sangrampur Unwal",
"climate": "Composite",
"code": 900491
},
{
"state": "Uttar Pradesh",
"district": "Gorakhpur",
"city": "Uruva Bazar",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Hamirpur",
"city": "Gohand",
"climate": "Composite",
"code": 801041
},
{
"state": "Uttar Pradesh",
"district": "Hamirpur",
"city": "Hamirpur",
"climate": "Composite",
"code": 801039
},
{
"state": "Uttar Pradesh",
"district": "Hamirpur",
"city": "Kurara",
"climate": "Composite",
"code": 801038
},
{
"state": "Uttar Pradesh",
"district": "Hamirpur",
"city": "Maudaha",
"climate": "Composite",
"code": 801044
},
{
"state": "Uttar Pradesh",
"district": "Hamirpur",
"city": "Rath",
"climate": "Composite",
"code": 801042
},
{
"state": "Uttar Pradesh",
"district": "Hamirpur",
"city": "Sarila",
"climate": "Composite",
"code": 801043
},
{
"state": "Uttar Pradesh",
"district": "Hamirpur",
"city": "Sumerpur",
"climate": "Composite",
"code": 801040
},
{
"state": "Uttar Pradesh",
"district": "Hapur",
"city": "Babugarh",
"climate": "Composite",
"code": 800738
},
{
"state": "Uttar Pradesh",
"district": "Hapur",
"city": "Garhmukhteshwar",
"climate": "Composite",
"code": 800739
},
{
"state": "Uttar Pradesh",
"district": "Hapur",
"city": "Hapur",
"climate": "Composite",
"code": 800737
},
{
"state": "Uttar Pradesh",
"district": "Hapur",
"city": "Pilkhuwa",
"climate": "Composite",
"code": 800736
},
{
"state": "Uttar Pradesh",
"district": "Hardoi",
"city": "Beniganj",
"climate": "Composite",
"code": 800926
},
{
"state": "Uttar Pradesh",
"district": "Hardoi",
"city": "Bilgram",
"climate": "Composite",
"code": 800921
},
{
"state": "Uttar Pradesh",
"district": "Hardoi",
"city": "Gopamau",
"climate": "Composite",
"code": 800918
},
{
"state": "Uttar Pradesh",
"district": "Hardoi",
"city": "Hardoi",
"climate": "Composite",
"code": 800919
},
{
"state": "Uttar Pradesh",
"district": "Hardoi",
"city": "Kachhauna Patseni",
"climate": "Composite",
"code": 800925
},
{
"state": "Uttar Pradesh",
"district": "Hardoi",
"city": "Kursath_H",
"climate": "Composite",
"code": 800924
},
{
"state": "Uttar Pradesh",
"district": "Hardoi",
"city": "Madhoganj",
"climate": "Composite",
"code": 800922
},
{
"state": "Uttar Pradesh",
"district": "Hardoi",
"city": "Mallawan",
"climate": "Composite",
"code": 800923
},
{
"state": "Uttar Pradesh",
"district": "Hardoi",
"city": "Pali_H",
"climate": "Composite",
"code": 800917
},
{
"state": "Uttar Pradesh",
"district": "Hardoi",
"city": "Pihani",
"climate": "Composite",
"code": 800916
},
{
"state": "Uttar Pradesh",
"district": "Hardoi",
"city": "Sandi",
"climate": "Composite",
"code": 800920
},
{
"state": "Uttar Pradesh",
"district": "Hardoi",
"city": "Sandila",
"climate": "Composite",
"code": 800927
},
{
"state": "Uttar Pradesh",
"district": "Hardoi",
"city": "Shahabad",
"climate": "Composite",
"code": 800915
},
{
"state": "Uttar Pradesh",
"district": "Hathras",
"city": "Hasayan",
"climate": "Composite",
"code": 800778
},
{
"state": "Uttar Pradesh",
"district": "Hathras",
"city": "Hathras",
"climate": "Composite",
"code": 800780
},
{
"state": "Uttar Pradesh",
"district": "Hathras",
"city": "Mendu",
"climate": "Composite",
"code": 800779
},
{
"state": "Uttar Pradesh",
"district": "Hathras",
"city": "Mursan",
"climate": "Composite",
"code": 800781
},
{
"state": "Uttar Pradesh",
"district": "Hathras",
"city": "Purdilnagar",
"climate": "Composite",
"code": 800777
},
{
"state": "Uttar Pradesh",
"district": "Hathras",
"city": "Sadabad",
"climate": "Composite",
"code": 800782
},
{
"state": "Uttar Pradesh",
"district": "Hathras",
"city": "Sahpau",
"climate": "Composite",
"code": 800783
},
{
"state": "Uttar Pradesh",
"district": "Hathras",
"city": "Sasni",
"climate": "Composite",
"code": 800775
},
{
"state": "Uttar Pradesh",
"district": "Hathras",
"city": "Sikandrarao",
"climate": "Composite",
"code": 800776
},
{
"state": "Uttar Pradesh",
"district": "Jalaun",
"city": "Ait",
"climate": "Composite",
"code": 900625
},
{
"state": "Uttar Pradesh",
"district": "Jalaun",
"city": "Jalaun",
"climate": "Composite",
"code": 801011
},
{
"state": "Uttar Pradesh",
"district": "Jalaun",
"city": "Kadaura",
"climate": "Composite",
"code": 801013
},
{
"state": "Uttar Pradesh",
"district": "Jalaun",
"city": "Kalpi",
"climate": "Composite",
"code": 801012
},
{
"state": "Uttar Pradesh",
"district": "Jalaun",
"city": "Konch",
"climate": "Composite",
"code": 801016
},
{
"state": "Uttar Pradesh",
"district": "Jalaun",
"city": "Kotra",
"climate": "Composite",
"code": 801015
},
{
"state": "Uttar Pradesh",
"district": "Jalaun",
"city": "Lalitpur",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Jalaun",
"city": "Madhogarh",
"climate": "Composite",
"code": 801010
},
{
"state": "Uttar Pradesh",
"district": "Jalaun",
"city": "Nadigaon",
"climate": "Composite",
"code": 801017
},
{
"state": "Uttar Pradesh",
"district": "Jalaun",
"city": "Orai",
"climate": "Composite",
"code": 801014
},
{
"state": "Uttar Pradesh",
"district": "Jalaun",
"city": "Rampura",
"climate": "Composite",
"code": 801008
},
{
"state": "Uttar Pradesh",
"district": "Jalaun",
"city": "Umri",
"climate": "Composite",
"code": 801009
},
{
"state": "Uttar Pradesh",
"district": "Jaunpur",
"city": "Badlapur",
"climate": "Composite",
"code": 900196
},
{
"state": "Uttar Pradesh",
"district": "Jaunpur",
"city": "Gaurabadshahpur",
"climate": "Composite",
"code": 900627
},
{
"state": "Uttar Pradesh",
"district": "Jaunpur",
"city": "Jafarabad",
"climate": "Composite",
"code": 801216
},
{
"state": "Uttar Pradesh",
"district": "Jaunpur",
"city": "Jaunpur",
"climate": "Composite",
"code": 801215
},
{
"state": "Uttar Pradesh",
"district": "Jaunpur",
"city": "Kajgaon",
"climate": "Composite",
"code": 900628
},
{
"state": "Uttar Pradesh",
"district": "Jaunpur",
"city": "Kerakat",
"climate": "Composite",
"code": 801218
},
{
"state": "Uttar Pradesh",
"district": "Jaunpur",
"city": "Khetasarai",
"climate": "Composite",
"code": 801212
},
{
"state": "Uttar Pradesh",
"district": "Jaunpur",
"city": "Machhlishahr",
"climate": "Composite",
"code": 801214
},
{
"state": "Uttar Pradesh",
"district": "Jaunpur",
"city": "Madiyahu",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Jaunpur",
"city": "Mariahu",
"climate": "Composite",
"code": 801217
},
{
"state": "Uttar Pradesh",
"district": "Jaunpur",
"city": "Mogra Badshahpur",
"climate": "Composite",
"code": 801213
},
{
"state": "Uttar Pradesh",
"district": "Jaunpur",
"city": "Rampur",
"climate": "Composite",
"code": 900626
},
{
"state": "Uttar Pradesh",
"district": "Jaunpur",
"city": "Shahganj",
"climate": "Composite",
"code": 801211
},
{
"state": "Uttar Pradesh",
"district": "Jhansi",
"city": "Babina Cantonment",
"climate": "Composite",
"code": 801033
},
{
"state": "Uttar Pradesh",
"district": "Jhansi",
"city": "Baragaon",
"climate": "Composite",
"code": 801029
},
{
"state": "Uttar Pradesh",
"district": "Jhansi",
"city": "Barua Sagar",
"climate": "Composite",
"code": 801028
},
{
"state": "Uttar Pradesh",
"district": "Jhansi",
"city": "Chirgaon",
"climate": "Composite",
"code": 801020
},
{
"state": "Uttar Pradesh",
"district": "Jhansi",
"city": "Erich",
"climate": "Composite",
"code": 801021
},
{
"state": "Uttar Pradesh",
"district": "Jhansi",
"city": "Garautha",
"climate": "Composite",
"code": 801023
},
{
"state": "Uttar Pradesh",
"district": "Jhansi",
"city": "Gursarai",
"climate": "Composite",
"code": 801022
},
{
"state": "Uttar Pradesh",
"district": "Jhansi",
"city": "Jhansi",
"climate": "Composite",
"code": 801030
},
{
"state": "Uttar Pradesh",
"district": "Jhansi",
"city": "Jhansi Cantonment",
"climate": "Composite",
"code": 801031
},
{
"state": "Uttar Pradesh",
"district": "Jhansi",
"city": "Kathera",
"climate": "Composite",
"code": 801027
},
{
"state": "Uttar Pradesh",
"district": "Jhansi",
"city": "Mauranipur",
"climate": "Composite",
"code": 801025
},
{
"state": "Uttar Pradesh",
"district": "Jhansi",
"city": "Moth",
"climate": "Composite",
"code": 801019
},
{
"state": "Uttar Pradesh",
"district": "Jhansi",
"city": "Ranipur",
"climate": "Composite",
"code": 801026
},
{
"state": "Uttar Pradesh",
"district": "Jhansi",
"city": "Samthar",
"climate": "Composite",
"code": 801018
},
{
"state": "Uttar Pradesh",
"district": "Jhansi",
"city": "Tondi Fatehpur",
"climate": "Composite",
"code": 801024
},
{
"state": "Uttar Pradesh",
"district": "Kannauj",
"city": "Chhibramau",
"climate": "Composite",
"code": 800975
},
{
"state": "Uttar Pradesh",
"district": "Kannauj",
"city": "Gursahaiganj",
"climate": "Composite",
"code": 800973
},
{
"state": "Uttar Pradesh",
"district": "Kannauj",
"city": "Kannauj",
"climate": "Composite",
"code": 800978
},
{
"state": "Uttar Pradesh",
"district": "Kannauj",
"city": "Samdhan",
"climate": "Composite",
"code": 800972
},
{
"state": "Uttar Pradesh",
"district": "Kannauj",
"city": "Saurikh",
"climate": "Composite",
"code": 800976
},
{
"state": "Uttar Pradesh",
"district": "Kannauj",
"city": "Sikanderpur_K",
"climate": "Composite",
"code": 800974
},
{
"state": "Uttar Pradesh",
"district": "Kannauj",
"city": "Talgram",
"climate": "Composite",
"code": 800977
},
{
"state": "Uttar Pradesh",
"district": "Kannauj",
"city": "Tirwaganj",
"climate": "Composite",
"code": 800979
},
{
"state": "Uttar Pradesh",
"district": "Kanpur",
"city": "Bilhaur",
"climate": "Composite",
"code": 801002
},
{
"state": "Uttar Pradesh",
"district": "Kanpur",
"city": "Bithoor",
"climate": "Composite",
"code": 801004
},
{
"state": "Uttar Pradesh",
"district": "Kanpur",
"city": "Ghatampur",
"climate": "Composite",
"code": 801007
},
{
"state": "Uttar Pradesh",
"district": "Kanpur",
"city": "Kanpur",
"climate": "Composite",
"code": 801005
},
{
"state": "Uttar Pradesh",
"district": "Kanpur",
"city": "Kanpur Cantonment",
"climate": "Composite",
"code": 801006
},
{
"state": "Uttar Pradesh",
"district": "Kanpur",
"city": "Shivrajpur",
"climate": "Composite",
"code": 801003
},
{
"state": "Uttar Pradesh",
"district": "Kanpur Dehat",
"city": "Akbarpur",
"climate": "Composite",
"code": 800998
},
{
"state": "Uttar Pradesh",
"district": "Kanpur Dehat",
"city": "Amraudha",
"climate": "Composite",
"code": 800999
},
{
"state": "Uttar Pradesh",
"district": "Kanpur Dehat",
"city": "Derapur",
"climate": "Composite",
"code": 800995
},
{
"state": "Uttar Pradesh",
"district": "Kanpur Dehat",
"city": "Jhinjhak",
"climate": "Composite",
"code": 800994
},
{
"state": "Uttar Pradesh",
"district": "Kanpur Dehat",
"city": "Kanchausi",
"climate": "Composite",
"code": 900755
},
{
"state": "Uttar Pradesh",
"district": "Kanpur Dehat",
"city": "Musanagar",
"climate": "Composite",
"code": 900631
},
{
"state": "Uttar Pradesh",
"district": "Kanpur Dehat",
"city": "Pukhrayan",
"climate": "Composite",
"code": 801000
},
{
"state": "Uttar Pradesh",
"district": "Kanpur Dehat",
"city": "Rajpur",
"climate": "Composite",
"code": 900630
},
{
"state": "Uttar Pradesh",
"district": "Kanpur Dehat",
"city": "Raniya",
"climate": "Composite",
"code": 900629
},
{
"state": "Uttar Pradesh",
"district": "Kanpur Dehat",
"city": "Rasulabad_Kd",
"climate": "Composite",
"code": 800993
},
{
"state": "Uttar Pradesh",
"district": "Kanpur Dehat",
"city": "Rura",
"climate": "Composite",
"code": 800997
},
{
"state": "Uttar Pradesh",
"district": "Kanpur Dehat",
"city": "Shivli",
"climate": "Composite",
"code": 800996
},
{
"state": "Uttar Pradesh",
"district": "Kanpur Dehat",
"city": "Sikandra",
"climate": "Composite",
"code": 801001
},
{
"state": "Uttar Pradesh",
"district": "Kasganj",
"city": "Amanpur",
"climate": "Composite",
"code": 801271
},
{
"state": "Uttar Pradesh",
"district": "Kasganj",
"city": "Bhargain",
"climate": "Composite",
"code": 801276
},
{
"state": "Uttar Pradesh",
"district": "Kasganj",
"city": "Bilram",
"climate": "Composite",
"code": 801268
},
{
"state": "Uttar Pradesh",
"district": "Kasganj",
"city": "Ganj Dundawara",
"climate": "Composite",
"code": 801273
},
{
"state": "Uttar Pradesh",
"district": "Kasganj",
"city": "Kasganj",
"climate": "Composite",
"code": 801269
},
{
"state": "Uttar Pradesh",
"district": "Kasganj",
"city": "Mohanpur",
"climate": "Composite",
"code": 801272
},
{
"state": "Uttar Pradesh",
"district": "Kasganj",
"city": "Patiyali",
"climate": "Composite",
"code": 801274
},
{
"state": "Uttar Pradesh",
"district": "Kasganj",
"city": "Sahawar",
"climate": "Composite",
"code": 801270
},
{
"state": "Uttar Pradesh",
"district": "Kasganj",
"city": "Sidhpura",
"climate": "Composite",
"code": 801275
},
{
"state": "Uttar Pradesh",
"district": "Kasganj",
"city": "Soron",
"climate": "Composite",
"code": 801267
},
{
"state": "Uttar Pradesh",
"district": "Kaushambi",
"city": "Ajhuwa",
"climate": "Composite",
"code": 801075
},
{
"state": "Uttar Pradesh",
"district": "Kaushambi",
"city": "Bharwari",
"climate": "Composite",
"code": 801079
},
{
"state": "Uttar Pradesh",
"district": "Kaushambi",
"city": "Chail",
"climate": "Composite",
"code": 801080
},
{
"state": "Uttar Pradesh",
"district": "Kaushambi",
"city": "Charwa",
"climate": "Composite",
"code": 900756
},
{
"state": "Uttar Pradesh",
"district": "Kaushambi",
"city": "Daranagar",
"climate": "Composite",
"code": 900633
},
{
"state": "Uttar Pradesh",
"district": "Kaushambi",
"city": "Karari",
"climate": "Composite",
"code": 801078
},
{
"state": "Uttar Pradesh",
"district": "Kaushambi",
"city": "Manjhanpur",
"climate": "Composite",
"code": 801077
},
{
"state": "Uttar Pradesh",
"district": "Kaushambi",
"city": "Poorav Pashchim Shareera",
"climate": "Composite",
"code": 900632
},
{
"state": "Uttar Pradesh",
"district": "Kaushambi",
"city": "Sarai Aquil",
"climate": "Composite",
"code": 801081
},
{
"state": "Uttar Pradesh",
"district": "Kaushambi",
"city": "Sirathu",
"climate": "Composite",
"code": 801076
},
{
"state": "Uttar Pradesh",
"district": "Kheeri",
"city": "Barwar",
"climate": "Composite",
"code": 800899
},
{
"state": "Uttar Pradesh",
"district": "Kheeri",
"city": "Bheera",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Kheeri",
"city": "Dhaurehra",
"climate": "Composite",
"code": 800903
},
{
"state": "Uttar Pradesh",
"district": "Kheeri",
"city": "Gola Gokaran Nath",
"climate": "Composite",
"code": 800897
},
{
"state": "Uttar Pradesh",
"district": "Kheeri",
"city": "Kheri",
"climate": "Composite",
"code": 800901
},
{
"state": "Uttar Pradesh",
"district": "Kheeri",
"city": "Lakhimpur",
"climate": "Composite",
"code": 800900
},
{
"state": "Uttar Pradesh",
"district": "Kheeri",
"city": "Mailani",
"climate": "Composite",
"code": 800896
},
{
"state": "Uttar Pradesh",
"district": "Kheeri",
"city": "Mohammadi",
"climate": "Composite",
"code": 800898
},
{
"state": "Uttar Pradesh",
"district": "Kheeri",
"city": "Nighasan",
"climate": "Composite",
"code": 900634
},
{
"state": "Uttar Pradesh",
"district": "Kheeri",
"city": "Oel Dhakwa",
"climate": "Composite",
"code": 800902
},
{
"state": "Uttar Pradesh",
"district": "Kheeri",
"city": "Paliya Kalan",
"climate": "Composite",
"code": 800895
},
{
"state": "Uttar Pradesh",
"district": "Kheeri",
"city": "Singahi Bhiraura",
"climate": "Composite",
"code": 800894
},
{
"state": "Uttar Pradesh",
"district": "Kushinagar",
"city": "Chhitauni",
"climate": "Composite",
"code": 900635
},
{
"state": "Uttar Pradesh",
"district": "Kushinagar",
"city": "Duddhi",
"climate": "Composite",
"code": 900671
},
{
"state": "Uttar Pradesh",
"district": "Kushinagar",
"city": "Fazilnagar",
"climate": "Composite",
"code": 900637
},
{
"state": "Uttar Pradesh",
"district": "Kushinagar",
"city": "Hata",
"climate": "Composite",
"code": 801170
},
{
"state": "Uttar Pradesh",
"district": "Kushinagar",
"city": "Kaptanganj",
"climate": "Composite",
"code": 801169
},
{
"state": "Uttar Pradesh",
"district": "Kushinagar",
"city": "Khadda",
"climate": "Composite",
"code": 801166
},
{
"state": "Uttar Pradesh",
"district": "Kushinagar",
"city": "Kushinagar",
"climate": "Composite",
"code": 801171
},
{
"state": "Uttar Pradesh",
"district": "Kushinagar",
"city": "Mathauli",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Kushinagar",
"city": "Padrauna",
"climate": "Composite",
"code": 801167
},
{
"state": "Uttar Pradesh",
"district": "Kushinagar",
"city": "Ramkola",
"climate": "Composite",
"code": 801168
},
{
"state": "Uttar Pradesh",
"district": "Kushinagar",
"city": "Sewarhi",
"climate": "Composite",
"code": 801172
},
{
"state": "Uttar Pradesh",
"district": "Kushinagar",
"city": "Sukrauli",
"climate": "Composite",
"code": 900665
},
{
"state": "Uttar Pradesh",
"district": "Kushinagar",
"city": "Tamkuhi Raj",
"climate": "Composite",
"code": 900636
},
{
"state": "Uttar Pradesh",
"district": "Lalitpur",
"city": "Lalitpur",
"climate": "Composite",
"code": 801035
},
{
"state": "Uttar Pradesh",
"district": "Lalitpur",
"city": "Mahroni",
"climate": "Composite",
"code": 801037
},
{
"state": "Uttar Pradesh",
"district": "Lalitpur",
"city": "Pali_L",
"climate": "Composite",
"code": 801036
},
{
"state": "Uttar Pradesh",
"district": "Lalitpur",
"city": "Talbehat",
"climate": "Composite",
"code": 801034
},
{
"state": "Uttar Pradesh",
"district": "Lucknow",
"city": "Amethi_L",
"climate": "Composite",
"code": 800954
},
{
"state": "Uttar Pradesh",
"district": "Lucknow",
"city": "Bakshi Ka Talab",
"climate": "Composite",
"code": 800949
},
{
"state": "Uttar Pradesh",
"district": "Lucknow",
"city": "Banthra",
"climate": "Composite",
"code": 900638
},
{
"state": "Uttar Pradesh",
"district": "Lucknow",
"city": "Gosainganj_L",
"climate": "Composite",
"code": 800953
},
{
"state": "Uttar Pradesh",
"district": "Lucknow",
"city": "Itaunja",
"climate": "Composite",
"code": 800948
},
{
"state": "Uttar Pradesh",
"district": "Lucknow",
"city": "Kakori",
"climate": "Composite",
"code": 800950
},
{
"state": "Uttar Pradesh",
"district": "Lucknow",
"city": "Lucknow",
"climate": "Composite",
"code": 800951
},
{
"state": "Uttar Pradesh",
"district": "Lucknow",
"city": "Lucknow Cantonment",
"climate": "Composite",
"code": 800952
},
{
"state": "Uttar Pradesh",
"district": "Lucknow",
"city": "Mahona",
"climate": "Composite",
"code": 800947
},
{
"state": "Uttar Pradesh",
"district": "Lucknow",
"city": "Malihabad",
"climate": "Composite",
"code": 800946
},
{
"state": "Uttar Pradesh",
"district": "Lucknow",
"city": "Mohanlalganj",
"climate": "Composite",
"code": 900639
},
{
"state": "Uttar Pradesh",
"district": "Lucknow",
"city": "Nagram",
"climate": "Composite",
"code": 800955
},
{
"state": "Uttar Pradesh",
"district": "Maharajganj",
"city": "Anandnagar",
"climate": "Composite",
"code": 801155
},
{
"state": "Uttar Pradesh",
"district": "Maharajganj",
"city": "Brijmanganj",
"climate": "Composite",
"code": 900642
},
{
"state": "Uttar Pradesh",
"district": "Maharajganj",
"city": "Chowk",
"climate": "Composite",
"code": 900757
},
{
"state": "Uttar Pradesh",
"district": "Maharajganj",
"city": "Ghughuli",
"climate": "Composite",
"code": 801156
},
{
"state": "Uttar Pradesh",
"district": "Maharajganj",
"city": "Maharajganj",
"climate": "Composite",
"code": 801157
},
{
"state": "Uttar Pradesh",
"district": "Maharajganj",
"city": "Nautanwa",
"climate": "Composite",
"code": 801152
},
{
"state": "Uttar Pradesh",
"district": "Maharajganj",
"city": "Nichlaul",
"climate": "Composite",
"code": 801153
},
{
"state": "Uttar Pradesh",
"district": "Maharajganj",
"city": "Paniyara",
"climate": "Composite",
"code": 900641
},
{
"state": "Uttar Pradesh",
"district": "Maharajganj",
"city": "Partawal",
"climate": "Composite",
"code": 900640
},
{
"state": "Uttar Pradesh",
"district": "Maharajganj",
"city": "Siswa Bazar",
"climate": "Composite",
"code": 801154
},
{
"state": "Uttar Pradesh",
"district": "Maharajganj",
"city": "Sonauli",
"climate": "Composite",
"code": 900455
},
{
"state": "Uttar Pradesh",
"district": "Mahoba",
"city": "Charkhari",
"climate": "Composite",
"code": 801047
},
{
"state": "Uttar Pradesh",
"district": "Mahoba",
"city": "Kabrai",
"climate": "Composite",
"code": 801049
},
{
"state": "Uttar Pradesh",
"district": "Mahoba",
"city": "Kharela",
"climate": "Composite",
"code": 801046
},
{
"state": "Uttar Pradesh",
"district": "Mahoba",
"city": "Kul Pahar",
"climate": "Composite",
"code": 801045
},
{
"state": "Uttar Pradesh",
"district": "Mahoba",
"city": "Mahoba",
"climate": "Composite",
"code": 801048
},
{
"state": "Uttar Pradesh",
"district": "Mainpuri",
"city": "Barnahal",
"climate": "Composite",
"code": 900643
},
{
"state": "Uttar Pradesh",
"district": "Mainpuri",
"city": "Bewar",
"climate": "Composite",
"code": 800827
},
{
"state": "Uttar Pradesh",
"district": "Mainpuri",
"city": "Bhogaon",
"climate": "Composite",
"code": 800826
},
{
"state": "Uttar Pradesh",
"district": "Mainpuri",
"city": "Ghiraur",
"climate": "Composite",
"code": 800823
},
{
"state": "Uttar Pradesh",
"district": "Mainpuri",
"city": "Jyoti Khuriya",
"climate": "Composite",
"code": 800822
},
{
"state": "Uttar Pradesh",
"district": "Mainpuri",
"city": "Karhal",
"climate": "Composite",
"code": 800825
},
{
"state": "Uttar Pradesh",
"district": "Mainpuri",
"city": "Kishni",
"climate": "Composite",
"code": 800829
},
{
"state": "Uttar Pradesh",
"district": "Mainpuri",
"city": "Kuraoali",
"climate": "Composite",
"code": 800821
},
{
"state": "Uttar Pradesh",
"district": "Mainpuri",
"city": "Kusmara",
"climate": "Composite",
"code": 800828
},
{
"state": "Uttar Pradesh",
"district": "Mainpuri",
"city": "Mainpuri",
"climate": "Composite",
"code": 800824
},
{
"state": "Uttar Pradesh",
"district": "Mathura",
"city": "Bajna",
"climate": "Composite",
"code": 800789
},
{
"state": "Uttar Pradesh",
"district": "Mathura",
"city": "Baldeo",
"climate": "Composite",
"code": 800793
},
{
"state": "Uttar Pradesh",
"district": "Mathura",
"city": "Barsana",
"climate": "Composite",
"code": 800786
},
{
"state": "Uttar Pradesh",
"district": "Mathura",
"city": "Chaumuhan",
"climate": "Composite",
"code": 800788
},
{
"state": "Uttar Pradesh",
"district": "Mathura",
"city": "Chhata",
"climate": "Composite",
"code": 800787
},
{
"state": "Uttar Pradesh",
"district": "Mathura",
"city": "Farah",
"climate": "Composite",
"code": 800794
},
{
"state": "Uttar Pradesh",
"district": "Mathura",
"city": "Gokul",
"climate": "Composite",
"code": 800791
},
{
"state": "Uttar Pradesh",
"district": "Mathura",
"city": "Govardhan",
"climate": "Composite",
"code": 800797
},
{
"state": "Uttar Pradesh",
"district": "Mathura",
"city": "Kosi Kalan",
"climate": "Composite",
"code": 800784
},
{
"state": "Uttar Pradesh",
"district": "Mathura",
"city": "Mahaban",
"climate": "Composite",
"code": 800792
},
{
"state": "Uttar Pradesh",
"district": "Mathura",
"city": "Mathura Cantonment",
"climate": "Composite",
"code": 800800
},
{
"state": "Uttar Pradesh",
"district": "Mathura",
"city": "Mathura-Vrindavan",
"climate": "Composite",
"code": 800799
},
{
"state": "Uttar Pradesh",
"district": "Mathura",
"city": "Nandgaon",
"climate": "Composite",
"code": 800785
},
{
"state": "Uttar Pradesh",
"district": "Mathura",
"city": "Radhakund",
"climate": "Composite",
"code": 800796
},
{
"state": "Uttar Pradesh",
"district": "Mathura",
"city": "Raya",
"climate": "Composite",
"code": 800790
},
{
"state": "Uttar Pradesh",
"district": "Mathura",
"city": "Saunkh",
"climate": "Composite",
"code": 800798
},
{
"state": "Uttar Pradesh",
"district": "Mau",
"city": "Adari",
"climate": "Composite",
"code": 801199
},
{
"state": "Uttar Pradesh",
"district": "Mau",
"city": "Amila",
"climate": "Composite",
"code": 801196
},
{
"state": "Uttar Pradesh",
"district": "Mau",
"city": "Chiraiyakot",
"climate": "Composite",
"code": 900457
},
{
"state": "Uttar Pradesh",
"district": "Mau",
"city": "Dohrighat",
"climate": "Composite",
"code": 801195
},
{
"state": "Uttar Pradesh",
"district": "Mau",
"city": "Ghosi",
"climate": "Composite",
"code": 801197
},
{
"state": "Uttar Pradesh",
"district": "Mau",
"city": "Kopaganj",
"climate": "Composite",
"code": 801198
},
{
"state": "Uttar Pradesh",
"district": "Mau",
"city": "Kurthi Jafarpur",
"climate": "Composite",
"code": 900644
},
{
"state": "Uttar Pradesh",
"district": "Mau",
"city": "Madhuban",
"climate": "Composite",
"code": 900458
},
{
"state": "Uttar Pradesh",
"district": "Mau",
"city": "Maunath Bhanjan",
"climate": "Composite",
"code": 801200
},
{
"state": "Uttar Pradesh",
"district": "Mau",
"city": "Muhammadabad Gohna",
"climate": "Composite",
"code": 801201
},
{
"state": "Uttar Pradesh",
"district": "Mau",
"city": "Walidpur",
"climate": "Composite",
"code": 900195
},
{
"state": "Uttar Pradesh",
"district": "Meerut",
"city": "Bahsuma",
"climate": "Composite",
"code": 800711
},
{
"state": "Uttar Pradesh",
"district": "Meerut",
"city": "Daurala",
"climate": "Composite",
"code": 800708
},
{
"state": "Uttar Pradesh",
"district": "Meerut",
"city": "Harra",
"climate": "Composite",
"code": 900445
},
{
"state": "Uttar Pradesh",
"district": "Meerut",
"city": "Hastinapur",
"climate": "Composite",
"code": 800712
},
{
"state": "Uttar Pradesh",
"district": "Meerut",
"city": "Karnawal",
"climate": "Composite",
"code": 800706
},
{
"state": "Uttar Pradesh",
"district": "Meerut",
"city": "Kharkhoda",
"climate": "Composite",
"code": 800719
},
{
"state": "Uttar Pradesh",
"district": "Meerut",
"city": "Khiwai",
"climate": "Composite",
"code": 900447
},
{
"state": "Uttar Pradesh",
"district": "Meerut",
"city": "Kithaur",
"climate": "Composite",
"code": 800715
},
{
"state": "Uttar Pradesh",
"district": "Meerut",
"city": "Lawar",
"climate": "Composite",
"code": 800709
},
{
"state": "Uttar Pradesh",
"district": "Meerut",
"city": "Mawana",
"climate": "Composite",
"code": 800713
},
{
"state": "Uttar Pradesh",
"district": "Meerut",
"city": "Meerut",
"climate": "Composite",
"code": 800716
},
{
"state": "Uttar Pradesh",
"district": "Meerut",
"city": "Meerut Cantonment",
"climate": "Composite",
"code": 800717
},
{
"state": "Uttar Pradesh",
"district": "Meerut",
"city": "Parikshitgarh",
"climate": "Composite",
"code": 800714
},
{
"state": "Uttar Pradesh",
"district": "Meerut",
"city": "Phalauda",
"climate": "Composite",
"code": 800710
},
{
"state": "Uttar Pradesh",
"district": "Meerut",
"city": "Sardhana",
"climate": "Composite",
"code": 800707
},
{
"state": "Uttar Pradesh",
"district": "Meerut",
"city": "Sewalkhas",
"climate": "Composite",
"code": 800718
},
{
"state": "Uttar Pradesh",
"district": "Meerut",
"city": "Shahjahanpur",
"climate": "Composite",
"code": 900446
},
{
"state": "Uttar Pradesh",
"district": "Mirzapur-Cum-Vindhyachal",
"city": "Ahraura",
"climate": "Composite",
"code": 801247
},
{
"state": "Uttar Pradesh",
"district": "Mirzapur-Cum-Vindhyachal",
"city": "Chunar",
"climate": "Composite",
"code": 801246
},
{
"state": "Uttar Pradesh",
"district": "Mirzapur-Cum-Vindhyachal",
"city": "Kachhwa",
"climate": "Composite",
"code": 801245
},
{
"state": "Uttar Pradesh",
"district": "Mirzapur-Cum-Vindhyachal",
"city": "Mirzapur-Cum-Vindhyachal",
"climate": "Composite",
"code": 801244
},
{
"state": "Uttar Pradesh",
"district": "Moradabad",
"city": "Agwanpur",
"climate": "Composite",
"code": 900443
},
{
"state": "Uttar Pradesh",
"district": "Moradabad",
"city": "Bhojpur Dharampur",
"climate": "Composite",
"code": 800681
},
{
"state": "Uttar Pradesh",
"district": "Moradabad",
"city": "Bilari",
"climate": "Composite",
"code": 800684
},
{
"state": "Uttar Pradesh",
"district": "Moradabad",
"city": "Dhakia",
"climate": "Composite",
"code": 900442
},
{
"state": "Uttar Pradesh",
"district": "Moradabad",
"city": "Kanth_M",
"climate": "Composite",
"code": 800679
},
{
"state": "Uttar Pradesh",
"district": "Moradabad",
"city": "Kundarki",
"climate": "Composite",
"code": 800683
},
{
"state": "Uttar Pradesh",
"district": "Moradabad",
"city": "Mehmoodpur Mafi",
"climate": "Composite",
"code": 900758
},
{
"state": "Uttar Pradesh",
"district": "Moradabad",
"city": "Moradabad",
"climate": "Composite",
"code": 800682
},
{
"state": "Uttar Pradesh",
"district": "Moradabad",
"city": "Pakbada",
"climate": "Composite",
"code": 900444
},
{
"state": "Uttar Pradesh",
"district": "Moradabad",
"city": "Thakurdwara",
"climate": "Composite",
"code": 800678
},
{
"state": "Uttar Pradesh",
"district": "Moradabad",
"city": "Umri Kalan",
"climate": "Composite",
"code": 800680
},
{
"state": "Uttar Pradesh",
"district": "Muzaffarnagar",
"city": "Bhokarhedi",
"climate": "Composite",
"code": 800658
},
{
"state": "Uttar Pradesh",
"district": "Muzaffarnagar",
"city": "Budhana",
"climate": "Composite",
"code": 800654
},
{
"state": "Uttar Pradesh",
"district": "Muzaffarnagar",
"city": "Charthawal",
"climate": "Composite",
"code": 800651
},
{
"state": "Uttar Pradesh",
"district": "Muzaffarnagar",
"city": "Jansath",
"climate": "Composite",
"code": 800657
},
{
"state": "Uttar Pradesh",
"district": "Muzaffarnagar",
"city": "Khatauli",
"climate": "Composite",
"code": 800656
},
{
"state": "Uttar Pradesh",
"district": "Muzaffarnagar",
"city": "Miranpur",
"climate": "Composite",
"code": 800659
},
{
"state": "Uttar Pradesh",
"district": "Muzaffarnagar",
"city": "Muzaffarnagar",
"climate": "Composite",
"code": 800652
},
{
"state": "Uttar Pradesh",
"district": "Muzaffarnagar",
"city": "Purquazi",
"climate": "Composite",
"code": 800650
},
{
"state": "Uttar Pradesh",
"district": "Muzaffarnagar",
"city": "Shahpur_Muz",
"climate": "Composite",
"code": 800655
},
{
"state": "Uttar Pradesh",
"district": "Muzaffarnagar",
"city": "Sisauli",
"climate": "Composite",
"code": 800653
},
{
"state": "Uttar Pradesh",
"district": "Pilibhit",
"city": "Barkhera",
"climate": "Composite",
"code": 800878
},
{
"state": "Uttar Pradesh",
"district": "Pilibhit",
"city": "Bilsanda",
"climate": "Composite",
"code": 800880
},
{
"state": "Uttar Pradesh",
"district": "Pilibhit",
"city": "Bisalpur",
"climate": "Composite",
"code": 800879
},
{
"state": "Uttar Pradesh",
"district": "Pilibhit",
"city": "Gulariya Bhindara",
"climate": "Composite",
"code": 800874
},
{
"state": "Uttar Pradesh",
"district": "Pilibhit",
"city": "Jahanabad",
"climate": "Composite",
"code": 800876
},
{
"state": "Uttar Pradesh",
"district": "Pilibhit",
"city": "Kalinagar",
"climate": "Composite",
"code": 800881
},
{
"state": "Uttar Pradesh",
"district": "Pilibhit",
"city": "Nyoria Husainpur",
"climate": "Composite",
"code": 800875
},
{
"state": "Uttar Pradesh",
"district": "Pilibhit",
"city": "Pakadia Naugawa",
"climate": "Composite",
"code": 900645
},
{
"state": "Uttar Pradesh",
"district": "Pilibhit",
"city": "Pilibhit",
"climate": "Composite",
"code": 800877
},
{
"state": "Uttar Pradesh",
"district": "Pilibhit",
"city": "Puranpur",
"climate": "Composite",
"code": 800882
},
{
"state": "Uttar Pradesh",
"district": "Pratapgarh",
"city": "Antu",
"climate": "Composite",
"code": 801070
},
{
"state": "Uttar Pradesh",
"district": "Pratapgarh",
"city": "Bela Pratapgarh",
"climate": "Composite",
"code": 801071
},
{
"state": "Uttar Pradesh",
"district": "Pratapgarh",
"city": "Derwa",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Pratapgarh",
"city": "Dhakwa",
"climate": "Composite",
"code": 900760
},
{
"state": "Uttar Pradesh",
"district": "Pratapgarh",
"city": "Gadwara Bazar",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Pratapgarh",
"city": "Heeraganj Bazar",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Pratapgarh",
"city": "Katra Gulab Singh Bazar",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Pratapgarh",
"city": "Katra Medniganj",
"climate": "Composite",
"code": 801073
},
{
"state": "Uttar Pradesh",
"district": "Pratapgarh",
"city": "Kohdaur",
"climate": "Composite",
"code": 900647
},
{
"state": "Uttar Pradesh",
"district": "Pratapgarh",
"city": "Kunda",
"climate": "Composite",
"code": 801069
},
{
"state": "Uttar Pradesh",
"district": "Pratapgarh",
"city": "Lalganj_P",
"climate": "Composite",
"code": 900448
},
{
"state": "Uttar Pradesh",
"district": "Pratapgarh",
"city": "Mandhata Bazar",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Pratapgarh",
"city": "Manikpur",
"climate": "Composite",
"code": 801068
},
{
"state": "Uttar Pradesh",
"district": "Pratapgarh",
"city": "Patti",
"climate": "Composite",
"code": 801074
},
{
"state": "Uttar Pradesh",
"district": "Pratapgarh",
"city": "Pratapgarh City",
"climate": "Composite",
"code": 801072
},
{
"state": "Uttar Pradesh",
"district": "Pratapgarh",
"city": "Prithviganj",
"climate": "Composite",
"code": 900646
},
{
"state": "Uttar Pradesh",
"district": "Pratapgarh",
"city": "Ramganj",
"climate": "Composite",
"code": 900759
},
{
"state": "Uttar Pradesh",
"district": "Pratapgarh",
"city": "Raniganj",
"climate": "Composite",
"code": 900449
},
{
"state": "Uttar Pradesh",
"district": "Pratapgarh",
"city": "Suwansa Bazar",
"climate": "Composite",
"code": 900648
},
{
"state": "Uttar Pradesh",
"district": "Prayagraj",
"city": "Allahabad Cantonment",
"climate": "Composite",
"code": 801087
},
{
"state": "Uttar Pradesh",
"district": "Prayagraj",
"city": "Bharatganj",
"climate": "Composite",
"code": 801091
},
{
"state": "Uttar Pradesh",
"district": "Prayagraj",
"city": "Handia",
"climate": "Composite",
"code": 801089
},
{
"state": "Uttar Pradesh",
"district": "Prayagraj",
"city": "Koraon",
"climate": "Composite",
"code": 801092
},
{
"state": "Uttar Pradesh",
"district": "Prayagraj",
"city": "Lal Gopalganj Nindaura",
"climate": "Composite",
"code": 801083
},
{
"state": "Uttar Pradesh",
"district": "Prayagraj",
"city": "Mau Aima",
"climate": "Composite",
"code": 801082
},
{
"state": "Uttar Pradesh",
"district": "Prayagraj",
"city": "Phulpur_Al",
"climate": "Composite",
"code": 801085
},
{
"state": "Uttar Pradesh",
"district": "Prayagraj",
"city": "Prayagraj",
"climate": "Composite",
"code": 801086
},
{
"state": "Uttar Pradesh",
"district": "Prayagraj",
"city": "Shankargarh",
"climate": "Composite",
"code": 801088
},
{
"state": "Uttar Pradesh",
"district": "Prayagraj",
"city": "Sirsa",
"climate": "Composite",
"code": 801090
},
{
"state": "Uttar Pradesh",
"district": "Raebareli",
"city": "Bachhrawan",
"climate": "Composite",
"code": 800956
},
{
"state": "Uttar Pradesh",
"district": "Raebareli",
"city": "Dalmau",
"climate": "Composite",
"code": 800961
},
{
"state": "Uttar Pradesh",
"district": "Raebareli",
"city": "Lalganj_Rb",
"climate": "Composite",
"code": 800960
},
{
"state": "Uttar Pradesh",
"district": "Raebareli",
"city": "Maharajganj",
"climate": "Composite",
"code": 800957
},
{
"state": "Uttar Pradesh",
"district": "Raebareli",
"city": "Nasirabad",
"climate": "Composite",
"code": 900451
},
{
"state": "Uttar Pradesh",
"district": "Raebareli",
"city": "Parsadepur",
"climate": "Composite",
"code": 800963
},
{
"state": "Uttar Pradesh",
"district": "Raebareli",
"city": "Rae Bareli",
"climate": "Composite",
"code": 800959
},
{
"state": "Uttar Pradesh",
"district": "Raebareli",
"city": "Salon",
"climate": "Composite",
"code": 800964
},
{
"state": "Uttar Pradesh",
"district": "Raebareli",
"city": "Shivgarh",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Raebareli",
"city": "Unchahar",
"climate": "Composite",
"code": 800962
},
{
"state": "Uttar Pradesh",
"district": "Rampur",
"city": "Bilaspur",
"climate": "Composite",
"code": 800693
},
{
"state": "Uttar Pradesh",
"district": "Rampur",
"city": "Darhiyal",
"climate": "Composite",
"code": 900649
},
{
"state": "Uttar Pradesh",
"district": "Rampur",
"city": "Kemri",
"climate": "Composite",
"code": 800694
},
{
"state": "Uttar Pradesh",
"district": "Rampur",
"city": "Maswasi",
"climate": "Composite",
"code": 800690
},
{
"state": "Uttar Pradesh",
"district": "Rampur",
"city": "Milak",
"climate": "Composite",
"code": 800697
},
{
"state": "Uttar Pradesh",
"district": "Rampur",
"city": "Narpat Nagar Doondawala",
"climate": "Composite",
"code": 900651
},
{
"state": "Uttar Pradesh",
"district": "Rampur",
"city": "Rampur",
"climate": "Composite",
"code": 800695
},
{
"state": "Uttar Pradesh",
"district": "Rampur",
"city": "Saifani",
"climate": "Composite",
"code": 900650
},
{
"state": "Uttar Pradesh",
"district": "Rampur",
"city": "Shahabad",
"climate": "Composite",
"code": 800696
},
{
"state": "Uttar Pradesh",
"district": "Rampur",
"city": "Suar",
"climate": "Composite",
"code": 800691
},
{
"state": "Uttar Pradesh",
"district": "Rampur",
"city": "Tanda_R",
"climate": "Composite",
"code": 800692
},
{
"state": "Uttar Pradesh",
"district": "Saharanpur",
"city": "Ambehta",
"climate": "Composite",
"code": 800634
},
{
"state": "Uttar Pradesh",
"district": "Saharanpur",
"city": "Behat",
"climate": "Composite",
"code": 800629
},
{
"state": "Uttar Pradesh",
"district": "Saharanpur",
"city": "Chhutmalpura",
"climate": "Composite",
"code": 900652
},
{
"state": "Uttar Pradesh",
"district": "Saharanpur",
"city": "Chilkana Sultanpur",
"climate": "Composite",
"code": 800631
},
{
"state": "Uttar Pradesh",
"district": "Saharanpur",
"city": "Deoband",
"climate": "Composite",
"code": 800637
},
{
"state": "Uttar Pradesh",
"district": "Saharanpur",
"city": "Gangoh",
"climate": "Composite",
"code": 800635
},
{
"state": "Uttar Pradesh",
"district": "Saharanpur",
"city": "Nakur",
"climate": "Composite",
"code": 800633
},
{
"state": "Uttar Pradesh",
"district": "Saharanpur",
"city": "Nanauta",
"climate": "Composite",
"code": 800638
},
{
"state": "Uttar Pradesh",
"district": "Saharanpur",
"city": "Rampur Maniharan",
"climate": "Composite",
"code": 800639
},
{
"state": "Uttar Pradesh",
"district": "Saharanpur",
"city": "Saharanpur",
"climate": "Composite",
"code": 800630
},
{
"state": "Uttar Pradesh",
"district": "Saharanpur",
"city": "Sarsawa",
"climate": "Composite",
"code": 800632
},
{
"state": "Uttar Pradesh",
"district": "Saharanpur",
"city": "Titron",
"climate": "Composite",
"code": 800636
},
{
"state": "Uttar Pradesh",
"district": "Sambhal",
"city": "Babrala",
"climate": "Composite",
"code": 800831
},
{
"state": "Uttar Pradesh",
"district": "Sambhal",
"city": "Bahjoi",
"climate": "Composite",
"code": 800687
},
{
"state": "Uttar Pradesh",
"district": "Sambhal",
"city": "Chandausi",
"climate": "Composite",
"code": 800689
},
{
"state": "Uttar Pradesh",
"district": "Sambhal",
"city": "Gawan",
"climate": "Composite",
"code": 800830
},
{
"state": "Uttar Pradesh",
"district": "Sambhal",
"city": "Gunnaur",
"climate": "Composite",
"code": 800832
},
{
"state": "Uttar Pradesh",
"district": "Sambhal",
"city": "Narauli",
"climate": "Composite",
"code": 800688
},
{
"state": "Uttar Pradesh",
"district": "Sambhal",
"city": "Sambhal",
"climate": "Composite",
"code": 800686
},
{
"state": "Uttar Pradesh",
"district": "Sambhal",
"city": "Sirsi",
"climate": "Composite",
"code": 800685
},
{
"state": "Uttar Pradesh",
"district": "Sant Kabir Nagar",
"city": "Baghnagar Urf Bakhira",
"climate": "Composite",
"code": 900653
},
{
"state": "Uttar Pradesh",
"district": "Sant Kabir Nagar",
"city": "Belhar Kala",
"climate": "Composite",
"code": 900654
},
{
"state": "Uttar Pradesh",
"district": "Sant Kabir Nagar",
"city": "Dharma Singhwa",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Sant Kabir Nagar",
"city": "Hansar Bazaar Dhanghata",
"climate": "Composite"
},
{
"state": "Uttar Pradesh",
"district": "Sant Kabir Nagar",
"city": "Hariharpur",
"climate": "Composite",
"code": 801151
},
{
"state": "Uttar Pradesh",
"district": "Sant Kabir Nagar",
"city": "Khalilabad",
"climate": "Composite",
"code": 801149
},
{
"state": "Uttar Pradesh",
"district": "Sant Kabir Nagar",
"city": "Maghar",
"climate": "Composite",
"code": 801150
},
{
"state": "Uttar Pradesh",
"district": "Sant Kabir Nagar",
"city": "Mehdawal",
"climate": "Composite",
"code": 801148
},
{
"state": "Uttar Pradesh",
"district": "Shahjahanpur",
"city": "Allahganj",
"climate": "Composite",
"code": 800893
},
{
"state": "Uttar Pradesh",
"district": "Shahjahanpur",
"city": "Banda",
"climate": "Composite",
"code": 900656
},
{
"state": "Uttar Pradesh",
"district": "Shahjahanpur",
"city": "Jalalabad",
"climate": "Composite",
"code": 800892
},
{
"state": "Uttar Pradesh",
"district": "Shahjahanpur",
"city": "Kalaan",
"climate": "Composite",
"code": 900761
},
{
"state": "Uttar Pradesh",
"district": "Shahjahanpur",
"city": "Kanth_S",
"climate": "Composite",
"code": 800891
},
{
"state": "Uttar Pradesh",
"district": "Shahjahanpur",
"city": "Katra_S",
"climate": "Composite",
"code": 800886
},
{
"state": "Uttar Pradesh",
"district": "Shahjahanpur",
"city": "Khudaganj",
"climate": "Composite",
"code": 800885
},
{
"state": "Uttar Pradesh",
"district": "Shahjahanpur",
"city": "Khutar",
"climate": "Composite",
"code": 800883
},
{
"state": "Uttar Pradesh",
"district": "Shahjahanpur",
"city": "Nigohi",
"climate": "Composite",
"code": 900655
},
{
"state": "Uttar Pradesh",
"district": "Shahjahanpur",
"city": "Powayan",
"climate": "Composite",
"code": 800884
},
{
"state": "Uttar Pradesh",
"district": "Shahjahanpur",
"city": "Shahjahanpur",
"climate": "Composite",
"code": 800889
},
{
"state": "Uttar Pradesh",
"district": "Shahjahanpur",
"city": "Shahjahanpur Cantonment",
"climate": "Composite",
"code": 800890
},
{
"state": "Uttar Pradesh",
"district": "Shahjahanpur",
"city": "Tilhar",
"climate": "Composite",
"code": 800887
},
{
"state": "Uttar Pradesh",
"district": "Shamli",
"city": "Ailam",
"climate": "Composite",
"code": 800644
},
{
"state": "Uttar Pradesh",
"district": "Shamli",
"city": "Banat",
"climate": "Composite",
"code": 800646
},
{
"state": "Uttar Pradesh",
"district": "Shamli",
"city": "Garhi Pukhta",
"climate": "Composite",
"code": 800647
},
{
"state": "Uttar Pradesh",
"district": "Shamli",
"city": "Jalalabad_Sh",
"climate": "Composite",
"code": 800649
},
{
"state": "Uttar Pradesh",
"district": "Shamli",
"city": "Jhinjhana",
"climate": "Composite",
"code": 800641
},
{
"state": "Uttar Pradesh",
"district": "Shamli",
"city": "Kairana",
"climate": "Composite",
"code": 800642
},
{
"state": "Uttar Pradesh",
"district": "Shamli",
"city": "Kandhla",
"climate": "Composite",
"code": 800643
},
{
"state": "Uttar Pradesh",
"district": "Shamli",
"city": "Shamli",
"climate": "Composite",
"code": 800645
},
{
"state": "Uttar Pradesh",
"district": "Shamli",
"city": "Thana Bhawan",
"climate": "Composite",
"code": 800648
},
{
"state": "Uttar Pradesh",
"district": "Shamli",
"city": "Un",
"climate": "Composite",
"code": 800640
},
{
"state": "Uttar Pradesh",
"district": "Siddharthnagar",
"city": "Badhani Chafa",
"climate": "Composite",
"code": 900657
},
{
"state": "Uttar Pradesh",
"district": "Siddharthnagar",
"city": "Bansi",
"climate": "Composite",
"code": 801143
},
{
"state": "Uttar Pradesh",
"district": "Siddharthnagar",
"city": "Barhani Bazar",
"climate": "Composite",
"code": 801139
},
{
"state": "Uttar Pradesh",
"district": "Siddharthnagar",
"city": "Bharatbhari",
"climate": "Composite",
"code": 900659
},
{
"state": "Uttar Pradesh",
"district": "Siddharthnagar",
"city": "Biskohar",
"climate": "Composite",
"code": 900660
},
{
"state": "Uttar Pradesh",
"district": "Siddharthnagar",
"city": "Domariyaganj",
"climate": "Composite",
"code": 801144
},
{
"state": "Uttar Pradesh",
"district": "Siddharthnagar",
"city": "Itwa",
"climate": "Composite",
"code": 900658
},
{
"state": "Uttar Pradesh",
"district": "Siddharthnagar",
"city": "Kapilavastu",
"climate": "Composite",
"code": 900661
},
{
"state": "Uttar Pradesh",
"district": "Siddharthnagar",
"city": "Shohratgarh",
"climate": "Composite",
"code": 801140
},
{
"state": "Uttar Pradesh",
"district": "Siddharthnagar",
"city": "Siddharthnagar",
"climate": "Composite",
"code": 801141
},
{
"state": "Uttar Pradesh",
"district": "Siddharthnagar",
"city": "Uska Bazar",
"climate": "Composite",
"code": 801142
},
{
"state": "Uttar Pradesh",
"district": "Sitapur",
"city": "Biswan",
"climate": "Composite",
"code": 800911
},
{
"state": "Uttar Pradesh",
"district": "Sitapur",
"city": "Hargaon",
"climate": "Composite",
"code": 800908
},
{
"state": "Uttar Pradesh",
"district": "Sitapur",
"city": "Khairabad",
"climate": "Composite",
"code": 800906
},
{
"state": "Uttar Pradesh",
"district": "Sitapur",
"city": "Laharpur",
"climate": "Composite",
"code": 800909
},
{
"state": "Uttar Pradesh",
"district": "Sitapur",
"city": "Mahmudabad",
"climate": "Composite",
"code": 800912
},
{
"state": "Uttar Pradesh",
"district": "Sitapur",
"city": "Maholi",
"climate": "Composite",
"code": 800904
},
{
"state": "Uttar Pradesh",
"district": "Sitapur",
"city": "Misrikh-Cum-Neemsar",
"climate": "Composite",
"code": 800905
},
{
"state": "Uttar Pradesh",
"district": "Sitapur",
"city": "Paintepur",
"climate": "Composite",
"code": 800913
},
{
"state": "Uttar Pradesh",
"district": "Sitapur",
"city": "Sidhauli",
"climate": "Composite",
"code": 800914
},
{
"state": "Uttar Pradesh",
"district": "Sitapur",
"city": "Sitapur",
"climate": "Composite",
"code": 800907
},
{
"state": "Uttar Pradesh",
"district": "Sitapur",
"city": "Tambaur-Cum-Ahamdabad",
"climate": "Composite",
"code": 800910
},
{
"state": "Uttar Pradesh",
"district": "Sonbhadra",
"city": "Anapara",
"climate": "Composite",
"code": 900662
},
{
"state": "Uttar Pradesh",
"district": "Sonbhadra",
"city": "Chopan",
"climate": "Composite",
"code": 801251
},
{
"state": "Uttar Pradesh",
"district": "Sonbhadra",
"city": "Churk Ghurma",
"climate": "Composite",
"code": 801250
},
{
"state": "Uttar Pradesh",
"district": "Sonbhadra",
"city": "Dala Bazar",
"climate": "Composite",
"code": 900663
},
{
"state": "Uttar Pradesh",
"district": "Sonbhadra",
"city": "Dudhi",
"climate": "Composite",
"code": 801253
},
{
"state": "Uttar Pradesh",
"district": "Sonbhadra",
"city": "Ghorawal",
"climate": "Composite",
"code": 801248
},
{
"state": "Uttar Pradesh",
"district": "Sonbhadra",
"city": "Obra",
"climate": "Composite",
"code": 801252
},
{
"state": "Uttar Pradesh",
"district": "Sonbhadra",
"city": "Pipri",
"climate": "Composite",
"code": 801257
},
{
"state": "Uttar Pradesh",
"district": "Sonbhadra",
"city": "Renukoot",
"climate": "Composite",
"code": 801254
},
{
"state": "Uttar Pradesh",
"district": "Sonbhadra",
"city": "Sonbhadra",
"climate": "Composite",
"code": 801249
},
{
"state": "Uttar Pradesh",
"district": "Srawasti",
"city": "Bhinga",
"climate": "Composite",
"code": 801127
},
{
"state": "Uttar Pradesh",
"district": "Srawasti",
"city": "Ikauna",
"climate": "Composite",
"code": 801128
},
{
"state": "Uttar Pradesh",
"district": "Sultanpur",
"city": "Dostpur",
"climate": "Composite",
"code": 801121
},
{
"state": "Uttar Pradesh",
"district": "Sultanpur",
"city": "Kadipur",
"climate": "Composite",
"code": 801122
},
{
"state": "Uttar Pradesh",
"district": "Sultanpur",
"city": "Koeripur",
"climate": "Composite",
"code": 801120
},
{
"state": "Uttar Pradesh",
"district": "Sultanpur",
"city": "Lambhua",
"climate": "Composite",
"code": 900664
},
{
"state": "Uttar Pradesh",
"district": "Sultanpur",
"city": "Sultanpur",
"climate": "Composite",
"code": 801119
},
{
"state": "Uttar Pradesh",
"district": "Unnao",
"city": "Achalganj",
"climate": "Composite",
"code": 900762
},
{
"state": "Uttar Pradesh",
"district": "Unnao",
"city": "Auras",
"climate": "Composite",
"code": 800934
},
{
"state": "Uttar Pradesh",
"district": "Unnao",
"city": "Bangarmau",
"climate": "Composite",
"code": 800929
},
{
"state": "Uttar Pradesh",
"district": "Unnao",
"city": "Bhagwant Nagar",
"climate": "Composite",
"code": 800945
},
{
"state": "Uttar Pradesh",
"district": "Unnao",
"city": "Bighapur",
"climate": "Composite",
"code": 800944
},
{
"state": "Uttar Pradesh",
"district": "Unnao",
"city": "Fatehpur Chaurasi",
"climate": "Composite",
"code": 800930
},
{
"state": "Uttar Pradesh",
"district": "Unnao",
"city": "Gangaghat",
"climate": "Composite",
"code": 800941
},
{
"state": "Uttar Pradesh",
"district": "Unnao",
"city": "Ganj Muradabad",
"climate": "Composite",
"code": 800928
},
{
"state": "Uttar Pradesh",
"district": "Unnao",
"city": "Hyderabad",
"climate": "Composite",
"code": 800935
},
{
"state": "Uttar Pradesh",
"district": "Unnao",
"city": "Kursath_U",
"climate": "Composite",
"code": 800933
},
{
"state": "Uttar Pradesh",
"district": "Unnao",
"city": "Maurawan",
"climate": "Composite",
"code": 800943
},
{
"state": "Uttar Pradesh",
"district": "Unnao",
"city": "Mohan",
"climate": "Composite",
"code": 800937
},
{
"state": "Uttar Pradesh",
"district": "Unnao",
"city": "Nawabganj",
"climate": "Composite",
"code": 800939
},
{
"state": "Uttar Pradesh",
"district": "Unnao",
"city": "Nyotini",
"climate": "Composite",
"code": 800938
},
{
"state": "Uttar Pradesh",
"district": "Unnao",
"city": "Purwa",
"climate": "Composite",
"code": 800942
},
{
"state": "Uttar Pradesh",
"district": "Unnao",
"city": "Rasulabad_U",
"climate": "Composite",
"code": 800936
},
{
"state": "Uttar Pradesh",
"district": "Unnao",
"city": "Safipur",
"climate": "Composite",
"code": 800932
},
{
"state": "Uttar Pradesh",
"district": "Unnao",
"city": "Ugu",
"climate": "Composite",
"code": 800931
},
{
"state": "Uttar Pradesh",
"district": "Unnao",
"city": "Unnao",
"climate": "Composite",
"code": 800940
},
{
"state": "Uttar Pradesh",
"district": "Varanasi",
"city": "Gangapur",
"climate": "Composite",
"code": 801232
},
{
"state": "Uttar Pradesh",
"district": "Varanasi",
"city": "Ramnagar",
"climate": "Composite",
"code": 801236
},
{
"state": "Uttar Pradesh",
"district": "Varanasi",
"city": "Varanasi",
"climate": "Composite",
"code": 801235
},
{
"state": "Uttar Pradesh",
"district": "Varanasi",
"city": "Varanasi Cantonment",
"climate": "Composite",
"code": 801233
},
{
"state": "Uttarakhand",
"district": "Almora",
"city": "Almora",
"climate": "Cold",
"code": 800327
},
{
"state": "Uttarakhand",
"district": "Almora",
"city": "Almora Cantonment",
"climate": "Cold",
"code": 800326
},
{
"state": "Uttarakhand",
"district": "Almora",
"city": "Bhikyasain",
"climate": "Cold",
"code": 900248
},
{
"state": "Uttarakhand",
"district": "Almora",
"city": "Chawkhutiya",
"climate": "Cold",
"code": 900604
},
{
"state": "Uttarakhand",
"district": "Almora",
"city": "Dwarhat",
"climate": "Cold",
"code": 800325
},
{
"state": "Uttarakhand",
"district": "Almora",
"city": "Ranikhet Cantonment",
"climate": "Cold",
"code": 800324
},
{
"state": "Uttarakhand",
"district": "Almora",
"city": "Ranikhet-Chiliyanaula",
"climate": "Cold",
"code": 900246
},
{
"state": "Uttarakhand",
"district": "Bageshwar",
"city": "Bageshwar",
"climate": "Cold",
"code": 800323
},
{
"state": "Uttarakhand",
"district": "Bageshwar",
"city": "Garud",
"climate": "Cold",
"code": 900849
},
{
"state": "Uttarakhand",
"district": "Bageshwar",
"city": "Kapkot",
"climate": "Cold",
"code": 900038
},
{
"state": "Uttarakhand",
"district": "Chamoli Gopeshwar",
"city": "Badrinath",
"climate": "Cold",
"code": 800290
},
{
"state": "Uttarakhand",
"district": "Chamoli Gopeshwar",
"city": "Chamoli-Gopeshwar",
"climate": "Cold",
"code": 800292
},
{
"state": "Uttarakhand",
"district": "Chamoli Gopeshwar",
"city": "Gairsain",
"climate": "Cold",
"code": 900032
},
{
"state": "Uttarakhand",
"district": "Chamoli Gopeshwar",
"city": "Gauchar",
"climate": "Cold",
"code": 800294
},
{
"state": "Uttarakhand",
"district": "Chamoli Gopeshwar",
"city": "Joshimath",
"climate": "Cold",
"code": 800291
},
{
"state": "Uttarakhand",
"district": "Chamoli Gopeshwar",
"city": "Karnaprayag",
"climate": "Cold",
"code": 800295
},
{
"state": "Uttarakhand",
"district": "Chamoli Gopeshwar",
"city": "Nandprayag",
"climate": "Cold",
"code": 800293
},
{
"state": "Uttarakhand",
"district": "Chamoli Gopeshwar",
"city": "Pipalkoti",
"climate": "Cold",
"code": 900438
},
{
"state": "Uttarakhand",
"district": "Chamoli Gopeshwar",
"city": "Pokhari",
"climate": "Cold",
"code": 900033
},
{
"state": "Uttarakhand",
"district": "Chamoli Gopeshwar",
"city": "Tharali",
"climate": "Cold",
"code": 900242
},
{
"state": "Uttarakhand",
"district": "Champawat",
"city": "Banbasa",
"climate": "Cold",
"code": 900110
},
{
"state": "Uttarakhand",
"district": "Champawat",
"city": "Champawat",
"climate": "Cold",
"code": 800328
},
{
"state": "Uttarakhand",
"district": "Champawat",
"city": "Lohaghat",
"climate": "Cold",
"code": 800329
},
{
"state": "Uttarakhand",
"district": "Champawat",
"city": "Tanakpur",
"climate": "Cold",
"code": 800330
},
{
"state": "Uttarakhand",
"district": "Dehradun",
"city": "Chakrata Cantonment",
"climate": "Composite",
"code": 800304
},
{
"state": "Uttarakhand",
"district": "Dehradun",
"city": "Clement Town Cantonment",
"climate": "Composite",
"code": 800311
},
{
"state": "Uttarakhand",
"district": "Dehradun",
"city": "Dehradun",
"climate": "Composite",
"code": 800309
},
{
"state": "Uttarakhand",
"district": "Dehradun",
"city": "Dehradun Cantonment",
"climate": "Composite",
"code": 800310
},
{
"state": "Uttarakhand",
"district": "Dehradun",
"city": "Doiwala",
"climate": "Composite",
"code": 800312
},
{
"state": "Uttarakhand",
"district": "Dehradun",
"city": "Herbertpur",
"climate": "Composite",
"code": 800306
},
{
"state": "Uttarakhand",
"district": "Dehradun",
"city": "Landour Cantonment",
"climate": "Composite",
"code": 800308
},
{
"state": "Uttarakhand",
"district": "Dehradun",
"city": "Mussoorie",
"climate": "Composite",
"code": 800307
},
{
"state": "Uttarakhand",
"district": "Dehradun",
"city": "Rishikesh",
"climate": "Composite",
"code": 800313
},
{
"state": "Uttarakhand",
"district": "Dehradun",
"city": "Selaqui",
"climate": "Composite",
"code": 900239
},
{
"state": "Uttarakhand",
"district": "Dehradun",
"city": "Vikasnagar",
"climate": "Composite",
"code": 800305
},
{
"state": "Uttarakhand",
"district": "Hardwar",
"city": "Bhagwanpur",
"climate": "Composite",
"code": 900112
},
{
"state": "Uttarakhand",
"district": "Hardwar",
"city": "Dhandhera",
"climate": "Composite",
"code": 900847
},
{
"state": "Uttarakhand",
"district": "Hardwar",
"city": "Hardwar",
"climate": "Composite",
"code": 800359
},
{
"state": "Uttarakhand",
"district": "Hardwar",
"city": "Imlikheda",
"climate": "Composite",
"code": 900844
},
{
"state": "Uttarakhand",
"district": "Hardwar",
"city": "Jhabrera",
"climate": "Composite",
"code": 800355
},
{
"state": "Uttarakhand",
"district": "Hardwar",
"city": "Laksar",
"climate": "Composite",
"code": 800360
},
{
"state": "Uttarakhand",
"district": "Hardwar",
"city": "Landhaura",
"climate": "Composite",
"code": 800357
},
{
"state": "Uttarakhand",
"district": "Hardwar",
"city": "Manglaur",
"climate": "Composite",
"code": 800356
},
{
"state": "Uttarakhand",
"district": "Hardwar",
"city": "Padli Gujjar",
"climate": "Composite",
"code": 900846
},
{
"state": "Uttarakhand",
"district": "Hardwar",
"city": "Piran Kaliyar",
"climate": "Composite",
"code": 900240
},
{
"state": "Uttarakhand",
"district": "Hardwar",
"city": "Rampur",
"climate": "Composite",
"code": 900845
},
{
"state": "Uttarakhand",
"district": "Hardwar",
"city": "Roorkee",
"climate": "Composite",
"code": 800353
},
{
"state": "Uttarakhand",
"district": "Hardwar",
"city": "Roorkee Cantonment",
"climate": "Composite",
"code": 800354
},
{
"state": "Uttarakhand",
"district": "Hardwar",
"city": "Shivalik Nagar",
"climate": "Composite",
"code": 900109
},
{
"state": "Uttarakhand",
"district": "Nainital",
"city": "Bhimtal",
"climate": "Composite",
"code": 800334
},
{
"state": "Uttarakhand",
"district": "Nainital",
"city": "Bhowali",
"climate": "Composite",
"code": 800333
},
{
"state": "Uttarakhand",
"district": "Nainital",
"city": "Haldwani",
"climate": "Composite",
"code": 800335
},
{
"state": "Uttarakhand",
"district": "Nainital",
"city": "Kaladhungi",
"climate": "Composite",
"code": 800337
},
{
"state": "Uttarakhand",
"district": "Nainital",
"city": "Lalkuan",
"climate": "Composite",
"code": 800338
},
{
"state": "Uttarakhand",
"district": "Nainital",
"city": "Nainital",
"climate": "Composite",
"code": 800331
},
{
"state": "Uttarakhand",
"district": "Nainital",
"city": "Nainital Cantonment",
"climate": "Composite",
"code": 800332
},
{
"state": "Uttarakhand",
"district": "Nainital",
"city": "Ramnagar_U",
"climate": "Composite",
"code": 800336
},
{
"state": "Uttarakhand",
"district": "Pauri Garhwal",
"city": "Dogadda",
"climate": "Composite",
"code": 800318
},
{
"state": "Uttarakhand",
"district": "Pauri Garhwal",
"city": "Kotdwara",
"climate": "Composite",
"code": 800319
},
{
"state": "Uttarakhand",
"district": "Pauri Garhwal",
"city": "Lansdowne Cantonment",
"climate": "Composite",
"code": 800317
},
{
"state": "Uttarakhand",
"district": "Pauri Garhwal",
"city": "Pauri",
"climate": "Composite",
"code": 800316
},
{
"state": "Uttarakhand",
"district": "Pauri Garhwal",
"city": "Satpuli",
"climate": "Composite",
"code": 900114
},
{
"state": "Uttarakhand",
"district": "Pauri Garhwal",
"city": "Srinagar",
"climate": "Composite",
"code": 800315
},
{
"state": "Uttarakhand",
"district": "Pauri Garhwal",
"city": "Swargashram",
"climate": "Composite",
"code": 900036
},
{
"state": "Uttarakhand",
"district": "Pauri Garhwal",
"city": "Thalisain",
"climate": "Composite",
"code": 900848
},
{
"state": "Uttarakhand",
"district": "Pithoragarh",
"city": "Berinag",
"climate": "Cold",
"code": 900111
},
{
"state": "Uttarakhand",
"district": "Pithoragarh",
"city": "Dharchula",
"climate": "Cold",
"code": 800320
},
{
"state": "Uttarakhand",
"district": "Pithoragarh",
"city": "Didihat",
"climate": "Cold",
"code": 800321
},
{
"state": "Uttarakhand",
"district": "Pithoragarh",
"city": "Gangolihat",
"climate": "Cold",
"code": 900037
},
{
"state": "Uttarakhand",
"district": "Pithoragarh",
"city": "Pithoragarh",
"climate": "Cold",
"code": 800322
},
{
"state": "Uttarakhand",
"district": "Rudraprayag",
"city": "Augustmuni",
"climate": "Cold",
"code": 900035
},
{
"state": "Uttarakhand",
"district": "Rudraprayag",
"city": "Kedarnath",
"climate": "Cold",
"code": 800296
},
{
"state": "Uttarakhand",
"district": "Rudraprayag",
"city": "Rudraprayag",
"climate": "Cold",
"code": 800297
},
{
"state": "Uttarakhand",
"district": "Rudraprayag",
"city": "Tilwara",
"climate": "Cold",
"code": 900440
},
{
"state": "Uttarakhand",
"district": "Rudraprayag",
"city": "Ukhimath",
"climate": "Cold",
"code": 900034
},
{
"state": "Uttarakhand",
"district": "Tehri",
"city": "Chamba_U",
"climate": "Cold",
"code": 800301
},
{
"state": "Uttarakhand",
"district": "Tehri",
"city": "Chamiyala",
"climate": "Cold",
"code": 900439
},
{
"state": "Uttarakhand",
"district": "Tehri",
"city": "Devaprayag",
"climate": "Cold",
"code": 800299
},
{
"state": "Uttarakhand",
"district": "Tehri",
"city": "Gaja",
"climate": "Cold",
"code": 900244
},
{
"state": "Uttarakhand",
"district": "Tehri",
"city": "Ghansali",
"climate": "Cold",
"code": 900113
},
{
"state": "Uttarakhand",
"district": "Tehri",
"city": "Kirtinagar",
"climate": "Cold",
"code": 800298
},
{
"state": "Uttarakhand",
"district": "Tehri",
"city": "Lamb Gaon",
"climate": "Cold",
"code": 900243
},
{
"state": "Uttarakhand",
"district": "Tehri",
"city": "Muni-Ki-Reti",
"climate": "Cold",
"code": 800303
},
{
"state": "Uttarakhand",
"district": "Tehri",
"city": "Narendranagar",
"climate": "Cold",
"code": 800302
},
{
"state": "Uttarakhand",
"district": "Tehri",
"city": "Tapovan",
"climate": "Cold",
"code": 900852
},
{
"state": "Uttarakhand",
"district": "Tehri",
"city": "Tehri",
"climate": "Cold",
"code": 800300
},
{
"state": "Uttarakhand",
"district": "Udhamsingh Nagar",
"city": "Bazpur",
"climate": "Composite",
"code": 800344
},
{
"state": "Uttarakhand",
"district": "Udhamsingh Nagar",
"city": "Dineshpur",
"climate": "Composite",
"code": 800349
},
{
"state": "Uttarakhand",
"district": "Udhamsingh Nagar",
"city": "Gadarpur",
"climate": "Composite",
"code": 800348
},
{
"state": "Uttarakhand",
"district": "Udhamsingh Nagar",
"city": "Gularbhoj",
"climate": "Composite",
"code": 900251
},
{
"state": "Uttarakhand",
"district": "Udhamsingh Nagar",
"city": "Jaspur",
"climate": "Composite",
"code": 800342
},
{
"state": "Uttarakhand",
"district": "Udhamsingh Nagar",
"city": "Kashipur",
"climate": "Composite",
"code": 800339
},
{
"state": "Uttarakhand",
"district": "Udhamsingh Nagar",
"city": "Kela Khera",
"climate": "Composite",
"code": 800345
},
{
"state": "Uttarakhand",
"district": "Udhamsingh Nagar",
"city": "Khatima",
"climate": "Composite",
"code": 800352
},
{
"state": "Uttarakhand",
"district": "Udhamsingh Nagar",
"city": "Kichha",
"climate": "Composite",
"code": 800347
},
{
"state": "Uttarakhand",
"district": "Udhamsingh Nagar",
"city": "Lalpur",
"climate": "Composite",
"code": 900851
},
{
"state": "Uttarakhand",
"district": "Udhamsingh Nagar",
"city": "Mahua Kheraganj",
"climate": "Composite",
"code": 800340
},
{
"state": "Uttarakhand",
"district": "Udhamsingh Nagar",
"city": "Mahuadabra",
"climate": "Composite",
"code": 800341
},
{
"state": "Uttarakhand",
"district": "Udhamsingh Nagar",
"city": "Nagla",
"climate": "Composite",
"code": 900850
},
{
"state": "Uttarakhand",
"district": "Udhamsingh Nagar",
"city": "Nanakamtta",
"climate": "Composite",
"code": 900250
},
{
"state": "Uttarakhand",
"district": "Udhamsingh Nagar",
"city": "Rudrapur",
"climate": "Composite",
"code": 800346
},
{
"state": "Uttarakhand",
"district": "Udhamsingh Nagar",
"city": "Shaktigarh",
"climate": "Composite",
"code": 800350
},
{
"state": "Uttarakhand",
"district": "Udhamsingh Nagar",
"city": "Sitarganj",
"climate": "Composite",
"code": 800351
},
{
"state": "Uttarakhand",
"district": "Udhamsingh Nagar",
"city": "Sultanpur_U",
"climate": "Composite",
"code": 800343
},
{
"state": "Uttarakhand",
"district": "Uttarkashi",
"city": "Barahat Uttarkashi",
"climate": "Cold",
"code": 800288
},
{
"state": "Uttarakhand",
"district": "Uttarkashi",
"city": "Barkot",
"climate": "Cold",
"code": 800287
},
{
"state": "Uttarakhand",
"district": "Uttarkashi",
"city": "Chimyalisaur",
"climate": "Cold",
"code": 900031
},
{
"state": "Uttarakhand",
"district": "Uttarkashi",
"city": "Gangotridham",
"climate": "Cold",
"code": 800289
},
{
"state": "Uttarakhand",
"district": "Uttarkashi",
"city": "Naugaon",
"climate": "Cold",
"code": 900241
},
{
"state": "Uttarakhand",
"district": "Uttarkashi",
"city": "Purola",
"climate": "Cold",
"code": 900030
},
{
"state": "West Bengal",
"district": "Bankura",
"city": "Bankura",
"climate": "Warm & humid",
"code": 801733
},
{
"state": "West Bengal",
"district": "Bankura",
"city": "Bishnupur_B",
"climate": "Warm & humid",
"code": 801735
},
{
"state": "West Bengal",
"district": "Bankura",
"city": "Sonamukhi",
"climate": "Warm & humid",
"code": 801734
},
{
"state": "West Bengal",
"district": "Barddhaman",
"city": "Asansol",
"climate": "Warm & humid",
"code": 801671
},
{
"state": "West Bengal",
"district": "Barddhaman",
"city": "Barddhaman",
"climate": "Warm & humid",
"code": 801678
},
{
"state": "West Bengal",
"district": "Barddhaman",
"city": "Dainhat",
"climate": "Warm & humid",
"code": 801676
},
{
"state": "West Bengal",
"district": "Barddhaman",
"city": "Durgapur",
"climate": "Warm & humid",
"code": 801674
},
{
"state": "West Bengal",
"district": "Barddhaman",
"city": "Guskara",
"climate": "Warm & humid",
"code": 801677
},
{
"state": "West Bengal",
"district": "Barddhaman",
"city": "Kalna",
"climate": "Warm & humid",
"code": 801679
},
{
"state": "West Bengal",
"district": "Barddhaman",
"city": "Katwa",
"climate": "Warm & humid",
"code": 801675
},
{
"state": "West Bengal",
"district": "Barddhaman",
"city": "Memari",
"climate": "Warm & humid",
"code": 801680
},
{
"state": "West Bengal",
"district": "Birbhum",
"city": "Bolpur",
"climate": "Warm & humid",
"code": 801669
},
{
"state": "West Bengal",
"district": "Birbhum",
"city": "Dubrajpur",
"climate": "Warm & humid",
"code": 801668
},
{
"state": "West Bengal",
"district": "Birbhum",
"city": "Nalhati",
"climate": "Warm & humid",
"code": 801664
},
{
"state": "West Bengal",
"district": "Birbhum",
"city": "Rampurhat",
"climate": "Warm & humid",
"code": 801665
},
{
"state": "West Bengal",
"district": "Birbhum",
"city": "Sainthia",
"climate": "Warm & humid",
"code": 801667
},
{
"state": "West Bengal",
"district": "Birbhum",
"city": "Suri",
"climate": "Warm & humid",
"code": 801666
},
{
"state": "West Bengal",
"district": "Dakshin Dinajpur",
"city": "Balurghat",
"climate": "Warm & humid",
"code": 801654
},
{
"state": "West Bengal",
"district": "Dakshin Dinajpur",
"city": "Buniadpur",
"climate": "Warm & humid",
"code": 900142
},
{
"state": "West Bengal",
"district": "Dakshin Dinajpur",
"city": "Gangarampur",
"climate": "Warm & humid",
"code": 801653
},
{
"state": "West Bengal",
"district": "Darjeeling",
"city": "Darjiling",
"climate": "Warm & humid",
"code": 801634
},
{
"state": "West Bengal",
"district": "Darjeeling",
"city": "Jalapahar Cantonment",
"climate": "Warm & humid",
"code": 900480
},
{
"state": "West Bengal",
"district": "Darjeeling",
"city": "Kalimpong",
"climate": "Warm & humid",
"code": 801635
},
{
"state": "West Bengal",
"district": "Darjeeling",
"city": "Kurseong",
"climate": "Warm & humid",
"code": 801637
},
{
"state": "West Bengal",
"district": "Darjeeling",
"city": "Lebong Cantonment",
"climate": "Warm & humid",
"code": 900481
},
{
"state": "West Bengal",
"district": "Darjeeling",
"city": "Mirik",
"climate": "Warm & humid",
"code": 801636
},
{
"state": "West Bengal",
"district": "Darjeeling",
"city": "Siliguri",
"climate": "Warm & humid",
"code": 801638
},
{
"state": "West Bengal",
"district": "Howrah",
"city": "Bally",
"climate": "Warm & humid",
"code": 801739
},
{
"state": "West Bengal",
"district": "Howrah",
"city": "Haora",
"climate": "Warm & humid",
"code": 801740
},
{
"state": "West Bengal",
"district": "Howrah",
"city": "Uluberia",
"climate": "Warm & humid",
"code": 801741
},
{
"state": "West Bengal",
"district": "Hugli-Chinsurah",
"city": "Arambag",
"climate": "Warm & humid",
"code": 801724
},
{
"state": "West Bengal",
"district": "Hugli-Chinsurah",
"city": "Baidyabati",
"climate": "Warm & humid",
"code": 801727
},
{
"state": "West Bengal",
"district": "Hugli-Chinsurah",
"city": "Bansberia",
"climate": "Warm & humid",
"code": 801720
},
{
"state": "West Bengal",
"district": "Hugli-Chinsurah",
"city": "Bhadreswar",
"climate": "Warm & humid",
"code": 801725
},
{
"state": "West Bengal",
"district": "Hugli-Chinsurah",
"city": "Champdani",
"climate": "Warm & humid",
"code": 801726
},
{
"state": "West Bengal",
"district": "Hugli-Chinsurah",
"city": "Chandannagar",
"climate": "Warm & humid",
"code": 801722
},
{
"state": "West Bengal",
"district": "Hugli-Chinsurah",
"city": "Dankuni",
"climate": "Warm & humid",
"code": 801731
},
{
"state": "West Bengal",
"district": "Hugli-Chinsurah",
"city": "Hugli-Chinsurah",
"climate": "Warm & humid",
"code": 801721
},
{
"state": "West Bengal",
"district": "Hugli-Chinsurah",
"city": "Konnagar",
"climate": "Warm & humid",
"code": 801730
},
{
"state": "West Bengal",
"district": "Hugli-Chinsurah",
"city": "Rishra",
"climate": "Warm & humid",
"code": 801729
},
{
"state": "West Bengal",
"district": "Hugli-Chinsurah",
"city": "Serampore",
"climate": "Warm & humid",
"code": 801728
},
{
"state": "West Bengal",
"district": "Hugli-Chinsurah",
"city": "Tarakeswar",
"climate": "Warm & humid",
"code": 801723
},
{
"state": "West Bengal",
"district": "Hugli-Chinsurah",
"city": "Uttarpara Kotrung",
"climate": "Warm & humid",
"code": 801732
},
{
"state": "West Bengal",
"district": "Jalpaiguri",
"city": "Alipurduar",
"climate": "Warm & humid",
"code": 801642
},
{
"state": "West Bengal",
"district": "Jalpaiguri",
"city": "Dhupguri",
"climate": "Warm & humid",
"code": 801641
},
{
"state": "West Bengal",
"district": "Jalpaiguri",
"city": "Jalpaiguri",
"climate": "Warm & humid",
"code": 801640
},
{
"state": "West Bengal",
"district": "Jalpaiguri",
"city": "Mal",
"climate": "Warm & humid",
"code": 801639
},
{
"state": "West Bengal",
"district": "Koch Bihar",
"city": "Dinhata",
"climate": "Warm & humid",
"code": 801648
},
{
"state": "West Bengal",
"district": "Koch Bihar",
"city": "Haldibari",
"climate": "Warm & humid",
"code": 801643
},
{
"state": "West Bengal",
"district": "Koch Bihar",
"city": "Koch Bihar",
"climate": "Warm & humid",
"code": 801646
},
{
"state": "West Bengal",
"district": "Koch Bihar",
"city": "Mathabhanga",
"climate": "Warm & humid",
"code": 801645
},
{
"state": "West Bengal",
"district": "Koch Bihar",
"city": "Mekliganj",
"climate": "Warm & humid",
"code": 801644
},
{
"state": "West Bengal",
"district": "Koch Bihar",
"city": "Tufanganj",
"climate": "Warm & humid",
"code": 801647
},
{
"state": "West Bengal",
"district": "Kolkata",
"city": "Kolkata",
"climate": "Warm & humid",
"code": 801742
},
{
"state": "West Bengal",
"district": "Maldah",
"city": "EnglishÃ¢Â Bazar",
"climate": "Warm & humid",
"code": 801656
},
{
"state": "West Bengal",
"district": "Maldah",
"city": "Old Maldah",
"climate": "Warm & humid",
"code": 801655
},
{
"state": "West Bengal",
"district": "Murshidabad",
"city": "Beldanga",
"climate": "Warm & humid",
"code": 801663
},
{
"state": "West Bengal",
"district": "Murshidabad",
"city": "Berhampore",
"climate": "Warm & humid",
"code": 801662
},
{
"state": "West Bengal",
"district": "Murshidabad",
"city": "Dhulian",
"climate": "Warm & humid",
"code": 801657
},
{
"state": "West Bengal",
"district": "Murshidabad",
"city": "Domkal",
"climate": "Warm & humid",
"code": 900141
},
{
"state": "West Bengal",
"district": "Murshidabad",
"city": "Jangipur",
"climate": "Warm & humid",
"code": 801658
},
{
"state": "West Bengal",
"district": "Murshidabad",
"city": "Jiaganj-Azimganj",
"climate": "Warm & humid",
"code": 801659
},
{
"state": "West Bengal",
"district": "Murshidabad",
"city": "Kandi",
"climate": "Warm & humid",
"code": 801661
},
{
"state": "West Bengal",
"district": "Murshidabad",
"city": "Murshidabad",
"climate": "Warm & humid",
"code": 801660
},
{
"state": "West Bengal",
"district": "Nadia",
"city": "Birnagar",
"climate": "Warm & humid",
"code": 801685
},
{
"state": "West Bengal",
"district": "Nadia",
"city": "Chakdaha",
"climate": "Warm & humid",
"code": 801688
},
{
"state": "West Bengal",
"district": "Nadia",
"city": "Cooper'S Camp",
"climate": "Warm & humid",
"code": 801687
},
{
"state": "West Bengal",
"district": "Nadia",
"city": "Gayespur",
"climate": "Warm & humid",
"code": 801690
},
{
"state": "West Bengal",
"district": "Nadia",
"city": "Haringhata",
"climate": "Warm & humid",
"code": 900140
},
{
"state": "West Bengal",
"district": "Nadia",
"city": "Kalyani",
"climate": "Warm & humid",
"code": 801689
},
{
"state": "West Bengal",
"district": "Nadia",
"city": "Krishnanagar",
"climate": "Warm & humid",
"code": 801682
},
{
"state": "West Bengal",
"district": "Nadia",
"city": "Nabadwip",
"climate": "Warm & humid",
"code": 801681
},
{
"state": "West Bengal",
"district": "Nadia",
"city": "Ranaghat",
"climate": "Warm & humid",
"code": 801686
},
{
"state": "West Bengal",
"district": "Nadia",
"city": "Santipur",
"climate": "Warm & humid",
"code": 801683
},
{
"state": "West Bengal",
"district": "Nadia",
"city": "Taherpur",
"climate": "Warm & humid",
"code": 801684
},
{
"state": "West Bengal",
"district": "North 24 Paraganas",
"city": "Ashokenagar Kalyangarh",
"climate": "Warm & humid",
"code": 801698
},
{
"state": "West Bengal",
"district": "North 24 Paraganas",
"city": "Baduria",
"climate": "Warm & humid",
"code": 801706
},
{
"state": "West Bengal",
"district": "North 24 Paraganas",
"city": "Baranagar",
"climate": "Warm & humid",
"code": 801712
},
{
"state": "West Bengal",
"district": "North 24 Paraganas",
"city": "Barasat",
"climate": "Warm & humid",
"code": 801707
},
{
"state": "West Bengal",
"district": "North 24 Paraganas",
"city": "Barrackpore",
"climate": "Warm & humid",
"code": 801702
},
{
"state": "West Bengal",
"district": "North 24 Paraganas",
"city": "Barrackpore Cantonment",
"climate": "Warm & humid",
"code": 801701
},
{
"state": "West Bengal",
"district": "North 24 Paraganas",
"city": "Basirhat",
"climate": "Warm & humid",
"code": 801718
},
{
"state": "West Bengal",
"district": "North 24 Paraganas",
"city": "Bhatpara",
"climate": "Warm & humid",
"code": 801695
},
{
"state": "West Bengal",
"district": "North 24 Paraganas",
"city": "Bidhannagar",
"climate": "Warm & humid",
"code": 801716
},
{
"state": "West Bengal",
"district": "North 24 Paraganas",
"city": "Bongaon",
"climate": "Warm & humid",
"code": 801691
},
{
"state": "West Bengal",
"district": "North 24 Paraganas",
"city": "Dum Dum",
"climate": "Warm & humid",
"code": 801713
},
{
"state": "West Bengal",
"district": "North 24 Paraganas",
"city": "Garulia",
"climate": "Warm & humid",
"code": 801699
},
{
"state": "West Bengal",
"district": "North 24 Paraganas",
"city": "Gobardanga",
"climate": "Warm & humid",
"code": 801696
},
{
"state": "West Bengal",
"district": "North 24 Paraganas",
"city": "Habra",
"climate": "Warm & humid",
"code": 801697
},
{
"state": "West Bengal",
"district": "North 24 Paraganas",
"city": "Halisahar",
"climate": "Warm & humid",
"code": 801692
},
{
"state": "West Bengal",
"district": "North 24 Paraganas",
"city": "Kamarhati",
"climate": "Warm & humid",
"code": 801711
},
{
"state": "West Bengal",
"district": "North 24 Paraganas",
"city": "Kanchrapara",
"climate": "Warm & humid",
"code": 801693
},
{
"state": "West Bengal",
"district": "North 24 Paraganas",
"city": "Khardah",
"climate": "Warm & humid",
"code": 801704
},
{
"state": "West Bengal",
"district": "North 24 Paraganas",
"city": "Madhyamgram",
"climate": "Warm & humid",
"code": 801708
},
{
"state": "West Bengal",
"district": "North 24 Paraganas",
"city": "Naihati",
"climate": "Warm & humid",
"code": 801694
},
{
"state": "West Bengal",
"district": "North 24 Paraganas",
"city": "New Barrackpore",
"climate": "Warm & humid",
"code": 801709
},
{
"state": "West Bengal",
"district": "North 24 Paraganas",
"city": "North Barrackpore",
"climate": "Warm & humid",
"code": 801700
},
{
"state": "West Bengal",
"district": "North 24 Paraganas",
"city": "North Dumdum",
"climate": "Warm & humid",
"code": 801710
},
{
"state": "West Bengal",
"district": "North 24 Paraganas",
"city": "Panihati",
"climate": "Warm & humid",
"code": 801705
},
{
"state": "West Bengal",
"district": "North 24 Paraganas",
"city": "South Dumdum",
"climate": "Warm & humid",
"code": 801714
},
{
"state": "West Bengal",
"district": "North 24 Paraganas",
"city": "Taki",
"climate": "Warm & humid",
"code": 801719
},
{
"state": "West Bengal",
"district": "North 24 Paraganas",
"city": "Titagarh",
"climate": "Warm & humid",
"code": 801703
},
{
"state": "West Bengal",
"district": "Paschim Medinipur",
"city": "Chandrakona",
"climate": "Warm & humid",
"code": 801752
},
{
"state": "West Bengal",
"district": "Paschim Medinipur",
"city": "Ghatal",
"climate": "Warm & humid",
"code": 801754
},
{
"state": "West Bengal",
"district": "Paschim Medinipur",
"city": "Jhargram",
"climate": "Warm & humid",
"code": 801756
},
{
"state": "West Bengal",
"district": "Paschim Medinipur",
"city": "Kharagpur",
"climate": "Warm & humid",
"code": 801757
},
{
"state": "West Bengal",
"district": "Paschim Medinipur",
"city": "Kharar_Pm",
"climate": "Warm & humid",
"code": 801753
},
{
"state": "West Bengal",
"district": "Paschim Medinipur",
"city": "Kshirpai",
"climate": "Warm & humid",
"code": 801751
},
{
"state": "West Bengal",
"district": "Paschim Medinipur",
"city": "Medinipur",
"climate": "Warm & humid",
"code": 801755
},
{
"state": "West Bengal",
"district": "Paschim Medinipur",
"city": "Ramjibanpur",
"climate": "Warm & humid",
"code": 801750
},
{
"state": "West Bengal",
"district": "Purba Midnapur",
"city": "Contai",
"climate": "Warm & humid",
"code": 801762
},
{
"state": "West Bengal",
"district": "Purba Midnapur",
"city": "Egra",
"climate": "Warm & humid",
"code": 801761
},
{
"state": "West Bengal",
"district": "Purba Midnapur",
"city": "Haldia",
"climate": "Warm & humid",
"code": 801760
},
{
"state": "West Bengal",
"district": "Purba Midnapur",
"city": "Panskura",
"climate": "Warm & humid",
"code": 801758
},
{
"state": "West Bengal",
"district": "Purba Midnapur",
"city": "Tamralipta",
"climate": "Warm & humid",
"code": 801759
},
{
"state": "West Bengal",
"district": "Puruliya",
"city": "Jhalda",
"climate": "Composite",
"code": 801736
},
{
"state": "West Bengal",
"district": "Puruliya",
"city": "Puruliya",
"climate": "Composite",
"code": 801738
},
{
"state": "West Bengal",
"district": "Puruliya",
"city": "Raghunathpur",
"climate": "Composite",
"code": 801737
},
{
"state": "West Bengal",
"district": "South 24 Paragnas",
"city": "Baruipur",
"climate": "Warm & humid",
"code": 801747
},
{
"state": "West Bengal",
"district": "South 24 Paragnas",
"city": "Budge Budge",
"climate": "Warm & humid",
"code": 801744
},
{
"state": "West Bengal",
"district": "South 24 Paragnas",
"city": "Diamond Harbour",
"climate": "Warm & humid",
"code": 801748
},
{
"state": "West Bengal",
"district": "South 24 Paragnas",
"city": "Jaynagar Mazilpur",
"climate": "Warm & humid",
"code": 801749
},
{
"state": "West Bengal",
"district": "South 24 Paragnas",
"city": "Maheshtala",
"climate": "Warm & humid",
"code": 801743
},
{
"state": "West Bengal",
"district": "South 24 Paragnas",
"city": "Pujali",
"climate": "Warm & humid",
"code": 801745
},
{
"state": "West Bengal",
"district": "South 24 Paragnas",
"city": "Rajpur Sonarpur",
"climate": "Warm & humid",
"code": 801746
},
{
"state": "West Bengal",
"district": "Uttar Dinajpur",
"city": "Dalkhola",
"climate": "Warm & humid",
"code": 801650
},
{
"state": "West Bengal",
"district": "Uttar Dinajpur",
"city": "Islampur",
"climate": "Warm & humid",
"code": 801649
},
{
"state": "West Bengal",
"district": "Uttar Dinajpur",
"city": "Kaliaganj",
"climate": "Warm & humid",
"code": 801652
},
{
"state": "West Bengal",
"district": "Uttar Dinajpur",
"city": "Raiganj",
"climate": "Warm & humid",
"code": 801651
}
]

# Pre-computed indexes (built once at import)
STATES = sorted({c["state"] for c in INDIA_CITIES})

def cities_for_state(state):
    return [c for c in INDIA_CITIES if c["state"] == state]

def cities_for_district(state, district):
    return [c for c in INDIA_CITIES if c["state"] == state and c["district"] == district]

def lookup_city(state, district, city):
    for c in INDIA_CITIES:
        if c["state"] == state and c["district"] == district and c["city"] == city:
            return c
    return None
