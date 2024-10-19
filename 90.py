import random

number = random.randint(1, 10)
chances = 5

print("**** Welcome To Number Guessing Game ****")
while chances > 0:
    guess = input("Guess the number (Between 1-10) : ")
    try:
        guess = int(guess)
        if 1 <= guess <= 10:
            if guess == number:
                print("You Won!😎🙈")
                break
            elif guess > number:
                print("Try Smaller")
            elif guess < number:
                print("Try Bigger")
            chances -= 1
        else:
            print("The number is between 1-10")
    except ValueError:
        print("Entry must be an integer. Try again")

else:
    print(f"Game Over! The number was {number} 😂🤡👍")

input("Press any key to exit")
