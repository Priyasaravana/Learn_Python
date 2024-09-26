class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def talk(self):
        print(self.name)
        print(self.age)

p = Person('Priya', 32)
p.talk()

class Employee:
    """ Practie class program"""
    def __init__(self, employee_name, age, dept):
        self.employee_name = employee_name
        self.age = age
        self.dept = dept

    def display(self):
        print('{} \t {} \t {}'.format(self.employee_name, self.age, self.dept))

e = Employee('Priya', 32, 'R&D')
e.display()


