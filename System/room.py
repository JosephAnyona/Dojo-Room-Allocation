"""Usage:
  room.py create_room (office|living) <room_name>...
  room.py add_person <person_name> <FELLOW|STAFF> [wants_accommodation]
  room.py print_room <room_name>

"""


class Room(object):

    def __init__(self):
        # rooms
        # 2 keys, offices living sapces
        self.all_rooms = {'offices': [], 'livingSpaces': ['green_living']}
        self.offices = {'green_living': []}
        self.livingSpaces = {}
        self.vacant_office = []
        self.vacant_living = []
        # people
        self.people = []
        self.fellows = []
        self.staff = []
        # allocated
        self.allocated = []
        self.unallocated = {'Fellows': [], 'Staff': []}

    def create_room(self, room_type, room_name):
        # print(names)
        space_name = (room_name+"_"+room_type)
       # check if the space exists
        for key in self.offices:
            if space_name == key:
                return("hey "+space_name+" exists, try another name")
            else:
                pass

        if room_type == 'office':
            # create new key with office name and append to offices
            self.offices[space_name] = None
            # append to dictionary using key offices
            self.all_rooms['offices'].append(space_name)
            print(self.all_rooms)
            print(self.offices)
            print('An '+room_type + ' space called ' + space_name +
                  ' has been successfully created!')
            # print(room_name, room_type)
            return self.all_rooms['offices']

        elif room_type == 'living':
            # create new key with office name and append to offices
            self.offices[space_name] = None
            # append to all_rooms dictionary using key offices
            self.all_rooms['livingSpaces'].append(space_name)
            print(self.all_rooms)
            print(self.offices)
            print('A '+room_type + ' space called ' + space_name +
                  ' has been successfully created!')

        return self.all_rooms['livingSpaces']

    def room_allocation(self, person_name, wants_accommodation):
        # getting from add person
        person_name = self.add_person.person_name
        wants_space = "Yes" if self.add_person.wants_accommodation is "Y" else "No"

    def add_person(self, person_name, person_type, wants_accommodation):
        # staff - no accommodation
        wants_space = "Yes" if wants_accommodation is "Y" else "No"

        if wants_space == "No":
            if person_type == "FELLOW":
                self.people.append(person_name)  # add to people
                self.fellows.append(person_name)  # add to fellows
                print(self.people)
                print('Fellow ' + person_name +
                      ' has been successfully added with no accommodation')

            elif person_type == "STAFF":
                self.people.append(person_name)  # add to people
                self.staff.append(person_name)  # add to staff
                print(self.people)
                print('Staff ' + person_name +
                      ' has been successfully added')

        if wants_space == "Yes":
            if person_type == "FELLOW":
                self.people.append(person_name)  # add to people
                self.fellows.append(person_name)  # add to fellows
                print(self.people)
                print('Fellow ' + person_name +
                      ' has been successfully added with accommodation')

            elif person_type == "STAFF":
                self.people.append(person_name)  # add to people
                self.staff.append(person_name)  # add to staff
                print(self.people)
                print('Staff can not be given accommodation')
                print('Staff ' + person_name + ' has been successfully added')

        return self.people
