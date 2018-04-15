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

emp_1 = Employee("test_con", "user_con", 4000)
emp_2 = Employee("hello_con", "world_con", 6000)

print(emp_1.pay)
emp_1.appy_raise()
print(emp_1.pay)

print(Employee.num_employees)
