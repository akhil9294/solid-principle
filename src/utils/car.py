from utils.vehicle import Vehicle
from utils.fuelable import Fuelable

class Car(Vehicle, Fuelable):

    def insurance_calculator(self):
        if self.year>2024:
            print("Insurance : " ,100)
        else:
            print("Insurance : " , 50)

    def vehicle_fuelable(self):
        print('Fueable with Petrol')