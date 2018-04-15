class Employee:
    pass


class Employee_constructor:
    #constructor The first argument of every class method, including init, is
    #always a reference to the current instance of the class. By convention,
    #this argument is always named self. In the init method, self refers to the
    #newly created object; in other class methods, it refers to the instance
    #whose method was called.
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return(' {} {} '.format(self.first, self.last))

emp_1 = Employee()
emp_2 = Employee()
#Setting up class variables manualy
emp_1.first = "test"
emp_1.last = "user"
emp_1.email = "test.user@company.uk"
emp_1.pay = "40000"

emp_2.first = "hello"
emp_2.last = "world"
emp_2.email = "hello.world@company.uk"
emp_2.pay = "60000"

print(emp_1.email)
print(emp_2.email)

print(' {} {} '.format(emp_1.first, emp_1.last))

emp_con_1 = Employee_constructor("test_con", "user_con", 4000)
emp_con_2 = Employee_constructor("hello_con", "world_con", 6000)

print(emp_con_1.email)
print(emp_con_2.email)
#implicitly passed emp_con_1 into the method (self)
print(emp_con_1.fullname())
print(emp_con_2.fullname())
print('''Using the class itself to perform the operation thats why need for
self in method def demonstration''')
#explicitly passed emp_con_1 into the method of the class (self)
print(Employee_constructor.fullname(emp_con_1))
print(Employee_constructor.fullname(emp_con_2))
