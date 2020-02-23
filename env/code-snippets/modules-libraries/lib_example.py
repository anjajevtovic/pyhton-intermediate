import os
import sys

folder = os.getcwd()
print(f"Current wokrking directory is {folder}")

with os.scandir(folder) as f:
    for entry in f:
        print(f"- {entry.name}")

# args are always strings
arguments = sys.argv
print(f"We received these arguments: {arguments}")

print(f"We are currently running on a {sys.platform} machine")


# GETTING ARGUMENTYS FORM COMMAND LINE

arguments = sys.argv[1:]
print(arguments)

name = input("Type in your wish: ")
print("Good luck with that :D")
