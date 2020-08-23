class Person:
    # Class attribute vs regular attribute
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        # We can implement this to keep track of the number of people
        # Person.number_of_people += 1
        Person.add_person()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


p1 = Person("Tim")
p2 = Person("Jill")
print(Person.number_of_people_())