#!/usr/bin/env python

import re

checklist = list()


def create(value):
    checklist.append(value)
    print("Added item: " + str(value))


def read(index):
    print("Value at index " + str(index) + " is: " + str(checklist[int(index)]))


def update(index, value):
    checklist[int(index)] = value
    print("Updated value at index: " + str(index) + " to: " + str(value))


def destroy(index):
    checklist.pop(int(index))
    print("Destroyed value at index: " + str(index))


def list_all_items():
    index = 0
    print("All items in the checklist: ")
    for item in checklist:
        print("{} : {}".format(index, item))
        index += 1


def mark_completed(index):
    checklist[int(index)] = "√ " + checklist[int(index)]


# Input-validating functions
def is_input_empty(user_input):
    return (len(user_input) == 0)


def validate_code(user_input):
    return (not is_input_empty(user_input) and user_input in codes)


def is_valid_index(user_input):
    return (not is_input_empty(user_input) and user_input.isdigit() and int(user_input) < len(checklist))


def test():
    create("hi")
    create(3)

    # Should print 3
    print(str(read(1)))

    list_all_items()

    update(0, "hi 2.0")
    create("dog")

    # Will delete 3
    destroy(1)

    list_all_items()

    mark_completed(0)
    mark_completed(1)

    # Should print hi 2.0 and dog and both should have a checkmark under them
    list_all_items()


codes = {
    "C": (create, "Enter a value: "),
    "R": (read, "Enter an index: "),
    "P": list_all_items,
    "U": (update, "Enter an index; ", "Enter a replacement value: "),
    "D": (destroy, "Enter an index: "),
    "M": (mark_completed, "Enter an index: "),
    "Q": "Quitting"
}


def select(function_code):

    should_i_quit = False

    if function_code == "U":
        index = user_input(codes[function_code][1])
        value = user_input(codes[function_code][2])

        if is_valid_index(index) and not is_input_empty(value):
            codes[function_code][0](index, value)
        else:
            print("Invalid input")

    elif function_code == "Q":
        should_i_quit = True
    elif function_code == "P":
        codes[function_code]()
    else:
        index_or_value = user_input(codes[function_code][1])

        if re.match("Enter an index: ", codes[function_code][1]):
            if is_valid_index(index_or_value):
                codes[function_code][0](index_or_value)
            else:
                print("Index out of range")
        else:
            if not is_input_empty(index_or_value):
                codes[function_code][0](index_or_value)
            else:
                print("No input")

    return should_i_quit


def user_input(prompt):
    return input(prompt)


def main():

    test()

    separator = "------------------------------------------------------------------"
    prompt = "Enter C to add item, enter R to read item, enter D to delete item,\nenter M to mark item completed, enter U to update item, enter P to\nlist all items, enter Q to quit: "

    should_i_quit = False

    while not should_i_quit:
        function_code = user_input(separator + "\n" + prompt).upper()
        if validate_code(function_code):
            should_i_quit = select(function_code.upper())
        else:
            print("Incorrect code, try again!\n")


if __name__ == "__main__":
    main()
