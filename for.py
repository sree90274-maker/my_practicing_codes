#for loop format
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
	print(fruit)

fruits = ["apple", "banana", "orange"]
for orange in fruits:
	print(orange)


print("__________________________")
fruits = ["apple", "banana", "orange"]
for i in range(3):
	print(i)

fruits = ["apple", "banana", "orange"]
for fruits in range(3):
	print(fruits)

#1 to 10 numbers print by using for loop
for i in range(1,10):
	print(i)
#reverse order

for i in range(9,0,-1):
	print(i)

#print all numbers ARE EVEN
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for i in numbers:
    if i % 2 == 0:
       print(i)
        
#print all numbers ARE ODD
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for i in numbers:
    if i % 2 != 0:
        print(i)

#check positive and negative numbers in list
numbers = [-2, 5, -1, 8, 3]
for i in numbers:
    if i > 0:
        print(i)

print("____________________________")
numbers = [-2, 5, -1, 8, 3]
for i in numbers:
    if i<0:
        print(i)
#sum of numbers from 1 to 100
sum = 0
for i in range(1,101):
	sum=sum+i
	print(sum)

#print string characters
name = "Durgasree"
for s in name:
	print(s)

name = "Durgasree"
for s in name:
    if s=="ga":
       print(s)
else:
	print("not ga")

name = "Durgasree"
for u in name:
    if u == "e":
       print(u)







	
       






