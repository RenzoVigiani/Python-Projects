# WAP to calculate the total number of character, alphabet, digits and spaces in a string.

str= input("Enter a String: ")
c=0
alphas=0
digits=0
spaces=0
for i in str:
    c += 1
    if i.isalpha():
        alphas +=1
    if i.isdigit():
        digits +=1
    if i.isspace():
        spaces +=1

print("The number of the Characters is: ",c)
print("The number of the Alphas is: ",alphas)
print("The number of the Digits is: ",digits)
print("The number of the Spaces is: ", spaces)