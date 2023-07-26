num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
num3 = int(input("Enter the third number"))
if num1>num2 and num1>num3:
    print("The greatest number is "+str(num1))
    if num2>num3:
        print("The middle number is "+str(num2))
        print("The least number is "+str(num3))
    else:
        print("The middle number is "+str(num3))
        print("The least number is "+str(num2))
if num2>num1 and num2>num3:
    print("The greatest number is "+str(num2))
    if num1>num3:
        print("The middle number is "+str(num1))
        print("The least number is "+str(num3))
    else:
        print("The middle number is "+str(num3))
        print("The least number is "+str(num1))
if num3>num2 and num3>num1:
    print("The greatest number is "+str(num3))
    if num2>num1:
        print("The middle number is "+str(num2))
        print("The least number is "+str(num1))
    else:
        print("The middle number is "+str(num1))
        print("The lowest number is "+str(num2))
      
    