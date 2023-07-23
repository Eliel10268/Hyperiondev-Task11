
#function declaration
def alternate_case(string):
    result = ''
    #the enumerate() function is used to get both the index and the character/word from the input string.
    for i, char in enumerate(string):
        if i % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
    return result

# Example usage
input_string = "Hello World"
output_string = alternate_case(input_string)
print(output_string)


#-----------Second part---------------------


#function declaration
def alternate_word_case(string):
    words = string.split()
    result = []
    #the enumerate() function is used to get both the index and the character/word from the input string.
    for i, word in enumerate(words):
        if i % 2 == 0:
            result.append(word.lower())
        else:
            result.append(word.upper())
    return ' '.join(result)

# Example usage
input_string = "I am learning to code"
output_string = alternate_word_case(input_string)
print(output_string)
