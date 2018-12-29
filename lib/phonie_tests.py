import phonie


def main():
    test0()
    test1()
    test2()
    test3()


def test0():
    actual = phonie.build_possibilities('0', [])
    print(actual)


def test1():
    actual = phonie.build_possibilities('1', [])
    print(actual)


def test2():
    actual = phonie.build_possibilities('2', [])
    print(actual)


def test3():
    actual = phonie.build_possibilities('2', [])
    actual = phonie.build_possibilities('3', actual)

    print(actual)


main()
