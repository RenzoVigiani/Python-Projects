#Sum of Digits

n=int(input("Enter a number:"))
s=0

while(n>0):
    d=n%10 #getting the last digit
    s=s+d #adding the last digit with the existing sum
    n=n//10
print(s)