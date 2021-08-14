from quick_sort import quick_sort


def human_is_smaller(a, b):
    print("Which one is worth more (1 or 2)?")
    print("1: ", a)
    print("2: ", b)
    bigger = ""
    while bigger != "1" and bigger != "2":
        bigger = input("Answer: ")
    is_a_bigger = (bigger == "1")
    return not is_a_bigger


def main():
    things = [
        "four",
        "one",
        "six",
        "two",
        "five",
        "three",
    ]
    increasing = quick_sort(things, human_is_smaller)
    print("From highest to lowest priority:")
    for thing in list(reversed(increasing)):
        print(thing)


if __name__ == '__main__':
    main()
