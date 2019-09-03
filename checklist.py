#!/usr/bin/env python

import re

checklist = list()
quit = False


def create(value):
    checklist.append(value)
    print("Added item")


def read(index):
    print(checklist[int(index)])


def update(index, value):
    checklist[int(index)] = value


def destroy(index):
    checklist.pop(int(index))


def list_all_items():
    index = 0
    for item in checklist:
        print("{} : {}".format(index, item))
        index += 1


def mark_completed(index):
    checklist[index] = "√" + checklist[index]


# Input-validating functions
def is_input_empty(user_input):
    return (len(user_input) == 0)


def validate_code(user_input):
    return (not is_input_empty(user_input) and user_input.upper() in codes)


def is_valid_index(user_input):
    return (not is_input_empty(user_input) and user_input.isdigit() and int(user_input) < len(checklist))


codes = {
    "C": (create, "Enter a value: "),
    "R": (read, "Enter an index: "),
    "P": list_all_items,
    "U": (update, "Enter an index; ", "Enter a replacement value: "),
    "D": (destroy, "Enter an index: "),
    "Q": quit
}


def select(function_code):

    is_input_accepted = True

    if function_code.upper() == "U":
        index = user_input(codes[function_code][1])
        value = user_input(codes[function_code][2])

        if is_valid_index(index) and not is_input_empty(value):
            codes[function_code][0](index, value)
        else:
            print("Invalid input")
            is_input_accepted = False

    elif function_code.upper() == "Q":
        quit = True
    elif function_code.upper() == "P":
        codes[function_code]()
    else:
        index_or_value = user_input(codes[function_code][1])

        if re.match("Enter an index: ", codes[function_code][1]):
            if is_valid_index(index_or_value):
                codes[function_code][0](index_or_value)
            else:
                print("Invalid input")
                is_input_accepted = False
        else:
            if not is_input_empty(index_or_value):
                codes[function_code][0](index_or_value)
            else:
                print("Invalid input")
                is_input_accepted = False

    return is_input_accepted


def user_input(prompt):
    return input(prompt)


def main():
    running = True
    prompt = "\nEnter C to add item, enter R to read item, enter D to delete item, enter U to update item, enter P to list all items, enter Q to quit: "

    index = 0

    while not quit or index < 5:
        input = user_input(prompt)
        if validate_code(input):
            running = select(input.upper())
        else:
            print("Incorrect code, try again!\n")

        index += 1

if __name__ == "__main__":
    main()
