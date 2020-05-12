alien_0 = {}
alien_0["color"] = "green"
alien_0["points"] = 5
print(alien_0)

alien_0["x_position"] = 0
alien_0["y-position"] = 25
print(alien_0)
print("\n")

print("The alien is color " + alien_0["color"].title() + ".")
alien_0["color"] = "yellow"
print("Now the alien color is " + alien_0["color"].title() + ".")
print("\n")

alien_0 = {"x_position": 0 , "y_position": 25 , "speed": "medium"}
print("Original X position " + str(alien_0["x_position"]))
#Alien move to right
#Determine how far to move the alien based on the current speed
if alien_0["speed"] == "low":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    #Alien is fast
    x_increment = 3

alien_0["x_position"] = alien_0["x_position"] + x_increment
print("New X postion  " + str(alien_0["x_position"]))

print(alien_0)
del alien_0["speed"]
print(alien_0)