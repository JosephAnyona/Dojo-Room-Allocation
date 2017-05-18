from rooms import Room, Office, LivingSpace
from person import Person, Fellow, Staff
import random


class Dojo(object):

    def __init__(self):
        # rooms
        # 2 keys, offices living sapces
        self.all_rooms = {'offices': [], 'livingSpaces': []}
        self.offices = {}

        self.vacant_offices = []
        self.livingSpaces = {}
        self.full_offices = []
        self.vacant_livingSpaces = []
        self.full_living = []
        # people
        self.people = {'FELLOW': [], 'STAFF': []}
        self.fellows = []
        self.staff = []
        # allocated
        self.allocated = {'FELLOW': [], 'STAFF': []}
        self.unallocated = {'FELLOW': [], 'STAFF': []}

    def create_room(self, room_type, room_name):
       # check invalid room_name
        if type(room_name) is not str:
            return("enter string as room_name")

        space_name = (room_name+"_" + room_type)

        # check if the space exists
        if room_type in ("office"):
            if space_name in self.offices:
                return("hey "+space_name+" exists, try another name")
            elif space_name not in self.offices:
                # create new key with office name and add to offices dict
                office = Office(space_name)  # instance of office
                # [] to create a key with empty list of values
                self.offices.update({space_name: []})
                # add office to dictionary using key offices
                self.all_rooms['offices'].append(office.name)
                # add to vacant
                self.vacant_offices.append(office.name)
                print('An '+room_type + ' space called ' + office.name +
                      ' has been successfully created!')
                return (str(self.all_rooms['offices']))

        elif room_type in ("living"):
            if space_name in self.livingSpaces:
                return("hey "+space_name+" exists, try another name")
            elif space_name not in self.livingSpaces:
                # instance of living space
                livingSpace = LivingSpace(space_name)
                # create new key with livingSpace name and add value
                self.livingSpaces.update({space_name: []})
                # add livingSpaces to dictionary using key livingSpaces
                self.all_rooms['livingSpaces'].append(livingSpace.name)
                # add to vacant
                self.vacant_livingSpaces.append(livingSpace)
                print('A '+room_type + ' space called ' + livingSpace.name +
                      ' has been successfully created!')

        elif room_type not in ("living", "office"):
            return("enter either office/living")

        elif room_type in ("office"):
            # create new key with office name and add to offices dict
            office = Office(space_name)  # instance of office
            # [] to create a key with empty list of values
            self.offices.update({space_name: []})
            # add office to dictionary using key offices
            self.all_rooms['offices'].append(office.name)
            # add to vacant
            self.vacant_offices.append(office)
            print('An '+room_type + ' space called ' + office.name +
                  ' has been successfully created!')
            return (str(self.all_rooms['offices']))
        return self.all_rooms['livingSpaces']

    def add_person(self, person_name, person_type, wants_accommodation):
        # staff - no accommodation
        wants_space = "Yes" if wants_accommodation is "Y" else "No"

        if wants_space == "No":
            if person_type == "FELLOW":
                # person_type from Fellow
                new_person_type = Fellow.person_type
                # instance of Fellow class
                new_person_name = Fellow(person_name)
                # add to fellows and add person to values
                self.people[new_person_type].append(new_person_name.name)
                # add to fellows
                self.fellows.append(new_person_name.name)  # add to fellows
                print('Fellow ' + new_person_name.name +
                      ' has been successfully added with no accommodation')
                return(self.people['FELLOW'])

            elif person_type == "STAFF":
                new_person_type = Staff.person_type
                new_person_name = Staff(person_name)
                self.people[new_person_type].append(
                    new_person_name.name)  # add to people
                self.staff.append(new_person_name.name)  # add to staff
                print('Staff ' + new_person_name.name +
                      ' has been successfully added')
                return(str(self.people['STAFF']))

        if wants_space == "Yes":
            if person_type == "FELLOW":
                office_capacity = Office.capacity
                living_space_capacity = LivingSpace.capacity
                # person_type from Fellow
                new_person_type = Fellow.person_type
                # instance of Fellow class
                new_person_name = Fellow(person_name)
                livingSpaces_list = self.vacant_livingSpaces

                livingSpace_allocated = random.choice(livingSpaces_list)
                self.people[person_type].append(new_person_name.name)
                self.fellows.append(new_person_name.name)  # add to fellows
                # check for vacancies
                if len(self.livingSpaces
                       [livingSpace_allocated.name]) < living_space_capacity:
                    self.allocated[person_type].append(new_person_name.name)
                    self.livingSpaces[livingSpace_allocated.name].append(
                        new_person_name.name)

                    print("Fellow " + new_person_name.name +
                          " has been successfully added with accommodation to "
                          + livingSpace_allocated.name)
                # no vacancies
                else:
                    self.unallocated[person_type].append(new_person_name.name)
                    print("No living space available at the moment")
                    print("This"+person_type +
                          " has been added to unallocated list")
                return(str(self.people[new_person_type]))

            elif person_type == "STAFF":
                office_capacity = Office.capacity
                # person_type from staff
                new_person_type = Staff.person_type
                # instance of staff class
                new_person_name = Staff(person_name)
                offices_list = self.vacant_offices
                office_allocated = random.choice(offices_list)
                if len(self.offices[office_allocated]) < office_capacity:
                    self.allocated[person_type].append(new_person_name.name)
                    self.offices[office_allocated].append(
                        new_person_name.name)
                    # check for vacancies
                    print("Staff " + new_person_name.name +
                          " has been successfully added with accommodation to "
                          + office_allocated)
                # no vacancies
                else:
                    self.unallocated[person_type].append(new_person_name)

                    print("No living space available at the moment")
                    print("This"+person_type +
                          " has been added to unallocated list")

                # add to list of that office
                self.offices[office_allocated].append(
                    new_person_name.name)
                self.people[new_person_type].append(
                    new_person_name.name)  # add to people
                self.staff.append(new_person_name.name)  # add to staff
                print('Staff can not be given accommodation')
                print('Staff ' + new_person_name.name +
                      ' has been successfully added to ' + office_allocated)
                return('Staff ' + new_person_name.name +
                       ' has been successfully added to an office')

    def print_room(self, room_name):
        if type(room_name) is not str:
            return("enter string as room_name")

        # if room_name is offices
        for keys in self.offices:
            if room_name in keys:
                office = Office(room_name)
                return(self.office.name)
        # if room_name is living
        for keys in self.livingSpaces:
            if room_name in keys:
                livingSpace = LivingSpace(room_name)
                print(self.livingSpaces)
                return(livingSpace.name)

    def print_room_text_file(self, room_name):
        if type(room_name) is not str:
            return("enter string as room_name")

        # if room_name is offices
        for keys in self.offices:
            if room_name in keys:
                office = Office(room_name)
                return(self.office.name)
        # if room_name is living
        for keys in self.livingSpaces:
            if room_name in keys:
                livingSpace = LivingSpace(room_name)
                return(livingSpace.name)

    def vacant_space(self, room_name):
        office_capacity = Office.capacity
        living_space_capacity = LivingSpace.capacity
        # for offices
        for keys in self.offices:
            if len(self.offices[room_name]) < office_capacity:
                self.vacant_offices.append(room_name)
                print('office vacant')
                return('office vacant')
            else:
                self.full_offices.append(room_name)
                print('office full')
                return('office full')
        for keys in self.livingSpaces:
            if len(self.livingSpaces[room_name]) < living_space_capacity:
                self.full_living.append(room_name)
                print('living space is vacant')
                return('living space is vacant')
            else:
                self.vacant_livingSpaces.append(room_name)
                print('living space is vacant')
                return('living space is full')

    def room_allocation(self):
        pass
