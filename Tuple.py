#Python TUPLE - Pack, Unpack, Compare, Slicing, Delete, Key
#packing and unpacking

x = ("Guru99", 20, "Education")    # tuple packing
(company, emp, profile) = x    # tuple unpacking
print(company)
print(emp)
print(profile)

a=("anojan",17,"education")
(name,years,profile)=a
print(name)
print(years)
print(profile)

#Comparing tuples
#case 1
a=(5,6)
b=(1,4)
if (a>b):
    print("a is bigger")
else: print("b is bigger")

#case 2
a=(5,6)
b=(5,4)
if (a>b):print ("a is bigger")
else: print ("b is bigger")

#case 3
a=(5,6)
b=(6,4)
if (a>b):print ("a is bigger")
else: print ("b is bigger")

#Tuples and dictionary
a = {'x':100, 'y':200}
b = a.items()
print (b)

#Slicing of Tuple
x = ("a", "b","c", "d", "e")
print (x[2:4])
