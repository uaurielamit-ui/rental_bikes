import json

class LoadData:
    def load_bike():
        with open ("bikes.json", "r") as file:
            data = json.load(file)
            return data

    def load_rental():
        with open ("rentals.json", "r") as file:
            data = json.load(file)
            return data

    def dump_bike(data):
        with open ("bikes.json", "w" , encoding="utf-8") as file:
            json.dump(data , file , indent = 2, ensure_ascii=False)

    def dump_rental(data):
        with open ("rentals.json", "w" , encoding="utf-8") as file:
            json.dump(data , file , indent = 2, ensure_ascii=False)