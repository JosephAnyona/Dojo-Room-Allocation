import unittest
from room import week2_class

class TestCreateRoom(unittest.TestCase):
	def test_create_room_successfully(self):
	    my_class_instance = week2_class()

	    initial_room_count = len(my_class_instance.all_rooms)
	    blue_office = my_class_instance.create_room("office", "Blue")	    
	    self.assertTrue(blue_office)
	    red_living = my_class_instance.create_room("living", "red")
	    self.assertTrue(red_living)

	    offices = my_class_instance.offices
	    new_room_count = len(my_class_instance.all_rooms)
	    self.assertEqual(new_room_count - initial_room_count, 2)


	def test_add_person_successfully(self):
	    my_class_instance = week2_class()

	    initial_people_count = len(my_class_instance.people)

	    joey_add = my_class_instance.add_person("joey", "FELLOW", "No")
	    jane_add = my_class_instance.add_person("jane", "STAFF", "Y")
	    viktor_add = my_class_instance.add_person("viktor", "STAFF", "No")
	    emily_add = my_class_instance.add_person("emily", "FELLOW", "Y")

	    self.assertTrue(joey_add)

	    # people = my_class_instance.people

	    new_people_count = len(my_class_instance.people)

	    self.assertEqual(new_people_count - initial_people_count, 4)

if __name__ == "__main__":
	unittest.main()


