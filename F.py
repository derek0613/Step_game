name = input("Welcome to the Escape room! Enter your name to get started! ")
attempts=0
while True:
    Line1 = print("Hi "+name+" You just woke up and you don't know where you are.") 
    Line2 = input("Would you like to check the surroundings?(Type 'yes' or 'no') ")
    if Line2=="yes":
        print("You check your surroundings and you see that you are in an abandoned jail cell ")
        