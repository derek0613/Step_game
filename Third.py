code="A"
Username="Derek"
counter =3
while True:
	login = input("Welcome to the calculator! Enter your username:  ")
	login2 = input("Enter your password: ")
	if login==Username and code==login2:
		print("Allow access, you can now use the calculator")
		number1 = int(input("Enter Number1 "))
		operation = input("Enter an operator (+,-,*,/):")
		number2 = int(input("Enter Number2 "))
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
	else:
		counter -= 1
		if counter==0:
			print("Too many tries, please try again later")
			break
		else:
			print("Incorrect Username or Password. You still have ", +counter, "Tries left")
			
		
		
