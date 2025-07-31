##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas as pd
import random
import smtplib

DUMMY_MAIL = "babzie_python@gmail.com"
DUMMY_PASSWORD = "broski5639$%%#@b_"


today = (dt.datetime.now().month, dt.datetime.now().day)

data = pd.read_csv("birthdays.csv")
new_dict = {(data_row["month"], data_row["day"]):data_row for (index, data_row) in data.iterrows()}


if today in new_dict:
    person = new_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter:
        content = letter.read()
        new_content = content.replace("[NAME]", person["name"])
        print(new_content)


# 4. Send the letter generated in step 3 to that person's email address.
with smtplib.SMTP("mail.guerrillamail.com") as connection:
    connection.starttls()
    connection.login(user=DUMMY_MAIL, password=DUMMY_PASSWORD)
    connection.sendmail(from_addr=DUMMY_MAIL,
                        to_addrs="facebook@gmail.com",
                        msg=f"Subject: Happy Birthday!\n\n {new_content}"
                        )



