class Vehicle:
    
    def __init__(self, brand, model, year, rental_price_per_day):
        
        self.brand = brand
        self.model = model
        self.year = year
        self.__rental_price_per_day = rental_price_per_day
        
    def get_rental_price(self):
        return self.__rental_price_per_day
        
    def set_rental_price(self, price):
        return self.__rental_price_per_day
        
    def display_info(self):
        print(f"{self.brand} {self.model}, Year: {self.year}, Rental Price: $ {self.__rental_price_per_day}/day")
        
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
        
def show_vehicle_info(Vehicle):
    Vehicle.display_info()
    
counter = 0

while counter != 3:
    
    counter = int(input("Enter 1 to see car, or 2 to see bike or 3 to exit: "))
    
    if counter == 1:
        
        car_brand = input("Enter the car brand: ")
        car_model = input("Enter the car model: ")
        car_year = int(input("Enter the car year: "))
        car_days = int(input("Enter how many days you want to rent the car: "))
        car_rental_price = 50
        car_seats = 5
        
        car = Car(car_brand, car_model, car_year, car_rental_price , car_seats)
        
        show_vehicle_info(car)
        
        print(f"Rental cost for {car_brand} {car_model} for {car_days} days: ${car.calculate_rental_cost(car_days)}")
        
    elif counter == 2:
        
        bike_brand = input("Enter the bike brand: ")
        bike_model = input("Enter the bike model: ")
        bike_year = int(input("Enter the bike year: "))
        bike_days = int(input("Enter how many days you want to rent the bike:"))
        bike_rental_price = 30
        bike_engine_capacity = 998
        
        bike = Bike(bike_brand, bike_model, bike_year, bike_rental_price , bike_engine_capacity)
        
        show_vehicle_info(bike)
        
        print(f"Rental cost for {bike_brand} {bike_model} for {bike_days} days: ${bike.calculate_rental_cost(bike_days)}")
