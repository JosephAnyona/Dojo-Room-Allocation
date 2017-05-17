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
        green_living = self.class_instance.create_room("living", "green")
        self.assertEqual(
            'hey green_living exists, try another name', green_living)
        chrome_office = self.class_instance.create_room("office", "chrome")
        self.assertEqual(
            'hey chrome_office exists, try another name', chrome_office)

    def test_room_invalid__room_type(self):
        invalid_room_type = self.class_instance.create_room("invalid", "green")
        self.assertEqual(
            "enter either office/living", invalid_room_type)
        invalid_room_type = self.class_instance.create_room("office", 11)
        self.assertEqual(
            "enter string as room_name", invalid_room_type)

    def test_add_person_successfully(self):
        initial_people_count = len(self.class_instance.people['FELLOW'])
        # multiple adds checking fellow/staff and wants accomodation
        joey_add = self.class_instance.add_person("joey", "FELLOW", "No")

        emily_add = self.class_instance.add_person("emily", "FELLOW", "Y") 
        self.assertTrue(joey_add)

        self.assertTrue(emily_add)


        new_people_count = len(self.class_instance.people['FELLOW']) 



        self.assertEqual(new_people_count - initial_people_count, 2)

        
        initial_people_count = len(self.class_instance.people['STAFF'])

        # multiple adds checking fellow/staff and wants accomodation 
        jane_add = self.class_instance.add_person("jane", "STAFF", "Y")
        viktor_add = self.class_instance.add_person("viktor", "STAFF", "No") 
        self.assertTrue(jane_add)
        self.assertTrue(viktor_add)

        new_people_count = len(self.class_instance.people['STAFF']) 

        self.assertEqual(new_people_count - initial_people_count, 2)

    def test_room_allocation(self):
        derek_add_allocate = self.class_instance.add_person(
            "derek", "FELLOW", "Y")
        self.assertEqual(
            "Fellow derek has been successfully added with accommodation " +
            "to a living space", derek_add_allocate)

    def test_print_room(self):
        chrome_office_print = self.class_instance.print_room("chrome_office")
        self.assertIn("sean", chrome_office_print)
        green_living_print = self.class_instance.print_room("green_living")
        self.assertIn("john", green_living_print)

    def test_vacant_space(self):
        full_office = self.class_instance.vacant_space("full_office")
        self.assertEqual("office full", full_office)
        # vacant_office = self.class_instance.vacant_space("chrome_office")
        # self.assertEqual("office vacant", vacant_office)


if __name__ == "__main__":
    unittest.main()
