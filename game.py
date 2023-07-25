import random
number = random.randint(1, 100)
name = input("Welcome to 'Guess the number' Game! Enter your name to get started!: ")
tries =0
while True:  
    num1=int(input("Guess a number between 1 to 100: "))
    if (number>num1):
        print("Too low!")
        tries += 1
    elif (number<num1):
        print("Too high!") 
        tries +=1
    else:
        print("Congratulations ",name," you guessed the number in ", +tries," tries!")
        break