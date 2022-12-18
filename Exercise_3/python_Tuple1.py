my_list = ["One","Two","Three"]
my_tuple = ("One","Two","Three")
print(type(my_list))
print(type(my_tuple))

#Using methods like count() and index () 
my_tuple2=("one", "two", "three", "one")
#how many times does "one" appear in the tuple
print(my_tuple2.count ("one"))
#at what position in the tuple can I first find "one")
print (my_tuple2.index ("one"))

print (my_tuple2.index ("six"))