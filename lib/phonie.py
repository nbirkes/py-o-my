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


def main():
    phone = input('What is your phone number?')

    if not is_valid(phone):
        print('Phone number %s is invalid' % phone)
        return

    poss = generate_possibilities(phone, 9, [])
    words = get_words()
    matches = get_matches(poss, words)

    if len(matches) == 0:
        print('Sorry, no matches found for', phone)
    else:
        print('MATCHES!')
        for match in matches:
            print('%s-%s-%s' % (phone[0:3], phone[3:6], match.upper()))


def get_words():
    return open(os.path.dirname(os.path.abspath(__file__)) + '/static/words.txt', 'r').read().split()


def generate_possibilities(phone, index, prev):
    if index <= 5:
        return prev

    digit = phone[index]

    if len(prev) == 0:
        for char in keypad[int(digit)]:
            prev.append(char)
    else:
        new_list = []

        for p in prev:
            for char in keypad[int(digit)]:
                new_list.append(char + p)

        prev = prev + new_list

    return generate_possibilities(phone, index - 1, prev)


def get_matches(possibilities, words):
    matches = []

    for p in possibilities:
        if len(p) != 4:
            continue

        p = p.lower()

        if p in words:
            matches.append(p)

    return matches


def is_valid(phone):
    for c in phone:
        try:
            int(c)
        except ValueError:
            return False

    return True


main()
