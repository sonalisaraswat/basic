import random
a = random.randint(1, 10)
print(a)

# To directly use function without writing module name again and again.

from random import *
a = randint(1, 10)
print(a)

# print() 
print("Hey", "There")   # Hey There

print("hakuna")
print("matata")
# hakuna
# matata

print("hakuna", end = ' ')
print("matata")
# hakuna matata

print("Hi", "how", "are", "you", sep = ":")
# Hi:how:are:you
