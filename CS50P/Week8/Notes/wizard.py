class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name
    ...
#inhertiance: links two or more classes together. Student "inherits" from (or is a subclass of) Wizard.
class Student(Wizard):
    def __init__(self, name, house):
        #super() accesses "super" class, or "parent" class (aka Wizard)
        super().__init__(name)
        self.house = house
    ...

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    ...

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")
...