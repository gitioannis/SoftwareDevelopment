# Task: create a database of members for the local club.
# Business rule: every member must have a unique occupation

myDict = {
    'customerName': ['John Miaris'],
    'age': ('65,'),
    'occupation': {'Brain Surgeon'},
    'address': {'street':['123 Anywhere Ave'], 'city':['Portsmouth']}
}

# add a new customer name
myDict['customerName'].append('Maria Kallas')

# tuple is immutable so add a new tuple and join
age = myDict['age']
newAge = ('108')
age = age + newAge
myDict['age'] = age

# add new occupation (.add not .append)
myDict['occupation'].add('Vocalist')

# add a new address
myDict['address']['street'].append('99 Somestreet Close')

# add a new city
myDict['address']['city'].append('London')

# add a new key and the values after the fact
myDict['address']['postCode'] = ['PO55 6AS','LO12 1SA']

for key in myDict:
    # the alternative is isinstance(key,type)
    thisType = type(myDict[key]).__name__
    thisKey = myDict[key]
    print(thisKey)
    print(thisType)
    print('-'*10)
    if thisType == 'list':
        for val in thisKey:
            print(val)
    elif thisType == 'dict':
        for key in thisKey:
            print(key)
            print(thisKey[key])
        
    
    
