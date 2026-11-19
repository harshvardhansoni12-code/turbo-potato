# static attribute and methods in python
class hello:
    def __init__(self):
        self.sno=0
        self.inc()
    def inc(self):
        self.sno+=1    

h=hello()        
print(h.sno)
print("=============")
c=hello()
print(c.sno) ## sno is instance var which will initialize to 0 for every time a new obk is created

