class Customer:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender

def greet(customer):
        if customer.gender=="Male":
            print("Hello",customer.name,"sir")

        else:
            print("Hello",customer.name,"sir")

        cust2=Customer("Nitish","Male")    
    
        return cust2


# def greet(customer):
#    print("Hello",customer.name) 

cust=Customer("Nitish","female")

new_cust = greet(cust)
print(new_cust.name)
# class ke objects are mutable like list dic and sets