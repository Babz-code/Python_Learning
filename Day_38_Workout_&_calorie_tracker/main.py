import requests
import datetime as dt
import os


API_KEY = os.environ.get("NUT_API_KEY")
APP_ID = os.environ.get("NUT_API_ID")
NUTRITION_EP = "https://trackapi.nutritionix.com/v2/natural/exercise"
AGE = 28
HEIGHT = 175
WEIGHT = 80

user_exercise = input("Tell me which exercise you did?\n")

# Getting response from NutritionApi
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": user_exercise,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=NUTRITION_EP, json=parameters, headers=headers)
formatted_response = response.json()["exercises"][0]
exercise = formatted_response["name"].title()
duration = formatted_response["duration_min"]
calories = formatted_response["nf_calories"]

# Getting the date and time
today = dt.datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%X")


# Adding new rows to the spreadsheet
SHEETY_EP = os.environ.get("SHEETY_EP")
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")

sheet_parameters = {
  "workout": {
      "date": date,
      "time": time,
      "exercise": exercise,
      "duration": duration,
      "calories": calories
  }
}

headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

add_row = requests.post(url=SHEETY_EP, json=sheet_parameters, headers=headers)
print(add_row.text)

