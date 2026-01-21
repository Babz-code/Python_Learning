import smtplib

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        #Fake emails & password
        self.MY_EMAIL = "babzie_code@gmail.com"
        self.MY_PASSWORD = "asije83t7gyhdbn"

    def send_mail(self, customer_email, origin, destination, price):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(self.MY_EMAIL, self.MY_PASSWORD)
            for email in customer_email:
                connection.sendmail(
                    from_addr=self.MY_EMAIL,
                    to_addrs=self.MY_EMAIL,
                    msg=f"Subject:Cheap Flight Deals\n\nLow Price Alerts! Only {price} to fly from {origin} to {destination}")
