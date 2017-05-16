"""Usage:
  room.py create_room (office|living) <room_name>...
  room.py add_person <person_name> <FELLOW|STAFF> [wants_accommodation]
  room.py print_room <room_name>

"""
import random


class Room(object):

    def __init__(self):
        # rooms
        # 2 keys, offices living sapces
        self.all_rooms = {'offices': ['chrome_office'], 'livingSpaces': [
            'green_living', 'Naivasha_living', ], }
        self.offices = {'chrome_office': []}
        self.livingSpaces = {'green_living': [], 'Naivasha_living': []}
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
       # check invalid room_name
        if type(room_name) is not str:
            return("enter string as room_name")
        space_name = (room_name+"_"+room_type)

       # check if the space exists
        if room_type == 'office':
            for values in self.all_rooms['offices']:
                if space_name in values:
                    return("hey "+space_name+" exists, try another name")

        elif room_type == 'living':
            for values in self.all_rooms['livingSpaces']:
                if space_name == values:
                    return("hey "+space_name+" exists, try another name")
        # for invalid room_type
        else:
            return("enter either office/living")

        if room_type == 'office':
            # create new key with office name and append to offices
            # [] to create a key with empty list of values
            self.offices[space_name] = []
            # append new room to dictionary using key offices
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
            print('A '+room_type + ' space called ' + space_name +
                  ' has been successfully created!')

            return self.all_rooms['livingSpaces']

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
                return(self.people)

            elif person_type == "STAFF":
                self.people.append(person_name)  # add to people
                self.staff.append(person_name)  # add to staff
                print(self.people)
                print('Staff ' + person_name +
                      ' has been successfully added')
                return(self.people)

        if wants_space == "Yes":
            if person_type == "FELLOW":
                livingSpaces_list = self.all_rooms['livingSpaces']
                livingSpace_allocated = random.choice(livingSpaces_list)
                # add to list of that room
                self.livingSpaces[livingSpace_allocated].append(person_name)

                # print(livingSpace_allocated)
                self.people.append(person_name)  # add to people
                self.fellows.append(person_name)  # add to fellows
                print(self.livingSpaces[livingSpace_allocated])  # check
                print("Fellow " + person_name +
                      " has been successfully added with accommodation to "
                      + livingSpace_allocated)

                return("Fellow " + person_name + " has been successfully "
                       + "added with accommodation to a living space")

            elif person_type == "STAFF":
                offices_list = self.all_rooms['offices']
                office_allocated = random.choice(offices_list)
                # add to list of that office
                self.offices[office_allocated].append(person_name)
                self.offices
                print(office_allocated)
                print(self.offices[office_allocated])
                self.people.append(person_name)  # add to people
                self.staff.append(person_name)  # add to staff
                print(self.people)
                print('Staff can not be given accommodation')
                print('Staff ' + person_name +
                      ' has been successfully added to ' + office_allocated)
                return('Staff ' + person_name +
                       ' has been successfully added to an office')
