def read_string(prompt_msg):

	return input(prompt_msg).strip()

def read_integer(prompt= "Enter an integer: ", error = "Error: Wrong input!\n"):
    while True:
        number = input(prompt).strip()
        try:
            number = int(number)
            if number > 0:
                return number
            else:
                print(error)
        except ValueError:
            print(error)
   