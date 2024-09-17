
class Student:
    def __init__(self, name, house):
        #calls setter function.. self.name
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getter for name
    #One argument for getter (self)
    #A getter lets you get the value in main
    @property
    def name(self):
        #Underscore bc function (name) and variable (name) cant be called the same thing
        #underscore is Pythons version of "private".. means "pls dont touch it!"
        return self._name

    # Setter for name
    #Two argruments for setter (self, name)
    #A setter lets you reassign the value in main
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Invalid name")
        self._name = name

    # Getter for house
    @property
    def house(self):
        return self._house

    # Setter for house
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house
#
#
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    #When this funct. is in class, python AUTOMATICALLY calls it anytime another function wants the obj as a string
    def __str__(self):
        return f"{self.name} from {self.house}"

    #replaces the get_student() function in main
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

def main():
    student = Student.get()
    #having the __str__ function allows you to simply say print(student) here
    print(student)

if __name__ == "__main__":
    main()

#Creates an object called Student
#Object: An instance of a class. When you use a class, you create an object.
class Student:
    #This function is a method from Python which initializes what you want to store
    #The word "self" is ALWAYS added in.. and its there to store "name" and "house" in the object "Student"
    #__ methodds are called "dunder"
    def __init__(self, name, house):
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    #Treated as a function.. passing in 2 values. "constructor call".
    return Student(name, house)

'''
if __name__ == "__main__":
    main()



def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)

if __name__ == "__main__":
    main()
#
#
def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")

def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student

if __name__ == "__main__":
    main()
#
#
def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()
#
#
class Student:
    ...

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

if __name__ == "__main__":
    main()
'''