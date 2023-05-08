import random

print("Welcome to the game!")
print("Hi, I am SF. Please type 'yes' to start!")

while True:
    start_game = input("Type 'yes' to start: ")
    if start_game.lower() == 'yes':
        break

while True:
    no_of_guesses = int(input("Please enter the limit of the number, the bigger the number the harder the game: "))
    if no_of_guesses > 0:
        break

numb = random.randrange(1, no_of_guesses + 1)

while True:
    guess = int(input("Okay then! Guess a number between 1 and {}: ".format(no_of_guesses)))
    if guess < 1 or guess > no_of_guesses:
        print("The number you guessed is not between your selection.")
    elif numb == guess:
        print("Your guess is correct!")
        break
    elif numb > guess:
        print("Your guess is lower.")
    else:
        print("Your guess is higher.")
