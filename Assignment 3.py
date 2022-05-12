# Q1

user_input = input("Enter a number: ")
print("The binary of this number is " + bin(int(user_input)).replace('0b',''))


# Q2

number_1 = float(input("Enter first number: "))
operator = input("Enter operator: \n For Addition:(+) \n For Substraction:(-) \n For Multiplication:(*) \n For Division:(/) \n For Floor Division:(//) \n For Modulus:(%)\n Enter the operator to be used: ")
number_2 = float(input("Enter second number: "))

if operator == "+":
    print("Result:", number_1 + number_2)
elif operator == "-":
    print("Result:", number_1 - number_2)
elif operator == "*":
    print("Result:", number_1 * number_2)
elif operator == "/":
    print("Result:", number_1 / number_2)
elif operator == "//":
    print("Result:", number_1 // number_2)
elif operator == "%":
    print("Result:", number_1 % number_2)
else:
  print("Please use a correct operator and try again...")


# Q3

from math import pi
from math import sin
from math import cos
# a)
print(" a) (3 + 4) * 5")
print("Result :", (3 + 4) * 5)
# b)
print(" b) n*(n-1)/2")
n = int(input("Enter the value of n: "))
print("Result:", n*(n-1)/2)
# c)
print(" c) 4 * pi * r1**2")
r1 = float(input("Enter the value of r1: "))
print("Result:", 4 * pi * r1**2)
# d)
print(" d) (r2 * cos(a)**2 + r2 * sin(b)**2) ** 0.5")
r2 = float(input("Enter the value of r2: "))
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
print("Result:", (r2 * cos(a)**2 + r2 * sin(b)**2) ** 0.5 )
# e)
print(" e) (y2 - y1) / (x2 - x1)")
x1 = float(input("Enter the value of x1: "))
x2 = float(input("Enter the value of x2: "))
y1 = float(input("Enter the value of y1: "))
y2 = float(input("Enter the value of y2: "))

print("Result:", (y2 - y1) / (x2 - x1))


# Q4

# a)
print(range(5))
# b)
print(range(3, 10))
# c)
print(range(4, 13, 3))
# d)
print(range(15, 5, -2))
# e)
print(range(5, 3))


# Q5

# Given weights of individual atoms
weight_of_hydrogen = 1.00794
weight_of_carbon = 12.0107
weight_of_oxygen = 15.9994

# Entering the number of atoms in the molecule
no_of_hydrogen = int(input("Enter the number of hydrogen atoms in the carbohydrate molecule: "))
no_of_carbon = int(input("Enter the number of carbon atoms in the carbohydrate molecule: "))
no_of_oxygen = int(input("Enter the number of oxygen atoms in the carbohydrate molecule: "))

# Calculating the weight of carbohydrate
weight_of_carbohydrate = no_of_carbon * weight_of_carbon + no_of_oxygen * weight_of_oxygen + no_of_hydrogen * weight_of_hydrogen

# Printing the answer
print(weight_of_carbohydrate)
