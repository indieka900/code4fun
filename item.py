import csv

class Item:
    
    pay_rate = 0.8 # the pay rate after 20% discount
    
    all = []
    
    def __init__(self,name:str,price:float,quantity=0):
        #validate the assigned data
        assert price >=0, f'Price {price} is less than zero'
        assert quantity >=0, f'Quantity {quantity} is less than zero'
        
        
        #Assign
        self.__name = name
        self.__price = price
        self.quantity = quantity
        
        #actions to excecute
        Item.all.append(self)
        
    @property
    #Property Decorator = Read Only Attribute
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price
    
    def apply_disc(self):
        self.__price = self.__price * self.pay_rate
        
    def apply_increment(self, incre_num:float):
        self.__price = self.__price + self.__price * incre_num
    
    @name.setter
    def name(self, value):
        self.__name = value
        
    def calculate(self):
        return self.quantity * self.__price
    
    
    @classmethod   
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )
            
    #static method
    @staticmethod
    def is_integer(num):
        #count out the floats that are point zero ie 12.0
        if isinstance(num, float):
            #count out the floats that are point zero
            return num.is_integer()
        
        elif isinstance(num, int):
            return True
        
        else:
            return False
        
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
    

