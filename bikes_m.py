import helpers
import datetime
import rental
import storage
import bikes

class BikeManeger:
    def __init__(self):
        self.row_bikes = storage.LoadData.load_bike()
        self.row_rents = storage.LoadData.load_rental()
        self.list_bikes = [bikes.Bike.load_dict(b) for b in self.row_bikes]
        self.list_rents = [rental.Rentals.from_dict(r) for r in self.row_rents]

    def show_all_bikes(self):
        for bike in self.list_bikes:
            print(bike.to_dict())