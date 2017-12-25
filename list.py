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


#Append in the List.

b =[2,3,4,5,6,7,8]
b.append(34)
print(b)

#output : [2, 3, 4, 5, 6, 7, 8, 34]

#count in the List.

b =[2,3,4,5,6,7,8,4]
print(b.count(4))

#output : 2

#Insert in the List at a specified index.

b =[2,3,4,5,6,7,8,4]
b.insert(4,4)
print(b)

#output :[2, 3, 4, 5, 4, 6, 7, 8, 4]

# Adding one List into another one.

a=[2,3,4]
b =[2,3,4,5,6,7,8,4]
b.extend(a)
print(b)

#output : [2, 3, 4, 5, 6, 7, 8, 4, 2, 3, 4]

#Note : There is no method in python which allow us to add a list in the specified position. 

#Delete the first occurence of an element in python.

b =[2,3,4,5,6,7,8,4]
b.remove(4)
print(b)

#Output : [2, 3, 5, 6, 7, 8, 4]

#Index of first occurence of a number.

b =[2,3,4,5,6,7,8,4]

print(b.index(4))

#output : 2

Note : if the number is not available in the List , we will get a ValueError.

b =[2,3,4,5,6,7,8,4]

print(b.index(33))

#output : ValueError: 33 is not in list

#Sorting in the List.

b =[2,3,4,5,6,7,8,4]
b.sort()
print(b)

#Output : [2, 3, 4, 4, 5, 6, 7, 8]

#reverse  the order in the List.

b =[2,3,4,5,6,7,8,4]
b.reverse()
print(b)

#output : [4, 8, 7, 6, 5, 4, 3, 2]

