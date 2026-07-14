"""
SINGLETON DESIGN PATTERN
In an Airpot there is always a single Air Traffic Control Tower to monitor and guide the movements
This requires that only one instance of the class exists all the time

"""

class ControlTower:
    def __init__(self):
        print("Initializing Control Tower")


tower1 = ControlTower()
tower2 = ControlTower() # Mistakenly creates another instance of the Control Tower

print(tower1 is tower2)



'''
The above code has 2 Control Towers. Let us correct this
instead of    __init__ : controls how we initialize an instance
we will use   __new__  : controls how we create an instance
'''

class ControlTower:
    instance = None

    def __new__(cls):  # check if an instance already exists
        if cls.instance is None:
            cls.instance = super().__new__(cls) # create a new instance if it does not exists
            print("Initializing Control Tower")
        return cls.instance



tower1 = ControlTower()
tower2 = ControlTower()

print(tower1 is tower2)