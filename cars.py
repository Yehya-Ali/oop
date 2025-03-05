class Vehicle:
    def __init__(self, brand, model, year, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.__rental_price_per_day = rental_price_per_day

    def get_rental_price(self):
        return self.__rental_price_per_day

    def set_rental_price(self, price):
        self.__rental_price_per_day = price

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Rental Price: ${self.__rental_price_per_day}/day")

    def calculate_rental_cost(self, days):
        return self.__rental_price_per_day * days

class Car(Vehicle):
    def __init__(self, brand, model, year, rental_price_per_day, seating_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.seating_capacity = seating_capacity

    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}, Seats: {self.seating_capacity}, Rental Price: ${self.get_rental_price()}/day")

class Bike(Vehicle):
    def __init__(self, brand, model, year, rental_price_per_day, engine_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.engine_capacity = engine_capacity

    def display_info(self):
        print(f"Bike: {self.brand} {self.model}, Year: {self.year}, Engine: {self.engine_capacity}cc, Rental Price: ${self.get_rental_price()}/day")

def show_vehicle_info(vehicle):
    vehicle.display_info()

car = Car("Toyota", "Corolla", 2020, 50, 5)
bike = Bike("Yamaha", "R1", 2019, 30, 998)

show_vehicle_info(car)
show_vehicle_info(bike)

print(f"Rental cost for Toyota Corolla for 3 days: ${car.calculate_rental_cost(3)}")
print(f"Rental cost for Yamaha R1 for 5 days: ${bike.calculate_rental_cost(5)}")

car.set_rental_price(55)

print(f"Updated rental price for Toyota Corolla: ${car.get_rental_price()}/day")
