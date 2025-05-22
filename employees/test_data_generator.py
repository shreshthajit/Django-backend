from faker import Faker
import random
from employees.models import Employee

fake = Faker('en_US')


def generate_employee_data():
    emp_id = fake.pyint(min_value=100000, max_value=999999)
    emp_name = fake.name()
    designation = random.choice(['Software Engineer', 'Software Tester', 'Manager', 'HR', 'Marketing'])
    return {
        'emp_id': emp_id,
        'emp_name': emp_name,
        'designation': designation
    }

data_count = 50
for _ in range(data_count):
    employee_data = generate_employee_data()
    employee = Employee(**employee_data)
    employee.save()

print(f'{data_count} employee data has been created successfully!')