# Google-Maps-API-Utility
Utility to extract one-offs custom output by using Google Maps API

# How to
## Install the required libraries (GoogleMaps SDK and othere dependencies)
```
pip install -r requirements.txt
```
## Fetch Google Maps API key from Google developer console
```
https://console.cloud.google.com/apis/credentials
```
## Add Google API Key to environment variable from terminal or IDE
```
EXPORT GOOGLE_MAPS_CREDENTIAL='<YOUR API KEY>'
```
## Run the existing one off jobs from the jobs folder
```
python jobs/update_store_lat_long.py
```
