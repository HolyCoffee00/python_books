input_name = input("Welcome, Whats your name?\n")
name = input_name.title()
greetings = "Welcome, " + name
print(greetings)

print("You can add only 3 toppings")
print("The available toppings are:")

avaliable_toppings = ["cheese" , "mushrooms" , "pepperoni" , "ham"]
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

#print(user_toppings)
print("Excelent, i took your order:")
for user_toppings in user_toppings:
    print(user_toppings.title())
