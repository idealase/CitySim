from service_classes import *
from suburbs import *
from grid_maker import *
import time


def set_diff():
    global money, diff_fac
    difficulty = input("How difficult do you want your game to be? Easy, medium or hard?").upper()
    if difficulty == "EASY":
        diff_fac = 1  # TODO: make this mean something
        money = 1000000
        print("You have chosen: " + difficulty + "\nYou have $" + str(money))
    elif difficulty == "MEDIUM":
        diff_fac = 2
        money = 500000
        print("You have chosen: " + difficulty + "\nYou have $" + str(money))
    elif difficulty == "HARD":
        diff_fac = 4
        money = 250000
        print("You have chosen: " + difficulty + "\nYou have $" + str(money))
    else:
        print("It already seems too hard for you...")
        set_diff()


def market_suburb():
    global money
    ad_spend = input("How much would you like to spend on marketing your new suburb?\n")
    tot_ads = int(int(ad_spend) / 1000)
    money -= int(ad_spend)
    i = 0
    for i in range(tot_ads):
        city_suburbs[-1].advertise()
        i += 1
    city_suburbs[-1].update_size()

def tot_pop():
    global tot_pop
    tot_pop = 0
    for s in city_suburbs:
        tot_pop += s.pop
    return tot_pop





mayor_name = input("What is your name?\n")
print("Welcome to your new city, Mayor " + mayor_name)

city_name = input("\nWhat would you like the city to be called?\n")
print("Ok, Mayor " + mayor_name + " behold...\n")
time.sleep(1)
print("The city of " + city_name + "\n\n")
time.sleep(1)


set_diff()

time.sleep(2)
print("\n\nLet's establish the first suburb of the city of " + city_name)

make_new_suburb()
time.sleep(2)

print("\nCongratulations, Mayor " + mayor_name + " your first suburb is...\n")
time.sleep(2)
see_city_suburbs()
time.sleep(2)
print("\nIt is empty of course...\n\nBut you can advertise your new suburb!\n")
print("For every $1000 spent on marketing, 50 people will move into the suburb")
time.sleep(1)

market_suburb()

print("Let's see how that worked...")
time.sleep(2)
see_city_suburbs()
time.sleep(1)
print("So now, " + str(city_suburbs[-1].pop) + " people live in " + city_suburbs[-1].name + "!!!\n")
time.sleep(1)
print("But now you only have $" + str(money) + " left to spend!\n")
time.sleep(2)
print("And " + str(city_suburbs[-1].name) + " now has a size of " + str(city_suburbs[-1].size) + "!!!")

time.sleep(2)
print("Total population of " + city_name + " is currently " + str(tot_pop()))

show_city_prompt()



print("The End!")


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