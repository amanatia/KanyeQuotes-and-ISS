import requests
from datetime import datetime
import smtplib 
import time

my_email = "fanaraamantia@gmail.com"
my_password = "reossoebhyezpmro"

MY_LAT = 40.640064 # Your latitude
MY_LONG = 22.944420 # Your longitude

def is_iss_overhead(): 
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if   45 >= int(iss_latitude) >= 35 and 27 >= int(iss_longitude) >= 17:
        return True

#Your position is within +5 or -5 degrees of the ISS position.

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    
    if time_now >= sunset or time_now <= sunrise:
        return True

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        print("Look up")
    '''with smtplib.SMTP("smtp.gmail.com") as connection :  
        connection.starttls() # if somebody intersepts our email then the message will be encripted for them because startls is enabled
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="amantiafanara@outlook.com", msg=f"Subject: iss\n\n Look up!")
    '''
