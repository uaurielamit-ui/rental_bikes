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

    def scerch_by_id(self):
        b_id = helpers.val_str("enter the bike id: ")
        for b in self.list_bikes:
            if b.bike_id == b_id:
                return b.to_dict()
        return "bike did not find"

    def show_avalable(self):
        for b in self.list_bikes:
            if b.is_available == True:
                print(b.to_dict())
    
    def uniq_id(self):
        max_id = 0
        for b in self.list_bikes:
            if int(b.bike_id[1:]) >= max_id:
                max_id = int(b.bike_id[1:])+1
        return "B" + str(max_id).zfill(3)

    def add_new_bike(self):
        bike_id = self.uniq_id()
        model = helpers.val_str("enter the model name: ")
        bike_type = helpers.val_str("for Regular bike press 1   for Mountain bike press 2   for Electric bike press 3:  ")
        if bike_type == "1":
            bike_type = "Regular"
        elif bike_type == "2":
            bike_type = "Mountain"
        elif bike_type == "3":
            bike_type = "Electric"
        else:
            print("wrong type")
            return 
        price_hourly = helpers.val_int("enter the price per houre: ")
        price_daily = helpers.val_int("enter the price per dey: ")
        is_available = True
        is_operational = True
        bike = bikes.Bike(bike_id, model, bike_type, 
        price_hourly, price_daily, is_available, is_operational)
        self.list_bikes.append(bike)
        to_load = []
        for l in self.list_bikes:
            to_load.append(l.to_dict())
        storage.LoadData.dump_bike(to_load)
        return "bikes added"

    def up_bike(self):
        b_id = helpers.val_str("enter the bike id: ")
        for b in self.list_bikes:
            if b.bike_id == b_id:
                b.model = helpers.val_str("enter the model name: ")
                bike_type = helpers.val_str("for Regular bike press 1   for Mountain bike press 2   for Electric bike press 3:  ")
                if bike_type == "1":
                    b.bike_type = "Regular"
                elif bike_type == "2":
                    b.bike_type = "Mountain"
                elif bike_type == "3":
                    b.bike_type = "Electric"
                else:
                    print("wrong type")
                    return 
                b.price_hourly = helpers.val_int("enter the price per houre: ")
                b.price_daily = helpers.val_int("enter the price per dey: ")
                b.is_available = True
                b.is_operational = True
                to_up = []
                for b in self.list_bikes:
                    to_up.append(b.to_dict())
                storage.LoadData.dump_bike(to_up)
                return "bike updated"
        return "bike did not found"

    def bike_bruak(self):
        b_id = helpers.val_str("enter the bike id: ")
        for bike in self.list_bikes:
            if bike.bike_id == b_id:
                bike.is_operational = False
        to_up = []
        for b in self.list_bikes:
            to_up.append(b.to_dict())
        storage.LoadData.dump_bike(to_up)
        return "bike updated"