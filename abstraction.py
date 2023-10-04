from abc import ABC,abstractmethod
class Vehicle(ABC):
    def __init__(self,n) -> None:
        self.tyers=n 
    @abstractmethod
    def start(self):
        pass 
    
    def display(self):
         print('this is abstract class')

class Bike(Vehicle):
    def __init__(self,n,color) -> None:
           self.n=n
           self.color=color
    #def start(self):
     #   print('start with kick')
    
class scooty(Vehicle):
    def __init__(self,n) -> None:
          super().__init__(n)
    def start(self):
        print('self start')
    
class Car(Vehicle):
    def __init__(self,n,x) -> None:
         super().__init__(n)
         self.gear=x
    def start(self):
        print('start with key')
        
'''v=Vehicle(2)
print(v.tyers)'''  
bike=Bike(2,"black")
bike.start()
bike.display()