number=5
for i in range(1, number):
    if i == 3 :
        print("*", end=" ")
    else:
        print(" ", end=" ")
    for j in range(1, number):
        print("*", end=" ")
    print()  # Print a newline after each row
