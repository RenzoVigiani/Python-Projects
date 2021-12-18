# WAP to check whether an entered string is palindrome or not

from typing import List


my_str = input("Enter a string: ")

#reverse the string
rev_str=reversed(my_str)

if list(my_str) == list(rev_str):
    print("Palindrome")
else: 
    print("Not Palindrome")
