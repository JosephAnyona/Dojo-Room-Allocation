from rooms import Room, Office, LivingSpace
from person import Person, Fellow, Staff
import random


class Dojo(object):

    def __init__(self):
        # rooms
        # 2 keys, offices living sapces
        self.all_rooms = {'offices': [], 'livingSpaces': []}
        self.offices = {}
        self.livingSpaces = {}
        
        self.vacant_offices = []
        self.full_offices = []
        self.vacant_livingSpaces = []
        self.full_living = []
        # people
        self.people = {'fellow': [], 'staff': []}
        self.fellows = []
        self.staff = []
        # allocated
        self.allocated = {'fellow': [], 'staff': []}
        self.unallocated = {'fellow': [], 'staff': []}

    def create_room(self, room_type, room_name):

        for room in room_name:
            
            space_name = (room+"_" + room_type)
        
            if room_type != ["living", "office"]:
                print("enter either office/living")

            # check if the space exists
            if room_type == ("office"):
                if space_name in self.offices:
                    print("hey "+space_name+" exists") 
                print(" try another name")
                    
                if space_name not in self.offices:

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
                    
            elif room_type == ("living"):
                if space_name in self.livingSpaces:
                    print("hey "+space_name+" exists") 
                    print("try another name")
                    
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


    
    def add_person(self, person_name, person_type, wants_accommodation):
        # staff - no accommodation
        wants_space = "Yes" if wants_accommodation is "y" else "No"

        if wants_space == "No":
            if person_type == "fellow":
                # instance of Fellow class
                new_person_name = Fellow(person_name)
                # person_type from Fellow
                new_person_type = Fellow.person_type
                # add to fellows and add person to values
                self.people['fellow'].append(new_person_name.name)
                # add to fellows
                self.fellows.append(new_person_name.name)  # add to fellows
                print('Fellow ' + new_person_name.name +
                      ' has been successfully added with no accommodation')

            if person_type == "staff":
                #new_person_type from class Staff 
                new_person_type = Staff.person_type
                #new_person_name from Staff
                new_person_name = Staff(person_name)
                # add name to people dict using new_person_type as key
                self.people[new_person_type].append(
                    new_person_name.name)  
                # add to staff 
                self.staff.append(new_person_name.name)  
                print('Staff ' + new_person_name.name +
                      ' has been successfully added')

        elif wants_space == "Yes":
            if person_type == "fellow":
                #living capacity from LivingSpace 
                living_space_capacity = LivingSpace.capacity
                # person_type from Fellow
                new_person_type = Fellow.person_type
                # instance of Fellow class
                new_person_name = Fellow(person_name)
                livingSpaces_list = self.vacant_livingSpaces
                #check if list of living spaces has any rooms 
                if len(livingSpaces_list) < 1:
                   #add to unallocated 
                   self.unallocated['fellow'].append(new_person_name.name)
                   print("no living spaces") 
                   print("added to unallocated")
                else: 
                    #pick random from vacant living spaces
                    livingSpace_allocated = random.choice(livingSpaces_list)
                    #add to dict people using person_type as key 
                    #and value as new_person name 
                    self.people[person_type].append(new_person_name.name)
                    #add to fellows
                    self.fellows.append(new_person_name.name)  
                    # check for vacancies in that allocated room
                    if len(self.livingSpaces
                           [livingSpace_allocated.name]) < living_space_capacity:
                        #add to allocated list for fellow/staff
                        self.allocated[person_type].append(new_person_name.name)
                        # add person's name to that living space
                        self.livingSpaces[livingSpace_allocated.name].append(
                            new_person_name.name)
                        print("Fellow " + new_person_name.name +
                              " has been successfully added with accommodation to "
                              + livingSpace_allocated.name)
                    # no vacancies
                    else:
                        #add to unallocated fellow/staff
                        self.unallocated[person_type].append(new_person_name.name)
                        print("No living space available at the moment")
                        print("This"+person_type +
                              " has been added to unallocated list")

            elif person_type == "staff":
                #office capacity from Office class
                office_capacity = Office.capacity
                # person_type from staff
                new_person_type = Staff.person_type
                # instance of staff class
                new_person_name = Staff(person_name)
                #list of vacant offices
                offices_list = self.vacant_offices
                if len(offices_list) < 1:
                   #add to unallocated 
                   self.unallocated['staff'].append(new_person_name)
                   print("no offices")
                else: 
                    #pick random from vacant living spaces
                    office_allocated = random.choice(offices_list)
                    #add to dict people using person_type as key 
                    #and value as new_person name 
                    self.people[person_type].append(new_person_name.name)
                    #add to fellows
                    self.staff.append(new_person_name.name)  
                    # check for vacancies in that allocated room
                    if len(self.offices
                        [office_allocated]) < office_capacity:
                        #add to allocated list for fellow/staff
                        self.allocated[person_type].append(new_person_name.name)
                        # add person's name to that living space
                        self.offices[office_allocated].append(new_person_name.name)
                        print("Staff " + new_person_name.name +
                              " has been successfully added to "
                              + office_allocated)
                        # no vacancies
                    else:
                        #add to unallocated fellow/staff
                        self.unallocated[person_type].append(new_person_name)
                        print("No office space available at the moment")
                        print("This"+person_type +
                              " has been added to unallocated list") 

    
    def print_room(self, room_name):
        if type(room_name) is not str:
            return("enter string as room_name")
        # if room_name is offices
        if room_name not in self.offices:
            print(room_name+" doesn't exist in Offices")
            
        elif room_name in self.offices:
            office = Office(room_name)
            members = self.offices[room_name]
            print("members in this Living Spaces"+str(members)) 
            print(self.office.name)


        # if room_name is living
        if room_name not in self.livingSpaces:
            print(room_name+" doesn't exist in Living Spaces")
        elif room_name in self.livingSpaces:
            livingSpace = LivingSpace(room_name)
            members = self.livingSpaces[room_name] 
            print("members in this Living Spaces"+str(members))
            print(livingSpace.name) 
 

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
           
    def print_allocated(self):
        print(self.offices) 
        for key in self.offices:
          print(key)
          print(self.offices[key])
        for key in self.livingSpaces:
          print(key)
          print(self.livingSpaces[key])
     
    def print_unallocated(self):
           print(self.unallocated)
           print("unallocated fellows") 
           print(self.unallocated['fellow'])
           print("unallocated staff")  
           print(self.unallocated['staff'])




        #outputs for the file text
 
 