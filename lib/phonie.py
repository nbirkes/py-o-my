import os

# Work in progress
# Takes your phone nubmer and determines if a vanity phone nubmer is available

keypad = {
    1: '1',
    2: ('A', 'B', 'C'),
    3: ('D', 'E', 'F'),
    4: ('G', 'H', 'I'),
    5: ('J', 'K', 'L'),
    6: ('M', 'N', 'O'),
    7: ('P', 'Q', 'R', 'S'),
    8: ('T', 'U', 'V'),
    9: ('W', 'X', 'Y', 'Z'),
    0: '0',
}


def main():
    # phone = input('What is your phone number?')
    phone = '2546447382'

    if not is_valid(phone):
        print('Phone number %s is invalid' % phone)
        return

    poss = do_it(phone, 5)
    words = get_words()
    matches = get_matches(poss, words)

    print('%s possibilities found' % len(poss))

    if len(matches) == 0:
        print('Sorry, no matches found for', phone)
    else:
        print('MATCHES!')
        for match in matches:
            print(format_vanity(phone, match))


def get_words():
    return open(os.path.dirname(os.path.abspath(__file__)) + '/static/words_2.txt', 'r').read().split()


def do_it(phone, num_digits):
    sample = ''.join(reversed(phone))[0:num_digits]
    poss = []

    for i in range(0, num_digits):
        poss = build_possibilities(sample[i], poss)

    return poss


def build_possibilities(digit, prev):
    temp = []

    if len(prev) == 0:
        for char in keypad[int(digit)]:
            prev.append(char)
    else:
        for poss in prev:
            for char in keypad[int(digit)]:
                temp.append(char + poss)

    prev = prev + temp

    return prev


def format_vanity(phone, vanity):
    phone_part = phone[0: 10 - len(vanity)]
    new_phone = phone_part + vanity
    return '%s-%s-%s' % (new_phone[0:3], new_phone[3:6], new_phone[6:10].upper())


def get_matches(possibilities, words):
    matches = []

    for p in possibilities:
        if p.lower() in words:
            matches.append(p)

    return matches


def is_valid(phone):
    for c in phone:
        try:
            int(c)
        except ValueError:
            return False

    return len(phone) == 10


if __name__ == '__main__':
    main()
