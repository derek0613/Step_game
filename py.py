import random

print("Welcome to Rock-Paper_Scissors game!")

choices = ["Rock", "Paper", "Scissors"]

while True:
    player_choice = int(input("Enter your choice:\n1. Rock\n2 Paper\n3 Scissors\nYour choice (1/2/3): "))

    if player_choice not in [1,2,3]:
        print("Invalid choice. Please select 1, 2, or 3.")
        continue

    player_choice -= 1 
    computer_choice = random.randint(0,2)

    print(f"Your choice: {choices[player_choice]}")
    print(f"Computer's choice: {choices[computer_choice]}")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif(player_choice == 0 and computer_choice == 2) or \
        (player_choice == 1 and computer_choice == 0) or \
        (player_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("Computer wins!")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing! Goodbye!")
        break