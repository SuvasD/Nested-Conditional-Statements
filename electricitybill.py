units=int(input("Please enter how many units you consumed: "))
if units<50:
    amount=(units*2.60)
    tax=25
elif units<=100:
    amount=(units-50)*3.25
    tax=35
elif units<=200:
    amount=(units-100)*5.26
    tax=45
else:
    amount=(units-200)*8.45
    tax=75
total=amount+tax
print("Electricity Bill is ",total)
