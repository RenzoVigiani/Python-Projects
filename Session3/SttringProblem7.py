#WAP that takes a string with multiple words and then capitalizes the first letter of each word and forms a new string out of it

str1=input("Enter the string: ")
str2=""
a=0

while(a<len(str1)):
    if a==0:
        str2=str2+str1[a].upper()
        a=a+1
    elif(str1[a]==" " and str1[a+1]!=" "):
        str2=str2+str1[a]
        str2=str2+str1[a+1].upper()
        a=a+2
    else:
        str2=str2+str1[a]
        a=a+1

print("Original string: ", str1)
print("Final string: ",str2)
    