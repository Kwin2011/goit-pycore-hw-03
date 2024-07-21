import random

def get_numbers_ticket(min, max, quantity):
    # Перевірка параметрів
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1) or min > max:
        return []
    
    # Генерація унікальних випадкових чисел
    numbers = random.sample(range(min, max + 1), quantity)
    
    numbers.sort()
    
    return numbers

# lottery_numbers = get_numbers_ticket(1, 49, 6)

print("Enter your min(1) , max(1000) , and quantity (min < quantity < max) : РРРР-ММ-ДД")

lottery_numbers = get_numbers_ticket(
    int(input("Enter min>> ")), 
    int(input("Enter max>> ")), 
    int(input("Enter quantity>> ")))

while (not lottery_numbers):
    print("Не відповідає параметрам спробуй ще раз:")

    lottery_numbers = get_numbers_ticket(
    int(input("Enter min>> ")), 
    int(input("Enter max>> ")), 
    int(input("Enter quantity>> ")))


print("Ваші лотерейні числа:", lottery_numbers)


