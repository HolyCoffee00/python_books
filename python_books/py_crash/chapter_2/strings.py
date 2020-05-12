#examples of how the modificators works on the strings
print("changing cases".upper())

name = "seRgIo lEzama"
print(name)
print(name.title())
print(name.upper())
print(name.lower())

print("\ncombining strings".upper())

first_name = "sergio"
last_name = "lezama"
full_name = first_name + " " + last_name
print(full_name.title())

print("\nconcatenation".upper())

greetings = "Hello," + " " + full_name.title() + "!" 
print(greetings)

print("\ntabs or new lines".upper()) 

print('lenguages "new lines examples":\nspanish\nenglish'.title())
print('lenguages "tabs examples": spanish\tenglish'.title())
print('lenguages "combinated":\n\tspanish\n\tenglish'.title())

print("\nstriping spaces".upper())
lenguage = " python "

print(lenguage.rstrip())
print(lenguage.lstrip())
print(lenguage.strip())
