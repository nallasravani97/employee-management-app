def search_employee(name):
    for employee in employees:
        if employee["name"].lower() == name.lower():
            return employee
