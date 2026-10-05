from utils.vehicle import Vehicle

class ObjectFormatter:
    def vehicle_to_json(self, veh: Vehicle):
        return {"brand": veh.brand, "model": veh.model, "year": veh.year}


    def dict_to_json(self):
        pass
