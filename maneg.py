import helpers
import datetime
import rental
import storage
import bikes

class RentalManager:
    def __init__(self, pricecal):
        self.pricecal = pricecal
        self.row_bikes = storage.LoadData.load_bike()
        self.row_rents = storage.LoadData.load_rental()
        self.bikes = [bikes.Bike.load_dict(row) for row in self.row_bikes]
        self.rents = [rental.Rentals.from_dict(row) for row in self.row_rents]

    
    def add_rent(self):
        rental_id = helpers.uniq_id(self.rents)
        customer_name = helpers.val_str("enter your name: ")
        b_id = helpers.if_in(self.bikes)
        if b_id != False:
            bike_id = b_id
        else:
            return "bike did not find"
        print("enter the start time")
        start_datetime = helpers.asc_time()  
        str_start_datetime = start_datetime.strftime("%Y-%m-%dT%H:%M")
        print("enter the end time")
        return_datetime = helpers.asc_time()
        expected_return_datetime = return_datetime.strftime("%Y-%m-%dT%H:%M")
        if start_datetime >= return_datetime:
            return "wrong time"
        if self.if_bike_avalable(bike_id, start_datetime, return_datetime) == False:
            return
        actual_return_datetime = None
        total_price = 0
        late_fee = 0
        status = "Active"

        new_rental = rental.Rentals(rental_id,customer_name, bike_id, str_start_datetime, 
        expected_return_datetime, actual_return_datetime, total_price, late_fee,status)
        self.rents.append(new_rental)
        to_load = new_rental.to_dict()
        self.row_rents.append(to_load)
        storage.LoadData.dump_rental(self.row_rents)
        return "order added"
 



    def if_bike_avalable(self, b_id ,start_d, return_d):
        for rent in self.rents:
            if rent.bike_id == b_id and rent.status == "Active":
                st =  datetime.datetime.strptime(rent.start_datetime,"%Y-%m-%dT%H:%M") 
                et = datetime.datetime.strptime(rent.expected_return_datetime,"%Y-%m-%dT%H:%M")  
                if start_d < et and return_d>st:
                    print("the bike not avalable")
                    return False
        return True
        
    def rent_by_id(self):
        r_id = helpers.val_str("enter the rent id: ")
        for rent in self.rents:
            if rent.id_rental == r_id:
                return rent.to_dict()
        return "rental id did not find"


    def scerch_by_client(self):
        name = helpers.val_str("enter the client name: ")
        history = []
        for rent in self.rents:
            if rent.customer_name == name:
                history.append(rent.to_dict())
        return history


    def all_active_orders(self):
        history = []
        for rent in self.rents:
            if rent.status == "Active":
                history.append(rent)
        return history


    def return_bike(self, rent_id):
        ...
        







class PriceCal:
    ...    