from utils.vehicle import Vehicle
from utils.rechargable import Rechargable


class ElectricCar(Vehicle, Rechargable):

    def insurance_calculator(self):
        print('Insurance : ', 250)

    def vehicle_rechargable(self):
        print('Rechargable with Electricity.')