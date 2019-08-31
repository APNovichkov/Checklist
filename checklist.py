#!/usr/bin/env python


checklist = list()


def create(item):
    checklist.append(item)


def read(index):
    return checklist[index]


def update(index, item):
    checklist[index] = item


def destroy(index):
    checklist.pop(index)


def list_all_items():
    index = 0
    for item in checklist:
        print("{} : {}".format(index, item))
        index += 1


def mark_completed(index):
    checklist[index] = "√" + checklist[index]


def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))

    list_all_items()


def select(function_code):
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)
    elif function_code == "R":
        item_index = user_input("Index Number?")
        print(read(int(item_index)))
    elif function_code == "P":
        list_all_items()
    elif function_code == "Q":
        return False
    else:
        print("Unknown Option")

    return True


def user_input(prompt):
    user_input = input(prompt)
    return user_input


def main():
    running = True
    while running:
        selection = user_input("Enter C to input item, R to read item, P to list all items")
        running = select(selection)


if __name__ == "__main__":
    main()
