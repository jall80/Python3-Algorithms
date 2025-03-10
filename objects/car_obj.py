import random
import warnings
import time
import os
import cars_dict

MAX_SKUS = 9999


class Vehicle:

    def __init__(
        self,
        SKU: str,
        make: str,
        model: str,
        year: int,
        mileage: int,
        speed: int,
        state: str,
        status: dict,
    ):
        """
        Initialize the car with make, model, and year.
        """
        self.SKU = SKU
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.speed = speed
        self.state = state
        self.status = status  # Dictionary containing component status

    def start(self):
        """
        Simulate starting the vehicle.
        """
        if self.state:
            print(f"\n⚠️ The {self.year} {self.make} {self.model} is already running!")
        else:
            print(f"\n🚗 Starting your {self.year} {self.make} {self.model}...\n")
            time.sleep(0.8)

            print("🔋 Checking battery...")
            time.sleep(0.5)
            print("⛽ Checking fuel levels...")
            time.sleep(0.5)
            print("🔧 Running system diagnostics...\n")
            time.sleep(1)

            print("✅ All systems go! Igniting engine... 🔥")
            time.sleep(1)

            self.state = True
            print(
                f"\n✅ The {self.year} {self.make} {self.model} is now running. Ready to hit the road! 🚀\n"
            )

    def stop(self):
        """
        Simulate stopping the vehicle.
        """
        if self.state:
            print(f"🛑 Stopping the {self.year} {self.make} {self.model}...")
            time.sleep(1)
            self.state = False
            print(f"✅ The {self.make} {self.model} is now turned off.")
        else:
            print(f"⚠️ The {self.make} {self.model} is already off.")

    def show_mileage(self):
        """
        Display the vehicle's mileage.
        """
        print(
            f" {self.make} {self.model} ({self.year}) has {self.mileage:,} km on the odometer."
        )

    def add_mileage(self, mileage_added):
        """
        Add mileage to the vehicle.
        """
        self.mileage += mileage_added

    def show_mileage(self):
        print(
            f"🚗 {self.make} {self.model} ({self.year}) has {self.mileage:,} km on the odometer."
        )

    def report(self):
        print("Report: {} \n".format(self))
        for component, status in self.status.items():
            status_text = "✅ Good" if status else "❌ Needs Attention"
            print(f"{component.replace('_', ' ').capitalize()}: {status_text}")

    def check_vehicle(self) -> bool:
        """
        Check the vehicle for any critical failures and print the status.

        Returns:
            bool: True if no critical failures are found, False otherwise.
        """
        print(f"Checking vehicle: {self} ... \n")

        # List of components that have failures
        failures = [
            component for component, status in self.status.items() if not status
        ]

        # Default state: assume the vehicle is fine
        is_vehicle_ok = True

        # Check if any failed components are critical
        for component, is_critical in cars_dict.fault_severity.items():
            if component in failures and is_critical:
                print(f"⚠️ Critical failure detected in -> {component}")
                is_vehicle_ok = False

        # Return the result
        return is_vehicle_ok

    def __str__(self):
        """
        Return a user-friendly string representation of the vehicle.
        """
        return f"SKU{self.SKU} {self.year} {self.make} {self.model}"

    def __repr__(self):
        """
        Return a detailed string representation of the vehicle (for debugging).
        """
        return f"Vehicle(SKU='{self.SKU}', make='{self.make}', model='{self.model}', year={self.year})"

    @staticmethod
    def vehicle_info():
        """
        A static method that provides general info about cars.
        """
        print("Vehicles are commonly used for transportation.")


class Car(Vehicle):
    """
    A class to represent a car.
    """

    # Class variable
    wheels = 4
    weight = "medium"

    car_draw = """ 
          ________
       _ //|_||__\\`-. _ 
      (   _        _    \\
      =`-(_)------(_)----'
    """

    def __init__(
        self,
        SKU: str,
        make: str,
        model: str,
        year: int,
        mileage: int,
        speed: int,
        state: str,
        status: dict,
    ):
        """
        Initialize the car with additional attributes.
        """
        super().__init__(SKU, make, model, year, mileage, speed, state, status)

    def drive(self):

        print("Welcome to your car simulator!\n")
        if not self.check_vehicle():
            return
        reply = (
            input(
                f"\n🚗 Ready to drive your {self.make} {self.model}? \n"
                "⚠️ This will clear the screen. \n"
                "🔘 Press [Y] to continue or [N] to cancel: "
            )
            .strip()
            .lower()
        )

        if reply.lower() == "y":

            if self.state.lower() == "off":
                print("\n⚠️ The car is currently OFF.")
                car_state = input("🔑 Do you want to start it? (Y/N): ").strip().lower()

                if car_state == "y":
                    print("\n🔄 Starting the car...")
                    time.sleep(0.5)
                    self.start()
                else:
                    print("\n🚗 No worries! We'll take a ride another time. 🏁")
                    return

            start = (
                input(
                    f"Ready to take a ride in the {self.make} {self.model}? Let's go! Press Y to start, or N to cancel: "
                )
                .strip()
                .lower()
            )
            if start == "y":
                print("\nPreparing the engine...\n")
                time.sleep(1)
                print("Vroom... vroom... Starting the engine!\n")
                time.sleep(1)

                # Simulate the car moving
                for n in range(0, 100):
                    os.system(
                        "cls" if os.name == "nt" else "clear"
                    )  # Clears the terminal screen
                    print(f"You're cruising in your {self.make} {self.model}!")
                    print(
                        "\n".join(" " * n + line for line in self.car_draw.splitlines())
                    )
                    time.sleep(0.05 / (self.speed / 100))
                print("\nThe car has drived through the road, enjoy the ride!")
                print(
                    f"\n⚡ Your {self.year} {self.make} {self.model} just conquered 100 km at an average speed of {self.speed} km/h! 🚀"
                )
                self.add_mileage(100)
            else:
                print("Not ready yet? No problem, we'll take a ride another time. 🏁")
        else:
            print(
                f"Alright, we'll wait for the next adventure with your {self.make} {self.model}! 🚗💨"
            )

    def stop(self):
        """
        Simulate stopping the car.
        """
        print(f"The {self.year} {self.make} {self.model} is stopping.")

    def honk(self):
        """
        Simulate honking the car horn.
        """
        print("Beep beep!")

    @staticmethod
    def car_info():
        """
        A static method that provides general info about cars.
        """
        print("Cars are commonly used for transportation.")

    @classmethod
    def car_class_info(cls):
        """
        A class method that gives general information about the class.
        """
        print(
            f"All cars of the {cls.__name__} class have {cls.wheels} wheels and their weight is {cls.weight}."
        )

    def __str__(self):
        """
        Return a user-friendly string representation of the car.
        """
        return f"SKU{self.SKU} {self.year} {self.make} {self.model}"

    def __repr__(self):
        """
        Return an unambiguous string representation of the car (for debugging).
        """
        return f"Car(SKU='{self.SKU}', make='{self.make}', model='{self.model}', year={self.year})"


def generate_a_exclusive_SKU(excluded_numbers: list) -> int:
    """Generates a unique SKU that is not in the excluded_numbers list."""

    if len(excluded_numbers) >= MAX_SKUS:
        warnings.warn(
            "\nThere aren't more SKUs available, limit '{}' SKUs reached. Consider increasing the number.".format(
                MAX_SKUS
            )
        )
        return -1  # Indicates no available SKU

    while True:
        number = random.randint(0, MAX_SKUS - 1)  # Ensuring it doesn't exceed MAX_SKUS
        if number not in excluded_numbers:
            return number


def create_dict_element(element: Car, direc: dict) -> str:
    """Adds a Car object to the dictionary, ensuring a unique SKU."""

    if element.SKU in direc:
        warnings.warn(
            "Cannot assign SKU: '{}' because it's already in use.\n".format(element.SKU)
        )
        element.SKU = str(generate_a_exclusive_SKU([int(sku) for sku in direc.keys()]))
        print("New SKU: {} assigned to {}".format(element.SKU, element))

    # Ensure the SKU is within the allowed range
    try:
        sku_int = int(element.SKU)
        if 0 <= sku_int < MAX_SKUS:
            direc[str(element.SKU)] = element
        else:
            warnings.warn(
                "SKU: '{}' out of range: '0 -> {}', could not be added.".format(
                    element.SKU, MAX_SKUS - 1
                )
            )
    except ValueError:
        warnings.warn("Invalid SKU format: '{}', must be a number.".format(element.SKU))

    return element.SKU


print(" \n=============== Basic init and actions ===============\n ")

# Create instances of the Car class and add them to the dictionary
# Define a unique SKU for each car

cars_parts = cars_dict.cars_parts

cars = {
    "0001": Car(
        "0001", "Toyota", "Corolla", 2020, 40000, 200, "OFF", cars_parts["0001"]
    ),
    "0002": Car("0002", "Honda", "Civic", 2019, 35000, 200, "OFF", cars_parts["0002"]),
    "0003": Car("0003", "Ford", "Focus", 2021, 15000, 200, "OFF", cars_parts["0003"]),
    "0004": Car(
        "0004", "Chevrolet", "Malibu", 2022, 5000, 100, "OFF", cars_parts["0004"]
    ),
    "0005": Car(
        "0005", "Nissan", "Altima", 2018, 60000, 220, "OFF", cars_parts["0005"]
    ),
    "0006": Car(
        "0006", "Geely", "Coolray", 2024, 20000, 210, "OFF", cars_parts["0006"]
    ),
    "0007": Car(
        "0007", "Nissan", "Skyline", 2000, 200000, 340, "OFF", cars_parts["0007"]
    ),
    "0008": Car(
        "0008", "Toyota", "Supra", 1999, 300000, 350, "OFF", cars_parts["0008"]
    ),
}

# Call instance methods
cars["0001"].start()  # Output: The 2020 Toyota Corolla is starting.
cars["0001"].honk()  # Output: Beep beep!
cars["0001"].stop()  # Output: The 2020 Toyota Corolla is stopping.

# Call class and static methods
Car.car_info()  # Output: Cars are commonly used for transportation.
Car.car_class_info()  # Output: All vehicles of the Car class have 4 wheels.

# Print string representation
print(cars["0001"])  # Output: 2020 Toyota Corolla

# Print unambiguous representation (used in debugging)
print(repr(cars["0001"]))  # Output: Car(make='Toyota', model='Corolla', year=2020)

print(" \n=============== Add mileage ===============\n ")

print("The car mileage is : {}".format(cars["0001"].mileage))
cars["0001"].add_mileage(2000)
print("After adding 2000 Km, the car mileage is : {}".format(cars["0001"].mileage))

print(" \n=============== Create another Car and add it to car_dict ===============\n ")

create_dict_element(
    Car(
        "0009", "Hyundai", "Creta", 2022, 33000, 150, "OFF", cars_dict.car_status_creta
    ),
    cars,
)
print("Car created: {}".format(cars["0009"]))

print(
    " \n=============== Create another Car and add it to car_dict, with an alreadt listed SKU ===============\n "
)

kia_sku = create_dict_element(
    Car(
        "0003",
        "Kia",
        "Sportage",
        2015,
        88000,
        180,
        "OFF",
        cars_dict.car_status_sportage,
    ),
    cars,
)
print("The element created is: {}".format(cars[kia_sku]))


print(" \n===============  Modify class variable ===============\n ")

Car.wheels = 6
Car.car_class_info()
Car.wheels = 4
Car.car_class_info()

print(" \n===============  drive the car function ===============\n ")


cars[kia_sku].drive()

print(" \n===============  Report a car status ===============\n ")


cars["0006"].report()


print(" \n===============  Report a car status ===============\n ")

cars["0008"].show_mileage()
cars["0008"].start()
cars["0008"].drive()
cars["0008"].show_mileage()

print(
    " \n===============  Try to drive a car with a critical failure ===============\n "
)

cars["0001"].start()
cars["0001"].drive()

### ADD KM WHEN DRIVE
