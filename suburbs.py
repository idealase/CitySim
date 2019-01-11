#
# suburbs.py - suburb methods
#

import random

suburb_names = ["Weablo", "Glemdor", "Quamlack", "Tistle", "Marlbornry", "Flantiline", "Tennerbro", "Gwizzly", "Howerton",
                "Norlop", "Streeves", "Bannawack", "Terrawom"]

city_suburbs = []
subs_loc_dict = {}
subs_size_dict = {}

class Suburb:
    def __init__(self, name, pop, wealth, size, coords):
        self.name = name
        self.pop = pop
        self.wealth = wealth
        self.size = size
        self.coords = coords

    def update_size(self):
        self.size = self.pop / 50
        subs_size_dict[self.name] = self.size

    def wealth_up(self):
        self.wealth += (self.wealth * 0.1)

    def wealth_down(self):
        self.wealth -= (self.wealth * 0.1)

    def advertise(self):
        self.pop += 50

    def grow_pop(self, rate):
        """Grows population at specified rate
        eg rate=0.1 is equal to 10% growth"""
        self.pop += (self.pop * rate)

    def shrink_pop(self, rate):
        """Shrinks population at specified rate
        eg rate=0.1 is equal to 10% shrinkage"""
        self.pop -= (self.pop * rate)


def make_new_suburb():
    """Generates a new empty suburb with ZERO wealth
    and ZERO population.
    Randomly selects name from suburb_names list and removes that name from list"""
    global new_suburb_name, new_sub
    
    # randomly choose suburb name from list
    new_suburb_name = random.choice(suburb_names)
    
    # remove that name from list
    suburb_names.remove(new_suburb_name)

    # determine new random coords for suburb
    new_coords = (random.randint(-5,5), random.randint(-5,5))
    
    # make new suburb object with that name
    new_sub = Suburb(new_suburb_name, 0, 0, 0, new_coords)
    city_suburbs.append(new_sub)
    subs_loc_dict[new_sub.name] = new_sub.coords
    subs_size_dict[new_sub.name] = new_sub.size


def see_city_suburbs():
    for s in city_suburbs:
        print(s.name, "Population: " + str(s.pop), "Wealth: " + str(s.wealth), "Size: " + str(s.size), "Location: " + str(s.coords), sep="...")


if __name__ == "__main__":
    print("main")
    make_new_suburb()
    print(new_sub.name, new_sub.pop, new_sub.wealth, new_sub.coords)