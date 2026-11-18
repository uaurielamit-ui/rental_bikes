class Bike:
    def __init__(self, bike_id ,model, bike_type ,price_hourly ,price_daily ,is_available ,is_operational):
        self.bike_id = bike_id
        self.model = model
        self.bike_type = bike_type
        self.price_hourly =price_hourly
        self.price_daily = price_daily 
        self.is_available = is_available 
        self.is_operational = is_operational

    def available(self):
        self.is_available = True
    def unavalable(self):
        self.is_available = False    

    def operational(self):
        self.is_operational = True
    def unoperational(self):
        self.is_operational = False

    def to_dict(self):
        return {
        "bike_id" : self.bike_id,
        "model" : self.model,
        "bike_type" : self.bike_type,
        "hourly_price" : self.price_hourly,
        "daily_price" : self.price_daily,
        "is_available" : self.is_available, 
        "is_operational" : self.is_operational
        }

    @classmethod
    def load_dict(cls, dict):
        return Bike(dict["bike_id"], dict["model"],
        dict["bike_type"],dict["hourly_price"],dict["daily_price"],
        dict["is_available"], dict["is_operational"])

