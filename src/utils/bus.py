from utils.vehicle import Vehicle

class Bus(Vehicle):

    def insurance_calculator(self):
        if self.year >2015:
            print("Insurance : " ,700)
        else:
            print("Insurance : ", 300)