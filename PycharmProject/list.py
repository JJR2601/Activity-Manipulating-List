# Print list
color = ["blue", "yellow", "red", "green", "gold", "orange", "violet", "brown", "black", "white"]
print (color[3:7])

# Change certain item in list
color = ["blue", "yellow", "red", "green", "gold", "orange", "violet", "brown", "black", "white"]
color[2:6] = ["magenta", "maroon"]
print (color)

# add in list
color = ["blue", "yellow", "red", "green", "gold", "orange", "violet", "brown", "black", "white"]

color.append("magenta")
color.append("cyan")
color.append("maroon")

color.extend(["magenta", "cyan", "maroon"])

print(color)

# Delete list
color = ["blue", "yellow", "red", "green", "gold", "orange", "violet", "brown", "black", "white"]
del color[5]
print(color)



