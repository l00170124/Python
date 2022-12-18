print("Pass, Continue, Break")
my_list=[1,2,3,0]
for my_number in my_list:
    if my_number==1:
        pass
    if my_number==2:
        continue
    if my_number==3:
        print(f"Found the number {my_number}")
    if my_number==0:
        break

print("nest tuples in lists")
list_of_tuples = [(1,2), (3,4), ("A", "B")] 
for item in list_of_tuples: 
    print(item)

print("Tuple unpacking")
list_of_tuples = [(1,2), (3,4), ("A", "B")] 
for a,b in list_of_tuples: 
    print(a) 
    print(b)

print("Tuple Indexing")
for index in range(1, 100, 5): 
    print(index)