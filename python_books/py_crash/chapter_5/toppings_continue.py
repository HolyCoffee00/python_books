available_toppings = ["mushrooms" , "olives" , "green peppers" , "pepperoni" , "pineapple" , "extracheese"]
requested_topping = ["mushrooms" , "french fries" , "olives"]

for requested_topping in requested_topping:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping)
    else:
        print("Sorry, we don't have " + requested_topping)
print("\nFinishing making your pizza")