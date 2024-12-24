# Dictionaries in Python
# {key1: value1, key2: value2}

animals = {
    'Dog': "An animal which says bhow bhow.",
    'Cat': "An animal which says mew mew."
}

#print(animals['Dog'])

# adding new keys to dictionary
animals["Cow"] = "An animal which says mao mao."

#print(animals["Cow"])

#wipe entire dictionary
animals = {}

#edit and item
animals["Dog"] = "says bhow bhow" #creates new if not existing
print(animals["Dog"])

#loop through dictionary
for key in animals:
    print(key)
    print(animals[key])
