from rental import Vehicle, Renter, ElectricCar, Motorbike


def main():
    print("=== CampusWheels Vehicle-Rental Desk ===")

    # Create vehicles and a renter
    car = Vehicle("Toyota", "Yaris", "1AB234")
    electric_car = ElectricCar("Tesla", "Model 3", "EV001", 60)
    motorbike = Motorbike("Honda", "Click", "MB001", 125)
    renter = Renter("May Myat Thu", 1001)

    print("\n1. New objects")
    print(car)
    print(electric_car)
    print(motorbike)
    print(f"Renter: {renter.name}, licence: {renter.license_no}")
    print(f"Rented list: {renter.rented}")

    # Rent and return a vehicle
    print("\n2. Rent and return")
    car.rent()
    renter.rented.append(car)
    print("After renting:")
    print(car)

    car.return_vehicle()
    renter.rented.remove(car)
    print("After returning:")
    print(car)

    # Show ValueError handling
    print("\n3. Validation with ValueError")
    try:
        Renter("", 2002)
    except ValueError as error:
        print("Bad name caught:", error)

    try:
        Renter("Invalid Licence", 0)
    except ValueError as error:
        print("Bad licence caught:", error)

    # Show validation also works when values are changed later
    try:
        renter.name = "   "
    except ValueError as error:
        print("Changed bad name caught:", error)

    try:
        renter.license_no = -5
    except ValueError as error:
        print("Changed bad licence caught:", error)

    # Inheritance and polymorphism
    print("\n4. Inheritance and polymorphism")
    vehicles = [car, electric_car, motorbike]
    for vehicle in vehicles:
        print(vehicle)
        print("  Is a Vehicle:", isinstance(vehicle, Vehicle))


if __name__ == "__main__":
    main()
