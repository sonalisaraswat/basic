#Given two integers (x,y) , he has to swap each element in that range with its related element
n=int(input())
a=[int(x) for x in (input().split())]
q=int(input())
for i in range(q):
    (x,y)=[int(x) for x in (input().split())]
    for j in range(x-1,y):
        a[j],a[n-(j+1)]=a[n-(j+1)],a[j]
b=[str(v) for v in a]
print(' '.join(b))
