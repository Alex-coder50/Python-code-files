"""
Write a program to check whether the student can take an exam or not. Students will be allowed only in two conditions: If they have a medical cause (Y for yes and N for no). If yes, then they will be allowed. If No, then check attendance If attendance is above 75, then allowed; otherwise, not allowed.
"""

medical_cause = input("Do you have a medical cause? y for yes, and n for no:")
if medical_cause=="y" :
    print("Go ahead you can take your exam!")
else :
    attendance = int(input("Enter your attendance!"))
    if attendance>75 :
        print("You are allowed to take the exam!")
    else:
       print("You are not allowed to take the exam!")


