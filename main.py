import maneg
import helpers
import rental

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
    to_exit = False
    while not to_exit:
        client_choice = input("""
        ========================
              bikes maneger
        ========================
        0.exit

        """)
        if client_choice == "0":
            to_exit = True











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