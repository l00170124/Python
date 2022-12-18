""" 
Class template by KMCD 
Revision History 23OCT22: Alpha 
""" 
class MyTemplate(): 
    # pass will do nothing
    # pass 
    # Constructor, called whenever an instance of the class is created. 
    def __init__(self) -> None: 
        print("Constructor ran")
# Instantiate the class 
my_object = MyTemplate() 
# Check the object and type 
print(type(my_object))