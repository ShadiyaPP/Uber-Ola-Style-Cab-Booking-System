class Vehicle:
    def __init__(self, vehicle_number, brand, driver_name, price_per_km):
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.driver_name = driver_name
        self.price_per_km = price_per_km

    def calculate_fare(self, distance):
        return distance * self.price_per_km


class Car(Vehicle):
    def __init__(self, vehicle_number, brand, driver_name, price_per_km):
        super().__init__(
            vehicle_number,
            brand,
            driver_name,
            price_per_km
        )
        self.vehicle_type = "Car"


class Bike(Vehicle):
    def __init__(self, vehicle_number, brand, driver_name, price_per_km):
        super().__init__(
            vehicle_number,
            brand,
            driver_name,
            price_per_km
        )
        self.vehicle_type = "Bike"


# Create 2 Cars
car1 = Car("KL01AB1234", "Toyota", "Rahul", 20)
car2 = Car("KL02CD5678", "Honda", "Arun", 18)

# Create 2 Bikes
bike1 = Bike("KL03EF1111", "Honda", "Vishnu", 10)
bike2 = Bike("KL04GH2222", "Yamaha", "Akhil", 12)


# Store all vehicles
vehicles = [car1, car2, bike1, bike2]


# Display available vehicles
print("Available Vehicles")
print("-" * 50)

for i, vehicle in enumerate(vehicles, start=1):
    print(
        f"{i}. {vehicle.vehicle_type} | "
        f"Driver: {vehicle.driver_name} | "
        f"Rate: ₹{vehicle.price_per_km}/KM"
    )


# Multiple trips
trips = [
    (1, 15),
    (2, 20),
    (3, 10),
    (4, 25)
]


# Calculate fares
print("\nTrip Details")
print("-" * 50)

for vehicle_choice, distance in trips:

    vehicle = vehicles[vehicle_choice - 1]

    fare = vehicle.calculate_fare(distance)

    print(f"Driver   : {vehicle.driver_name}")
    print(f"Vehicle  : {vehicle.vehicle_type}")
    print(f"Distance : {distance} KM")
    print(f"Rate     : ₹{vehicle.price_per_km}/KM")
    print(f"Fare     : ₹{fare}")
    print("-" * 50)