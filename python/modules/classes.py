#   OOP

class Computer:
    # class attribute/varaibles
    name = "HP"
    
    # special method inbuild
    def __init__(self, ram, processor):
        self.ram = ram
        self.processor = processor
    
    # method
    #instance method
    def info(self):
        print(f"This  -- {self.ram} ----- {self.processor}")
        
    #classmethod
    @classmethod
    def compare(cls):
        print(cls.name)
        
    #static method
    @staticmethod
    def detail():
        print("This is a computer class created by Joseph")
        
class Car:
    
    def __init__(self, brand, year, model):
        self.brand = brand 
        self.year = year
        self.model = model
        
    # instance method
    def info(self):
        print(f"{self.model} model belongs to {self.brand} brand {self.year}")     

comp1 = Computer("8gb", "i7")
comp2 = Computer("8gb", "i3")
print(comp1.name)
print(type(comp1))

comp1.info()
Computer.info(comp1)
Computer.detail()
comp2.info()

car1 = Car("Nissan",2015,"X-Trail")
car1.model = "Note"
car1.year = 2020
car1.info()
