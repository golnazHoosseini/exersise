class Vehicle:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year

    def display_info(self):
        print(f"brand: {self.brand}")  
        print(f"year: {self.year}")

class Car (Vehicle):
    def __init__(self,brand,year,num_doors):
        super().__init__(brand, year)
        self.num_doors=num_doors

    def display_info(self):
        super().display_info()
        print(f"num doors : {self.num_doors}") 

class Motorcycle(Vehicle):
    def __init__(self, brand, year, has_sidecar):
        super().__init__(brand, year)
        self.has_sidecar = has_sidecar 

    def display_info(self):
        super().display_info()
        if self.has_sidecar:
            print("sidecar=true")
        else:
            print("sidecar=false")    



print("vehicle: ")
v1 = Vehicle("Toyota", 2020)
v1.display_info()
print()

print("car:")
c1 = Car("Tesla", 2023, 4)
c1.display_info()

c2 = Car("BMW", 2022, 2)
c2.display_info()

print("motorcycle:")
m1 = Motorcycle("Harley-Davidson", 2021, True)
m1.display_info()

m2 = Motorcycle("Yamaha", 2023, False)
m2.display_info()



         
