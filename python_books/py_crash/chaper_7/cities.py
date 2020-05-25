prompt = "\nPlease enter the names of the cities that you have visited:"
prompt += "\nTo finish the program, enter (quit) "

while True:
    city = input(prompt)
    if city == "quit":
        break
    else:
        print("i'd love to go to " + city.title() + "!")