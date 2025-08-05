#Return the numnber of words in the input_string
def count_words(input_string):
    words = input_string.split()
    return len(words)

#Return the number of vowels in the input_string
def count_vowels(input_string):
    return len([character for character in input_string if character.lower() in ['a', 'e', 'i', 'o', 'u']])

#Return the number of vowels 'a', 'e', 'i', 'o', 'u' separately
def count_vowel_aeiou(input_string):
    input_string = input_string.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    # counts = {vowel: input_string.count(vowel) for vowel in vowels}
    a = input_string.count('a')
    e = input_string.count('e')
    i = input_string.count('i')
    o = input_string.count('o')
    u = input_string.count('u')

    frequency = [a, e, i, o, u]
    
    return dict(zip(vowels, frequency))

#Return the average of word length in the input_string
def calculate_average_word_length(input_string):
    total = 0
    for i in input_string.split():
        total += len(i)
    return (total / len(input_string.split()))

def main1():
    # Get user input
    text = input("Enter a phrase: ").strip()

    #print the number of words
    print("No. of words:", count_words(text))

    #count the number of vowels
    print("Total vowels:", count_vowels(text))

    #count the number of each vowel
    for vowel, frequency in count_vowel_aeiou(text).items():
        print(f"No of {vowel}: {frequency:d}")

    #calculate the average word length
    average_length = calculate_average_word_length(text)    
    print("Average word length:", f"{average_length:.2f}")

# Remove irrelevant contents from the input_string.
def remove_noise(input_string):
    return "".join([letter if letter.isalpha() else "" for letter in input_string])

# Convert all elements in the input_string to a consistent case.
def normalize_case(input_string):
    return input_string.lower()

# Return true if the input_string is a palindrome.
def is_palindrome(input_string):
    input_string = normalize_case(remove_noise(input_string))
    return input_string == input_string[::-1]


def main2():
    text = input("Enter string: ").strip()

    print(" '{}' is {} a palindrome!".format(text," is " if is_palindrome(text) else " is not "))

#constants variable
ANNUAL_INTEREST = 0.05
MONTHLY_INTEREST = ANNUAL_INTEREST / 12

def read_base():
    while True:
        base = float(input("Enter the base amount: "))
        try:
            if base<=0:
                print("Please enter a positive amount!")
            else:
                return base
        except:
            print("Error: only numbers are allowed!\n")

def get_month():
    while True:
        month_input = input("Enter no of months: ")
        if month_input.isdigit():
            month = int(month_input)
            if month <= 0:
                print("Please enter a positive number!")
            else:
                return month
        else:
            print("Error: only numbers are allowed!\n")
#claculate based
def calculate_monthly_savings(base, total):
    return (base + total) * (1 + MONTHLY_INTEREST)

#print the monthly savings
def print_monthly_savings(base, no_month):
    total = 0
    for count in range(1, no_month):
        total = calculate_monthly_savings(base, total)
        print(f"Month {get_ordinal_prefix(count)} \tTotal: {total:.2f} ")

def get_ordinal_prefix(number):
    
    if number >= 11 and number <= 13:
        return str(number) + "th"
    else:
        match(number % 10):
            case 1:
                return str(number) + "st"
            case 2:
                return str(number) + "nd"
            case 3:
                return str(number) + "rd"
            case _:
                return str(number) + "th"

def main3():
    base = read_base()
    month = get_month()
    print_monthly_savings(base, month)


main1()
print("--------------------------------------------------------")
main2()
print("--------------------------------------------------------")
main3()
print("--------------------------------------------------------")

