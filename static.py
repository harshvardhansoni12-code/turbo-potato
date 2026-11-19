# static attribute and methods in python
class hello:
    _counter=1 # this is static/class var always outside constructor
    def __init__(self):
        self.sno=hello.__counter
        self.inc()
    def inc(self):
        hello.__counter=hello.__counter+1   

    def get_counter(self):
        return hello.__counter

    def set_counter(self):
        return hello.__counter        

h=hello()        
print(h.sno)
print("=============")
c=hello()
print(c.sno)

# sno is instance var which will initialize to 0 for every time a new obk is created
# suppose we have to retain any var value we will make it static/class var.

d=hello()
print(d.sno)