# CitySim
### Toy parametric city simulator for practicing classes, modules, PEP 8 and version control

#### Developed with:
+ Python 3.7
+ The scipy packages pandas, numpy and matplotlib

### Running CitySim:

RUN city.py for basic functionality
    
You will be prompted for your name and the city's name
The difficulty prompt is currently pointless, so you can select 'hard'
When prompted for days to run city, 30 days is a nice amount (not 50000, Karen)
        
Running suburbs.py and its main() will produce some data frames but no plots
    
Running grid_maker.py will check grid functionality, but all suburbs on grid will have size:0
    
#### MODULES:
+ city.py - the mostly text driven script to put it all together.
    
+ suburbs.py - contains methods and data for suburbs class.
    performs the expand suburb function - the bulk of the work
    records suburb attributes to pandas dataframe each iteration (day)

+ grid_maker.py - makes a 10x10 numpy meshgrid and performs plotting of suburbs.
    refers to dictionaries in suburbs.py for size, density and coords

+ service_classes.py - this is where I began, just revising classes, with some basic city services like police and fire.
    currently still unused

#### Example Plot:
    
NB: Suburb density not mapped to alpha in this example
    
![image](https://user-images.githubusercontent.com/24471071/51315742-2f51ab80-1a53-11e9-9cb0-c72499380215.png)

#### TODO:
1. The coverage of services, suburb density and the level of wealth determines happiness levels
happiness levels determine growth factor

2. GrowthFactor needs positive modifiers to counter density effect


