import requests
import smtplib

with open("secret.txt", "r") as file:
    new_file = file.readlines()

DUMMY_MAIL = "babzie_python@gmail.com"
DUMMY_PASSWORD = "broski5639$%%#@b_"


parameters = {
    "lat" : 5.958650,
    "lon" : 10.147510,
    "appid" : new_file[1],
    "cnt" : 4
}

response = requests.get("http://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
new_response = response.json()


id_code_for_12hour = new_response["list"][3]["weather"][0]["id"]
if id_code_for_12hour < 700:
    with smtplib.SMTP("mail.guerrillamail.com") as connection:
        connection.starttls()
        connection.login(user=DUMMY_MAIL, password=DUMMY_PASSWORD)
        connection.sendmail(from_addr=DUMMY_MAIL,
                            to_addrs="facebook@gmail.com",
                            msg=f"Subject: Happy Birthday!\n\n Bring an Umbrella! It's going to rain"
                            )
