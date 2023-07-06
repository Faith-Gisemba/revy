class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

dog = Dog()
cat = Cat()

dog.make_sound()  
cat.make_sound()  


# the make_sound function demonstrates polymorphism.It takes an object of the Animal class 
# (or any of its subclasses) asa parameter and calls the sound method on that object. 


# When the make_sound function is called with a Dog object, it prints "Woof!". When called with a Cat object,
#  it prints "Meow!". This behavior showcases how polymorphism allows different objects to respond to the same 
# method call in different ways, based on their specific implementations.