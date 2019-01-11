#
# grid_maker.py - makes meshgrid and plots suburb locations on it
#

import numpy as np
import matplotlib.pyplot as plt
import time
from suburbs import *


def gen_grid():
    global xx, yy
    xvalues = np.arange(-5,6,1)
    yvalues = np.arange(-5,6,1)
    xx, yy = np.meshgrid(xvalues, yvalues)


def show_city():
    gen_grid()
    # plot grid and suburbs
    plt.figure(figsize=(10,10))
    plt.plot(xx, yy, marker='.', color='k', linestyle='none')  # the mesh grid

    for k, (v1, v2) in subs_loc_dict.items():
        sub_radius = 100 * subs_size_dict[k]
        plt.scatter(v1, v2, s = sub_radius, marker = 'o')  # the suburb
        plt.annotate(k, xy= (v1,v2))  # adds suburb name as label

    plt.show()


def show_city_prompt():
    answer = input("Would you like to view your city? y/n?")
    if answer.upper() == 'Y':
        print("OK, here it is...")
        time.sleep(1)
        show_city()
    else:
        print("OK then")


def main():
    make_new_suburb()
    make_new_suburb()
    make_new_suburb()
    print(city_suburbs)
    print(subs_loc_dict)
    print(subs_size_dict)
    see_city_suburbs()
    show_city()

if __name__ == "__main__":
    main()