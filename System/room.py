"""Usage:
  room.py create_room (office|living) <room_name>...
  room.py add_person <person_name> <FELLOW|STAFF> [wants_accommodation]

"""

class week2_class(object):
  def __init__ (self):
    #rooms
    self.all_rooms = []
    self.offices=[]
    self.livingSpaces = []

    #people
    self.people = []
    self.fellows = []
    self.staff = []

    
  def create_room(self, room_type, room_name):
    # print(names)
    if room_type == 'office':
      names = [room_name]
      for name in names:
        office_name = (name+"_office")
        self.offices.append(office_name)

        self.all_rooms.append(office_name)
        # print(room_name, room_type)
        print(self.offices)
        return('An office called ' + name + ' has been successfully created!')

    elif room_type == 'living':
      names = [room_name]
      for name in names:
        office_name = (name+"_living")
        self.livingSpaces.append(office_name)

        self.all_rooms.append(office_name)

        print(self.all_rooms)
        print('A living space called ' + name + ' has been successfully created!')

    return self.all_rooms



  def add_person(self, person_name, person_type, wants_accommodation):
    #staff - no accommodation
    wants_space = "Yes" if wants_accommodation is "Y" else "No"

    if wants_space == "No":
      if person_type == "FELLOW":
        self.people.append(person_name) #add to people
        self.fellows.append(person_name)#add to fellows
        print(self.people)
        print('Fellow ' + person_name + ' has been successfully added with no accommodation')

      elif person_type == "STAFF":
        self.people.append(person_name) #add to people
        self.staff.append(person_name) #add to staff
        print(self.people)
        print('Staff ' + person_name + ' has been successfully added')

    if wants_space == "Yes":
        if person_type == "FELLOW":
            self.people.append(person_name) #add to people
            self.fellows.append(person_name)#add to fellows
            print(self.people)
            print('Fellow ' + person_name + ' has been successfully added with accommodation')

        elif person_type == "STAFF":
          self.people.append(person_name) #add to people
          self.staff.append(person_name) #add to staff
          print(self.people)
          print('Staff can not be given accommodation')
          print('Staff ' + person_name + ' has been successfully added')

    return self.people