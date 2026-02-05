# Python lists
# A list is a collection which is ordered and changeable.
# A list is introduced by square brackets [].
# The items of a list are stored inside of indexes. In programming, indexes start at 0. bmw, benz, audi, toyota...
# A list is mutable i.e the contents of a list can be changed.

cars=["bmw", "benz", "audi", "toyota"]

print(cars)
print(type(cars))

# Accessing items in a list
print(cars[0]) # bmw
print(cars[1]) # benz
print(cars[2]) # audi
print(cars[3]) # toyota

# List slicing - This is creating a list from a given bigger list.
print(cars[0:2]) # ['bmw', 'benz']

# printing from index zero to the end of the list
print(cars[0:]) # ['bmw', 'benz', 'audi', 'toyota']

#printing from bmw to toyota
print(cars[:]) # ['bmw', 'benz', 'audi', 'toyota']

#list- mutability
# We use the function append to add items to a list. It adds the item at the end of the list.
print(cars[:]) # ['bmw', 'benz', 'audi', 'toyota']
cars.append("lexus")
print(cars)

cars.append("honda")
print(cars)

# we use the pop function to remove an item at the end of the list.
cars.pop()
print(cars)

# We can use the sort function to sort the items in a list in alphabetical order.
cars.sort(reverse=True) 
print(cars)

del cars[1]
print(cars)

cars.pop(0)
print(cars)