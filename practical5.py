#Q1
text = input("Enter a Phrase: ").strip()
word = text.split()
acronym = ""

for characterInWord in word:
    acronym += characterInWord[0].upper()

print("The acronym for " + text +  " is " + acronym)

print("--------------------------------------------------")
#Q2
text = input("Enter a phrase: ").strip()

words = text.split()
print("\nNo. of words: ", len(words))

vowel = "aeiou"
text = text.lower()

print("Vowel\t Occurance")
for character in vowel:
    print(character,"\t",text.count(character))

total = 0
for word in words:
    total += len(word)
print("The average word length is : ", f"{total/len(words):.2f}")

print("--------------------------------------------------------")
#Q3
annual_interest = 0.05
monthly_interest = annual_interest/12

base = 100
total = 0
repeat = 10
month = ""

print("Month \tTotal ")
for count in range(repeat):
    total = (base + total) * (1 + monthly_interest)

    match(count + 1) % 10:
        case 1:
            month = str(count + 1) + "st"
        case 2:
            month = str(count + 1) + "nd"
        case 3:
            month = str(count + 1) + "rd"
        case _:
            month = str(count + 1) + "th"
    print(f"{month:10s}RM{total:10.2f}")

print("---------------------------------------------------")
#Q4
str1 = input("Enter a string: ").strip()
str2 = str1.lower()

for letter in str2:
    if not letter.isalpha():
        str2 = str2.replace(letter, '')

length = len(str2)
result = True

for i in range(len(str2)):
    if str2[i] != str2[length -1 - i]:
        result = False
        break

print("'{}' {} a palindrome!".format(str1, "is" if result else "is not"))
print("------------------------------------------------------------------")
#Q7
while True:
    print("1. Encoding \n2. Decodling \n3. Exit")
    option = int(input("Enter an option (1,2, or 3): "))

    match option:
        case 1:
            print("\n--------------------------Encoding-------------------------")
            message = input("Enter a message to be encoded: ").strip()
            key = int(input("Enter a key: "))

            code = ""

            char_list = list(message)
            for char in char_list:
                code += chr(ord(char)+key)
            
            print(f" The encoded message is '{code}'")

        case 2:
            print("\n-------------------------Decoding-------------------------")
            message = input("Enter a message to be decoded: ").strip()
            key = int(input("Enter a key: "))

            decode = ""

            char_list = list(message)
            for char in char_list:
                decode += chr(ord(char)-key)
            
            print(f" The decoded message is '{code}'")

        case 3:
            print("Thank You! See You again!")
            break

        case _:
            print("Wrong Input!")
print("---------------------------------------------------------------------------------")