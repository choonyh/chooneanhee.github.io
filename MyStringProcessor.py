def count_words(input_string):
    
    return len(input_string.split())

def count_vowels(input_string):
    input_string = input_string.lower()
    vowel = ['a', 'e', 'i', 'o', 'u']

    a = input_string.count('a')
    e = input_string.count('e')
    i = input_string.count('i')
    o = input_string.count('o')
    u = input_string.count('u')
    freq = [a, e, i, o, u]

    return dict(zip(vowel, freq))

def calculate_average_length(input_string):
    total = 0
    for i in input_string.split():
        total += len(i)
    return (total / len(input_string.split()))