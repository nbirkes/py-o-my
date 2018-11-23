class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

cosette = Dog('Cosette')
cosette.add_trick('bark')
cosette.add_trick('play dead')
print(cosette.tricks)

