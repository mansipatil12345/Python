from abc import ABC , abstractmethod
class payments(ABC):
    @abstractmethod
    def pay(self,amount):
        pass