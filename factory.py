"""
FACTORY DESIGN PATTERN:


"""

class CheesePizza:
    def prepare(self):
        return "Preparing Cheese Pizza!!!"


class MacroniPizza:
    def prepare(self):
        return "Preparing Macroni Pizza!!!"


class OnionPizza:
    def prepare(self):
        return "Preparing Onion Pizza!!!"
    

# Manually creating Pizz objects
pizza1 = CheesePizza()
pizza2 = MacroniPizza()
pizza3 = OnionPizza()


print(pizza1.prepare())
print(pizza2.prepare())
print(pizza3.prepare())