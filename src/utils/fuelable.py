from abc import ABC , abstractmethod


class Fuelable(ABC):

    @abstractmethod
    def vehicle_fuelable(self):
        pass
