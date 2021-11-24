from unittest import TestCase, main

from project.vehicle import Vehicle

class TestVehicle(TestCase):
    def setUp(self):
        self.test_vehicle = Vehicle(30.5, 200)

    def test_init_creates_all_attributes(self):
        self.assertEqual(30.5, self.test_vehicle.fuel)
        self.assertEqual(200, self.test_vehicle.horse_power)
        self.assertEqual(self.test_vehicle.fuel, self.test_vehicle.capacity)
        self.assertEqual(self.test_vehicle.fuel_consumption, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_if_fuel_decrease_when_drive(self):
        self.test_vehicle.drive(10)
        self.assertEqual(18, self.test_vehicle.fuel)

    def test_check_capacity_unchanged_if_fuel_changed(self):
        self.assertEqual(30.5, self.test_vehicle.capacity)
        self.test_vehicle.fuel = 20
        self.assertEqual(30.5, self.test_vehicle.capacity)

    def test_when_not_enough_fuel(self):
        with self.assertRaises(Exception) as  ex:
            self.test_vehicle.drive(100)
        self.assertEqual(30.5, self.test_vehicle.fuel)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_when_refuel_too_much(self):
        with self.assertRaises(Exception) as  ex:
            self.test_vehicle.refuel(100)
        self.assertEqual(30.5, self.test_vehicle.fuel)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_when_refuel_normal(self):
        self.test_vehicle.drive(10)
        self.assertEqual(18, self.test_vehicle.fuel)
        self.test_vehicle.refuel(10)
        self.assertEqual(28, self.test_vehicle.fuel)

    def test_return_string(self):
        self.assertEqual("The vehicle has 200 " \
               "horse power with 30.5 fuel left and 1.25 fuel consumption", self.test_vehicle.__str__())



if __name__ == '__main__':
    main()