import random

# Function to loop until random number is guessed
def start_guess(guess_limit):

    # Range for random number
    low_num = 1
    high_num = 100

    # Generate a random number between low_num and high_num
    random_number = random.randint(low_num, high_num)

    # print("Random Number: " + str(random_number)) # Print the generated random number

    guess = ""
    attempts = 0
    out_of_guesses = False

    while guess != random_number and not(out_of_guesses):
        guess = int(input("Enter Guess: "))
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

# Choose difficulty
print("__Difficulty__\n(1) Easy (10 attempts)\n(2) Hard (5 attempts)\n")
difficulty = input("Choose difficulty: ")

if difficulty == "1":
    start_guess(10)
elif difficulty == "2":
    start_guess(5)
else:
    print("Incorrect input")
