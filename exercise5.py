#Exercise 5
#Let's use functions to calculate your trip's costs:

#Define a function called hotel_cost with one argument nights as input. The hotel costs $140 per night.
#So, the function hotel_cost should return 140 * nights.
#Define a function called plane_ride_cost that takes a string, city, as input.
#The function should return a different price depending on the location, similar to the code example above.
#Below are the valid destinations and their corresponding round-trip prices.
#"Charlotte": 183
#"Tampa": 220
#"Pittsburgh": 222
#"Los Angeles": 475
#-Below your existing code, define a function called rental_car_cost with an argument called days.
#Calculate the cost of renting the car: Every day you rent the car costs $40.(cost=40*days)
#if you rent the car for 7 or more days, you get $50 off your total(cost-=50).
#Alternatively (elif), if you rent the car for 3 or more days, you get $20 off your total.
#You cannot get both of the above discounts. Return that cost. -Then, define a function called trip_cost that takes two arguments, city and days.
#Like the example above, have your function return the sum of calling the rental_car_cost(days), hotel_cost(days), and plane_ride_cost(city) functions.
#Modify your trip_cost function definion. Add a third argument, spending_money.
#Modify what the trip_cost function does. Add the variable `spending_money to the sum that it returns.

def hotel_cost(nights):
    return nights*140


def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    if city == "Tampa":
        return 220
    if city == "Pittsburgh":
        return 222
    if city == "Los Angeles":
        return 475
    else:
        return 0

def rental_car_cost(days):
    totalcost = 0
    cost = 40*days
    if days >= 7:
        totalcost = cost - 50
    elif days >= 3 and days < 7 :
        totalcost = cost - 20
    else:
        totalcost = cost
    return totalcost


def trip_cost(city, days,spending_money):
    total_trip_cost = hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money
    print("Hotel Cost: $ ", hotel_cost(days))
    print("Plane ride cost: $ ", plane_ride_cost(city))
    print("Rental Car Cost: $", rental_car_cost(days))
    print("Your Total Trip Cost: $", total_trip_cost)


city = input("Type the city you wanna go: Charlotte, Tampa, Pittsburgh, Los Angeles")
days = int(input("How many days are you going to spend(Only numbers)"))
spending_money = int(input("How much are you going to spend?"))

trip_cost(city,days,spending_money)












