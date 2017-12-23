# The List are the another kind of data structure present in the python.
# They are more like arrays but they are not array.
#1.)Initializing  an empty list.

a=[]

print(a)

# The output will be an []. 
#Initializing  a list with some elements.

a=[2,3,4]

print(a)

#Another way of creating list is by list comprehension .we will see this point later.


# 2.) Indexing with List.

a=[2,3,4]

print(a[2])

#output : 4

#Negative Indexing :

a=[2,3,4]

print(a[-2])

#output : 3

# 3).Slicing in List

a=[2,3,4]

print(a[:2])

#output : [2,3]

a=[2,3,4,6,9,0,5]

print(a[2:4])  

#output : [4, 6]

a=[2,3,4,6,9,0,5]

print(a[:])

#output : [2, 3, 4, 6, 9, 0, 5]

a=[2,3,4,6,9,0,5]

print(a[:-2])

#output :[2, 3, 4, 6, 9]

#4.) Nesting in List.

#We can create a list inside a list and there is no limit on the number of nesting.

a=[2,3,4,[6,9],0,5]

print(a[3])

#output : [6, 9]

a=[2,3,4,[6,9],0,5]

print(a[2:4])

#output : [4, [6, 9]]

#5.) Chnaging and updating a List.

#With the helpof assignment operator , we can be able to change the contents of a list unlike tuples.

a=[2,3,4,[6,9],0,5]

a[2] = 7

print(a)

#output : [2, 3, 7, [6, 9], 0, 5]

a=[2,3,4,[6,9],0,5]

a[2:4] = [7,5,6]

print(a)
 
#output : [2, 3, 7, 5, 6, 0, 5]


#We can also use + operator to combine two lists. This is also called concatenation.


a =[2,34,4]

b =[4,5,6]

print(a + b)

#output= [2, 34, 4, 4, 5, 6]

#The * operator repeats a list for the given number of times.

b =["san"]

print(b*3)

#output= ['san', 'san', 'san']



