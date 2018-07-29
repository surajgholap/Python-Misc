class Employee:

    num_of_emp = 0
    raise_amount = 1.02

    def __init__(self, fname, lname, age, salary):
        self.fname = fname
        self.lname = lname
        self.email = fname + '.' + lname + '@company.com'
        self.age = age
        self.salary = salary
       
        Employee.num_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    def salary_raise(self):
        self.salary = self.salary * self.raise_amount

    @classmethod
    def set_raise(cls, amount):
        cls.raise_amount = amount
   
    @classmethod
    def from_string(cls, emp_str):
        fname, lname, age, salary = emp_str.split('-')
        return cls(fname, lname, age, salary)

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, fname, lname, age, salary, progl):
        Employee.__init__(self, fname, lname, age, salary)
        self.progl = progl


class Manager(Employee):
    raise_amount = 1.20

    def __init__(self, fname, lname, age, salary, employees=None):
        Employee.__init__(self, fname, lname, age, salary)
        if employees == None:
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
        
Emp_1 = Employee('John', 'Leon', 25, 90000)
Emp_2 = Employee('hn', 'on', 26, 90000)


mgr = Manager('J', 'L', 25, 90000, [Emp_1])
mgr.add_emp(Emp_2)
mgr.list_emp()

print(mgr.fullname())

print(Emp_1.fullname())
print(Employee.num_of_emp)

Employee.set_raise(2)
Employee.salary_raise(Emp_1)
print(Emp_1.salary)

emp1str = 's-g-22-100000'
new_emp = (Employee.from_string(emp1str))
print(new_emp.__dict__)

d1 = Developer('S', 'E', 22, 111000, 'python')

print(d1.progl)
print(d1.email)