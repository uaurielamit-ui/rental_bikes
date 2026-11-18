from datetime import *
def val_int(text):
    legal = False
    while not legal:
        try:
            client_choice = int(input(text))
            if client_choice >0:
                legal = True
        except ValueError:
            print("only positiv numbers ")
    return client_choice

def val_str(text):
    legal = False
    while not legal:
        client_choice = input(text).strip()
        if client_choice != "":
            legal = True
        else:
            print("enter a text")
    return client_choice

def uniq_id(rents):
    max_rent = 0
    try:
        for r in rents:
            if int(r.id_rental [1:])>= max_rent:
                max_rent = int(r.id_rental [1:])+1
    except ValueError:
        return ValueError
    return "R"+ str(max_rent).zfill(3)

def if_in(bikes):
    choose_bike = val_str("enter the bike id: ")
    for b in bikes:
        if b.bike_id == choose_bike and b.available_is and b.operational_is:
            return choose_bike
    return False


def asc_time():
    get_date = val_str("enter the date end time like this  YYYY-mm-ddT%H:%M")
    try:
        result = datetime.strptime(get_date,"%Y-%m-%dT%H:%M")
        return result
    except ValueError:
        print ("wrong input")
        return False

# def if_avlable(bikes, b_id):
#     for b in bikes:
#         if b.id_bike == b_id:
#             if b.available_is == True and b.operational_is == True:
#                 return True
