#Q1

input_string = input("Enter a sring: ")
# Creating an empty string.
reverse = ""
# Each element from the inputstring is added from left side.
for character in input_string:
  reverse = character + reverse

print("Reverse of the entered string is: ", reverse) 


#Q2

input_upper_limit = int(input("Enter upper limit of range: "))
input_lower_limit = int(input("Enter lower limit of range: "))
input_number = int(input("Enter a number: "))

for i in range(input_upper_limit, input_lower_limit):
  if i % input_number == 0:
    print(i)
  else:
    continue
print("End")


#Q3

#User inputs three sides
a = int(input("Enter the lenght of first side: "))
b = int(input("Enter the lenght of second side: "))
c = int(input("Enter the lenght of third side: "))

# Sum of any 2 sides taken one by one
x = a + b 
y = b + c
z = c + a

# If any of the three lengths is greater than the sum of the other two, then you cannot form a triangle.
if x > c and y > a and z > b:
  #Use Heron's formula if the sides form a triangle
  s = (a + b + c)/2
  area = (s*(s - a)*(s - b)*(s - c))**(0.5)
  print(area)
else:
  print("Invalid triangle")


#Q4

n = 5

for i in range (n):
  for j in range (i):
    print("*", end = " ")
  print("")

for i in range (n,0,-1):
  for j in range (i):
    print("*", end = " ")
  print("")


#Q6

#Taking upper and lower limit values
lower_limit = int(input("Insert lower limit limit for range: "))
upper_limit = int(input("Insert upper limit limit for range: "))

print("Prime numbers between", lower_limit, "and", upper_limit, "are:")

for number in range(lower_limit, upper_limit + 1):
   if number > 1:
       for i in range(2, number):
           if (number % i) == 0:
               break
       else:
           print(number)


#Q7

for i in range(0,500):
    if i % 7 == 0 and i % 11 == 0:
        print(i)
    else:
        continue


#Q8

# Creating blank list
Test_list = []
# Taking 10 values from user
for i in range(10):
    Test_list.append(int(input("Enter number: ")))
    
print(Test_list)

print('''
      Press 1 for positive numbers
      Press 2 for negative numbers
      Press 3 for odd numbers 
      Press 4 for even numbers
      Press 5 for checking frequency of numbers ''',"\n")
      
operation = int(input("Please choose output "))

if operation == 1:
    for j in Test_list:
        if j>0:
            print(j)
elif operation == 2:
    for j in Testlist:
        if j<0:
            print(j)
elif operation == 3:
    #Checking for odd numbers
    for j in Test_list:
        if j%2!=0:
            print(j)
elif operation == 4:
    #Checking for even numbers
    for j in Test_list:
        if j%2==0:
            print(j)
elif operation == 5:
    #Converting list to dictionary and using count
    Test_dict={num:Test_list.count(num) for num in Testlist}
    print(Test_dict)


#Q9

#Creating empty list
Test_list = []
#Taking 10 inputs from user and then adding them to list
for i in range(10):
    Test_list.append(input("Enter word: "))
print(Test_list)
#Converting list to dictionary and then using count 
Test_dict = {word:Testlist.count(word) for word in Testlist}

print(Test_dict)

