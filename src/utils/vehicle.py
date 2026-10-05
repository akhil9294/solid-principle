from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, year, model):
        self.brand = brand
        self.year = year
        self.model = model
    
    @abstractmethod
    def insurance_calculator(self):
        pass
    
    # If we create these 2 inside the same Vehicle class it's a problem. 
    # For Gas vehicle we don't need  rechargable method.
    # For electric vehicle we don't need  refulable method.
    # But we have to make sure for all Vehicle it shouls be either rechargable or fuelable function implemented.
    # That's why created seperate classes for these 2 functions. 

    # @abstractmethod
    # def rechargable(self):
    #     pass
    
    # @abstractmethod
    # def fuelable(self):
    #     pass