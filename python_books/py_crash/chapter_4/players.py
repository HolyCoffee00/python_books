players = ["andreina" , "siuddy" , "jeanny" , "zafiro" , "angelica"]
print(players)
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
print("\n")

print("Here are my best players: ")
for players in players[:3]:
	print(players.title())
