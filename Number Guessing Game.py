# PINEDA, SOPHIA KEZIAH G. ICT - 107 | MIDTERM ACTIVITY | FIRST YEAR
# NUMBER GUESSING GAME


lowest = 1
highest = 50
correct_number = 24  # Can be manipulated

attempts = 0

# INTRO  
print("Welcome to Pia's guessing game!")
print(f"Start the Game, Guess a number from {lowest} to {highest}")

while True:
    attempts += 1

    # Determine suffix (st, nd, rd)
    if 10 < attempts % 100 < 14:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(attempts % 10, "th")

    guess = input(f"{attempts}{suffix} Try: ")

    try:
        guess = int(guess)
        if guess < lowest or guess > highest:
            print(f"Out of range. Guess a number from {lowest} to {highest}.")
        elif guess < correct_number:
            print(f"The number is higher than {guess}.")
        elif guess > correct_number:
            print(f"The number is lower than {guess}.")
        else:
            print(f"You got it right! The correct number is {correct_number}")
            print(f"Your total attempts: {attempts}")

            # Reset to avoid bugs
            attempts = 0
            print("\nLet's play again!")
    except ValueError:
        print(f"Invalid input! Guess a number from {lowest} to {highest}.")
