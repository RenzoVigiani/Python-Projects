# Program to check if a number is prime or not
num = int(input("Input the number: "))
flag = False
if num>1:
    for i in range(2,(num//2)+1):
        if (num%i==0): 
            flag=True
            break
#check if flag is true
if flag: 
    print("Not Prime")
else:
    print("Prime")
        