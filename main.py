from evaluation import evaluate
from bases import Bases
bases = Bases()


a = input("a:")
b = input("b:")
c = input("Choose function (multiply, divide or add):")

try:
    print(evaluate(a, b, c))
except TypeError:
    print("Please input integers")
