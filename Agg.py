#Aggregation:

#creating an object of one class inside another class and using it.

class Engine:
    def start(self):
        print("Engine is starting")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def drive(self):
        self.engine.start()
        print("Car is moving")        

c=Car(Engine())
c.drive()        