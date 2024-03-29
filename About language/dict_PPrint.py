# dictionary and pprint (pretty print)

D1 = {"Name":"AA", "Age":10, "Color":"Black"}
print(D1)

# {'Name': 'AA', 'Age': 10, 'Color': 'Black'}

----------------------------------------------------------------------------------------------------

for k in D1.keys():
  print(k)
  
# Name
# Age
# Color
  
----------------------------------------------------------------------------------------------------

for v in D1.values():
  print(v)
 
# AA
# 10
# Black

----------------------------------------------------------------------------------------------------

for k,v in D1.items():
  print(k, v)
  
# Name AA
# Age 10
# Color Black

----------------------------------------------------------------------------------------------------
  
for i in D1.items():
  print(i)
  
# ('Name', 'AA')
# ('Age', 10)
# ('Color', 'Black')

----------------------------------------------------------------------------------------------------

print(D1.get("Age", 2))
# 10

print(D1.get("Feet",0))  # since D1 dictionary did not have "Feet" as key so we get "0" as output. 
# 0  
#No changes done to D1.

----------------------------------------------------------------------------------------------------

print(D1.setdefault("Age", 2))
# 10

print(D1.setdefault("Tail", "long"))   # D1 get a new key as "Tail" with value "long" in it.
# long
# Changes done to D1.
----------------------------------------------------------------------------------------------------

import pprint # the pretty print module

D2 = {2:"B", 10:"j", 7:"G", 5:"E", 8:"H",  4:"D", 6:"F", 3:"C", 1:"A", 9:"i"}

print(D2)

# {2: 'B', 10: 'j', 7: 'G', 5: 'E', 8: 'H', 4: 'D', 6: 'F', 3: 'C', 1: 'A', 9: 'i'}

pprint.pprint(D2) # use the pretty print funct. of pretty print module

# {1: 'A',
#  2: 'B',
#  3: 'C',
#  4: 'D',
#  5: 'E',
#  6: 'F',
#  7: 'G',
#  8: 'H',
#  9: 'i',
#  10: 'j'}
