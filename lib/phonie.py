import os

# Work in progress
# Takes your phone nubmer and determines if a vanity phone nubmer is available

keypad = {
    1: (),
    2: ('A', 'B', 'C'),
    3: ('D', 'E', 'F'),
    4: ('G', 'H', 'I'),
    5: ('J', 'K', 'L'),
    6: ('M', 'N', 'O'),
    7: ('P', 'Q', 'R', 'S'),
    8: ('T', 'U', 'V'),
    9: ('W', 'X', 'Y', 'Z'),
}


class Possibility:
    def __init__(self, phone, vanity):
        self.phone = phone
        self.vanity = vanity

    def to_string(self):
        return self.phone + self.vanity


def main():
    # phone = input('What is your phone number?')
    phone = '2546447382'
    if not is_valid(phone):
        print('Phone number {phone} is invalid')
        return

    get_possibilities(phone, [])


def get_words():
    words = open(os.path.dirname(os.path.abspath(__file__)) + '/static/words.txt')
    return words.read()


def get_possibilities(phone, possibilities):
    digit = phone[len(phone) - 1:len(phone)]
    new_phone = phone[:len(phone) - 1]

    for x in keypad[int(digit)]:
        possibility = Possibility(new_phone, x)
        possibilities.append(possibility)
        print(possibility.to_string())

    return get_possibilities(new_phone, possibilities)


def is_valid(phone):
    for c in phone:
        try:
            int(c)
        except ValueError:
            return False

    return True


main()
