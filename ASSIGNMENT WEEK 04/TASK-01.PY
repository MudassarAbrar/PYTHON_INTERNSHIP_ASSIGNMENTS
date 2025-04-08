'''
1. Create a Bus child class that inherits from the Vehicle class. The default
fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus
instance, we need to add an extra 10% on full fare as a maintenance
charge. So total fare for bus instance will become the final amount =
total fare + 10% of the total fare.

'''

class Vehicle:
    def __init__(self, name, seating_capacity):
        self.name = name
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100
    
    def __str__(self):
        return f"Vehicle Name: {self.name}, Seating Capacity: {self.seating_capacity}"
    
    def __repr(self):
        return f"Vehicle({self.name}, {self.seating_capacity})"
    
    
class Bus(Vehicle):
    def fare(self):
        base_fare = super().fare()
        maintanance_charge = 0.10 * base_fare
        total_fare = base_fare + maintanance_charge 
        return total_fare
    def __str__(self):
        return f"Bus Name: {self.name}, Seating Capacity: {self.seating_capacity}"

bus1 = Bus("School Bus", 50)
print(bus1)  
print(bus1.fare())