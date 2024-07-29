# my_num = int(input("Enter your number: "))

arm_nums = []

for my_num in range(0,999):

    # power_of_my_num = len(str(my_num))
    power_of_my_num = 3

    total = 0
    i = my_num

    while i > 0:
        reminder = i % 10
        total += reminder ** power_of_my_num
        i = i // 10
        
    if total == my_num:
        arm_nums.append(my_num)
    #     print(f"{my_num} is Armstrong number")
    # else:
    #     print(f'{my_num} is not Armstrong number')
    
print(arm_nums)