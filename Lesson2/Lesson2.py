fruits = ["apple","banana","cherry"]

print(fruits)

#Create a tuple
words = ("spam","eggs","sausages")
print(words[1])

#Create a tuple with information about a person

person = ('Blerta', 24, "Engineer")

name, age, proffesion = person

print (name, "'s", "proffesion is:", proffesion, " and she is", age, "years old" )


person = ('Elvedin', 17, 'Programmer')

name, age, proffesion = person

print (name, "'s", "proffesion is:", proffesion, "and he is", age, "years old" )


#Create dictionary

my_dictionary = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"

    #more keys more valus pairs
}

contact_info = {
    "Blerta": "444-333405",
    "Drini" : "3339-3333"
}

#Create variable calles kreative's phone and use [] we can specify which key we want to acces

kreative_phone = contact_info["Blerta"]

print(kreative_phone)
print(contact_info)

contact_info ["Drini"] = "0294-48575"

print(contact_info)

#We want to add another friend to contact_info

contact_info ["Eros"] = "9384-117348"

print(contact_info)

#Delete a contact info

del contact_info["Blerta"]
print(contact_info)

keys = contact_info.keys()

print(keys)

#Print only the keys of the dictionary

keys = contact_info.keys()

print(keys)

values = contact_info.values()
print(values)

#print items
items = contact_info.items
print(items)


