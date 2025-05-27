import random
import time 

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
            print("❌ Invalid input! please enter a number.")

            

def play_game():
    ranges = {"easy": 50, "medium": 100, "hard": 200}
    difficulty = input("Choose difficulty (Easy/Medium/Hard): ").lower()
    max_value = ranges.get(difficulty, 100)  # Default to medium
    n = random.randint(1, max_value)

    print(f"Guess the number between 1 and {max_value}")

    a = -1
    guesses = 1

    score = 100
    start_time = time.time()

    while a != n:
        try:
            a = get_valid_number("Guess the number: ")
            if a > n:
                print("Lower Number Please!")
            elif a < n:
                print("Higher Number Please!")
        
            if a != n:  # used this if block to avoid duplication 
                # score -= 5
                score = max(0, score - 5)
            
            guesses += 1
        except ValueError:
            print("Please enter a valid number.")

    end_time = time.time()
    time_taken = end_time - start_time

    if time_taken <= 15: #calculating bonus score
        bonus = 10
    elif time_taken <= 30:
        bonus = 5
    else:
        bonus = 0

    score += bonus

    print(f"You have guessed the number {n} correctly in {guesses - 1} attempts.")
    print(f"Bonus for time: {bonus}")
    print(f"Final score (with bonus): {score}")

    high_score = get_high_score()

    if score > high_score:
        print("🎉 New High Score!")
        with open("highscore.txt", "w") as f:
            f.write(str(score))
    else:
        print(f"High Score: {high_score}")


    print(f"You took {time_taken:.2f} seconds to guess the number.")


while True:
    play_game()
    again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thanks for playing! 👋")
        break

