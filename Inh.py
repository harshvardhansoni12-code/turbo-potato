## this is inheritance
class vehicle:
    counter=0
    def __init__(self):
        self.fuel_required=true
        self.type="4wheels"

    def engine(self):
        print("engine is starting")  

    @staticmethod
    def get_count():
        print(vehicle.counter)
        return vehicle.counter

    @staticmethod
    def set_count():
        vehicle.counter += 1
        print(vehicle.counter)
        return vehicle.counter

class car(vehicle):
    def __init__(self):
        self.car="carwaa"

    def start(self):
        print("car is starting")    

c=car()
s=car()
c.start()
c.engine()
c.get_count()
c.set_count()
s.set_count()