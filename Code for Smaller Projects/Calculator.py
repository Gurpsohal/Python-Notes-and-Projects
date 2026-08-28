#type casting convertign from one type to another. 

operator = input("Enter an Operator (+- */):")
num1 = float(input("Enter the first number"))
num2 = float(input("Enter the second numbe"))

if operator == "+":
    print (num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print (num1/num2)
else:
    print("Please try again and select a valid operator, Thanks.")