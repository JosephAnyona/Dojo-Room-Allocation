class Room(object):
    # Creates Room object where the class Office and Livingspace inherit from
    def __init__(self, name):
        self.name = name

class Office(Room):
    capacity = 6

    def __init__(self, name):
        Room.__init__(self, name)

class LivingSpace(Room):
    capacity = 4    

    def __init__(self, name):
        Room.__init__(self, name)
