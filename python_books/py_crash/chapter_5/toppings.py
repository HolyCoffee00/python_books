requested_topping = "mushroom"

if requested_topping != "anchovies":
    print("Hold the anchovies")

names = ["sergio", "rivas", "coso"]

for names in names:
    if names != "sergio":
        print("Hola " + names)
    else:
        print("Eres un puto " + names)
        print("\n")
print("\n")

extra_topping = ["extra cheese", "mushroom"]

if "mushroom" in extra_topping:
    print("Adding extra mushrooms")
if "extra cheese" in extra_topping:
    print("Adding extra cheese")
if "pepperoni" in extra_topping:
    print("Adding extra pepperoni")
print("\n")

input_name = input("Welcome, Whats your name?\n")
name = input_name.title()
greetings = "Welcome, " + name
print(greetings)

print("You can add only 3 toppings")
print("The available toppings are:")

avaliable_toppings = ["Chesse" , "Mushrooms" , "Pepperoni" , "Ham"]
for avaliable_toppings in avaliable_toppings:
    print(avaliable_toppings)
print("\n")

user_toppings = []
user_first_topping = input("What is your first topping?:\n")
user_toppings.append(user_first_topping.lower())
user_second_topping = input("Good, what is your second topping?:\n")
user_toppings.append(user_second_topping.lower())
user_last_topping = input("Good, What is your last topping?:\n")
user_toppings.append(user_last_topping.lower())
print("\n")

print("Excelent, your toppings are:")
for user_toppings in user_toppings:
    print(user_toppings.title())
print("Please wait for your pizza")
print("\n")

empty_list = []
if empty_list:
    for empty_list in empty_list:
        print("There is something in the list")
else:
    print("This list is empty brah")





