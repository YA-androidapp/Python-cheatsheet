import os

print(os.getcwd())
print(__file__)

print(os.path.basename(__file__))
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
