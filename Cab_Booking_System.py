class Vehicle:
    def __init__(
        self,
        vehicle_number,
        brand,
        driver_name,
        price_per_km
    ):
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.driver_name = driver_name
        self.price_per_km = price_per_km

    def calculate_fare(self, distance):
        if distance <= 0:
            return 0

        return distance * self.price_per_km

    def __str__(self):
        return (
            f"Vehicle No: {self.vehicle_number} | "
            f"Brand: {self.brand} | "
            f"Driver: {self.driver_name} | "
            f"Rate: ₹{self.price_per_km}/KM"
        )

    def __eq__(self, other):
        if isinstance(other, Vehicle):
            return (
                self.vehicle_number
                == other.vehicle_number
            )
        return False

    def __hash__(self):
        return hash(self.vehicle_number)


class Car(Vehicle):
    def __init__(
        self,
        vehicle_number,
        brand,
        driver_name,
        price_per_km,
        seating_capacity=4
    ):
        super().__init__(
            vehicle_number,
            brand,
            driver_name,
            price_per_km
        )

        self.seating_capacity = seating_capacity

    def __str__(self):
        return (
            f"Car | {super().__str__()} | "
            f"Seats: {self.seating_capacity}"
        )


class Bike(Vehicle):
    def __init__(
        self,
        vehicle_number,
        brand,
        driver_name,
        price_per_km
    ):
        super().__init__(
            vehicle_number,
            brand,
            driver_name,
            price_per_km
        )

    def __str__(self):
        return f"Bike | {super().__str__()}"


class CabBookingSystem:
    def __init__(self):
        self.vehicles = {}

    def add_vehicle(self, vehicle):

        if vehicle.vehicle_number in self.vehicles:
            print(
                f"❌ Vehicle number "
                f"{vehicle.vehicle_number} already exists."
            )
            return False

        self.vehicles[vehicle.vehicle_number] = vehicle

        print(
            f"✅ {vehicle.brand} "
            f"({vehicle.vehicle_number}) added successfully."
        )

        return True

    def display_vehicles(self):

        if not self.vehicles:
            print("❌ No vehicles available.")
            return

        print("\n========== AVAILABLE VEHICLES ==========")

        for vehicle in self.vehicles.values():
            print(vehicle)

    def find_vehicle(self, vehicle_number):

        return self.vehicles.get(vehicle_number)

    def book_cab(self, vehicle_number, distance):

        if vehicle_number not in self.vehicles:
            print("❌ Vehicle not found.")
            return

        if distance <= 0:
            print("❌ Distance must be greater than 0.")
            return

        vehicle = self.vehicles[vehicle_number]

        fare = vehicle.calculate_fare(distance)

        print("\n========== TRIP SUMMARY ==========")
        print(f"Driver   : {vehicle.driver_name}")
        print(
            f"Vehicle  : "
            f"{vehicle.__class__.__name__}"
        )
        print(f"Brand    : {vehicle.brand}")
        print(f"Distance : {distance} KM")
        print(
            f"Rate     : "
            f"₹{vehicle.price_per_km}/KM"
        )
        print(f"Total Fare: ₹{fare}")
        print("==================================")


def get_positive_distance():

    while True:

        try:
            distance = float(
                input("Enter travel distance (KM): ")
            )

            if distance <= 0:
                print(
                    "❌ Distance must be greater than 0."
                )
                continue

            return distance

        except ValueError:
            print(
                "❌ Invalid input. "
                "Please enter a numeric distance."
            )


def main():

    cab_system = CabBookingSystem()

    # -----------------------------------------
    # Create 2 Cars
    # -----------------------------------------

    car1 = Car(
        "KL01AB1234",
        "Toyota",
        "Rahul",
        20,
        4
    )

    car2 = Car(
        "KL02CD5678",
        "Honda",
        "Arun",
        25,
        4
    )

    # -----------------------------------------
    # Create 2 Bikes
    # -----------------------------------------

    bike1 = Bike(
        "KL03EF9012",
        "Royal Enfield",
        "Vishnu",
        12
    )

    bike2 = Bike(
        "KL04GH3456",
        "Yamaha",
        "Akhil",
        10
    )

    # -----------------------------------------
    # Add Vehicles
    # -----------------------------------------

    print("========== ADDING VEHICLES ==========")

    cab_system.add_vehicle(car1)
    cab_system.add_vehicle(car2)
    cab_system.add_vehicle(bike1)
    cab_system.add_vehicle(bike2)

    # -----------------------------------------
    # Display Vehicles
    # -----------------------------------------

    cab_system.display_vehicles()

    # -----------------------------------------
    # Multiple Trips
    # -----------------------------------------

    print("\n========== TRIP 1 ==========")

    distance1 = 15
    cab_system.book_cab(
        "KL01AB1234",
        distance1
    )

    print("\n========== TRIP 2 ==========")

    distance2 = 20
    cab_system.book_cab(
        "KL02CD5678",
        distance2
    )

    print("\n========== TRIP 3 ==========")

    distance3 = 10
    cab_system.book_cab(
        "KL03EF9012",
        distance3
    )

    print("\n========== TRIP 4 ==========")

    distance4 = 25
    cab_system.book_cab(
        "KL04GH3456",
        distance4
    )

    # -----------------------------------------
    # Duplicate Vehicle Test
    # -----------------------------------------

    print("\n========== DUPLICATE TEST ==========")

    duplicate_car = Car(
        "KL01AB1234",
        "Tata",
        "Suresh",
        30
    )

    cab_system.add_vehicle(duplicate_car)

    # -----------------------------------------
    # Invalid Distance Test
    # -----------------------------------------

    print("\n========== VALIDATION TEST ==========")

    cab_system.book_cab(
        "KL01AB1234",
        -5
    )

    # -----------------------------------------
    # Invalid Vehicle Test
    # -----------------------------------------

    cab_system.book_cab(
        "KL99XX9999",
        10
    )


if __name__ == "__main__":
    main()