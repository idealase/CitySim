# CitySim
## Toy parametric city simulator for practicing classes, modules, PEP 8 and version control

### MODULES:
+ city.py - the mostly text driven script to put it all together.
    
+ suburbs.py - contains methods and data for suburbs class.
    performs the expand suburb function - the bulk of the work
    records suburb attributes to pandas dataframe each iteration (day)

+ grid_maker.py - makes a 10x10 numpy meshgrid and performs plotting of suburbs.
    refers to dictionaries in suburbs.py for size, density and coords

+ service_classes.py - this is where I began, just revising classes, with some basic city services like police and fire.
    currently still unused


![image](https://user-images.githubusercontent.com/24471071/51315742-2f51ab80-1a53-11e9-9cb0-c72499380215.png)

### TODO:
1. The coverage of services, suburb density and the level of wealth determines happiness levels

    happiness levels determine growth factor

