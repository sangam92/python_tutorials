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

#Slicing a tuple:

a =(2,"san",6,7,9)
print(a[2:4])

#The output is 6,7

print(a[:3])

#The output is(2, 'san', 6).

print(a[:])

#The output is (2,"san",6,7,9)

print(a[:-1])

(2, 'san', 6, 7)

# The tuples are immutable but if the element inside tuple is mutable .it can be changed.

a =(2,"san",6,7,9)

a[2]= 4

#we get the below error;
#TypeError: 'tuple' object does not support item assignment.
#but in case of a list ,the result is different.

my_tuple = (4, 2, 3, [6, 5])


my_tuple[3][1]=9

print(my_tuple)


#The output is (4, 2, 3, [6, 9]).

#deleting a tuple.



my_tuple = (4, 2, 3, [6, 5])


del my_tuple

print(my_tuple)

# The output is NameError: name 'my_tuple' is not defined.


#concatenation of Tuples.


a =(2,3,4)

b =(4,5,6)

print(a + b)

# The output is (2, 3, 4, 4, 5, 6)


a =(2,3,4,4,5)

print(a.count(4))

# The output is 2.


a =(2,3,4,4,5)

print(a.index(3))

# The output is 1.
 
 
 
 

