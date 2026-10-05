from abc import ABC , abstractmethod


class Rechargable(ABC):

    @abstractmethod
    def vehicle_rechargable(self):
        pass