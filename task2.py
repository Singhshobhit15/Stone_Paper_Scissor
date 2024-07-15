import random

def get_user_choice():
    choice = input("Enter choice (stone, paper, scissors): ").lower()
    while choice not in ["stone", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        choice = input("Enter choice (stone, paper, scissors): ").lower()
    return choice

def get_computer_choice():
    return random.choice(["stone", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "stone" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "stone") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
