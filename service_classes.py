# service_classes

rad_factor = 3

class Hospital:

    cost = 50000

    def __init__(self, name, suburb, doctors, patients, beds, ambulances):
        self.name = name
        self.suburb = suburb
        self.doctors = doctors
        self.patients = patients
        self.beds = beds
        self.ambulances = ambulances

    def capacity(self):
        capacity = self.beds - self.patients
        return capacity

    def OpRadius(self):
        opradius = (self.ambulances ** 0.5) * rad_factor
        return int(opradius)

class CopShop:

    cost = 25000

    def __init__(self, suburb, officers, prisoners, cells, cars):
        self.suburb = suburb
        self.officers = officers
        self.prisoners = prisoners
        self.cells = cells
        self.cars = cars

    def OpRadius(self):
        opradius = (self.cars ** 0.5) * rad_factor
        return int(opradius)

class FireStation:

    cost = 25000

    def __init__(self, suburb, firies, trucks):
        self.suburb = suburb
        self.firies = firies
        self.trucks = trucks

    def OpRadius(self):
        opradius = (self.trucks ** 0.5) * rad_factor
        return int(opradius)

class RubbishTip:

    cost = 10000

    def __init__(self, suburb, garbos, trucks):
        self.suburb = suburb
        self.garbos = garbos
        self.trucks = trucks

    def OpRadius(self):
        opradius = (self.trucks ** 0.5) * rad_factor
        return int(opradius)




def main():
    print("main")
    h2 = Hospital("Maks", "howerton", 5, 20, 25, 3)
    print(h2.ambulances)

if __name__ == "__main__":
    main()
