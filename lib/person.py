class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.clipped = False
        self.clipped_by = None
        self.clipped_message = None

    def clip(self, person, message):
        person.clipped = True
        person.clipped_by = self.full_name()
        person.clipped_message = message

    def full_name(self):
        return self.first_name + ' ' + self.last_name
