subjects = {}
total = 0

try:
    noOfSubjects = int(input("Enter the number of subjects: "))
except ValueError:
    print("The number of subjects should not be a string\n")    
    exit()

for i in range(noOfSubjects):
    name = input(f"Enter the name of the subject {i+1}: ")
    while True:
        try:
            marks = int(input(f"Enter the marks of the subject {i+1}: "))
            if 0 <= marks <= 100  :
                break
            else:
                print("Enter marks that ranges 0 to 100")
        except ValueError:
            print("Marks should be an integer")
    total += marks
    subjects[name] = marks
    
avarage = total/len(subjects)
subjects["Total"] = total
subjects["Average"] = avarage
print(subjects)