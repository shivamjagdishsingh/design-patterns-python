class Building:
    def __init__(self):
        self.floors = None
        self.roof_type = None
        self.carpet_area = None

    def set_floor(self, floor):
        self.floors = floor
        return self

    def set_roof_type(self, roof_type):
        self.roof_type = roof_type
        return self

    def set_carpet_area(self, carpet_area):
        self.carpet_area = carpet_area
        return self

    def show_details(self):
        print("Floors:", self.floors)
        print("Roof type:", self.roof_type)
        print("Carpet area:", self.carpet_area)


class Architect:
    def __init__(self, building: Building):
        self.building = building

    def bunglow(self):
        return self.building.set_floor(2).set_carpet_area(4500).set_roof_type("pyramid")

    def flat(self):
        return self.building.set_floor(20).set_carpet_area(20000).set_roof_type("shed")

    def duplex(self):
        return self.building.set_floor(2).set_carpet_area(3000).set_roof_type("flat")


building = Building()
architect = Architect(building)

bunglow = architect.bunglow()
bunglow.show_details()

flat = architect.flat()
flat.show_details()

duplex = architect.duplex()
duplex.show_details()
