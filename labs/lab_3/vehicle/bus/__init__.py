from vehicle import Vehicle, DEFAULT_CAPACITY

MAINTENANCE_CHARGE_RATE = 1.1


class Bus(Vehicle):
    capacity: int

    def __init__(self, max_speed, mileage, capacity=DEFAULT_CAPACITY):
        super().__init__(max_speed, mileage, capacity)

    def __repr__(self):
        data_dict = {
            'max_speed': self.max_speed,
            'mileage': self.mileage,
            'capacity': self.capacity,
            'fare': self.calculate_fare(),
        }
        return f"Bus: {data_dict}"

    def calculate_fare(self):
        total_fare = super().calculate_fare()
        return total_fare * MAINTENANCE_CHARGE_RATE
