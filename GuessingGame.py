import random
attempts = 0
number = random.randint(1,100)


def guess_number():
    global attempts
    global guess
    guess = int(input("Try to guess the number from 1 to 100: "))
    attempts += 1

for attempts in range(7):
    guess_number()
    if guess == number:
        print(f"Congratulations, {guess} is the correct number!")
        break
    elif guess < number:
        print("Too low")
    else:
        print("Too high")
if attempts == 7 and guess !=number:
    print("Game Over")
              