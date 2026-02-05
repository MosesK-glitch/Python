# Tuple
# A tuple is an immutable type of a list i.e the contents of a tuple cannot be changed once it is created.
# To inrtroduced a tuple we use parentheses () instead of square brackets [].

counties = ("Kajiado", "Kisumu", "Kampala", "Mombasa", "Nairobi")

print(counties)
print(type(counties))   

# Slicing a tuple
print(counties[3:1])

# Accessing items in a tuple by index
print(counties[0]) # Kajiado

# Note: Below will generate an error because tuples are immutable
counties.append("Machakos")  # This will raise an AttributeError since tuples don't support append method
print(counties)