import csv

class Item:
    
    pay_rate = 0.8 # the pay rate after 20% discount
    
    all = []
    
    def __init__(self,name:str,price:float,quantity=0):
        #validate the assigned data
        assert price >=0, f'Price {price} is less than zero'
        assert quantity >=0, f'Quantity {quantity} is less than zero'
        
        
        #Assign
        self.name = name
        self.price = price
        self.quantity = quantity
        
        #actions to excecute
        Item.all.append(self)
        
        
    def calculate(self):
        return self.quantity * self.price
    
    def apply_disc(self):
        self.price = self.price * self.pay_rate
    
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
        return f"Item('{self.name}', {self.price}, {self.quantity})"
  
'''item1 = Item("Phone",400,20)
item2 = Item('Laptop',100,2)
item3 = Item('Cable', 10, 3)
item4 = Item('Mouse', 50, 5)
item5 = Item('Keyboard', 75, 5)'''

'''print(item1.name)
print(item1.quantity)'''
  

# item2.has_numpi = False
'''print(item2.name)
print(item2.quantity)'''

'''print(item1.calculate())
print(item2.calculate())'''

'''print(Item.__dict__) #returns all the attributes for class level
print(item1.__dict__) #returns all attributes for instance level
'''

'''item1.apply_disc()
print(item1.price)'''

'''item2.pay_rate = 0.7
item2.apply_disc()
print(item2.price)'''

'''

for instance in Item.all:
    print(instance.name)'''
    
'''Item.instantiate_from_csv()
print(Item.all)'''

print(Item.is_integer(7.0))