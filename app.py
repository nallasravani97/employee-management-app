print("Employee Management App")

employees = []

def add_employee(name, employee_id):
    employees.append({
        "id": employee_id,
        "name": name
    })

add_employee("Rahul", 101)

print(employees)
