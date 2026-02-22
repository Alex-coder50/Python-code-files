Amount = int(input("Enter the amount for withdraw :"))

note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10

print("Notes of 100 euros" ,note_1)
print("Notes of 50 euros" ,note_2)
print("Notes of 10 euros" ,note_3)