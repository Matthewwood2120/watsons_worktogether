#Matthew Wood

def length_of_last_word(word):
    # ''' Returns the length of the last word in a string '''
    words=word.split()
    if words:
        return len(words[-1])
    return 0

user_input = input("Enter a string: ")
print(length_of_last_word(user_input))
