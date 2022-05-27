# Q1

choice = "y"

while choice == "y":
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
         
     choice = input("press 'y' to continue or any key to stop.\n")


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

n = 1
while n <= 10:

  import random

  a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

  num1 = random.choice(a)
  num2 = random.choice(a)

  print("Q", n, ":", num1, "x", num2)

  answer = int(input("Enter the correct answer:\n"))

  if answer is num1*num2:
    print("Correct.")
  elif answer is not num1*num2:
    print("Wrong!, the correct answer is ", num1*num2)
  n = n + 1

print("Thank you for playing the game.")


# Q4

among_5 = int(input("If the candy is divided evenly among 5 people, how many candies left?: "))
among_6 = int(input("If the candy is divided evenly among 6 people, how many candies left?: "))
among_7 = int(input("If the candy is divided evenly among 7 people, how many candies left?: "))

for candies in range(0,200):
  if candies % 5 == among_5 and candies % 6 == among_6 and candies % 7 == among_7:
    print("The amount of candies in the bowl are", candies)


  



