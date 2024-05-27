from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def create(self):
        pass

class Car(Vehicle):
    
    def create(self):
        print("Car created")

class Bike(Vehicle):
    
    def create(self):
        print("Bike created")


class VehicleFactory(ABC):
    
    @abstractmethod
    def createVehicle(self):
        pass

class CarFactory(VehicleFactory):
    
    def createVehicle(self):
        return Car()

class BikeFactory(VehicleFactory):
    
    def createVehicle(self):
        return Bike()

if __name__ == '__main__':
    car = CarFactory().createVehicle()
    bike = BikeFactory().createVehicle()
    car.create()
    bike.create()
