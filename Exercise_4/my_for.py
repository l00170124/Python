iterable_variable=[1,2,3,4,5,6]
for item in iterable_variable:
    #for each item, execute this code block
    print(item)

print("Print all odd numbers from the loop")
for item in iterable_variable:
    if item%2!=0:
        print(item)
        
print("Print all even numbers from the loop")
for item in iterable_variable:
    if item%2!=1:
        print(item)