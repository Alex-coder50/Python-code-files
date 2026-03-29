def add(P,Q):
    return P + Q
def subtract(P,Q):
    return P - Q
def multiply(P,Q):
    return P * Q
def divide(P,Q):
    return P / Q
print("the options are: \n a.Add \n b.Subtract \n c.Multiply \n d.Divide")
choice = input("Whats you choice?")
num_1 = int(input("The first number?"))
num_2 = int(input("The second number?"))
if choice == "a":
    print(add(num_1, num_2))
elif choice== "b":
    print(subtract(num_1, num_2))
elif choice == "c":
    print(multiply(num_1, num_2))
elif choice=="d":
    print(divide(num_1, num_2))
else:
    print("Invalid input message")