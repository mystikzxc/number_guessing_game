import random

# Function to loop until random number is guessed
def play_game(guess_limit):

    # Range for random number
    LOW_NUM = 1
    HIGH_NUM = 100

    # Generate a random number between low_num and high_num
    random_number = random.randint(LOW_NUM, HIGH_NUM)

    guess = ""
    attempts = 0
    out_of_guesses = False

    while guess != random_number and not(out_of_guesses):

            # Input for guess and try to catch an error if guess is a string
            try:
                guess = int(input(f"Enter Guess ({LOW_NUM}-{HIGH_NUM}): "))
            except ValueError:
                print(f"Please enter a number ({LOW_NUM}-{HIGH_NUM})")
                continue

            attempts += 1

            if attempts < guess_limit:
                if guess > random_number:
                    print("Too high")
                elif guess < random_number:
                    print("Too low")
            else:
                out_of_guesses = True
            
    if out_of_guesses:
        print("You ran out of guesses")
    else:
        print("You WON! It took you " + str(attempts) + " attempts")

# Function to choose difficulty
def choose_difficulty():
        
    print("__Difficulty__\n(1) Easy (10 attempts)\n(2) Hard (5 attempts)\n")
    difficulty = input("Choose difficulty: ")

    if difficulty == "1":
        play_game(10)
    elif difficulty == "2":
        play_game(5)
    else:
        print("Incorrect input")

# Main function to choose difficulty and replay game
def main():
    while True:
        choose_difficulty()

        replay = input("Would you like to play again? (y/n): ").lower()
        if replay != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()