# From Corey Schafer's OOP tutorial
import datetime


class Employee:
    """Classes allows us to logical group the
     data(Attributes) and functions(methods)
     in a way to reuse. Its basically an blueprint
     for creating instances."""

    "Class variables are shared by all the instances of the class."
    num_of_emp = 0
    raise_amount = 1.02

    def __init__(self, fname, lname, age, salary):
        """This is the constructor for the Employee.
        Instance variables like fname, lname...salary
        are unique to each instance."""
        self.fname = fname
        self.lname = lname
        self.email = fname + '.' + lname + '@company.com'
        self.age = age
        self.salary = salary

        Employee.num_of_emp += 1

    # Special methods are also called as magic/dunder methods.
    # __repr__ is an unambiguous representation of an object and is
    # used for logging debugging etc. Used by developers.
    def __repr__(self):
        return "Employee({}, {}, {})".format(self.fname, self.lname,
                                             self.age)

    # __str__ is more readable representation of an object.
    # Used by end users in general.
    def __str__(self):
        return "{} - {}".format(self.fname, self.email)

    def fullname(self):  # regular method.
        return '{} {}'.format(self.fname, self.lname)

    def salary_raise(self):
        self.salary = self.salary * self.raise_amount

    @classmethod
    def set_raise(cls, amount):  # class method.
        cls.raise_amount = amount

    # class methods can also be used as an alternative constructor.
    @classmethod
    def from_string(cls, emp_str):
        fname, lname, age, salary = emp_str.split('-')
        return cls(fname, lname, age, salary)

    # static methods: when you don't access instance methods or attributes.
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, fname, lname, age, salary, progl):
        Employee.__init__(self, fname, lname, age, salary)
        # super().__init__(fname, lname, age, salary)
        self.progl = progl


class Manager(Employee):
    raise_amount = 1.20

    def __init__(self, fname, lname, age, salary, employees=None):
        Employee.__init__(self, fname, lname, age, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def rem_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def list_emp(self):
        for emp in self.employees:
            print(emp.fullname())


emp_1 = Employee('John', 'Leon', 25, 90000)
emp_2 = Employee('hn', 'on', 26, 90000)

my_date = datetime.date(2017, 5, 2)
print(Employee.is_workday(my_date))

mgr = Manager('J', 'L', 25, 90000, [emp_1])
mgr.add_emp(emp_2)
mgr.list_emp()

print(mgr.fullname())

print(emp_1.fullname())
print(Employee.num_of_emp)

print(emp_1)

Employee.set_raise(2)
Employee.salary_raise(emp_1)
print(emp_1.salary)

emp1str = 's-g-22-100000'
new_emp = (Employee.from_string(emp1str))
print(new_emp.__dict__)

d1 = Developer('S', 'E', 22, 111000, 'python')

print(d1.progl)
print(d1.email)

print(isinstance(d1, Developer))
print(isinstance(mgr, Developer))

print(issubclass(Manager, Employee))
