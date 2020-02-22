
# everything in python is object
class Car:
    runs = True
    number_of_wwheels = 4

    #INIT ARGUMENTS ARE CALLED POSITIONAL
    #they are mandatory
    def __init__(self, name):
        self.name = name
        print("new car")


    def __str__(self):
        return f"{self.name} runs({self.runs}) and has {self.number_of_wwheels} wheels."

    #repr is used by system when there is no asignemnt to var for ex
    def __repr__(self):
        return f"Car({self.name})"


    def start(self):
        #instance attribute, variable associated with instance
        #self.name = name
        if self.runs:
            print(f"{self.name} car just started")

    #classmethod does not take self arg, instead it takes
    #cls
    @classmethod 
    def get_number_of_wheels(cls):
        return cls.number_of_wwheels            


subaru = Car("baby")
type(subaru)
subaru.start() 
print(subaru.name)
print(subaru)

####
# FOR REPL:
# import nameOfPyFile
# import importlib
# importlib.reload(name of py file without py extension)
####


print(isinstance(42,str))
print(isinstance(42,int))
print(isinstance(subaru, Car))

# booleans are subclass of int
print(issubclass(bool,int))
print(issubclass(Car,object))

