#WAP to calculate simple interest
p= float(input("Enter the Principle amount: "))
t= int(input("Enter the number of years: "))
r= float(input("Enter the rate of interest: "))
si= (p*t*r)/100
print(f"The simple interest is {si}")


'''WAP to calculate BMI(Body Mass Index) of a person
The formula is BMI = kg/m square, where kg is a person's weight in kilograms
and m square is their height in meters squared.'''

w= float(input("Enter weight in kg: "))
h= float(input("Enter the height in meters: "))

bmi=w/(h*h)
print(f"The BMI is {bmi}")
