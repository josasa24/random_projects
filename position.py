# Position finder

def position_finder():
    letter = input("Please enter a letter.")
    alphabet_list = list("abcdefghijklmnopqrstuvwxyz")
    if letter not in alphabet_list:
        raise Exception("Please enter a letter that is one of the 26 letters in the English alphabet.")
    else:
        return print(f"The Position of {letter} is {alphabet_list.index(letter) + 1}.")
    
position_finder()