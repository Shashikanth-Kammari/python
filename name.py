number= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 21]

for num in number:
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    