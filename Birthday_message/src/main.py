from twilio.rest import Client
import os
from datetime import datetime
import json
from keys import Keys


client = Client(Keys.account_sid, Keys.auth_token)

def get_current_date():
    current_date = datetime.now()
    return current_date.strftime("%d-%m")

def get_birthday_list_by_date(date: str):
    try:
        birthdays: dict
        file_path = os.path.join(os.path.dirname(__file__), 'birthdays.json')
        with open(file_path, "r") as file_pointer:
            birthdays = json.load(file_pointer)
        return birthdays[date]
    except:
        raise ValueError("JSON file is empty")

if __name__ == "__main__":
    current_date = get_current_date()
    persons_list= get_birthday_list_by_date(current_date)
    if current_date == "01-06":
        message = client.messages.create(
            body="Congratulations, it's your birthday",
            from_=Keys.twilio_number,
            to=Keys.target_number,
        )
    elif persons_list:
        message = client.messages.create(
            body=f"Birthdays: {', '.join(person for person in persons_list)}",
            from_=Keys.twilio_number,
            to=Keys.target_number,
        )
