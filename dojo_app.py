"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.

Usage:
    dojo create_room <room_type> <room_name>...
    dojo add_person <first_name> <last_name> <person_type> <wants_space>
    dojo print_room <room_name>
    dojo print_allocated
    dojo print_unallocated
    dojo (-i | --interactive)
    dojo (-h | --help)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""


import sys
import cmd
from docopt import docopt, DocoptExit

sys.path.append('../3')
from dojo import Dojo


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyInteractive (cmd.Cmd):

    def introduction():

        print ("dojo space allocation!".center(70))
        print ("1. create_room <room_type> <room_name>...".center(70))

        print ("2. add_person <first_name> <last_name> <person_type> <wants_space>".center(70))

        print ("3. print_allocated".center(70))

        print ("4. print_unallocated".center(70))

        print ("other commands:".center(70))

        print ("1. help".center(70))

        print ("2. Exit".center(70)) 


    intro=introduction()
    prompt = '(dojo)'
    file = None

    dojo = Dojo()

    @docopt_cmd
    def do_create_room(self, args):
        """Usage: create_room <room_type> <room_name>..."""
        room_name = args["<room_name>"]
        room_type = args["<room_type>"]
        if room_type == "living":
            self.dojo.create_room(room_type, room_name)
        if room_type == "office":
            self.dojo.create_room(room_type, room_name)

    @docopt_cmd
    def do_add_person(self, args):
        """Usage: add_person <first_name> <last_name> <person_type> <wants_space>"""
        first_name = args["<first_name>"]
        last_name = args["<last_name>"]

        person_type = args["<person_type>"]
        wants_space = args["<wants_space>"]
        person_name = (first_name + " " + last_name)
        if person_type == "fellow":
            self.dojo.add_person(person_name, "fellow", wants_space)
        if person_type == "staff":
            self.dojo.add_person(person_name, "staff", wants_space)

    @docopt_cmd
    def do_print_room(self, args):
        """Usage: print_room <room_name>"""
        room_name = args["<room_name>"]
        self.dojo.print_room(room_name)

    @docopt_cmd
    def do_print_allocated(self, args):
        """Usage: print_allocated"""
        self.dojo.print_allocated()
        
    @docopt_cmd
    def do_print_unallocated(self, args):
        """Usage: print_allocated"""
        self.dojo.print_unallocated()


        
    @docopt_cmd
    def do_exit(self, args):
        """Exit"""

        exit() 

opt = docopt(__doc__, sys.argv[1:])

if opt["--interactive"]:
    MyInteractive().cmdloop()

print(opt)
