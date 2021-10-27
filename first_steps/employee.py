class Employee:
    def __init__(self, id: int, first_name: str, last_name: str, salary: float):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_annual_salary(self):
        return self.salary * 12

    def raise_salary(self, amount: float):
        self.salary += amount

        return self.salary



employee = Employee(3333, "C", "B", 400)
print(employee.get_full_name())
print(employee.raise_salary(500))
print(employee.get_annual_salary())
