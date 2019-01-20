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
        
Running suburbs.py and its main() will produce dataframes AND plots now. 
These features are yet to be added to city.py
    
Running grid_maker.py will check grid functionality, but all suburbs on grid will have size:0
    
#### MODULES:
+ city.py - the mostly text driven script to put it all together.

    Really pretty uninteresting thus far, with no meaningful user options
    
    I'm currently having more fun playing with the growth parameters in the suburbs module
    
+ suburbs.py - contains methods and data for suburbs class.

    performs the expand suburb function - the bulk of the work
    
    records suburb attributes to pandas dataframe each iteration (day)
    
    produces plots of population, wealth, density and growth factor, which are useful for adapting parameters

+ grid_maker.py - makes a 10x10 numpy meshgrid and performs plotting of suburbs.

    refers to dictionaries in suburbs.py for size, density and coords
    
    the "for k, (v1, v2) in dict.items():" loop cost me an afternoon 

+ service_classes.py - this is where I began, just revising classes, with some basic city services like police and fire.

    currently still unused
    
    not sure how to incorporate these objects into each suburb so they meaningfully alter parameters

#### Example Plot of City:
    
![image](https://user-images.githubusercontent.com/24471071/51438974-e51b3500-1cb3-11e9-854c-81ad1ae33688.PNG)

#### Example Info Plot:

![image](https://user-images.githubusercontent.com/24471071/51438968-c7e66680-1cb3-11e9-8231-ae4cec70f6be.PNG)




#### TODO:
1. The coverage of services, suburb density and the level of wealth determines happiness levels
happiness levels determine growth factor

2. GrowthFactor needs positive modifiers to counter density effect


