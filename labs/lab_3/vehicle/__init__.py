"""
Write a Python program to create a Vehicle class with max_speed and mileage 
instance attributes.
-Create a Bus class that inherits from the Vehicle class. Give the capacity argument 
of Bus.seating_capacity() a default value of 50.
-Create a Bus child class that inherits from the Vehicle class. The default fare 
charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to 
add an extra 10% on full fare as a maintenance charge. So total fare for bus instance 
will become the final amount = total fare + 10% of the total fare.
"""

DEFAULT_CAPACITY = 50
DEFAULT_RATE = 100

class Vehicle:
    max_speed: float
    mileage: float

    def __init__(self, max_speed, mileage, capacity=DEFAULT_CAPACITY):
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def __repr__(self):
        data_dict = {
            'max_speed': self.max_speed,
            'mileage': self.mileage,
            'capacity': self.capacity,
            'fare': self.calculate_fare(),
        }
        return f"Vehicle: {data_dict}"

    def calculate_fare(self):
        return self.get_capacity() * DEFAULT_RATE

    def get_capacity(self):
        return self.capacity
