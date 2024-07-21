import re

def normalize_phone(phone_number):
    # print(f"in>>> {phone_number}")
    # Лишаємо тільки фифри і плюс
    cleaned_number = re.sub(r'[^\d+]', '', phone_number)
    print(cleaned_number)
    # Перевіряємо, чи номер починається з '+'
    if cleaned_number.startswith('+'):
        # Якщо номер вже містить міжнародний код, то видаляємо зайві '0' після коду
        if cleaned_number.startswith('+3800'):
            cleaned_number = '+38' + cleaned_number[4:]
    else:
        # Якщо міжнародний код відсутній, додаємо код '+38'
        if cleaned_number.startswith('380'):
            cleaned_number = '+380' + cleaned_number[3:]
        else:
            cleaned_number = '+38' + cleaned_number
    # print(f"out>>> {phone_number}" , )
    return cleaned_number

# Source
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

# Done
print("Нормалізовані номери телефонів для SMS-розсилки:")
[print(num) for num in sanitized_numbers]
