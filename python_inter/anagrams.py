string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# check if the string lens are not equal
if len(string1) != len(string2):
    print("The strings are not anagrams. ")

else:
    # convert strings to lowercase and sort them
    s_string1 = sorted(string1.lower()) 
    s_string2 = sorted(string2.lower())
    
    print(f"Sorted string 1 {s_string1} and string 2 {s_string2}") 
    
    # compare the two sorted strings
    if s_string1 == s_string2:
        print("The strings are anagrams.")
    else:
        print("The strings are not aragrams")