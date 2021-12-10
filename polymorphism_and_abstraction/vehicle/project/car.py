from project.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)


    def drive(self, distance):
        required_fuel = (self.fuel_consumption +0.9) * distance
        if self.fuel_quantity >= required_fuel:
            self.fuel_quantity -= required_fuel



    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


