from datetime import datetime, timedelta
# # Алгоритм враховує +7 днів від поточної дати, а також потім окремо враховуються чи дата випадає суботу та неділю.

def get_upcoming_birthdays(users):
    # Отримуємо поточну дату
    today = datetime.today().date()
    # Визначаємо поточний день тижня (0 - понеділок, 6 - неділя)
    curent_weekday = today.weekday()
    upcoming_birthdays = []
    
    for user in users:
        # Конвертуємо рядок з датою народження у об'єкт datetime.date
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        # Змінюємо рік дати народження на поточний рік
        birthday_this_year = birthday.replace(year=today.year)
        
        # Якщо день народження вже пройшов цього року, розглядаємо дату на наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        # Визначаємо різницю у днях між сьогоднішньою датою та датою дня народження
        delta_days = (birthday_this_year - today).days
        
        # Перевіряємо, чи випадає день народження на наступні 7 днів включно з поточним днем
        if 0 <= delta_days <= 7:
            congratulation_date = birthday_this_year
            
            # Якщо день народження випадає на вихідний, переносимо його на наступний понеділок
            if congratulation_date.weekday() == 5:  # Субота
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:  # Неділя
                congratulation_date += timedelta(days=1)
                
            # Додаємо ім'я користувача та дату привітання до списку результатів
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    
    return upcoming_birthdays

# Для більшеї наглядності згенерована більша база співробітників

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Alice Johnson", "birthday": "1987.02.15"},
    {"name": "Bob Brown", "birthday": "1992.03.02"},
    {"name": "Charlie Davis", "birthday": "1984.04.10"},
    {"name": "Diana Evans", "birthday": "1991.05.20"},
    {"name": "Eve Harris", "birthday": "1989.06.30"},
    {"name": "Frank Green", "birthday": "1986.07.05"},
    {"name": "Grace Hall", "birthday": "1983.07.14"},
    {"name": "Hank Wright", "birthday": "1994.07.22"},
    {"name": "Ivy Clark", "birthday": "1993.10.01"},
    {"name": "Jack Turner", "birthday": "1988.11.19"},
    {"name": "Kate Young", "birthday": "1985.12.25"},
    {"name": "Leo Scott", "birthday": "1982.01.07"},
    {"name": "Mia Adams", "birthday": "1990.02.21"},
    {"name": "Noah Walker", "birthday": "1987.03.11"},
    {"name": "Olivia Martinez", "birthday": "1991.04.29"},
    {"name": "Paul Lewis", "birthday": "1989.05.18"},
    {"name": "Quinn Robinson", "birthday": "1984.06.07"},
    {"name": "Rose Allen", "birthday": "1988.07.27"},
    {"name": "Sam King", "birthday": "1992.07.16"},
    {"name": "Tina Baker", "birthday": "1986.07.09"},
    {"name": "Uma Lee", "birthday": "1983.10.15"},
    {"name": "Vince Perez", "birthday": "1993.11.05"},
    {"name": "Wendy Carter", "birthday": "1990.12.14"},
    {"name": "Xander Mitchell", "birthday": "1987.01.03"},
    {"name": "Yara Sanchez", "birthday": "1985.02.25"},
    {"name": "Zachary Morgan", "birthday": "1984.03.30"},
    {"name": "Amy Griffin", "birthday": "1991.04.12"},
    {"name": "Brian Russell", "birthday": "1989.05.22"}
]

# Done
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:")
[print(f"{birthdays['name']} - {birthdays['congratulation_date']}") for birthdays in upcoming_birthdays]