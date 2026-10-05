from utils.vehicle import Vehicle
from utils.insurance_calculator import InsuranceCalculator
from utils.object_formatter import ObjectFormatter
from utils.car import Car
from utils.truck import Truck
from utils.bus import Bus
from utils.electric_car import ElectricCar
from utils.maintenance_service import MaintenanceService
from utils.brake_inspection_tool import BrakeInspectionTool
from utils.maintenance_tool import MaintenanceTool

def main():

    object_formatter_obj1 = ObjectFormatter()
    insurance_calculator_obj1 = InsuranceCalculator()


    # vehicle_obj1 = Vehicle('mahendra',2025, 'xuv700')
    # print(object_formatter_obj1.vehicle_to_json(vehicle_obj1))
    

    car_obj1 = Car('mahendra',2025, 'xuv700')
    print(object_formatter_obj1.vehicle_to_json(car_obj1))
    insurance_calculator_obj1.vehicle_insurance_calculator(car_obj1)
    car_obj1.vehicle_fuelable()

    electric_car_obj1 = ElectricCar('mahendra',2025, 'ev_xuv7x0')
    print(object_formatter_obj1.vehicle_to_json(electric_car_obj1))
    insurance_calculator_obj1.vehicle_insurance_calculator(electric_car_obj1)
    electric_car_obj1.vehicle_rechargable()

    truck_obj1 = Truck('ford',2010, 'x1-t')
    print(object_formatter_obj1.vehicle_to_json(truck_obj1))
    insurance_calculator_obj1.vehicle_insurance_calculator(truck_obj1)
    truck_obj1.vehicle_fuelable()

    bus_obj1 = Bus('volvo', 2022, 'exl-500')
    print(object_formatter_obj1.vehicle_to_json(bus_obj1))
    insurance_calculator_obj1.vehicle_insurance_calculator(bus_obj1)
    
    MaintenanceService(BrakeInspectionTool()).vehicle_service(car_obj1)

if __name__=='__main__':
    main()