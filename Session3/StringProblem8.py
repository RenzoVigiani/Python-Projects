#WAP to replace every space in a string with a hyphen('-')

string=input("Enter the string: ")

for i in range(0,len(string)):
    if (string[i]==" "):
        final=string.replace(" ","-")

print(final)