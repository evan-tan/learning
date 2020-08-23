class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what to say")


class Dog(Pet):
    def __init__(self, name, age, color):
        # You could also specify
        # Pet.__init__(name, age)
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Woof")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old "
              f"and I am {self.color}")


class Cat(Pet):
    def speak(self):
        print("Meow")


if __name__ == "__main__":
    p = Pet("Tim", 19)
    p.show()
    c = Cat("Bill", 34)
    c.show()
    d = Dog("Jill", 25, "Brown")
    d.show()
