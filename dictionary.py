#Initialization of Dictionary:

dict1={} #empty dictionary

dict2={1:"test",2:"rest"} #dictionary with integer keys

dict3={1:"test","name":"rest"} #dictionary with mixed type

dict4= dict({1:"test",2:"rest"}) # dictionary with dict built in function

dict5 = dict([(1,'apple'), (2,'ball')]) #from sequence having each item as a pair


#Accessing value in dictonary:

dict2={1:"test",2:"rest"}

print(dict2[2])

#output : rest

dict2={1:"test",2:"rest"}

print(dict2.get(2))

#output : rest


dict2={1:"test",2:"rest"}

print(dict2[3])

#output:    print(dict2[3])

KeyError: 3

dict2={1:"test",2:"rest"}

print(dict2.get(3))

#output: None


#Adding or Changing an element in dictionary:

#updated :
dict2={1:"test",2:"rest"}

dict2[1]= "set"

print(dict2)

#output:{1: 'set', 2: 'rest'}

#Changed :

dict2={1:"test",2:"rest"}

dict2[3]= "set"

print(dict2)

#output : {1: 'test', 2: 'rest', 3: 'set'}


# Removing or deleting item from a dictionary:

dict2={1:"test",2:"rest"}

dict2.pop(2)

print(dict2)

#output :-  {1: 'test'}


#popitem() :-  The popitem() function removes an item from the dictionary arbitarily.

dict2={1:"test",2:"rest"}

dict2.popitem()

print(dict2)

#output :- {2: 'rest'}


#del :-  It removes an individual item and also the whole dictionary.

dict2={1:"test",2:"rest"}

del dict2[2]

print(dict2)

#Output :- {1: 'test'}

dict2={1:"test",2:"rest"}

del dict2

print(dict2)

#Output :- NameError: name 'dict2' is not defined

#Dictionary membership test :-

dict2={1:"test",2:"rest"}

print(1 in dict2)

#output :- True


