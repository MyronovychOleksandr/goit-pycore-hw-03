import re

def normalize_phone(phone_number: str) -> str | None:
    if type(phone_number) != str: 
        print("Put phone number in string format!")
        return None
    
    pattern = r"[^\d+]+"
    cleaned_phone_number = re.sub(pattern, "", phone_number)

    has_plus = cleaned_phone_number.startswith("+")
    digits = cleaned_phone_number.replace("+", "")

    if has_plus:
        return "+" + digits
    elif digits.startswith("380"):
        return "+" + digits
    elif digits.startswith("0"):
        return "+38" + digits
    else:
        return "+380" + digits


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
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)