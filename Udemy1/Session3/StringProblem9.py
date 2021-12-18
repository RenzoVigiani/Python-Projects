#WAP that reads email-id of a person in the form of a string and ensures that it
#belongs to domain @gmail.com.(Assumption: No invalid characters are there in email-id).
'''
ex- rupamdas00001@gmail.com

l1= 25
l2= 10
l1-l2'''

address=input("Enter your personal email ID: ")

domain="@gmail.com"

if(address[(len(address)-len(domain)):])== (domain):
    print(" It belongs to domain @gmail.com ")
else:
    print(" It is not belong to domain @gmail.com ")
