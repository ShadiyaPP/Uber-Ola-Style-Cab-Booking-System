# 🚕 Uber/Ola-Style Cab Booking System

A simple **Cab Booking System** built using **Python Object-Oriented Programming (OOP)** concepts. The project simulates a basic Uber/Ola-style booking system where customers can select a vehicle, enter their travel distance, and calculate the total fare.

---

## 📌 Project Overview

This project demonstrates how **OOP concepts such as classes, objects, inheritance, constructors, methods, and `super()`** can be used to build a real-world application.

The system supports different types of vehicles, including:

- 🚗 Cars
- 🏍️ Bikes

Each vehicle contains common information such as:

- Vehicle Number
- Brand
- Driver Name
- Price Per KM

The customer can select a vehicle and enter the required travel distance. The system then calculates and displays the total fare.

---
## 🎯 Project Objectives

The main objectives of this project are to:

- Understand and implement Object-Oriented Programming.
- Create a parent class and child classes using inheritance.
- Store vehicle and driver information using objects.
- Allow customers to select available vehicles.
- Accept travel distance from the customer.
- Calculate the total fare dynamically.
- Handle multiple cab bookings.
- Implement basic input validation and exception handling.

---

## 🧩 OOP Concepts Used

### 1. Class

The project uses classes to represent vehicles.

```python
class Vehicle:
    pass
```

### 2. Object

Objects are created from the `Car` and `Bike` classes.

```python
car1 = Car(...)
bike1 = Bike(...)
```

### 3. Inheritance

`Car` and `Bike` inherit common properties and methods from the `Vehicle` class.

```text
                Vehicle
                /     \
              Car     Bike
```

### 4. Constructor

The `__init__()` method initializes the vehicle details.

```python
def __init__(self, vehicle_number, brand, driver_name, price_per_km):
```

### 5. `super()`

The `super()` function is used to call the constructor of the parent `Vehicle` class.

```python
super().__init__(
    vehicle_number,
    brand,
    driver_name,
    price_per_km
)
```

### 6. Methods

Methods are used to perform operations such as fare calculation and displaying vehicle details.

```python
def calculate_fare(self, distance):
    return distance * self.price_per_km
```

---
## 🔄 Application Flow

```text
Start
  │
  ▼
Display Menu
  │
  ▼
Select "Book a Cab"
  │
  ▼
Display Available Vehicles
  │
  ▼
Customer Selects Vehicle
  │
  ▼
Enter Travel Distance
  │
  ▼
Calculate Total Fare
  │
  ▼
Display Booking Details
  │
  ▼
Book Another Cab?
  │
  ├── Yes ──► Book Again
  │
  └── No ───► Exit
```

---
