
#def __init__ is what gives access to 'self'.. alternatively use a class variable
import random
class Hat:
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]


    def sort(self, name):
        house = random.choice(self.houses)
        print(name, "is in", house)

#instantiate (represent) a class' object
hat = Hat()
hat.sort("Harry")

######
import random

class Hat:
    #rid of self
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    #self is replaced by cls (class)
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

#replaces hate = Hat() bc nothing needs to be instantiated
#Hat.sort is now capitzlied (Class.method)
Hat.sort("Harry")