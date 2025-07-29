numbers = []
#checking the value - exception handling

while True:
    number = input("Enter an integer or the 'Q'/'q' to exit: ")

    if number == 'Q' or number == 'q':
        break
    try:
        numbers.append(int(number))
    except ValueError:
        print("Only interger is allowed!\n")

if len(numbers):
    # number = numbers[::-1]
    # print("\n Integer in reverse order : ", end = " ")
    numbers.reverse()

    for num in numbers:
        print(num, end = " ")
        # print("Intergers in reverse order list : ", numbers)
    
else:
    print("No integers!")
print("\n---------------------------------------------------")

#Q4
import random

guesses = []
answers = []
outputs = []

while True:
    answer = random.randint(1, 2)
    guess = input("Enter your guess as head - 1, tail - 2, exit - 0 : ")

    if guess.isdigit():
        guess = int(guess)
        
        if not (guess >= 0 and guess <= 2):
            print("Please enter 0, 1 or 2 only!\n")
        else:
            if guess == 0:
                print("Exit!")
                break
            else:
                answers.append(answer)
                guesses.append(guess)
                
                if answer == guess:
                    print("Correct! \n")
                    outputs.append(True)
                else:
                    print("Wrong! \n")
                    outputs.append(False)
    else:
        print("Please enter 0, 1, or 2!\n")

correct = [output for output in outputs if output]
wrong = [output for output in outputs if not output]

print("RESULTS")
print("-"*4)
print(" You have made {} correct guess".format(len(correct)),"es" if len(correct) > 1 else "")
print(" and {} wrong guess".format(len(wrong)),"es" if len(wrong) > 1 else "")

for i in range(len(guesses)):
    print("-"*40)
    print("Round #{:d}".format(i + 1))
    print("-"*40)
    print("Answer: {:s}".format("Head" if answers[i] == 1 else "Tail"))
    print("Answer: {:s}".format("Head" if guesses[i] == 1 else "Tail"))
    print("Result: {:s}".format("Correct" if outputs[i] else "Wrong"))

print("-"*40)

#Q8
import random

state_capitals = {"Johor": "Johor Bahru", "Perak": "Ipoh", "Pulau Pinang": "George Town", "Selangor": "Shah Alam", }
count = 0
capital = list(state_capitals.keys())
random.shuffle(capital)

correct = 0
print("Identify the capital of state : \n")

for state in state_capitals:
    user_input = input(f"Enter the capital of {state < 4}: ")
    if user_input.strip().lower() == state_capitals[state].lower():
        print("Correct! \n")
        correct += 1
    else:
        print("Wrong! \n")

print(f"You answered {correct} questions correctly !")