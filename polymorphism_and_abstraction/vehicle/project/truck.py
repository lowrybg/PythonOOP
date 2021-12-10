from project.vehicle import Vehicle


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)



    def drive(self, distance):
        required_fuel = (self.fuel_consumption + 1.6) * distance
        if self.fuel_quantity >= required_fuel:
            self.fuel_quantity -= required_fuel



    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95