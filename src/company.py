from typing import List
import requests


class Employee:
    def __init__(self, name: str, email: str, salary: float = 0.0):
        self.name = name
        self.email = email
        self.salary = salary


class Company:
    LOG_PATH = "log.txt"

    def __init__(self, name: str, employees: List[Employee]):
        self.name = name
        self.employees = employees
        self.changes: List[str] = []

    def fetch_employees(self):
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        response.raise_for_status()

        employees_data = response.json()

        for d in employees_data:
            name = d["name"]
            email = d["email"]
            self.employees.append(Employee(name=name, email=email))
            self.changes.append(f"Added employee {name} with email {email}")

    def setup_company(self, base_salary: float) -> None:
        self.fetch_employees()
        for employee in self.employees:
            employee.salary = base_salary
            self.changes.append(f"Set base salary (NOK {base_salary}) as salary for {employee.name}")
        self.write_logs()

    def write_logs(self):
        with open(self.LOG_PATH, "a") as f:
            for change in self.changes:
                f.write(change + "\n")
