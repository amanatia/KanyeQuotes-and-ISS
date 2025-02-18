import requests
from datetime import datetime

LATITUDE = 40.634781
LONGITUDE = 22.943090

parameters = {
    "lat" : LATITUDE, 
    "lng" : LONGITUDE,
    "formatted": 0,
}

response = requests.get("http://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

# print(sunrise.split("T")[1].split(":")[0])  seperates the time from the date we get the hour 

print(f"sunrise: {sunrise}")
print(f"sunset: {sunset}")

time = datetime.now()

print(f"time: {time.hour}")