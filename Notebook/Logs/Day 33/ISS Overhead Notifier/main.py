#--------------------------------- TASK ---------------------------------
# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

import requests
from datetime import datetime
import smtplib
import time

# My Latitude & Longitude
MY_LAT = -48 # 23.810331 
MY_LONG = 0 # 90.412521

# Dummy Mail Credentials
MY_EMAIL = "testmailkabir137@gmail.com"
PASSWORD = "zruq cpby ftax tybm"
SEND_TO = "ikabir125@gmail.com"

def iss_checker(lat_iss, long_iss, hour_now, sunrise, sunset):
    if abs(lat_iss - MY_LAT) <= 5 and abs(long_iss - MY_LONG) <= 5:
        # Checking for positions within +5 or -5 degrees of the ISS position
        if hour_now > sunset or hour_now < sunrise:
            print("Sending Mail...")
            # sending the mail
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                
                # setting up Transport Layer Security (TLS)
                connection.starttls()
                
                # logging in via smtplib
                connection.login(user=MY_EMAIL, password=PASSWORD)
                
                # notifying via email
                msg_body = "Satellite is passing over the roof.\nLOOK UP!!"
                msg = f"Subject: ISS OVERHEAD!! \n\n{msg_body}"
                connection.sendmail(from_addr=MY_EMAIL, 
                                    to_addrs=SEND_TO, 
                                    msg=msg
                                    )
                
                print("Mail Sent")

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
print(iss_latitude, iss_longitude)

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

hour_now = 22 # datetime.now().hour
print(sunrise, sunset, hour_now)

while True:
    time.sleep(60)
    iss_checker(iss_latitude, iss_longitude, hour_now, sunrise, sunset)

