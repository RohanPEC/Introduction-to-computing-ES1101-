# Q1

# a.
input_string = "Python is a case sensitive language"
print(len(input_string))
# b.
print(input_string[::-1])
# c.    
new_string = input_string[10:26]
print(new_string)
# d.
replaced_string = input_string[:10] + "object oriented" + input_string[26:]
print(replaced_string)
# e.
print(input_string.find('a'))
# f.
print(input_string.replace(' ', ''))


# Q2

name = input("Enter name:")
Sid = input("Enter SID:")
dep_name = input("Enter department name:")
cgpa = input("Enter CGPA:")
print("Hey,", name, "here!" )
print("My SID is", Sid)
print("I am from", dep_name, "department and my CGPA is", cgpa) 


# Q3

a = 56
b = 10
# a.
print("a&b = " + str(a&b))
# b.
print("a|b = " + str(a|b))
# c.
print("a^b = " + str(a^b))
# d.
print("a shifted left by 2 bits is " + str(a<<2) + " and b shifted left by 2 bits is " + str(b<<2))
# e.
print("a shifted right by 2 bits is " + str(a>>2) + " and b shifted right by 4 bits is " + str(b>>4))


# Q4

user_input = input("Enter input:")
if 'name' in user_input:
    print("yes")

else:
    print("no")


# Q5

Lenght_1 = float(input("Enter the lenght 1: "))
Lenght_2 = float(input("Enter the lenght 2: "))
Lenght_3 = float(input("Enter the lenght 3: "))

a = Lenght_1 + Lenght_2
b = Lenght_2 + Lenght_3
c = Lenght_3 + Lenght_1

x = (Lenght_1 < b)
y = (Length_2 < c)
z = (Lenght_3 < a)

answer = str(x & y & z)
answer = answer.replace("True", "Yes")
answer = answer.replace("False", "No")

print(answer)


# Q6

a = int(input("enter the number a: "))
b = int(input("enter the number b: "))

print((str(bin(a^b))).count("1"))
