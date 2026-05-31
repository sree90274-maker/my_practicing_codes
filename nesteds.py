a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
c = int(input("Enter a number:"))
if a>b:
   if a>c:
     print("largest number is a:")
else:
	print("c is a largest number:")


print("_"*90)

num_1 = 20
num_2 = 80
num_3 = 2.5
if a>b:
   if a>c:
       print("num_1 is largest:")

 

#check wheather a chracter is alphabet . if yes check whether it is a vowel or consonent

character = input("Enter a character:")
if character is "alpha":
   if character in "aeiou":
      print("character is vowel:")
else:
   print("consonent")
print("_______________________________________")
# check eligible for vote or not.if eligible ,check they are senior citizen
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible for voting")
    if age >= 60:
        print("Senior Citizen")
    else:
        print("Not a Senior Citizen")
else:
    print("Not Eligible for voting")

print("__________________")
#positive number /even or odd
num = int(input("Enter a number: "))
if num > 0:
    print("num is positive")
    if num % 2 == 0:
        print("num is even")
    else:
        print("num is odd")
else:
    print("Not a Positive Number")
print("_________________________")
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin":
    print("Username Correct")
    if password == "1234":
        print("Login")
    else:
        print("Wrong Password")
else:
    print("Wrong Username")	



	