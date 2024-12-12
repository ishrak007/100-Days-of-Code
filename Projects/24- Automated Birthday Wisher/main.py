################################ imports ################################
import datetime as dt
import random
import smtplib

############################### date today ################################
today = dt.datetime.now()
cur_month = today.month
cur_day = today.day

######################## checking for birthdays ########################
bday_peeps = []

with open(r"/home/ishrak114/Automated Birthday Wisher/birthdays.csv") as csv_file:
    bday_info = csv_file.readlines()[1:]

for row in bday_info:
    info = row.replace("\n", "").split(",")
    if int(info[3]) == cur_month and int(info[4]) == cur_day:
        bday_peeps.append(info)

############### selecting letter if there are birthdays today #################
letters = []
if bday_peeps:
    chosen = random.choice(["letter_1", "letter_2", "letter_3"])
    with open(f"/home/ishrak114/Automated Birthday Wisher/letter_templates/{chosen}.txt") as txt_file:
        letter = txt_file.readlines()
        for person in bday_peeps:
            custom_letter = letter.copy()
            name = person[0]
            email = person[1]
            custom_letter[0] = custom_letter[0].replace("[NAME]", name)
            custom_letter = "".join(custom_letter)
            letter_dict = {}
            letter_dict["message"] = custom_letter
            letter_dict["address"] = email
            letters.append(letter_dict)
# print(letters)

######################### sending birthday email ##########################
if bday_peeps:

    # dummy mail credentials
    my_email = "testmailkabir137@gmail.com"
    password = "zruq cpby ftax tybm"

    # sending the mail
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        
        # setting up Transport Layer Security (TLS)
        connection.starttls()
        
        # logging in via smtplib
        connection.login(user=my_email, password=password)
        
        # emailing the message
        for letter in letters:
            msg_body = letter["message"]
            msg_address = letter["address"]
            msg = f"Subject: Wish Letter for your special day <3 \n\n{msg_body}"
            # print(msg)
            connection.sendmail(from_addr=my_email, 
                                to_addrs=msg_address, 
                                msg=msg
                                )
    

    
