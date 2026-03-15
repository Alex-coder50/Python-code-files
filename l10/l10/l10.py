lower = int(input("give an integer?"))
upper = int(input("give an 2nd integer?"))
print("the prime number: ", lower,"and",upper,"are:")
for num in range(lower, upper +1):
    if num > 1:
        for i in range(2, num):
            if (num%i) ==0:
                break
        else:
            print(num)    
