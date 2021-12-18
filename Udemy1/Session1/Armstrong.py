#Armstrong check

# take input from the user
num=int(input("Enter a number:"))
#inicialize sum
s=0

# find the sum of the cube of each digit
temp = num
while(num>0):
    d=num%10 #getting the last digit
    s=s+d**3 #adding the last digit with the existing sum
    num=num//10

#Display de result
if temp == s:
    print("Armstrong")
else:
    print("Not armstrong")