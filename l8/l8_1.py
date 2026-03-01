"""
Write a program to calculate the sum of whole numbers.
"""
number = int(input("Enter a number!"))
sum = 0
for i in range(1,number+1):
    print("The sum of:", sum,"and", i ,"is")
    sum = sum + i
    print(sum)