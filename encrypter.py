# Simple encryption program

def simple_encryption(shifter):
    storage_list = []
    converted_list = []
    alphabet_list = list("abcdefghijklmnopqrstuvwxyz")
    message = input("Enter a message to encrypt:")
    storage_list.append(message)
    for letter in message:
        letter_index = alphabet_list.index(letter)
        letter_index += shifter
        if letter_index > 25:
            letter_index
        converted_list.append(alphabet_list[letter_index])
    else:
        converted_list.append(letter)
    final_list = "".join(converted_list)
    print(final_list)

simple_encryption(3)

# Printing an additional letter for all entries?