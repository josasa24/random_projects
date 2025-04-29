# Divisible number finder

def divisible_number_finder():
    number = int(input("Please enter a number."))
    number_list = []
    divisible_list = []
    if (number < 1):
        raise ValueError("Please enter a number that is greater than or equal to 1.")
    for i in range(number + 1, 1, -1):
        number_list.append(i)
    for j in number_list:
        if number % j == 0:
            divisible_list.append(j)
    divisible_list.append(1)
    return print(f"{divisible_list}")

divisible_number_finder()