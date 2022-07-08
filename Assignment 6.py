#Q1

user_input = int(input("Enter a number:"))
sum_of_the_divisor = 0
for i in range(1 ,user_input):
    if (user_input%i==0):
        sum_of_the_divisor += i
        if sum_of_the_divisor==user_input:
            print("Yes, It is a perfect number.")
            break

else:
    print("No, It is not a perfect number.")


#Q2

user_input = str(input("Enter a word, phrase or sequence: "))
user_input1 = user_input.replace(" ", "")
palindrome = user_input1[::-1]
if user_input1 == palindrome :
  print("Input is a palindrome.")
else:
  print("Input is not a palindrome.")


#Q3

from math import factorial

n = int(input("Enter the number of rows of pascal triangle: "))
for i in range(n):
    for j in range(n-1-i):
        print(" ", end="")
    for k in range (i+1):
        print(factorial(i) // (factorial(i-k)*factorial(k)) , end=" ") # nCr = n! / ((n-r)! * r!)
    print()


#Q4

user_input = str(input("Enter a word or sentence: "))
user_input1 = user_input.lower()
alphabets = "abcdefghijklmnopqrstuvwxyz"
for i in alphabets :
  if i not in user_input1 :
    print("No, It is NOT a Pangram.")
    break
else:
    print("Yes, It is a Pangram.")


#Q5

user_input = str(input("Enter words with hyphen(For example:green-red-yellow-black-white): "))
user_input1 = user_input.lower()
input_split = user_input1.split("-")
input_split.sort()
print("-".join(input_split))


#Q6

def student_data(student_name , student_branch, student_id):
    print("Student name: ",student_name)
    print("Student branch: ",student_branch)
    print("Student ID: ",student_id)

student_data("Rohan","Mechanical",21107021)


#Q7

class Student:
    pass 
class Marks:
    pass 
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks)) 
print(isinstance(student1, Marks))
print("Check whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))
print()


#Q8

list=[]
def findTriplets(arr, n):
  
    found = False
    for i in range(0, n-2):
      
        for j in range(i+1, n-1):
          
            for k in range(j+1, n):
              
                if (arr[i] + arr[j] + arr[k] == 0):
                    list.append([arr[i],arr[j],arr[k]])
                    print(list)
                    found = True
      
    if (found == False):
        print(" not exist ")
  
arr = [-25, -10, -7, -3, 2, 4, 8, 10]
n = len(arr)
findTriplets(arr, n)


#Q9

class parantheses:
    def find(str):
        a= ['()', '{}', '[]'] 
        while any(i in str for i in a):
            for j in a:
                str = str.replace(j, '') 
        return not str 

s = input("Enter the sequence of parantheses : ")
if parantheses.find(s):
    print(s,"-","is balanced")
else:
    print(s,"-","is unbalanced")