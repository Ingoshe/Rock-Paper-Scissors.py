import random

choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
rounds = 0
max_rounds = 3  

while user_score < 2 and computer_score < 2 and rounds < max_rounds:
    computer_choice = random.choice(choices)
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    rounds += 1

# Declare the winner
if user_score > computer_score:
    print("Congratulations! You win the game!")
elif user_score < computer_score:
    print("Computer wins the game. Better luck next time!")
else:
    print("It's a tie game!")
