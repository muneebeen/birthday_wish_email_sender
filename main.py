import smtplib
import datetime as dt
import random
import pandas as pd
import os


def send_email(quote):
    email = "Use Your Email"
    password = "Use Your Pass"  # This password is generated after creating an app password from gmail account settings.
    print(f"I am in send email method. Quote is {quote}")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=email, msg=f"Subject: Birthday Wish\n\n {quote}")


def random_letter():
    letters = os.listdir("./letter_templates")
    random_file = random.choice(letters)
    return random_file


now = dt.datetime.now()
month = now.today().month
day = now.today().day
name = ""
data = pd.read_csv("birthdays.csv").to_dict("records")
for record in data:
    if record["month"] == month and record["day"] == day:
        name = record["name"]
        random_file = random_letter()
        file_path = f"./letter_templates/{random_file}"
        with open(file_path, 'r') as f:
            content = f.read()
            updated_content = content.replace("[NAME]", name)
            print("Updated Content", updated_content, end="\n")
        send_email(updated_content)

