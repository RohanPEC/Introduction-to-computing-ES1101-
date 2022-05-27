# Q1


while(True):
     marks = float(input("Enter your marks: "))
     if marks < 25:
         print("Grade: F")
     elif marks >= 25 and marks < 45 :
         print("Grade: E")
     elif marks >= 45 and marks < 50 :
         print("Grade: D")
     elif marks >= 50 and marks < 60 :
         print("Grade: C")
     elif marks >= 60 and marks < 80 :
         print("Grade: B")
     elif marks >= 80 and marks <= 100 :
         print("Grade: A")
     else :
         print("Enter valid marks.")


# Q2

year = int(input("Enter any random year: "))

if year % 400 == 0 :
  print(year, "is a leap year")
elif year % 100 == 0 :
  print(year, "is not a leap year")
elif year % 4 == 0 :
  print(year, "is a leap year")
else :
  print(year, "is not a leap year.")


# Q3

import random

counter = 1

while counter < 11 :
  num1 = random.randint(0, 9)
  num2 = random.randint(0, 9)

  user_input = int(input("Question {} : {} * {} = " . format(counter, num1, num2)))

  if user_input == num1 * num2:
    print("Right!")
  else:
    print("Wrong. The answer is ", num1 * num2)
  counter = 1 + counter


# Q4

for candies in range(0,200):
    if candies % 5 == 2:
      if candies % 6 == 3:
        if candies % 7 == 2:
          print("The amount of candies are", candies)






