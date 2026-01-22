operator=input("enter an operator(+,-,*,/):")

num1=float(input("enter first number:"))
num2=float(input("enter second number:"))

if operator=="+":
    print(f"Sum of the given numbers is {num1+num2}")
elif operator=="-":
    print(f"Difference of the given numbers is {num1-num2}")
elif operator=="*":
    print(f"Product of the given numbers is {num1*num2}")
elif operator=="/":
    print(f"Quotient of the given numbers is {num1/num2}")
elif operator=="%":
    print(f"Remainder of the given numbers is {num1%num2}")
else:
    print("please enter a valid operator")
