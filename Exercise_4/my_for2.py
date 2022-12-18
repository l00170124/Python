iterable_variable=[1,2,3,4,5,6]
total=0

print("With the Print command indented the for loop processes all the options and then prints them")
for item in iterable_variable:
    total=total+item
print(total)

print("With the Print command is not indented the for loop processed all the options and then prints the final result")
for item in iterable_variable:
    total=total+item
    print(total)
