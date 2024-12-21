def greetPerson():
    name = input("Enter the name of the person: ")
    return print(f"Hello {name}")

'''def addSum():
    number1 = int(input("Please enter the first number: "))
    number2 = int(input("Please enter the second number: "))
    # if number1.is_integer
    return number1 + number2'''

# break, continue and pass

def addSum(number1, number2=15):
    return number1 + number2

def leapYear(year: int):
    if (year % 4 == 0):
        return print("Is a leap year")
    else:
        return print("Not a leap year")
    
leapYear(2003)