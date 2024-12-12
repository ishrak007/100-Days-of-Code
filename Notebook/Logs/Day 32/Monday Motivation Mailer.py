import smtplib
import datetime as dt
import random

# dummy mail credentials
my_email = "testmailkabir137@gmail.com"
password = "zruq cpby ftax tybm"

# datetime
now = dt.datetime.now()
weekday = now.weekday()

# quote picker
with open(r"Projects\24- Automated Birthday Wisher\quotes.txt", "r") as quote_diary:
    quotes = quote_diary.readlines()
quote = random.choice(quotes)

# email msg
msg_body = quote
msg = f"Subject: Inspiring your day \n\n{msg_body}"

# email sender
if weekday == 0:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls() # tls is Transport Layer Security
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, 
                            to_addrs="ikabir125@gmail.com", 
                            msg=msg
                            )

