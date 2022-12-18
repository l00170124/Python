my_dictionary = {"Fname":"John", "SName":"ORaw","Occupation":"Rocket Scientist"}
print(my_dictionary)
print("Works as a " + my_dictionary ["Occupation"])

#Adding a new Entry to the dictionary
my_dictionary["Salary"] = "Not Enough!"
print(my_dictionary)

#editing an entry
my_dictionary["Occupation"] = "Professor"
print(my_dictionary)

#print just the keys - Extracting the Keys
print(my_dictionary.keys())

#Extracting the values
print(my_dictionary.values())

#Returning all values
print(my_dictionary.items())