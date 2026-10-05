from utils.vehicle import Vehicle
from utils.maintenance_tool import MaintenanceTool


class BrakeInspectionTool(MaintenanceTool):
    def maintenance_tool(self, veh : Vehicle):
        print('performing brake inspection', veh.brand)