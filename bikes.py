class Bike:
    def __init__(self, bike_id ,model, bike_type ,price_hourly ,price_daily ,available_is ,operational_is):
        self.bike_id = bike_id
        self.model = model
        self.bike_type = bike_type
        self.price_hourly =price_hourly
        self.price_daily = price_daily 
        self.available_is = available_is 
        self.operational_is = operational_is

    def available(self):
        self.available_is = True
    def unavalable(self):
        self.available_is = False    

    def operational(self):
        self.operational_is = True
    def unoperational(self):
        self.operational_is = False

    def to_dict(self):
        bike_dikt = {
        "bike_id" : self.bike_id,
        "model" : self.model,
        "bike_type" : self.bike_type,
        "hourly_price" : self.price_hourly,
        "daily_price" : self.price_daily,
        "is_available" : self.available_is, 
        "is_operational" : self.operational_is
        }

    @classmethod
    def load_dict(cls, dict):
        return Bike(dict["bike_id"], dict["model"],
        dict["bike_type"],dict["hourly_price"],dict["daily_price"],
        dict["is_available"], dict["is_operational"])

