import random


def get_lowest_highest():
    lowest = int(input("Enter the lowest number: "))
    highest = int(input("Enter the highest number: "))
    return lowest, highest


def play(number):
    while True:
        guess = int(input("Enter your guess: "))
        if guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")
        else:
            print("Correct!")
            break


def main():
    lowest, highest = get_lowest_highest()
    number = random.randint(lowest, highest)
    print("Guess the number between", lowest, "and", highest)
    play(number)


main()