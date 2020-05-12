alien_0 = {"color": "green" , "points": 5 ,"speed": "slow"}
alien_1 = {"color": "yellow" , "points": 10 ,"speed": "medium"}
alien_2 = {"color": "red" , "points": 15 ,"speed": "fast"}

aliens = [alien_0 , alien_1 , alien_2]

for alien in aliens:
    print(alien)
print("\n")
###########################
aliens = []

#Make 30 green aliens
for aliens_number in range(30):
    new_alien = {"color": "green" , "points": 5 ,"speed": "slow"}
    aliens.append(new_alien)

#First 3 aliens to yellow
for alien in aliens[0:3]:
    if alien["color"] == "green":
        alien["color"] = "red"
        alien["points"] = 15
        alien["speed"] = "fast"
    elif alien["color"] == "red":
        alien["color"] = "yellow"
        alien["points"] = 10
        alien["speed"] = "medium"

#Show first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...\n")

#Quantity of aliens
print(str(len(aliens)))



