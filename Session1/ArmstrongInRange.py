#Armstrong check

# take input from the user
lower = int(input("Enter the lower limit: "))
upper= int(input("Enter the upper limit: "))

for num in range (lower,upper):
    
        #inicialize sum
        s=0

        # find the sum of the cube of each digit
        temp = num
        while(temp>0):
            d=temp%10 #getting the last digit
            s=s+d**3 #adding the last digit with the existing sum
            temp=temp//10

        #Display de result
        if num == s:
            print(num)
