import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return "You win!"
    else:
        return "You lose!"

def display_result(user_choice, computer_choice, result):
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    print(result)

def rock_paper_scissors():
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock-Paper-Scissors Game")
        print("1. Rock\n2. Paper\n3. Scissors\n4. Quit")

        try:
            user_choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if user_choice == 4:
            print("Thanks for playing! Final Scores:")
            print(f"You: {user_score}, Computer: {computer_score}")
            break
        elif user_choice not in range(1, 4):
            print("Invalid choice. Please choose a number between 1 and 3.")
            continue

        choices = ['rock', 'paper', 'scissors']
        user_choice = choices[user_choice - 1]
        computer_choice = random.choice(choices)

        result = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, result)

        if 'win' in result:
            user_score += 1
        elif 'lose' in result:
            computer_score += 1

        print(f"Scores - You: {user_score}, Computer: {computer_score}")

if __name__ == "__main__":
    rock_paper_scissors()
