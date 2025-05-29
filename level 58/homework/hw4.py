# List of temperatures in Celsius
celsius = [0, 20, 37, 100]

# Convert each temperature using lambda + map
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))

print(fahrenheit)