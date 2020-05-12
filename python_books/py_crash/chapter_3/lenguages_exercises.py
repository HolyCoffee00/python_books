lenguages = ["spanish" , "english" , "italian" , "french"]
print("original order".upper())
print(lenguages)
print("\n")

print("I can speak " + lenguages[0].title() + " and " + lenguages[1].title() + "." + "\n")

print(lenguages)
lenguages[3] = "indian"
print(lenguages)
print("\n")

lenguages = ["spanish" , "english" , "italian" , "french"]
print(lenguages)
lenguages.append("indian")
print(lenguages)
print("\n")

lenguages = ["spanish" , "english" , "italian" , "french"]
print(lenguages)
lenguages.insert(1,"indian")
print(lenguages)
print("\n")

lenguages = ["spanish" , "english" , "italian" , "french"]
print(lenguages)
del lenguages[2]
print(lenguages)
print("\n")

lenguages = ["spanish" , "english" , "italian" , "french"]
print("My favourite lenguages are: " + str(lenguages))
english_popped = lenguages.pop(1)
spanish_popped = lenguages.pop(0)
print("But i already know " + english_popped.title() + " and " + spanish_popped.title())
print("\n")

lenguages = ["spanish" , "english" , "italian" , "french"]
print("My favourite lenguages are: " + str(lenguages))
english = "english"
spanish = "spanish"
lenguages.remove(english)
lenguages.remove(spanish)
print("But i already know " + english.title() + " and " + spanish.title())
print("The lenguages left are: " + str(lenguages))
print("\n")













