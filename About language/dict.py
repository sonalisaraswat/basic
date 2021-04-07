# dictionary and pprint (pretty print)

D1 = {"Name":"AA", "Age":10, "Color":"Black"}
print(D1)
# 


for k in D1.keys():
  print(k)
  
for v in D1.values():
  print(v)
  
for k,v in D1.items():
  print(k, v)
  
for i in D1.items():
  print(i)
  
  
D1.get("Feet",0)



D1.setdefault("Tail", "long")



import pprint
D2 = {2:"B", 10:"j", 7:"G", 5:"E", 8:"H",  4:"D", 6:"F", 3:"C", 1:"A", 9:"i"}
print(D2)
print()
pprint.pprint(D2)
