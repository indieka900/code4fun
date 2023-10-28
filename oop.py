from item import Item
from phone import Phone


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


#print(Item.is_integer(7.0)) #return true

phone1 = Phone("iPhonev12",300, 15, 1)
#print(phone1.calculate())
phone2 = Phone("iphonev13", 45, 60,3)

#print(Item.all)

#Encapsulation
item1 = Item("MyItem", 750)
print(item1.name)
item1.name = "Second"
print(item1.name)