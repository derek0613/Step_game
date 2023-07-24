code="A"
counter =0
while True:
	answer = input("Enter your password: ")
	if answer==code:
		print("Allow access")
		break
	else:
		counter+=1
		print("Wrong Password, Try Again")
		if counter==3:
			print("Password Denied, Account Locked For 12 Hours")
			break
		
		
