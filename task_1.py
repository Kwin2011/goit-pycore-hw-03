import re
from datetime import datetime, date

dataNow = datetime.today().date()
print("Сьогоднішня дата:", dataNow)

def validate_date(date_str):
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", date_str):
        return False, "Неправильний формат. Використовуйте формат РРРР-ММ-ДД."
    
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return True, "Дата правильна."
    except ValueError:
        return False, "Неправильна дата. Перевірте значення місяця та дня."

def get_days_from_today(data_str):
    year, month, day = map(int, data_str.split("-"))
    delta = dataNow - date(year, month, day)
    return abs(delta.days) # завжди позитивне число""""""

data_str = input("Enter date РРРР-ММ-ДД >> ")
is_valid, message = validate_date(data_str)

while not is_valid:
    print(message)
    data_str = input("Enter your year, months, and day (separated by dash as ): РРРР-ММ-ДД >> ")
    is_valid, message = validate_date(data_str)

print("Введена дата:", data_str)

days_difference = get_days_from_today(data_str)
print("Кількість днів від сьогодні до введеної дати:",  days_difference)