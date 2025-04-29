# Name generator

first_list = ["Wolf", "Dolphin", "Canine", "Feline"]
second_list = ["Elephant", "Giraffe", "Monkey", "Tiger", "Bear", "Giraffe"]

def name_generator():
    first_name = first[:3]
    #Original code below, replaced with improved line
    # second_name = second[len(second)-4:len(second)]
    second_name = second[-4:]
    return first_name + second_name

def name_generator_version2(first_list, second_list):
    name_list = []
    for f in first_list:
        for s in second_list:
            name_list.append(f[:3] + s[-4:])

    for s in second_list:
        for f in first_list:
            name_list.append(s[:3] + f[-4:])

    return print(name_list)

# name_generator("Wolf", "Dolphin")

name_generator_version2(first_list, second_list)