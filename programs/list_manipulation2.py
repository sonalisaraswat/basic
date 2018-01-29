# List using range
a=list(range(1,10))
print(a)

a=[i for i in range(1,10)]
print(a)

a=[i*2 for i in range(1,11)]
print(a)

a=[x for x in range(2,21) if x%2==0]
print(a)

# Manipulation in list...Iteration!
a=[y+1 for y in a]
print(a)

x=['a','b','c','d','e','f']
for index,item in enumerate(x):
    print(index,item)

# String to list
t="Hello World"
print(t)
t=list(t)
print(t)

# Merge two lists
a=[1,2,3,4,5]
b=['a','b','c','d','e']
a=a+b
print(a)

# Multiply operation on list
a=[1,2,3]
print(a*3)

# Using 'in' and 'not in' on list to check membership
x=[10,20,30,40,50,70,80,90,100]
print(50 in x)
print(60 in x)
print(50 not in x)
print(60 not in x)

# Length of list
print(len(x))

#use of 'min,'max','sum'
print("Max of list x: ",min(x))
print("Max of list x: ",max(x))
print("Sum of list x: ",sum(x))
print("Sum of first 3 elements",sum(x[0:3]))

# Sorting
q=[34,87,44,67,1,0,22,3,4,100,23,7,]
# 'Sorted' funct. makes no changes in original list
print(sorted(q))
print(q)
# 'Sort' funct. sorts the list permanently
q.sort()
print(q)

# Count the occurance of elements
x=[1,7,5,5,2,1,7,9,2,4,0,50,1]
print("\n",x)
print("Frequency of 7: ",x.count(7))
print("Frequency of 3: ",x.count(3))

# Unpacking the n items into n variables
q=[1,2,3]
a,b,c=q
print(a,b,c)

"""
Output
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
[3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
0 a
1 b
2 c
3 d
4 e
5 f
Hello World
['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
[1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']
[1, 2, 3, 1, 2, 3, 1, 2, 3]
True
False
False
True
9
Max of list x:  10
Max of list x:  100
Sum of list x:  490
Sum of first 3 elements 60
[0, 1, 3, 4, 7, 22, 23, 34, 44, 67, 87, 100]
[34, 87, 44, 67, 1, 0, 22, 3, 4, 100, 23, 7]
[0, 1, 3, 4, 7, 22, 23, 34, 44, 67, 87, 100]

 [1, 7, 5, 5, 2, 1, 7, 9, 2, 4, 0, 50, 1]
Frequency of 7:  2
Frequency of 3:  0
1 2 3
"""
