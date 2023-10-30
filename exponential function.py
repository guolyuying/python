def exponential_function(base, pow):
    result = 1
    for index in range(pow):
        result = result * base
    return result

print(exponential_function(2,8))

# Use built-in exponential function in Python
print(2**8)
