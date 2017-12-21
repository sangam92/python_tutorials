#Tuples are immutable sequence of an element.
#They can be represented by the parenthesis ().
#The element contained in the tuple can be of any datatypes.

#1.) How to initialize  a tuple ?

#empty tuple
a =()

#Tuple with values.

a =(2,"san",6)

#Tuple with one value.
#The Tuple with single value should have a comma.
a= (5,)


#2.) Accessing values in tuple.

#The value in tuple can be accessed via indexing and slicing.

#The value in the tuple starts from the zero index.


#Example :- 

a =(2,"san",6,7,9)

print(a[2])

# The Output will be 6.


print(a[0])

# The Output will be 2.

print(a[2:4])

# The Output will be 6,7.


#3.) Nested Tuples.

#We can have a tuple inside a tuple but to access this is a tricky one.


nestedtuple = (2,3,(4,6,7))

print(nestedtuple[2])
    
# The output will be (4,6,7).

nestedtuple = (2,3,(4,6,(3,5),7))

print(nestedtuple[2][0])
    
#The output will be 4.

#Negative Indexing:


nestedtuple = (2,3,(4,6,(3,5),7))

print(nestedtuple[-2]


# The Output will be 3.

 

