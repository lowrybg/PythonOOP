from unittest import TestCase, main

from project.mammal import Mammal

class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Joe", 'bird', 'kwak')

    def test_init_creates_all_attributes(self):
        self.assertEqual('Joe', self.mammal.name)
        self.assertEqual('bird', self.mammal.type)
        self.assertEqual('kwak', self.mammal.sound)

    def test_private_mammal_type(self):
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_if_return_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual('animals', result)

    def test_make_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual("Joe makes kwak", result)

    def test_if_get_info(self):
        result = self.mammal.info()
        self.assertEqual("Joe is of type bird", result)



if __name__ == '__main__':
    main()