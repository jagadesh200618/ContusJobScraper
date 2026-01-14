# Define a class
class Car:
    # Constructor
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    # Method to display car details
    def display_details(self):
        print("Car Brand:", self.brand)
        print("Car Model:", self.model)
        print("Car Year:", self.year)
