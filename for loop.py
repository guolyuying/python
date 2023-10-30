for letter in "Giraffe Academy": #ex. Use FOR LOOP to loop through a string
    print(letter)

print()

friends = ["Irene", "Jayde", "Alex"]
for name in friends: #ex. Use FOR LOOP to loop through an array: a very common use case for FOR LOOP
    print(name)

print()

for index in range(10): #ex. Use FOR LOOP to loop through a series of numbers
    print(index)

print()

for index in range(3,10): #ex. Use FOR LOOP to loop through a specified range of numbers
    print(index)

print()

friends = ["Irene", "Jayde", "Alex"]
print(len(friends))

for index in range(len(friends)): #ex. Use FOR LOOP to figure out the number of elements in an array
    print(index)

print(friends[0])

for index in range(len(friends)): #ex. Another way to use FOR LOOP to loop through an array (looks way too winding to me, though)
    print(friends[index])

print()

# Use all sorts of Logic inside of a FOOR LOOP
for index in range(5):
    if index == 0:
        print("first")
    else:
        print("not first")

print()

# Another test on adding Logic to FOR LOOP
for index in range(5):
    if index == 0:
        print(1)
    if index == 1:
        print(2)
    if index == 2:
        print(3)
    if index == 3:
        print(4)
    if index == 4:
        print(5)
