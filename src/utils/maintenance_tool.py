from abc import ABC, abstractmethod


class MaintenanceTool(ABC):

    @abstractmethod
    def maintenance_tool(self):
        pass

