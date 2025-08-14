import random

options = ["rock", "paper", "scissors"]


while True:
    
    computer_choice = random.choice(options)

    user_choice = input("Enter rock, paper, or scissors: ").lower()

    if user_choice not in options:
        print("Invalid choice. Please try again.")
    else:
        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("Match tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")
            
    play_again = input("Do you want to play Rock, Paper, Scissors? (yes/no): ").lower()
    if play_again not in ["yes", "no"]:
        print("Please enter 'yes' or 'no'.")
    elif play_again == "no":
        print("Thanks for playing!")
        break
        
        