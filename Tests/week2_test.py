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
        blue_office = self.class_instance.create_room("office", "Blue")
        for key in self.class_instance.offices:  # one liner
            if key == "Blue_office":
                self.assertIn("Blue_office", key)
        offices = self.class_instance.offices
        new_room_count = len(self.class_instance.all_rooms['offices'])
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_room_exists(self):
        green_living1 = self.class_instance.create_room(
            "living", "green")  # no hardcode
        green_living2 = self.class_instance.create_room(
            "living", "green")

        self.assertEqual(
            'hey green_living exists, try another name', green_living2)

        chrome_office1 = self.class_instance.create_room("office", "chrome")
        chrome_office2 = self.class_instance.create_room("office", "chrome")
        self.assertEqual(
            'hey chrome_office exists, try another name', chrome_office2)

    def test_room_invalid__room_type(self):
        invalid_room_type = self.class_instance.create_room("invalid", "green")
        self.assertEqual(
            "enter either office/living", invalid_room_type)
        invalid_room_type = self.class_instance.create_room("office", 11)
        self.assertEqual(
            "enter string as room_name", invalid_room_type)

    def test_add_person_successfully(self):
        add_room = self.class_instance.create_room("living", "mara")
        add_room
        add_room2 = self.class_instance.create_room("office", "chrome")
        add_room2
        # multiple adds checking fellow/staff and wants accomodation
        initial_people_count = len(self.class_instance.people['FELLOW'])
        self.class_instance.add_person("joey", "FELLOW", "No")
        self.class_instance.add_person("emily", "FELLOW", "Y")

        self.assertEqual("joey" in self.class_instance.fellows, True)
        self.assertEqual("emily" in self.class_instance.fellows, True)

        new_people_count = len(self.class_instance.people['FELLOW'])
        self.assertEqual(new_people_count - initial_people_count, 2)
        # multiple adds checking fellow/staff and wants accomodation
        initial_people_count = len(self.class_instance.people['STAFF'])

        jane_add = self.class_instance.add_person("jane", "STAFF", "Y")
        viktor_add = self.class_instance.add_person("viktor", "STAFF", "No")
        self.assertIn('jane', jane_add)
        self.assertIn('viktor', viktor_add)
        new_people_count = len(self.class_instance.people['STAFF'])
        self.assertEqual(new_people_count - initial_people_count, 2)

    def test_room_allocation(self):
        add_room = self.class_instance.create_room("living", "mara")
        derek_add_allocate = self.class_instance.add_person(
            "derek", "FELLOW", "Y")
        add_room
        derek_add_allocate

        self.assertEqual(self.class_instance.livingSpaces[
                         "mara_living"], ["derek"])

    def test_print_room(self):
        add_room = self.class_instance.create_room(
            "living", "mara")  # should be added
        add_person = self.class_instance.add_person(
            "emily", "FELLOW", "Y")  # should be added
        add_room
        add_person
        self.assertIn("emily", self.class_instance.livingSpaces["mara_living"])
        print_room = self.class_instance.print_room

    def test_vacant_space(self):
        add_room = self.class_instance.create_room("living", "mara")
        add_room
        self.assertEqual("living space is vacant",
                         self.class_instance.vacant_space("mara_living"))


if __name__ == "__main__":
    unittest.main()
