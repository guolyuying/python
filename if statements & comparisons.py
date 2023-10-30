def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(23, 507, 300))



def creature_comparison(species1, species2):
    if species1 != species2:
        return("You are not the same species :( But you can still be in love with each other!")
    else:
        return("You are the same species :)")













result = creature_comparison("human", "human")
print(result)