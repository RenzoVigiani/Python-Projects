# 0,7,26,63,124 like sequence2
'''upper = int(input("Enter the upper limit: "))

pot=3
for i in range(1,upper+1):
    print(i**3-1)'''

#1,2,2,4,8,32  like fibonacci series
# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
a,b= 1,2
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
      c=a*b
      #update the values
      a=b
      b=c
      count += 1