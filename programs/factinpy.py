def fact():
 f=1
 num=int(input(":::"))
 for i in range(num):
  f=f*(i+1)
 return f

print(fact())