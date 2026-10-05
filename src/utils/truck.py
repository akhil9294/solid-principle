from utils.vehicle import Vehicle
from utils.fuelable import Fuelable
class Truck(Vehicle, Fuelable):

    def insurance_calculator(self):
        if self.year>2024:
            print("Insurance : " ,1000)
        else:
            print("Insurance : " , 500)

    def vehicle_fuelable(self):
        print('Fueable with Deisel')