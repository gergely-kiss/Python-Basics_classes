class Employee:

    num_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_employees += 1

    def fullname(self):
        return(' {} {} '.format(self.first, self.last))

    def appy_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    #makes it so insted of the instance we recive the class as the first
    #attribute
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    #usecase an alternative constructor
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    #note; if you dont use self or cls you should consider to use static
    def is_workday(day):
        if day.weekday() > 4:
            return False
        return True

emp_1 = Employee("test_con", "user_con", 4000)
emp_2 = Employee("hello_con", "world_con", 6000)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

Employee.set_raise_amount(1.10)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_str_1 = "John-Doe-54444"
emp_str_2 = "Tina-Tuna-4500"
emp_str_3 = "Bob-Nope-99999"

first, last, pay = emp_str_1.split('-')
emp_3 = Employee(first, last, pay)

print(emp_3.email)

emp_4 = Employee.from_string(emp_str_2)

print(emp_4.email)
print(Employee.num_employees)

import datetime
my_date = datetime.date(2018, 4, 4)
print(Employee.is_workday(my_date))
