"""Usage:
  week2.py create_room (office|living) <room_name>...
  week2.py add_person <person_name> <FELLOW|STAFF> [wants_accommodation]
"""

from docopt import docopt



# week2_class.create_room("office","yellow")






  # def add_person(self, args):
  #   person_name = args['<person_name>']

  #   wants_space = "Yes" if args.get("<wants_space>") is "Y" else "No"

  #   if wants_space == "No":
  #     if args['<FELLOW>']:
  #       self.persons['fellows'].append(person_name)
  #       print('Fellow ' + person_name + 'has been successfully added')

  #     elif args['<STAFF>']:
  #       for person in persons:
  #         self.persons['staff'].append(person_name)
  #         print('Staff ' + person_name + 'has been successfully added')

      




# if __name__ == '__main__':
#   arguments = docopt(__doc__)
#   # print(arguments)
#   if arguments['create_room']:
#     week2_class().create_room(arguments)