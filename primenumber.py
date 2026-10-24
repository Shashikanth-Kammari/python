number = [1, 2, 3, 4, 21, 31]
count = 0
for num in number:
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break 
        else:
            print(num, "is a prime number")
            count += 1
            print(count)
    else:
        print(num, "is not a prime number")