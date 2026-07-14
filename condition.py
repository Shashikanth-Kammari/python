userinputs= int(input("Enter the number : "))

#userinputs= int(userinputs)

if userinputs >= 10:
    print("your enter the greater or equal than 10")
else:
    print("your entering the less than 10  ")

#Method2

userinputs= int(input("Enter the number : "))
if userinputs == 10:
    print("userinputs input is equals to 10")
elif userinputs > 10:
    print("userinputs input is greater than 10")
elif userinputs < 10:
    print("userinputs input less than 10")
else:
    print("please enter valid value")

#exception  handling 
try:
    userinputs= int(input("Enter the number : "))
    if userinputs == 10:
        print("userinputs input is equals to 10")
    elif userinputs > 10:
        print("userinputs input is greater than 10")
    elif userinputs < 10:
        print("userinputs input less than 10")
except:
    print("please enter value")
