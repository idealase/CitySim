#
# suburbs.py - suburb methods
#

import random
import pandas as pd

# list of made up names to draw from when making new suburbs
suburb_names = ["Weablo", "Glemdor", "Quamlack", "Tistle", "Marlbornry", "Flantiline", "Tennerbro", "Gwizzly", "Howerton",
                "Norlop", "Streeves", "Bannawack", "Terrawom", "Glable", "Karenton", "Glebulp", "Nennafet", "Seeply"]

# init lists/dicts for suburb features
city_suburbs = []
full_suburbs = []
subs_loc_dict = {}
subs_size_dict = {}

suburbs_df = pd.DataFrame()

# suburb growth params
# TODO: make growth_fac a suburb feature
growth_fac = 0.3  # set between 0 and 1
expand_limit = 20  # size at which suburb stops expanding and makes new suburb

class Suburb:
    def __init__(self, name, pop, wealth, size, coords):
        self.name = name
        self.pop = pop
        self.wealth = wealth
        self.size = size
        self.coords = coords

    def update_size(self):
        self.size = self.pop / 100
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
        self.pop += int((self.pop * rate))

    def shrink_pop(self, rate):
        """Shrinks population at specified rate
        eg rate=0.1 is equal to 10% shrinkage"""
        self.pop -= (self.pop * rate)

    def insert_to_df(self):
        sub_name_pop = str(self.name) + ' Pop.'
        suburbs_df.insert(0, sub_name_pop, self.pop)

        sub_name_size = str(self.name) + ' Size.'
        suburbs_df.insert(1, sub_name_size, self.size)

        sub_name_wealth = str(self.name) + ' Wealth.'
        suburbs_df.insert(2, sub_name_wealth, self.wealth)

    def append_to_df(self):
        # TODO: Fix this. doesnt work
        sub_name_pop = str(self.name) + ' Pop.'
        suburbs_df.append(sub_name_pop, self.pop)

        sub_name_size = str(self.name) + ' Size.'
        suburbs_df.append(sub_name_size, self.size)

        sub_name_wealth = str(self.name) + ' Wealth.'
        suburbs_df.append(sub_name_wealth, self.wealth)


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
    new_coords = (random.randint(-2,2), random.randint(-2,2))
    
    # make new suburb object with that name
    new_sub = Suburb(new_suburb_name, 0, 0, 0, new_coords)
    
    # TODO: Create new pd df for new suburb
    new_sub.insert_to_df()
    
    city_suburbs.append(new_sub)
    subs_loc_dict[new_sub.name] = new_sub.coords
    subs_size_dict[new_sub.name] = new_sub.size


def gen_new_coords(adj_to):
    """
    takes adj_to arg, which is the suburb the new one will grow next to
    """
    global new_coords
    movements = [1,-1,2,-2,0]  # list of possible movement directions
    adj_sub_movementx = random.choice(movements)
    adj_sub_movementy = random.choice(movements)
    # determine new adjacent coords for suburb
    new_coords = (adj_to.coords)[0] + adj_sub_movementx, (adj_to.coords)[1] + adj_sub_movementy
    
    # prevent suburbs forming beyond grid
    if -5 > new_coords[0] > 5 or -5 > new_coords[1] > 5:
        gen_new_coords(adj_to)
    
    # prevent suburbs forming atop existing suburbs
    for s in city_suburbs:
        if s.coords == new_coords:
            gen_new_coords(adj_to)
        else:
            continue


def make_adj_suburb(adj_to):
    """Generates a new empty suburb with ZERO wealth
    and INITIAL population 25-100.
    Randomly selects name from suburb_names list and removes that name from list
    Puts suburb next to most recent suburb
    
    PROBLEM: Suburbs beging to extend beyond the initial grid"""
    global new_suburb_name, new_sub, new_coords

    # randomly choose suburb name from list
    try:
        new_suburb_name = random.choice(suburb_names)
    except IndexError:
        print("...the populace are out of names for new suburbs...")
        
    # remove that name from list
    suburb_names.remove(new_suburb_name)

    gen_new_coords(adj_to)

    rand_init_pop = random.randint(25, 100)

    # make new suburb object with that name
    new_sub = Suburb(new_suburb_name, rand_init_pop, 0, 0, new_coords)
    # TODO: Create new pd df for new adjacent suburb

    city_suburbs.append(new_sub)
    subs_loc_dict[new_sub.name] = new_sub.coords
    subs_size_dict[new_sub.name] = new_sub.size


def expand_suburbs():
    """Makes suburbs expand proportional to global growth factor
    
    When suburb reaches expand_limit it stops expanding and
    a new suburb is generated nearby
    """
    print("\nCity Suburb Summary:")
    for s in city_suburbs:
        print(s.name, "\tPopulation: " + str(s.pop), sep="...")
        # TODO: Store all suburb features in pandas SUBURBS DATAFRAMES at this point

    for s in city_suburbs:
        if s.size < expand_limit:
            s.grow_pop(rate=growth_fac)
            s.update_size()
        elif (s.size >= expand_limit) and s not in full_suburbs:
            make_adj_suburb(s)
            full_suburbs.append(s)


def see_city_suburbs():
    """
    prints full stats of all suburbs

    used mostly for early testing
    """
    for s in city_suburbs:
        print(s.name, "Population: " + str(s.pop), "Wealth: " + str(s.wealth), "Size: " + str(s.size), "Location: " + str(s.coords), sep="...")


if __name__ == "__main__":
    print("main")
    make_new_suburb()
    print(new_sub.name, new_sub.pop, new_sub.wealth, new_sub.coords)
    new_sub.pop = 5
    print(suburbs_df.head(5))

    for i in range(50):
        expand_suburbs()
    print(suburbs_df.head(5))