def greet(age : int, school, name="Guest"):
    # what function does
    print(f"Hello, {name.upper()} you are {age} years old")
    
def avr(number1 : int, number2 : int, number3 = 10):
    return (number1 + number2 + number3) / 3

average = avr(45, 76, 84)

def grade(average_marks):
    if 80 <= average_marks <= 100:
        return "A"
    elif 70 <= average_marks < 80:
        return "B"
    elif 60 <= average_marks < 70:
        return "C"
    elif 50 <= average_marks < 60:
        return "D"
    elif 0 <= average_marks < 50:
        return "E"
    else:
        return "Invalid marks"
        
print(grade(75))

def numbers(*args):
    return sum(args)

def details(**kwargs):
    print(kwargs)
    
details(name="Joseph", age =10)

print(numbers(12,14,26))

print(average)
greet(name="Joseph", age=10, school="emobilis")   
greet("joseph")