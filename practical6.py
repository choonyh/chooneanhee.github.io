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
    number = numbers[::-1]
    print("\n Integer in reverse order : ", end = " ")

    for num in numbers:
        print(num, end = " ")
else:
    print("No integers!")

