import unittest
import sys
from os import path
sys.path.append('../System')
from dojo import Dojo


class TestCreateRoom(unittest.TestCase):

    def setUp(self):
        self.class_instance = Dojo()

    def test_create_room_successfully(self):
        initial_room_count = len(self.class_instance.all_rooms['offices'])
        blue_office = self.class_instance.create_room("office", ["Blue"])
        for key in self.class_instance.offices:  # one liner
            if key == "Blue_office":
                self.assertIn("Blue_office", key)
        offices = self.class_instance.offices
        new_room_count = len(self.class_instance.all_rooms['offices'])
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_room_exists(self):
        green_living1 = self.class_instance.create_room(
            "living", ["green"])  # no hardcode
        green_living2 = self.class_instance.create_room(
            "living", ["green"])
        self.assertEqual(len(self.class_instance.livingSpaces), 1) 

        chrome_office1 = self.class_instance.create_room("office", ["chrome"])
        chrome_office2 = self.class_instance.create_room("office", ["chrome"])
        self.assertEqual(len(self.class_instance.offices), 1)

    def test_room_invalid__room_type(self):
        invalid_room_type = self.class_instance.create_room("invalid", ["green"])
        self.assertEqual(len(self.class_instance.offices), 0)

    def test_add_person_successfully(self):
        add_room = self.class_instance.create_room("living", ["mara"])
        add_room
        add_room2 = self.class_instance.create_room("office", ["chrome"])
        add_room2
        # multiple adds checking fellow/staff and wants accomodation
        initial_people_count = len(self.class_instance.people['fellow'])
        self.class_instance.add_person("joey", "fellow", "No")
        self.class_instance.add_person("emily", "fellow", "Y")
        new_people_count = len(self.class_instance.people['fellow'])
        #check if there has been any additions 
        self.assertEqual(new_people_count - initial_people_count, 2)
        # multiple adds checking fellow/staff and wants accomodation
        initial_people_count = len(self.class_instance.people['staff'])
        jane_add = self.class_instance.add_person("jane", "staff", "Y")
        viktor_add = self.class_instance.add_person("viktor", "staff", "No")
        new_people_count = len(self.class_instance.people['staff'])
        #check if there has been any additions  
        self.assertEqual(new_people_count - initial_people_count, 2)

    def test_room_allocation(self):
        add_room = self.class_instance.create_room("living", ["mara"])
        derek_add_allocate = self.class_instance.add_person(
            "derek", "fellow", "y")
        add_room
        derek_add_allocate

        self.assertEqual(self.class_instance.livingSpaces[
                         "mara_living"], ["derek"])

    def test_print_room(self):
        add_room = self.class_instance.create_room(
            "living", ["mara"])  # should be added
        add_person = self.class_instance.add_person(
            "emily", "fellow", "y")  # should be added
        add_room
        add_person
        print(self.class_instance.livingSpaces)
        print(self.class_instance.fellows) 
        self.assertIn("emily", self.class_instance.livingSpaces["mara_living"])
        print_room = self.class_instance.print_room

    def test_vacant_space(self):
        add_room = self.class_instance.create_room("living", ["mara"])
        add_room
        self.assertEqual("living space is vacant",
                         self.class_instance.vacant_space("mara_living"))


if __name__ == "__main__":
    unittest.main()
