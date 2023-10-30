lucky_numbers = [8, 93.3, 42, 5, 17]
friends = ["Irene", "Jayde", "Alex", "Isa", "Chris"]
friends.extend(lucky_numbers)
print(friends)

lucky_numbers = [8, 93.3, 42, 5, 17]
friends = ["Irene", "Jayde", "Alex", "Isa", "Chris"]
lucky_numbers.extend(friends)
print(lucky_numbers)

friends = ["Irene", "Jayde", "Alex", "Isa", "Chris"]
friends.append("Rose")
print(friends)

friends = ["Irene", "Jayde", "Alex", "Isa", "Chris"]
friends.insert(2,"Rose")
print(friends)

lucky_numbers = [8, 93.3, 42, 5, 17]
lucky_numbers.insert(1,4)
print(lucky_numbers)

friends = ["Irene", "Jayde", "Alex", "Isa", "Chris"]
friends.remove("Alex")
print(friends)

friends = ["Irene", "Jayde", "Alex", "Isa", "Chris"]
friends.clear()
print(friends)

friends = ["Irene", "Jayde", "Alex", "Isa", "Chris"]
friends.pop()
print(friends)

friends = ["Irene", "Jayde", "Alex", "Isa", "Chris"]
print(friends.index("Irene"))

friends = ["Irene", "Jayde", "Jayde","Jayde", "Alex", "Isa", "Chris"]
print(friends.count("Jayde"))

friends = ["Irene", "Jayde", "Alex", "Isa", "Chris"]
friends.sort()
print(friends)

lucky_numbers = [8, 93.3, 42, 5, 17]
lucky_numbers.sort()
print(lucky_numbers)

friends = ["Irene", "Jayde", "Alex", "Isa", "Chris"]
friends.reverse()
print(friends)
lucky_numbers = [8, 93.3, 42, 5, 17]
lucky_numbers.reverse()
print(lucky_numbers)

friends = ["Irene", "Jayde", "Alex", "Isa", "Chris"]
friends2 = friends.copy()
print(friends2)






