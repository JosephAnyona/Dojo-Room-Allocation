class Person(object):
   # Creates Person object where the class Office and Livingspace inherit from

    def __init__(self, name):
        self.name = name


class Fellow(Person):
    person_type = "FELLOW"

    def __init__(self, name):
        Person.__init__(self, name)
        
class Staff(Person):

    person_type = "STAFF"



    def __init__(self, name):

        Person.__init__(self, name)


