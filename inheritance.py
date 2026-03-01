class Parent:
    def __init__(self,animal):
        self.animal = animal
    def animals(self,name):
        print(f"Hi, i am {self.animal} and my name is {name} ")

class Child(Parent):
    def __init__(self,breed_type,animal):
        super().__init__(animal)
        self.breed_type = breed_type
    def dog(self):
        print(f"Hello i am {self.animal} and my breed is {self.breed_type}")

par = Parent("Dog")
par.animals("Zoo")

chi = Child("Lapador","zoo")
chi.dog()
chi.animals("zpp")