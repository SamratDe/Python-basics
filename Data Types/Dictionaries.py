# --------- DICTIONARIES ---------
# unordered mappings for storing objects

myDict = {'val1': 'key1', 'val2': 'key2'}
print(myDict)

# getting value from dictionary
print(myDict['val1'])

# adding a new key in dictionary
myDict['val3'] = 'key3'

# nested dictionaries
myDict1 = {'abc': [1, 2], 'def': {'xy': 3, 'yz': 4}}
print(myDict1['def']['yz'])     # output - 4
print(myDict1['abc'][0])        # output- 1

# keys
myDict.keys()

# values
myDict.values()

# pairings
myDict.items()