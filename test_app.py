from app import employee_count
def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 5

def test_employee_count():
    employees = ["John", "Priya", "Rahul"]
    assert employee_count(employees) == 3
