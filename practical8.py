from MyInputReaders import *
from MyStringProcessor import *

def main():
    text = read_string("Enter a string: ")
    number = read_integer()

    print("\nThe number is", number)
    print("\nNumber of string :", count_words(text))

    for vowel, freq in count_vowels(text).items():
        print(f"No of {vowel} is {freq:d}")

    #print average of the length of the string
    print("The average of the length of the string is", calculate_average_length(text))

main()