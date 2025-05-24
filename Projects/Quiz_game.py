
questions = ("1. Which is the fastest animal on earth?",
             "2. Which is the largest animal?",
             "3. Which is the tallest animal on land?",
             "4. Which animal lays the largest eggs?",
             "5. Which continent is made only of ice?")

options = ( ("A. Leopard", "B. Tiger", "C. Cheetah", "D. Lion"),
            ("A. Blue Whale", "B. Elephant", "C. Giraffe", "D. Chimpanzee"),
            ("A. Elephant", "B. Giraffe", "C. Kangaroo", "D. Camel"),
            ("A. Duck", "B. Elephant", "C. Crow", "D. Ostrich"),
            ("A. Antarctica", "B. Asia", "C. South America", "D. Australia"))

answers = ['C', 'A', 'B', 'D', 'A']
guesses = []
score = 0
question_num = 0

for question in questions:
    print("---------------------------")
    print(f"{question}")
    print(f"{options[question_num]}")
    guess = input("Choose an option (A, B, C, D): ").upper()
    guesses.append(guess)
    if(guess == answers[question_num]):
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print("The correct answer is: ", answers[question_num])
    question_num += 1
    print()
print()
print("-------------------")
print("      RESULTS      ")
print("-------------------")

print("Answers: ", end='')
for answer in answers:
    print(answer, end=' ')
print()

print("Guesses: ", end='')
for guess in guesses:
    print(guess, end=' ')
print()

print(f'Score: {(score/len(questions))*100}%')