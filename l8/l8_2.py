"""
Write a program to reverse the string entered by the user.
"""
write = input("Write something!")
reverse =""
for i in write:
    reverse = i + reverse
print("the original string is:", write)
print("The reversed string is:", reverse)