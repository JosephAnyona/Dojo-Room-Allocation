import unittest
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from System.room import Room


class TestCreateRoom(unittest.TestCase):

    def setUp(self):
        self.class_instance = Room()

    def test_create_room_successfully(self):
        initial_room_count = len(self.class_instance.all_rooms['offices'])
        blue_office = self.class_instance.create_room("office", "Blue")
        for key in self.class_instance.offices:
            if key == "Blue_office":
                self.assertIn("Blue_office", key)
        offices = self.class_instance.offices
        new_room_count = len(self.class_instance.all_rooms['offices'])
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_room_exists(self):
        # self.assertEqual('hey green_living  exists, try another name',)
        green_living = self.class_instance.create_room("living", "green")
        self.assertEqual(
            'hey green_living exists, try another name', green_living)

    def test_add_person_successfully(self):
        initial_people_count = len(self.class_instance.people)
        # multiple adds checking fellow/staff and wants accomodation
        joey_add = self.class_instance.add_person("joey", "FELLOW", "No")
        jane_add = self.class_instance.add_person("jane", "STAFF", "Y")
        viktor_add = self.class_instance.add_person("viktor", "STAFF", "No")
        emily_add = self.class_instance.add_person("emily", "FELLOW", "Y")
        self.assertTrue(joey_add)
        self.assertTrue(jane_add)
        self.assertTrue(viktor_add)
        self.assertTrue(emily_add)
        # people = class_instance.people
        new_people_count = len(self.class_instance.people)
        self.assertEqual(new_people_count - initial_people_count, 4)

    def test_room_allocation(self):
        derek_add_allocate = self.class_instance.add_person(
            "derek", "FELLOW", "Y")

if __name__ == "__main__":
    unittest.main()
