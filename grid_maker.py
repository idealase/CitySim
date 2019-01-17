#
# grid_maker.py - makes meshgrid and plots suburb locations on it
#

import numpy as np
import matplotlib.pyplot as plt
import time
from suburbs import *


def gen_grid():
    """Generates xx and yy for 10x10 grid on which suburbs are plotted"""
    global xx, yy
    x_values = np.arange(-5, 6, 1)
    y_values = np.arange(-5, 6, 1)
    xx, yy = np.meshgrid(x_values, y_values)


def show_city():
    """Generates 10x10 grid and plots suburbs at their coords w/ name"""
    gen_grid()
    # plot grid and suburbs
    plt.figure(figsize=(10, 10))
    plt.plot(xx, yy, marker='.', color='k', linestyle='none')  # the mesh grid

    for k, (v1, v2) in subs_loc_dict.items():
        sub_radius = 100 * subs_size_dict[k]
        plt.scatter(v1, v2, s=sub_radius, marker='o', alpha=subs_dens_dict[k])  # the suburb TODO: relate alpha suburb density
        plt.annotate(k, xy=(v1, v2))  # adds suburb name as label

    plt.show()


def show_city_prompt():
    "Give user the option to see the plot. Calls show_city()"
    answer = input("\nWould you like to view your city? y/n?")
    if answer.upper() == 'Y':
        print("OK, here it is...\n")
        time.sleep(1)
        show_city()
    else:
        print("OK then...")


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
