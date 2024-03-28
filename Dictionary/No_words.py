def count_words(string):
    
    words = string.split()

    word_freq = {}

    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    return word_freq

input_string = input("Enter a string: ")
result = count_words(input_string)
print(result)