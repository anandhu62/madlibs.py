
weight=float(input("Enter the weight: "))

unit=input("Kilogram or Pounds?(K for kg//L for Pounds):")
valid=True

if unit=="K":
    weight=weight*2.205
    unit="Lbs"
elif unit=="L":
    weight=weight/2.205
    unit="kg"
else:
    print(f"Sorry, {unit} is not a valid unit")
    valid=False

if valid==True:
    print(f"Your weight is {round(weight, 2)} {unit}")
else:
    print("please be carefull")
