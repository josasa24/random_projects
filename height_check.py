# Simple sequential height check program

list1 = [-3, -1, 1, 2, 3, 10, 100]

def height_check(list):
    for i in range(1, len(list)):
        if list[i] <= list[i - 1]:
            return False
    return True

height_check(list1)