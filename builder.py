# Builder Design Pattern #

# The Bad Code

class House:
    def __init__ (self, bedrooms, bathrooms, kitchen, garden, garage, pool, solar_panels, smart_home):
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.kitchen = kitchen
        self.garden = garden
        self.garage = garage
        self.pool = pool
        self.solar_panels = solar_panels
        self.smart_home = smart_home


    def __str__(self):
        features = [
            f"Bedrooms : {self.bedrooms}",
            f"Bathrooms : {self.bathrooms}",
            f"Kitchen : {'Yes' if self.kitchen else 'No'}",
            f"Garden : {'Yes' if self.garden else 'No'}",
            f"Garage : {'Yes' if self.garage else 'No'}",
            f"Pool : {'Yes' if self.pool else 'No'}",
            f"Solar Panels : {'Yes' if self.solar_panels else 'No'}",
            f"Smart Home : {'Yes' if self.smart_home else 'No'}",

        ]
        return " | ".join(features)

# Creating a house
house = House(3, 2, True, False, False, True, False, False)
print(house)



# This is liitle incovenient #

# The better Code #
class House:
    def __init__ (self, bedrooms, bathrooms, kitchen, garden, garage, pool, solar_panels, smart_home):
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.kitchen = kitchen
        self.garden = garden
        self.garage = garage
        self.pool = pool
        self.solar_panels = solar_panels
        self.smart_home = smart_home


    def __str__(self):
        features = [
            f"Bedrooms : {self.bedrooms}",
            f"Bathrooms : {self.bathrooms}",
            f"Kitchen : {'Yes' if self.kitchen else 'No'}",
            f"Garden : {'Yes' if self.garden else 'No'}",
            f"Garage : {'Yes' if self.garage else 'No'}",
            f"Pool : {'Yes' if self.pool else 'No'}",
            f"Solar Panels : {'Yes' if self.solar_panels else 'No'}",
            f"Smart Home : {'Yes' if self.smart_home else 'No'}",

        ]
        return " | ".join(features)



class HouseBuilder:
    def __init__(self):
        self.bedrooms = 1
        self.bathrooms = 1
        self.kitchen = True
        self.garden = False
        self.garage = False
        self.pool = False
        self.solar_panels = False
        self.smart_home = False

    def set_bedrooms(self, count):
        self.bedrooms = count
        return self
    
    def set_bathrooms(self, count):
        self.bathrooms = count
        return self
    
    def add_garden(self):
        self.garden = True
        return self
    
    def add_garage(self):
        self.garage = True
        return self
    
    def add_pool(self):
        self.pool = True
        return self
    
    def add_solar_panels(self):
        self.solar_panels = True
        return self
    
    def add_smart_home(self):
        self.smart_home = True
        return self
    

    def build(self):
        return House(self.bedrooms,
                     self.bathrooms,
                     self.kitchen,
                     self.garden,
                     self.garage,
                     self.pool,
                     self.solar_panels,
                     self.smart_home
                     )


# Creating a custom house using a builder pattern
house_builder = HouseBuilder()

custom_house = (
    house_builder.set_bedrooms(4)
    .set_bathrooms(3)
    .add_garden()
    .add_solar_panels()
    .build()
)

print("Custom house: ", custom_house)