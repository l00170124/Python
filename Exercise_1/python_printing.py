print(f"Using the + operator to add different types")
a="Do not be a Karen"
print("Good Morning Karen just a reminder " + a)

print(f"Using the .format method")
b = 5
c = 22
print("Good Morning Karen. For breakfast we have {}, is this ok?".format("fruit"))
print("In the pantry the b&b has {} Apples and {} Oranges left over, which is a total of {}.".format(b,c,b+c))

print("Complex Programmes with keywords")
d="Good"
e="Morning"
f="Karen"
print("message is: {first} {second} {third}".format(first=d,second=e,third=f))

print("Float")
Number=12345
Divisor=333
Result=Number/Divisor
print("Result of {} divided by {} is {}".format(Number,Divisor,Result))
print("Limiting to a float with 4 decimal places would give {r:1.4f}".format(r=Result))

print("Formatted Strings")
print(f"Result of {Number} divided by {Divisor} is {Result}")

print("Escape Sequences")
print("Good Morning, Karen \nWould you like breakfast")

print("More Functions")
my_string=("Almost Finished")
my_upper=my_string.upper()
my_lower=my_string.lower()
print(f"Original: {my_string}")
print(f"UPPER: {my_upper}")
print(f"lower: {my_lower}")

print("How Many Character Function")
k ="How many Characters"
print(len(a))