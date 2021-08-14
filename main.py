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
    lines = open("unsorted_things.txt", "r").read()
    things_including_blanks = lines.splitlines()
    things_without_blanks = [line.strip() for line in things_including_blanks if line.strip()]
    sorted_things = quick_sort(things_without_blanks, human_is_smaller)
    print("From lowest to highest:")
    for thing in sorted_things:
        print(thing)


if __name__ == '__main__':
    main()
