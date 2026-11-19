# static attribute and methods in python

class hello:
    __counter=1 # this is static/class var always outside constructor
    def __init__(self):
        self.sno=hello.__counter
        self.inc()
    def inc(self):
        hello.__counter=hello.__counter+1   

    @staticmethod
    def get_counter(): ## self refers to obj
    # is method mei hum self pass ni krenge kyu yaha hum class var se deal kr rhe h
        return hello.__counter

    @staticmethod
    def set_counter(new):
        if type(new)==int:
            hello.__counter=new
            return hello.__counter
        else:
            print("invalid value of counter")         

h=hello()     

print(h.sno)
print("=============")
print(hello.get_counter())
print("=============")
print(hello.set_counter(7))
print("=============")
c=hello()
print(c.sno)

# sno is instance var which will initialize to 0 for every time a new obk is created
# suppose we have to retain any var value we will make it static/class var.

d=hello()
print(d.sno) #2:30:00

# hui hui hui
