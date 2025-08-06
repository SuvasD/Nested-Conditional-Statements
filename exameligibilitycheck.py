medical_cause=input("Do you have a medical condition Y or N ")
attendance=int(input("What is your Attendance "))
if medical_cause=="Y":
    if attendance>=75:
        print("You are allowed to take the exam")
    else:
        print("You are not allowed to take the exam")
else:
    print("You are not allowed to take the exam")        