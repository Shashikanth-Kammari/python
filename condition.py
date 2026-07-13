user_input= int(input("Enter the number : "))

#user_input= int(user_input)

if user_input >= 10:
    print("your enter the greater or equal than 10")
else:
    print("your entering the less than 10  ")

#Method2

user_input= int(input("Enter the number : "))
if user_input == 10:
    print("user_input input is equals to 10")
elif user_input > 10:
    print("user_input input is greater than 10")
elif user_input < 10:
    print("user_input input less than 10")
else:
    print("please enter valid value")

#exception  handling 
try:
    user_input= int(input("Enter the number : "))
    if user_input == 10:
        print("user_input input is equals to 10")
    elif user_input > 10:
        print("user_input input is greater than 10")
    elif user_input < 10:
        print("user_input input less than 10")
except:
    print("please enter valid number")
