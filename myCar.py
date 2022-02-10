
class Car(object):
    def __init__(self, model, color, company, speedLimit):
        self.model = model
        self.color = color
        self.company = company
        self.speedLimit = speedLimit
    def start(self):
        print("Started...")
    def stop(self):
        print("Stopped...")
    def gearChanged(self):
        print("Changes the gear...")

# Audi is the object of Car Class in which four values are passed(model, color, company, speedlimit)
audi = Car('A6','black','Audi', 70)
# This statement goes into the function gearChanged and takes the print statement. Using the object of the class(Audi),
# the function/method defined in the class.
print(audi.gearChanged())
# Using the object of the class, accessed the element(color).
print(audi.color)