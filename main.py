import random
import time 
from colorama import Fore, init, Style
init(autoreset=True) # Automatically reset style for each print 

def get_high_score():
    try:
        with open("highscore.txt", "r") as f:
            return int(f.read())
    except FileNotFoundError:
        return 0
    
def get_valid_number(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        else:
            print(Fore.RED + "❌ Invalid input! please enter a number.")

            

def play_game():
    ranges = {"easy": 50, "medium": 100, "hard": 200}
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
                print(Fore.MAGENTA + "Lower Number Please!")
            elif a < n:
                print(Fore.MAGENTA + "Higher Number Please!")
        
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

    print(Fore.GREEN + f"You have guessed the number {n} correctly in {guesses - 1} attempts.")
    print(Fore.BLUE + f"Bonus for time: {bonus}")
    print(Fore.BLUE + f"Final score (with bonus): {score}")

    high_score = get_high_score()

    if score > high_score:
        print(Style.BRIGHT + Fore.YELLOW + "🎉 New High Score!")
        with open("highscore.txt", "w") as f:
            f.write(str(score))
    else:
        print(Style.NORMAL + Fore.WHITE + f"High Score: {high_score}")


    print(Style.BRIGHT+ Fore.YELLOW + f"You took {time_taken:.2f} seconds to guess the number.")


while True:
    play_game()
    again = input(Fore.CYAN + "\nDo you want to play again? (yes/no): ").strip().lower()
    if again != "yes":
        print(Style.BRIGHT + Fore.YELLOW + "Thanks for playing! 👋")
        break

