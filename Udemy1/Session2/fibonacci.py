# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
a,b= 0,1
count=0

# check if the number of terms is valid
if nterms <=0:
   print("Please enter a positive integer: ")
elif nterms==1:
   print("Fibonacci series: ")
   print(a)
else:
   print("Fibonacci series: ")
   while(count<nterms):
      print(a)
      c=a+b
      #update the values
      a=b
      b=c
      count += 1