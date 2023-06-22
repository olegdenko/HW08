from datetime import datetime, timedelta
from collections import deque

employees = [
    {"name": "Piter", "birthdate": datetime(1998, 6, 28)},
    {"name": "Angel", "birthdate": "24.06.2000"},
    {"name": "Lilu", "birthdate": datetime(1985, 6, 25)},
]


def get_period() -> tuple[datetime.date, datetime.date]:
    current_date = datetime.now()
    start_period = current_date + timedelta(days=5 - current_date.weekday())
    return start_period.date(), (start_period + timedelta(6)).date()


def check_elp(list_of_emp: list) -> None:
    current_year = datetime.now().year
    for emploee in list_of_emp:
        bd = emploee["birthdate"]
        if isinstance(bd, datetime):
            bd = bd.date()
        else:
            bd = datetime.strptime(bd, "%d.%m.%Y").date()
        bd = bd.replace(year=current_year)
        (
            start,
            end,
        ) = get_period()

        if start <= bd <= end:
            if bd.weekday in (5, 6):
                result[bd].append(emploee['name'])
            else:
                result[bd].append(emploee['name'])
    return result
        # print(bd)


if __name__ == "__main__":
    for item, value in check_elp(employees).items():
        print(key.strftime("%A") for v in value])
    # check_elp(employees)
