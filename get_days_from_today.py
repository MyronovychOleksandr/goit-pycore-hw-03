from datetime import datetime

def get_days_from_today(date: str) -> int | None:
    """
    Retuns time difference from today
    """
    if type(date) != str:
        print("Put correct date in string format!")
        return None
    
    try:
        parsed_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Put correct date!")
        return None

    today = datetime.today()
    diff = today.date() - parsed_date.date()
    return diff.days
    

print(get_days_from_today('2026-10-09'))