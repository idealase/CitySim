#
# city.py - runs the city sim
#

from service_classes import *
from suburbs import *
from grid_maker import *
import time, sys

# TODO: global parameter specifications


def set_diff():
    """
    Gives user a choice of easy, medium or hard difficulty.
    Adjusts available funds accordingly

    Sets a difficulty factor, diff_fac, to be used in later calculations.
    """
    global money, diff_fac
    difficulty = input("How difficult do you want your game to be? Easy, medium or hard?").upper()
    if difficulty == "EASY" or "E":
        diff_fac = 1  # TODO: make this mean something
        money = 1000000
        print("You have chosen: " + difficulty + "\nYou have $" + str(money))
    elif difficulty == "MEDIUM" or "M":
        diff_fac = 2
        money = 500000
        print("You have chosen: " + difficulty + "\nYou have $" + str(money))
    elif difficulty == "HARD" or "H":
        diff_fac = 4
        money = 250000
        print("You have chosen: " + difficulty + "\nYou have $" + str(money))
    else:
        print("It already seems too hard for you...")
        set_diff()


def market_suburb():
    """
    Grants the user the option to spend some money to inject some population into
    their NEWEST suburb -- city_suburbs[-1]
    """
    global money
    ad_spend = input("How much would you like to spend on marketing your new suburb?\n")
    try:
        tot_ads = int(int(ad_spend) / 1000)
        money -= int(ad_spend)
        i = 0
        for i in range(tot_ads):
            city_suburbs[-1].advertise()
            i += 1
        city_suburbs[-1].update_size()
    except ValueError:
        print("Please enter a dollar amount with numbers, eg 1000, 2000")
        market_suburb()
    
    
def tot_pop():
    """
    Returns the total population of city
    """
    global tot_pop
    tot_pop = 0
    for s in city_suburbs:
        tot_pop += s.pop
    return tot_pop


mayor_name = input("What is your name?\n")
print("Welcome to your new city, Mayor " + mayor_name)
city_name = input("\nWhat would you like the city to be called?\n")

waste_time = False
welcome_msg = str("\n\nOk, Mayor " + mayor_name + ". Behold...\n   \n" + "***The City of " + city_name + "***\n\n")
if waste_time:
    for char in welcome_msg:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
else:
    print(welcome_msg)

set_diff()

print("\n\nLet's establish the first suburb of the city of " + city_name)
make_new_suburb()
print("\nCongratulations, Mayor " + mayor_name + " your first suburb is...\n")
see_city_suburbs()
print("\nIt is empty of course...\n\nBut you can advertise your new suburb!\n")
print("For every $1000 spent on marketing, 50 people will move into the suburb")

market_suburb()
print("\nLet's see how that worked...\n")

see_city_suburbs()

print("\nSo now, " + str(city_suburbs[-1].pop) + " people live in " + city_suburbs[-1].name + "!!!\n")
print("But now you only have $" + str(money) + " left to spend!\n")
print("And " + str(city_suburbs[-1].name) + " now has a size of " + str(city_suburbs[-1].size) + "!!!")
print("\nTotal population of " + city_name + " is currently " + str(tot_pop()))

show_city_prompt()

def run_city():
    """
    Prompts user to input number of days to run city
    
    Performs expand_suburbs() method from suburbs.py for i=days
    
    Calls show_city_prompt() from grid_maker.py to check if user wants
    to see city
    """

    run_days = 1  # default
    # take user input to set how many days the city will run for
    run_days = int(input("How many days should we run the city for..?"))

    # for as many days as run_days, run the expand suburbs function
    try:
        for i in range(run_days):
            expand_suburbs()
    except OverflowError:
        print("Whoa slow down. OvErFloW")
        run_city()

    show_city_prompt()



run_city()

# TODO: check if this is the right spot to declare this
def keep_going():
    global tot_pop
    cont_status = input("\nWould you like to keep going? y/n?")
    if cont_status.upper() == 'Y':
        run_city()
        keep_going()
    elif cont_status.upper() == 'N':
        try:
            print("Total population of " + city_name + " reached " + str(tot_pop()))
        except TypeError:
            pass  #TODO: not do this
        plotinfo(city_name)
        print("\nThe End!")
    else:
        plotinfo(city_name)
        print("\nThe End!")


keep_going()

# TODO: how to build new buildings?
"""
h1 = Hospital("Maks", "Howerton", 5, 20, 25, 3)
p1 = CopShop("Howerton", 10, 2, 5, 4)
f1 = FireStation("Howerton", 8, 2)
r1 = RubbishTip("Howerton", 30, 1)

s_buildings = [h1, p1, f1, r1]

for b in s_buildings:
    print(b.suburb, b.OpRadius())
"""