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

digit_map = {
    0: 0,
    1: 1,
    'A': 2,
    'B': 2,
    'C': 2,
    'D': 3,
    'E': 3,
    'F': 3,
    'G': 4,
    'H': 4,
    'I': 4,
    'J': 5,
    'K': 5,
    'L': 5,
    'M': 6,
    'N': 6,
    'O': 6,
    'P': 7,
    'Q': 7,
    'R': 7,
    'S': 7,
    'T': 8,
    'U': 8,
    'V': 8,
    'W': 9,
    'X': 9,
    'Y': 9,
    'Z': 9,
}


def main():
    # phone = input('What is your phone number?')
    phone = '2546447382'

    if not is_valid_phone(phone):
        print('Phone number %s is invalid' % phone)
        return

    poss = do_it(phone, 5)

    # words = get_words()
    # matches = get_matches(poss, words)
    #
    # print('%s possibilities found' % len(poss))
    #
    # if len(matches) == 0:
    #     print('Sorry, no matches found for', phone)
    # else:
    #     print('MATCHES!')
    #     for match in matches:
    #         print(format_vanity(phone, match))


def get_words():
    return open(os.path.dirname(os.path.abspath(__file__)) + '/static/words_2.txt', 'r').read().split()


def do_it(phone, num_digits):
    sample = ''.join(reversed(phone))[0:num_digits]
    poss = []
    prev = []
    cur = []

    for i in range(0, num_digits):
        cur = build_possibilities(sample[i], prev)
        poss.append(cur)
        prev = cur
        cur = []

        # for p in poss:
        #     if not is_valid_vanity(p, phone):
        #         print('INVALID', p)
        #     else:
        #         print(p)

    return poss


def build_possibilities(digit, prev):
    temp = []

    if len(prev) == 0:
        for char in keypad[int(digit)]:
            prev.append(char)
    else:
        for char in keypad[int(digit)]:
            for poss in prev:
                new_poss = char + poss
                temp.append(new_poss)
                # print(digit, new_poss)
                # if new_poss == 'GRUB':
                #     print(prev)
                #     raise Exception('stop')

    print('BEGIN', digit)
    print('PREV', prev)
    print('TEMP', temp)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    prev = prev + temp

    return prev


def is_valid_vanity(vanity, phone):
    return phone.endswith(vanity_to_phone(vanity))


def vanity_to_phone(vanity):
    phone = []
    for char in vanity:
        phone.append(str(digit_map[char]))

    return ''.join(phone)


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


def is_valid_phone(phone):
    for c in phone:
        try:
            int(c)
        except ValueError:
            return False

    return len(phone) == 10


if __name__ == '__main__':
    main()
