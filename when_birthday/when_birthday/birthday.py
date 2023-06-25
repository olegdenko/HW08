from datetime import datetime, timedelta
from collections import defaultdict

filename = "employees.txt"


def get_employees_list(filename):
    employees = []
    with open(filename, "r") as file:
        while True:
            line = file.readline()
            line = line.strip()
            if line:
                name, date_str = line.split(":")
                date_str = date_str.replace(".", ",")  # Заміна крапок на коми
                birthdate = datetime.strptime(date_str.strip(), "%Y, %m, %d")
                employee = {"name": name.strip(), "birthdate": birthdate}
                employees.append(employee)
            else:
                break
    return employees


def get_period() -> tuple[datetime.date, datetime.date]:
    current_date = datetime.now()
    start_period = current_date + timedelta(days=5 - current_date.weekday())
    return start_period.date(), (start_period + timedelta(6)).date()


def check_epl(list_of_emp: list) -> None:
    result = defaultdict(list)
    current_year = datetime.now().year
    for employee in list_of_emp:
        bd = employee["birthdate"]
        if isinstance(bd, datetime):
            bd = bd.date()
        else:
            bd = datetime.strptime(bd, "%d.%m.%Y").date()
        bd = bd.replace(year=current_year)

        start, end = get_period()

        if start <= bd <= end:
            if bd.weekday() in (5, 6):
                result[bd].append(employee["name"])
            else:
                result[bd].append(employee["name"])
    return result


if __name__ == "__main__":
    employees = get_employees_list(filename)
    for key, value in check_epl(employees).items():
        print(key.strftime("%A"), value)
    # print(get_period())
