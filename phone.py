from item import Item

#Inheritance
class Phone(Item):
    
    pay_rate = 0.6
    
    def __init__(self,name:str,price:float,quantity=0,broken_phones=0):
        #Call to super function to have access to all attributes / methods
        
        super().__init__(
            name, price, quantity
        )
        
        #validate the assigned data
        assert broken_phones >=0, f'Broken phones {broken_phones} is less than zero'
        
        
        #Assign
        self.broken_phones = broken_phones
        
        