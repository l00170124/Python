a = "Greetings!"
#forward indexing
print(f"**Forward Indexing**")
print(a[0:4:1])
print(a[0:4:2])
print(a[0:4:3])
print(a[0:5:1])
print(a[0:5:2])
print(a[2:7:2])

 #reverse indexing
print(f"**Reverse Indexing**")
print(a[-2:-7:-1])

#individual
print(f"**Individual**")
print(a[-10])

print(f"Slice the String Options")
b="Karen"
first_letters=b[0:2:1]
last_letter=b[-1]
insert_letter="garoo"
c = first_letters + last_letter + insert_letter
print(c) 

print(f"Adding a string and a number")
first_character = 1
second_character = "k"
d = first_character + second_character
print(d)