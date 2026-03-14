string = input("enter a word: ")
char = input("Enter a single character!")
t = 0
count = 0
while t < len(string):
    if string[t] == char:
        count = count + 1
    t = t + 1
print("The character ",char, " has occured ",count," times in the string ",string )