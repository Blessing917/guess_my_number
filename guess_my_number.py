"""Author: Blessing Glory Tsikey.

Purpose: Guess my number game, including the stretch challenges.
"""
import random  

play_again = "yes"
# As long as they say "yes" we will keep playing

while play_again.lower() == "yes":
    magic_number = random.randint(1, 100)
    guess = -1
    guess_count = 0
    print("\nWelcome to the Guess My Number game!")
    print("Try to guess the magic number between 1 and 100.\n")
    while guess != magic_number:
        try:
            guess = int(input("What is your guess? "))
            guess_count += 1  
            if guess < magic_number:
                print("Higher")
            elif guess > magic_number:
                print("Lower")
            else:
                print(f"Congratulations! You guessed it right in {guess_count} tries!")
        except ValueError:
            print(" Please enter a valid number.")
    play_again = input("\nDo you want to play again? (yes/no) ")
print("Thanks for playing! Goodbye! ")
