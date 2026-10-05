from utils.vehicle import Vehicle
from utils.maintenance_tool import MaintenanceTool

class MaintenanceService:
    def __init__(self, tool: MaintenanceTool):
        self.tool = tool
    
    def vehicle_service(self, veh: Vehicle):
        self.tool.maintenance_tool(veh)

