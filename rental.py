class Rentals:
    def __init__(self, id_rental ,customer_name ,bike_id ,datetime_start ,expected_return_datetime ,datetime_return_actual ,price_total ,fee_late ,status):
        self. id_rental = id_rental
        self.customer_name =customer_name
        self.bike_id = bike_id
        self.datetime_start = datetime_start
        self.expected_return_datetime = expected_return_datetime
        self.datetime_return_actual = datetime_return_actual
        self.price_total = price_total
        self.fee_late = fee_late
        self.status = status

    # def status_active(self):
    #     self.status = "active"
    # def status_complit (self):
    #     self.status = "Completed"


    def complete_rental(self,return_datetime,late_fee):
        self.datetime_return_actual = return_datetime
        self.fee_late = late_fee

    def to_dict (self):
        return {
            "rental_id": self.id_rental ,
            "customer_name" : self.customer_name ,
            "bike_id" : self.bike_id ,
            "start_datetime" : self.datetime_start ,
            "expected_return_datetime" : self.expected_return_datetime ,
            "actual_return_datetime" : self.datetime_return_actual ,
            "total_price" : self.price_total ,
            "late_fee" : self.fee_late ,
            "status" :self.status
        }

    @classmethod
    def from_dict(cls, ren_dict):
        return Rentals(ren_dict["rental_id"] ,ren_dict["customer_name"] ,
        ren_dict["bike_id"] ,ren_dict["start_datetime"] ,ren_dict["expected_return_datetime"] ,
        ren_dict["actual_return_datetime"] ,ren_dict["total_price"] ,ren_dict["late_fee"] ,ren_dict["status"])
