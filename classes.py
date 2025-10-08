class Animal():
    def __init__(self,name):
        self.name = name
    def speak(self):
        print("The Animal makes a sound")

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
    def speak(self):
        print(f"{self.name} barks loudly")
    def fetch(self):
        print(f"{self.name} is fetching")

my_dog = Dog("Zoo","Persian")
my_dog.speak()

dir(Dog)