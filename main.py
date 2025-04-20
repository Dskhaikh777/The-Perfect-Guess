import random

ranges = {"easy": 50, "medium": 100, "hard": 200}
difficulty = input("Choose difficulty (Easy/Medium/Hard): ").lower()
max_value = ranges.get(difficulty, 100)  # Default to medium
n = random.randint(1, max_value)

print(f"Guess the number between 1 and {max_value}")

a = -1
guesses = 1

while a != n:
    try:
        a = int(input("Guess the number: "))
        if a > n:
            print("Lower Number Please!")
        elif a < n:
            print("Higher Number Please!")
        guesses += 1
    except ValueError:
        print("Please enter a valid number.")

print(f"You have guessed the number {n} correctly in {guesses - 1} attempts.")
