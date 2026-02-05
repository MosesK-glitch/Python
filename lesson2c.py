# A dictionary is a data type that stores data in key-value pairs.
# Dictionaries are mutable, meaning their contents can be changed after creation.
# Dictionaries are introduced by curly braces {}.
# Creating a dictionary
# To access values in a dictionary, we use their corresponding keys.


phonebook = {
    "John": "123-456-7890",
    "Jane": "987-654-3210",
    "Doe": "555-555-5555"
}
# showing the entire dictionary
print(phonebook)
print(type(phonebook))
student = {
    "name": "John Doe",
    "age": 21,
    "courses": ["Math", "Science", "History"]
}
print(student)
print(type(student))
# Accessing values in a dictionary using keys
print(phonebook["John"])  # Output: 123-456-7890
print(student["name"])  # Output: John Doe
print(student["courses"])  # Output: ['Math', 'Science', 'History']
# Adding a new key-value pair to the dictionary
phonebook["Alice"] = "111-222-3333"
print(phonebook)
# Modifying an existing value in the dictionary
phonebook["John"] = "999-888-7777"
print(phonebook)
# Removing a key-value pair from the dictionary
del phonebook["Jane"]
print(phonebook)
phonebook.pop("Doe")
print(phonebook)
