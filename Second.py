#friendsName = input("Enter your friends name?")
#print(friendsName)
number1 = int(input("Enter Number1"))
operation = input("Enter an operator (+,-,*,/):")
number2 = int(input("Enter Number2"))
if operation == "+":
	print(number1 + number2)
elif operation == "-":
	print(number1 - number2)
elif operation == "*":
	print(number1 * number2)
elif operation == "/":
	if(number2==0):
		print("Cant divide by zero, TRY AGAIN YOU FOOLISH CHILD")
	else:
		print(number1/number2)
else: 
	print("Invalid operator. Please try again")
