import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    user_score = 0
    computer_score = 0
    while True:
        print("\nChoose: rock, paper, or scissors.")
        user_choice = input("Your choice: ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please choose again.")
            continue
        
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f"Computer chooses: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if 'win' in result:
            user_score += 1
        elif 'lose' in result:
            computer_score += 1
        
        print(f"Score - You: {user_score}, Computer: {computer_score}")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

play_game()
