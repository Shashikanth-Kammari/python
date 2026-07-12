number=121
temp=number
reverse=0

while temp>0:
    digit=temp%10    #it remaider store that is 1
    reverse=reverse*10+digit   # it first reversed number
    temp=temp//10  #it give removed last digit that is 1 now it is 12
if number == reverse:
    print("this number is Palidrome number "+ str(reverse))
else:
    print("this number is not palidrome number "+ str(reverse))
name="shashi"

reversed=name[::-1]

if number ==reversed:
    print("this is palidrone number"+ str(reversed))