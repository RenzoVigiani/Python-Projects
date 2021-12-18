#WAP to remove the characters of odd index values in a string

str1=input("Enter the string: ")
final=""

for i in range(len(str1)):
    if i%2 ==0:
        final= final+ str1[i]

print(final)