#Wap to remove the nth index character from a non-empty string

str = input("Enter the String:  ")
n= int(input("Enter the index value: "))

first= str[0:n]
last=str[n+1:]

final= first+last

print(f"Modified string: {final}")
