user= int(input("Enter the number : "))

#user= int(user)

if user >= 10:
    print("your enter the greater or equal than 10")
else:
    print("your entering the less than 10  ")

#Method2

user= int(input("Enter the number : "))
if user == 10:
    print("user input is equals to 10")
elif user > 10:
    print("user input is greater than 10")
elif user < 10:
    print("user input less than 10")
else:
    print("please enter valid value")

#exception  handling 
try:
    user= int(input("Enter the number : "))
    if user == 10:
        print("user input is equals to 10")
    elif user > 10:
        print("user input is greater than 10")
    elif user < 10:
        print("user input less than 10")
except:
    print("please enter valid number")
