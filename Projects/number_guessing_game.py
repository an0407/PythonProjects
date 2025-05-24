import random as rd
low_num = 0
high_num = 100
number = rd.randint(low_num, high_num)
guesses = 0
flag = 0
print("PYTHON NUMBER GUESSING GAME")
print(f"YOU HAVE TO GUESS THE CORRECT NUMBER BETWEEN {low_num} and {high_num} WITHIN 10 GUESSES!")
print()

while flag == 0:
    if(guesses == 9):
        flag = 1
    guess = input(f"Guess a number between {low_num} and {high_num}: ")
    if guess.isdigit():
        if(int(guess) <low_num or int(guess) >high_num):
            print(f"Please enter a valid number between {low_num} and {high_num}")
        elif(int(guess) < number):
            print("Your guess is too low.")
            guesses += 1
            print(f"guesses left : {10 - guesses}")
        elif(int(guess) > number):
            print("Your guess is too high.")
            guesses += 1
            print(f"guesses left : {10 - guesses}")
        else:
            print("That's right!")
            print(f"guesses = {guesses}")
            guesses += 1
            flag = 1
    else:
        print(f"Please enter a valid number between {low_num} and {high_num}")
print()
if(guesses == 10):
    print(f"THE CORRECT NUMBER WAS {number}")