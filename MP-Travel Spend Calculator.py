def hotel_costs(days):
    nights = days -1
    nights = nights * 140
    print("Hotel costs:",nights)

def plane_ride_cost(city):
    if city == "Charolette":
        print("plnae cost 183")
    elif city == "Tampa":
        print("plane cost 220")
    elif city == "Pittsburgh":
        print("plane cost 222")
    elif city == "Los Angeles":
        print("plane cost 475")

def rental_car_cost(days):
    if days >= 7:
       days = (days * 40)-50
    elif days >=3 and days <7:
        days = (days*40)-20
    else:
        days= (days*40)
    print ("The car costs", days)

def total_trip_cost(city, days):
    return hotel_costs(days), plane_ride_cost(city),rental_car_cost(days)


total_trip_cost(city = input("What city are you going to?(Charolette, Tampa, Pittsburgh, Los Angeles)"), days = (int(input("How many days are you going"))))
