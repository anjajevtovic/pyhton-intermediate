
# to run interactive code put -i after python keyword when ruuning script


class Vehicle():

    def __init__(self, make, model, fuel="gas"):
        self.make = make
        self.model = model
        self.fuel = fuel

    def __str__(self):
        return f"I drive {self.make} {self.model}"



daily = Vehicle("Subaru", "Crosstrek")
print(daily)

class Truck(Vehicle):

    number_of_wheels = 6

    def __init__(self, make, model, fuel="diesel"):
        super(make,model,fuel)

#if doesnot have its own __init__ method, form super() is called
class Car(Vehicle): 
     number_of_wheels = 4