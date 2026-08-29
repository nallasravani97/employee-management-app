def update_employee(employee_id, new_name):
    for employee in employees:
        if employee["id"] == employee_id:
            employee["name"] = new_name
def search_employee(name):
    for employee in employees:
        if employee["name"].lower() == name.lower():
            return employee
