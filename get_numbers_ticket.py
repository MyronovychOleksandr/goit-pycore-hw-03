import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    if type(min) != int or type(max) != int or type(quantity) != int:
        return []
    if min < 1 or max > 1000 or quantity <= 0 or (max + 1 - min) < quantity:
        return []
    
    return sorted(random.sample(range(min, max + 1), k=quantity))


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)