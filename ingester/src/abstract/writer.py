from abc import ABC, abstractmethod

class AbstractWriter(ABC):
    
    @abstractmethod
    def write(self):
        pass