import os

# Work in progress
# Takes your phone nubmer and determines if a vanity phone nubmer is available

keypad = {
    1: (),
    2: ('a', 'b', 'c'),
    3: ('d', 'e', 'f'),
    4: ('g', 'h', 'i'),
    5: ('j', 'k', 'l'),
    6: ('m', 'n', 'o'),
    7: ('p', 'q', 'r', 's'),
    8: ('t', 'u', 'v'),
    9: ('w', 'x', 'y', 'z'),
}


def main():
    phone = input('What is your phone number?')
    if not is_valid(phone):
        print('Phone number {phone} is invalid')
        return

    print(phone)


def get_words():
    words = open(os.path.dirname(os.path.abspath(__file__)) + '/static/words.txt')
    return words.read()


def get_possibilities(phone):
    possibilities = []
    for c in phone:
        for x in keypad[int(c)]:
            print(x)

    return possibilities


def is_valid(phone):
    for c in phone:
        try:
            int(c)
        except ValueError:
            return False

    return True


main()
