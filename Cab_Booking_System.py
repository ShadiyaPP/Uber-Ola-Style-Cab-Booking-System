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
            raise ValueError("Distance must be greater than 0.")

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
            raise ValueError(
                f"Vehicle number "
                f"{vehicle.vehicle_number} already exists."
            )

        self.vehicles[vehicle.vehicle_number] = vehicle

    def get_vehicles(self):
        return list(self.vehicles.values())

    def get_vehicle_by_index(self, index):

        vehicles = self.get_vehicles()

        if index < 0 or index >= len(vehicles):
            raise IndexError("Invalid vehicle selection.")

        return vehicles[index]

    def calculate_trip_fare(
        self,
        vehicle_number,
        distance
    ):

        if vehicle_number not in self.vehicles:
            raise ValueError("Vehicle not found.")

        if distance <= 0:
            raise ValueError(
                "Distance must be greater than 0."
            )

        vehicle = self.vehicles[vehicle_number]

        fare = vehicle.calculate_fare(distance)

        return {
            "driver": vehicle.driver_name,
            "vehicle_type": vehicle.__class__.__name__,
            "brand": vehicle.brand,
            "vehicle_number": vehicle.vehicle_number,
            "distance": distance,
            "rate": vehicle.price_per_km,
            "fare": fare
        }


# ---------------------------------------------------------
# Display Functions
# ---------------------------------------------------------

def display_vehicles(cab_system):

    vehicles = cab_system.get_vehicles()

    print("\n========== AVAILABLE VEHICLES ==========")

    if not vehicles:
        print("No vehicles available.")
        return

    for index, vehicle in enumerate(vehicles, start=1):

        print(
            f"{index}. "
            f"{vehicle.__class__.__name__} | "
            f"{vehicle.brand} | "
            f"Driver: {vehicle.driver_name} | "
            f"₹{vehicle.price_per_km}/KM"
        )


def get_vehicle_selection(cab_system):

    vehicles = cab_system.get_vehicles()

    while True:

        display_vehicles(cab_system)

        try:

            choice = int(
                input(
                    "\nSelect vehicle number: "
                )
            )

            if choice < 1 or choice > len(vehicles):

                print(
                    "❌ Invalid selection. "
                    "Please choose from the available options."
                )

                continue

            return vehicles[choice - 1]

        except ValueError:

            print(
                "❌ Invalid input. "
                "Please enter a number."
            )


def get_distance():

    while True:

        try:

            distance = float(
                input(
                    "Enter travel distance (KM): "
                )
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


def display_trip_summary(trip):

    print("\n========== TRIP SUMMARY ==========")

    print(f"Driver        : {trip['driver']}")
    print(f"Vehicle       : {trip['vehicle_type']}")
    print(f"Brand         : {trip['brand']}")
    print(f"Vehicle Number: {trip['vehicle_number']}")
    print(f"Distance      : {trip['distance']} KM")
    print(f"Rate          : ₹{trip['rate']}/KM")
    print(f"Total Fare    : ₹{trip['fare']}")

    print("==================================")


# ---------------------------------------------------------
# Main Application
# ---------------------------------------------------------

def main():

    cab_system = CabBookingSystem()

    # 2 Cars

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

    # 2 Bikes

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

    # Add vehicles

    cab_system.add_vehicle(car1)
    cab_system.add_vehicle(car2)
    cab_system.add_vehicle(bike1)
    cab_system.add_vehicle(bike2)

    # -----------------------------------------------------
    # Booking Menu
    # -----------------------------------------------------

    while True:

        print("\n========== 🚕 CAB BOOKING SYSTEM ==========")
        print("1. Book a Cab")
        print("2. Show Available Vehicles")
        print("3. Exit")
        print("============================================")

        choice = input("Enter your choice: ").strip()

        # -------------------------------------------------
        # Book Cab
        # -------------------------------------------------

        if choice == "1":

            vehicle = get_vehicle_selection(
                cab_system
            )

            distance = get_distance()

            try:

                trip = cab_system.calculate_trip_fare(
                    vehicle.vehicle_number,
                    distance
                )

                display_trip_summary(trip)

            except ValueError as error:

                print(f"❌ {error}")

        # -------------------------------------------------
        # Show Vehicles
        # -------------------------------------------------

        elif choice == "2":

            display_vehicles(cab_system)

        # -------------------------------------------------
        # Exit
        # -------------------------------------------------

        elif choice == "3":

            print(
                "\n👋 Thank you for using "
                "the Cab Booking System!"
            )

            break

        else:

            print(
                "❌ Invalid choice. "
                "Please select 1, 2, or 3."
            )


if __name__ == "__main__":
    main()