# test-script.py
import openmeteo_requests
import requests_cache
from retry_requests import retry

# Set up the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important
# to assign them correctly below
url = "https://air-quality-api.open-meteo.com/v1/air-quality"
params = {
  "latitude": 44.0582,
  "longitude": -121.3153,
  "current": ["pm10", "pm2_5"],
  "timezone": "America/Los_Angeles"
}
responses = openmeteo.weather_api(url, params=params)

# Process first location.
response = responses[0]
print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
print(f"Elevation {response.Elevation()} m asl")
print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

# Current values. The order of variables needs to be the same as requested.
current = response.Current()
current_pm10 = current.Variables(0).Value()
current_pm2_5 = current.Variables(1).Value()

print(f"Current time {current.Time()}")
print(f"Current pm10 {current_pm10}")
print(f"Current pm2_5 {current_pm2_5}")