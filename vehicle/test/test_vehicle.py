from unittest import TestCase, main

from project.vehicle import Vehicle

class TestVehicle(TestCase):
    def setUp(self):
        self.test_vehicle = Vehicle(30.5, 200)

    def test_init_creates_all_attributes(self):
        self.assertEqual(30.5, self.test_vehicle.fuel)
        self.assertEqual(200, self.test_vehicle.horse_power)
        self.assertEqual(30.5, self.test_vehicle.capacity)
        self.assertEqual(self.test_vehicle.DEFAULT_FUEL_CONSUMPTION,self.test_vehicle.fuel_consumption)



if __name__ == '__main__':
    main()