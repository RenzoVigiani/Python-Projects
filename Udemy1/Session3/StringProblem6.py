#WAP to calculate the number of uppercase letters and lowercase letters in a string

s=input("Enter a string: ")
c1=0
c2=0
for i in s:
    if(i.islower()):
        c1=c1+1
    elif(i.isupper()):
        c2=c2+1

print(f"Total number of lowercase letters: {c1}")
print(f"Total number of uppercase letters: {c2}")
