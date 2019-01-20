#
# suburbs.py - suburb methods
#

import random
import pandas as pd
import matplotlib.pyplot as plt

# list of made up names to draw from when making new suburbs
# I try and add one every now and then
suburb_names = ["Weablo", "Glemdor", "Quamlack", "Tistle", "Marlbornry", "Flantiline", "Tennerbro", "Gwizzly", "Howerton",
                "Norlop", "Streeves", "Bannawack", "Terrawom", "Glable", "Karenton", "Glebulp", "Nennafet", "Seeply", "Lamaton", "Woorap"]

# init lists/dicts for suburb features
city_suburbs = []
full_suburbs = []
subs_loc_dict = {}
subs_size_dict = {}
subs_dens_dict = {}

current_day = 0


city_df = pd.read_csv('City_Records_Template.csv')
city_df.set_index('Day', drop=True, inplace=True)

# suburb growth params
growth_fac = 0.2  # set between 0 and 1
expand_limit = 20  # size at which suburb stops expanding and makes new suburb
density_thresh = 0.51

base_wealth = 2
wealth_growf = 0.01

class Suburb:
    def __init__(self, name, pop, wealth, size, density, coords, growf):
        self.name = name
        self.pop = pop
        self.wealth = wealth
        self.size = size
        self.density = density
        self.coords = coords
        self.growf = growf

    def update_size(self):
        self.size = self.pop / 100
        subs_size_dict[self.name] = self.size

    def update_density(self):
        self.density = min((self.pop / (expand_limit * 300)), 1) 
        subs_dens_dict[self.name] = self.density

    def update_growf(self):
        if self.density > density_thresh:
            dens_mod = ((self.density * 2) ** 4) / 1000
            self.growf -= dens_mod
        #wealth_mod = (self.wealth / 100)
        #self.growf += wealth_mod  #FIXME this line is breaking python

    def update_wealth(self):
        self.wealth += (self.wealth * wealth_growf)

    def advertise(self):
        "Initialises suburb population when in city.py"
        self.pop += 50

    def grow_pop(self):
        """Grows population according to suburb growth factor"""
        self.pop = int((self.pop * (1 + self.growf)))

    def full_grow_pop(self):
        """A slowed growth rate for full suburbs - grows pop. according to suburb growth factor w/ penalty"""
        self.pop = int((self.pop * (0.8 + self.growf)))



def make_new_suburb():
    """Generates a new empty suburb with TEN wealth and ZERO population.
    Randomly selects name from suburb_names list and removes that name from list"""
    global new_suburb_name, new_sub
    
    new_suburb_name = random.choice(suburb_names)
    suburb_names.remove(new_suburb_name)

    # determine new random coords for suburb
    new_coords = (random.randint(-2,2), random.randint(-2,2))
    
    # make new suburb object with that name
    new_sub = Suburb(new_suburb_name, 0, base_wealth, 0, 0.1, new_coords, growth_fac)
    city_suburbs.append(new_sub)
    subs_loc_dict[new_sub.name] = new_sub.coords
    subs_size_dict[new_sub.name] = new_sub.size
    subs_dens_dict[new_sub.name] = new_sub.density

    # replacing template column names with those of new suburb
    city_df.rename(index=str, columns={"Sub1 Pop": str(new_sub.name) + " Pop.", "Sub1 Wealth": str(new_sub.name) + " Wealth", \
    "Sub1 Size": str(new_sub.name) + " Size", "Sub1 Density": str(new_sub.name) + " Density", \
    "Sub1 GrowthFac": str(new_sub.name) + " GrowthFac"}, inplace=True)


def gen_new_coords(adj_to):
    """Generates the coordinates of the new suburb
    Moves both x and y randomly either (-2,-1,0,1,2) places

    Performs two checks:
        one to make coords unique
        one to restrict to 10x10

    Keyword arguments:
    adj_to -- the <suburb> the new one will be adjacent to
    """
    global new_coords
    movements = [1,-1,2,-2,0]  # list of possible movement directions
    adj_sub_movementx = random.choice(movements)
    adj_sub_movementy = random.choice(movements)
    # determine new adjacent coords for suburb
    new_coords = (adj_to.coords)[0] + adj_sub_movementx, (adj_to.coords)[1] + adj_sub_movementy
    
    # restrict to 10x10
    # FIXME: possibly not working in all cases
    if -5 > new_coords[0] > 5 or -5 > new_coords[1] > 5:
        gen_new_coords(adj_to)
    
    # prevent suburbs forming atop existing suburbs
    for s in city_suburbs:
        if s.coords == new_coords:
            gen_new_coords(adj_to)
        else:
            continue


def make_adj_suburb(adj_to):
    """Generates a new empty suburb adjacent to full one. 
    With TEN wealth and random INITIAL population 25-100.
    Randomly selects name from suburb_names list and removes that name from list
    Puts suburb next to most recent suburb with gen_new_coords() func.
    
    Keyword arguments:
    adj_to -- the <suburb> the new one will be adjacent to
        passed to gen_new_coords(adj_to)
    """
    global new_suburb_name, new_sub, new_coords

    # randomly choose suburb name from list
    try:
        new_suburb_name = random.choice(suburb_names)
    except IndexError:
        print("...the populace are out of names for new suburbs...")

    suburb_names.remove(new_suburb_name)
    gen_new_coords(adj_to)  # passes own adj_to arg to gen_new_coords(adj_to)
    rand_init_pop = random.randint(25, 100)

    new_sub = Suburb(new_suburb_name, rand_init_pop, base_wealth, 0, 0.2, new_coords, growth_fac)
    city_suburbs.append(new_sub)
    subs_loc_dict[new_sub.name] = new_sub.coords
    subs_size_dict[new_sub.name] = new_sub.size
    subs_dens_dict[new_sub.name] = new_sub.density

    # assiging new cols to city_df for new suburb
    new_cols = [" Pop.", " Wealth", " Size", " Density", " GrowthFac"]
    for col in new_cols:
        city_df[str(new_sub.name) + col] = ""
   

def expand_suburbs():
    """Makes suburbs expand proportional to global growth factor
    
    When suburb reaches expand_limit it stops expanding and
    a new suburb is generated nearby
    """
    global current_day
    current_day +=1
    
    # FIXME: this isn't working... related to no. iterations????
    for s in city_suburbs:
        cols_dict = {s.pop: " Pop.", s.wealth: " Wealth", s.size: " Size", s.density: " Density", s.growf: " GrowthFac"}
        for k,v in cols_dict.items():
            city_df.loc[str(current_day), (str(s.name) + str(v))] = k

    for s in city_suburbs:
        if s.size < expand_limit:
            s.grow_pop()
            s.update_size()
            s.update_density()
            s.update_growf()
            s.update_wealth()
        elif (s.size >= expand_limit) and s not in full_suburbs:
            make_adj_suburb(s)
            full_suburbs.append(s)

    for s in full_suburbs:
        s.full_grow_pop()
        s.update_size()
        s.update_density()
        s.update_growf()
        s.update_wealth()


def see_city_suburbs():
    """Prints full stats of all suburbs; used mostly for early testing"""
    for s in city_suburbs:
        print(s.name, "Population: " + str(s.pop), "Wealth: " + str(s.wealth), "Size: " + str(s.size), "Location: " + str(s.coords), sep="...")




def plotinfo(title):
    # Dataframe manipulation
    city_df.replace("", 0, inplace=True)
    pops_df = city_df.filter(regex='Pop')
    density_df = city_df.filter(regex='Density')
    growf_df = city_df.filter(regex='Grow')
    wealth_df = city_df.filter(regex='Wealth')

    plt.figure(1, figsize=(10,10))
    fig, axes = plt.subplots(nrows=2, ncols=2, num=1)
    fig.suptitle(str(title) + ' Suburb History', fontsize=16)
    pops_df.plot(ax=axes[0,0])
    growf_df.plot(ax=axes[0,1])
    wealth_df.plot(ax=axes[1,0])
    density_df.plot(ax=axes[1,1])
    plt.show()


if __name__ == "__main__":
    print("main\n Testing dfs")
    make_new_suburb()
    print(new_sub.name, new_sub.pop, new_sub.wealth, new_sub.coords)
    new_sub.pop = 10
    print(city_df.head(5))

    for i in range(55):  # the value chosen here has unexpected effects on df performance???
        expand_suburbs()

    print("City ran for " + str(current_day) + " days")
    print(subs_dens_dict)
    print(city_df.head(5))
    print(city_df.tail(5))
    print(city_df.iloc[49])
