import random as rd

#input number from 1-5 from user
num = int(input("enter a number from 1 to 5: "))

#generate random number
guess = rd.randint(1,5)

#check if user's guess i right?
if(num == guess):
    print("Correct!")
else:
    print(f"Incorrect! The number is {guess}")
