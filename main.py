import maneg
import helpers
import rental
import bikes_m

def main():
    to_exit = False
    while not to_exit:
        client_choice = input("""
        ========================
              Rental bikes
        ========================
        0.exit
        1.bikes managment
        2.rentals managment
        """)
        if client_choice == "0":
            to_exit = True
        if client_choice =="1":
            main_bike()
        elif client_choice == "2":
            main_rent()



def main_bike():
    b = bikes_m.BikeManeger()
    to_exit = False
    while not to_exit:
        client_choice = input("""
        ========================
              bikes maneger
        ========================
        0.exit
        1.show all bike
        2.scerch by id
        3.show avalable bikes
        4.add new bike
        5.change bike ditels
        6.to unoprtional bike
        """)
        if client_choice == "0":
            to_exit = True
        elif client_choice == "1":
            b.show_all_bikes()
        elif client_choice == "2":
            print (b.scerch_by_id())
        elif client_choice == "3":
            b.show_avalable()
        elif client_choice =="4":
            print(b.add_new_bike())
        elif client_choice == "5":
            print(b.up_bike())
        elif client_choice == "6":
            print(b.bike_bruak())











def main_rent():
    
    price = None
    m = maneg.RentalManager(price)
    to_exit = False
    while not to_exit:
        client_choice = input("""
        ========================
            Rental manegment
        ========================
        0.exit
        1.add new order
        2.if bike avalable
        3.fund rental by id
        4.all client orders
        5.all active rents
        6.return bike

        """)
        if client_choice == "0":
            to_exit = True
        if client_choice == "1":
            print(m.add_rent())
        if client_choice == "2":
            print(m.if_bike_avalable())
        if client_choice =="3":
            print(m.rent_by_id())
        if client_choice == "4":
            print(m.scerch_by_client())
        if client_choice == "5":
            active = m.all_active_orders()
            print ([rent.to_dict() for rent in active])











if __name__ == ("__main__"):
    main()