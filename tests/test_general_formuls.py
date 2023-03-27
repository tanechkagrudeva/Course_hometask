import json
from datetime import datetime

filename = "operations.json"
with open(filename, "r", encoding='utf-8') as file:
        data = json.load(file)

def sort():
    user_info = []
    for item in data:
        if item.get('date') == "EXECUTED":
            user_info.append(item)
        user_info.sort(key=lambda x:x.get("date"), reverse=True)
        return user_info

def correct_date():
    date = sort(str(datetime.strptime(['date'][0:10], '%Y-%m-%d')))
    return date

correct_date()