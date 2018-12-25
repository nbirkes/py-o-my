import datetime


def main():
    greeting = seasons_greetings()
    print(greeting)


def seasons_greetings():
    now = datetime.datetime.now()

    if now.day == 25 and now.month == 12:
        return 'Merry Christmas!'
    else:
        return 'Bah Humbug!'


main()
