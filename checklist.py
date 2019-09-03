#!/usr/bin/env python

import re

checklist = list()


def create():
    input = user_input("Enter a value: ")
    checklist.append(input)
    print("Added item")
    return True


def read():
    print(checklist[int(input("Enter an index: "))])
    return True


def update():
    index = int(input("Enter an index: "))
    item = input("Enter a replacement value: ")
    checklist[index] = item
    return True


def destroy():
    checklist.pop(int(input("Enter an index: ")))
    return True


def list_all_items():
    index = 0
    for item in checklist:
        print("{} : {}".format(index, item))
        index += 1


def quit():
    return False


def mark_completed(index):
    checklist[index] = "√" + checklist[index]


# Validating functions
def validate_general_input(user_input):
    if(len(user_input) > 0):
        return True
    else:
        return False


def validate_code(user_input):
    return (validate_general_input(user_input) and user_input.upper() in codes)


def validate_code_1(user_input):
    if validate_general_input(user_input) and user_input in codes:
        return True
    else:
        return False


def validate_index(user_input):
    if validate_general_input() and user_input.isdigit() and int(user_input) <= len(checklist):
        return True
    else:
        return False


codes = {
    "C": create,
    "R": read,
    "P": list_all_items,
    "U": update,
    "D": destroy,
    "Q": quit

}


def select(function_code):
    return codes[function_code]()


def user_input(prompt):
    user_input = input(prompt)
    return user_input


def main():
    running = True
    prompt = "\nEnter C to add item, enter R to read item, enter D to delete item, enter U to update item, enter P to list all items, enter Q to quit: "

    while running:
        input = user_input(prompt)
        if validate_code(input):
            running = select(input)
        else:
            input = user_input("Incorrect code, try again!\n\n")


if __name__ == "__main__":
    main()
