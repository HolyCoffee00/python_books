#Store info aboout the ordered pizza
pizza = {
    "crust": "thick",
    "toppings": ["mushrooms" , "extra cheese"]
}

#Summarize te order
print("Your ordered a " + pizza["crust"] + "- crust pizza" +
      "with the following toppings:")

for top in pizza["toppings"]:
    print("\t" + top.title())


