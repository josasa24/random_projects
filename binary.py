# Binary converter

def binary_converter():
    binary_list = [4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    concat_list = []
    number_to_convert = int(input("Please enter a number to convert to binary."))
    if (number_to_convert < 0) or (number_to_convert > 8191):
        raise ValueError("Please enter a number that is greater than or equal to 0 and less than or equal to 8191.")
    else:
        for binary in binary_list:
            if number_to_convert >= binary:
                concat_list.append("1")
                number_to_convert -= binary
            else:
                concat_list.append("0")
    result = "".join(concat_list)
    return print(result)

binary_converter()