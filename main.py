import random
import time 
import json
from colorama import Fore, init, Style
init(autoreset=True) # Automatically reset style for each print 

try:
    with open("high_scores.json", "r") as f:
        high_scores = json.load(f)
except FileNotFoundError:
    high_scores = {} # <-- If file doesn't exit

def show_high_scores(high_scores_dict):
    for name, score in sorted(high_scores_dict.items(), key= lambda x: x[1], reverse=True):
        print(f"{name}: {score}")

    
def get_valid_number(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        else:
            print(Fore.RED + "❌ Invalid input! please enter a number.")

            
def main_menu():
    while True:
        print(Style.BRIGHT + Fore.YELLOW + "\n🎮=== The Perfect Guess ===🎮")
        print("1. Play Game")
        print("2. View High Score")
        print("3. Exit")

        choice = input(Fore.CYAN + "Enter your choice (1/2/3): ")

        if choice == '1':
            while True:
                play_game()
                again = input(Fore.CYAN + "\nDo you want to play again? (yes/no): ").strip().lower()
                if again != "yes":
                    print(Style.BRIGHT + Fore.YELLOW + "Thanks for playing! 👋")
                    break
        elif choice == '2':
            print(Fore.BLUE + "\n🏆 High Scores:")
            show_high_scores(high_scores)

        elif choice == '3':
            print(Style.BRIGHT + Fore.YELLOW + "Thank you for playing! Goodbye! 👋")
            break
        else:
            print(Fore.RED + "❌ Invalid choice. Please try again.")

def play_game():
    ranges = {"easy": 50, "medium": 100, "hard": 200}
    player_name = input("Enter your name: ").strip().capitalize()
    difficulty = input(Style.BRIGHT + Fore.BLUE + "Choose difficulty (Easy/Medium/Hard): ").lower()
    max_value = ranges.get(difficulty, 100)  # Default to medium
    n = random.randint(1, max_value)

    print(Fore.CYAN + f"Guess the number between 1 and {max_value}")

    a = -1
    guesses = 1

    score = 100
    start_time = time.time()

    while a != n:
        try:
            a = get_valid_number(Fore.CYAN + "Guess the number: ")
            if a > n:
                print(Fore.MAGENTA + "📉 Lower Number Please!")
            elif a < n:
                print(Fore.MAGENTA + "📈 Higher Number Please!")
        
            if a != n:  # used this if block to avoid duplication 
                # score -= 5
                score = max(0, score - 5)
            
            guesses += 1
        except ValueError:
            print(Fore.RED + "Please enter a valid number.")

    end_time = time.time()
    time_taken = end_time - start_time

    if time_taken <= 15: #calculating bonus score
        bonus = 10
    elif time_taken <= 30:
        bonus = 5
    else:
        bonus = 0

    score += bonus

    print(Fore.GREEN + f"🎯 You have guessed the number {n} correctly in {guesses - 1} attempts.")
    print(Fore.BLUE + f"Bonus for time: {bonus}")
    print(Fore.BLUE + f"Final score (with bonus): {score}")

    global high_scores # Dictionary to store names and scores

    if player_name not in high_scores or score > high_scores[player_name]:
        high_scores[player_name] = score
        with open("high_scores.json", "w") as f:
            json.dump(high_scores, f)
        print(Style.BRIGHT + Fore.YELLOW + f"🎉 New high score for {player_name}!")

    print(Style.BRIGHT+ Fore.YELLOW + f"You took {time_taken:.2f} seconds to guess the number.")

main_menu()