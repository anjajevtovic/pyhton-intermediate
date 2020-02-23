
input = "a"

try:
    int(input)
except ValueError as e:
    print(f"No way, that is not a number. {e}")

d = {1:1}

try:
    int(input)
    d[input]
except (ValueError, KeyError, KeyError):
    print("Oh, no")

input = 21

# ZeroExc is swollowed by Arithemthic because it is its ancestor
def division(input):
    try:
        result = 3.14/input
        print(result)
    except ArithmeticError:
        print("We have a general mathematic error")
    #except ZeroDivisionError:
    #  print("Divide by zero error.")

# CUSTOM EXCEPTIONS

class CustomException(Exception):
    def __init__(self, value):
        message = f"Got a bad value: {value}"
        super().__init__(message)

# call of custom excp
val = 500

#if val > 400:
#    raise CustomException(val)

