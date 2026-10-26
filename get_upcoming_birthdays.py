from datetime import date, datetime, timedelta

DAYS_AHEAD = 7


def _birthday_in_year(birthday: date, year: int) -> date:
    try:
        return birthday.replace(year=year)
    except ValueError:
        return birthday.replace(year=year, day=28)


def get_upcoming_birthdays(users: list[dict[str, str]]) -> list[dict[str, str]]:
    today = datetime.today().date()
    upcoming = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        next_birthday = _birthday_in_year(birthday, today.year)
        if next_birthday < today:
            next_birthday = _birthday_in_year(birthday, today.year + 1)

        days_until = (next_birthday - today).days
        if days_until >= DAYS_AHEAD:
            continue

        congratulation_date = next_birthday
        weekday = congratulation_date.weekday()
        if weekday >= 5:
            congratulation_date += timedelta(days=7 - weekday)

        upcoming.append({
            "name": user["name"],
            "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
        })

    return upcoming


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
]

print("Список привітань на цьому тижні:", get_upcoming_birthdays(users))