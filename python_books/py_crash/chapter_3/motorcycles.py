motorcycles = ["honda" , "yamaha" , "suzuki"]
print(motorcycles)
print(motorcycles[0])
print("\n")

#Changing "motorcycle" element[0] from "honda" to "ducati"

motorcycles[0] = "ducati"
print(motorcycles)
print(motorcycles[0])
print("\n")

#Adding "horse" to the list using .append()

motorcycles.append("horse")
print(motorcycles)
print("\n")

#Using .append i can build a list

cars = []
cars.append("chevrolet")
cars.append("toyota")
cars.append("fiat")

print(cars)
print("\n")

#Using .insert(#position, element) to add elements at any position

cars_2 = ["honda" , "nissan" , "ferrari"]
print(cars_2)
cars_2.insert(1,"lambo")
print(cars_2)
print("\n")

#Use del to remove a element

del cars_2[1]
print(cars_2)
print("\n")

#Use .popped to remove the last element but can still use it

print(cars)
popped_car = cars.pop()
print(cars)
print(popped_car)

owned_cars = ["corsa" , "optra"]
print("My list of owned cars is" + str(owned_cars) + ".")
last_car = owned_cars.pop()
print("The last car i owned was a Chevrolet " + last_car.title() + ".")
print("\n")

dream_cars = ["dodge hellcat" , "ferrari" , "lamborguini"]
first_dream_car = dream_cars.pop(0)
print("My first dream car is a " + first_dream_car.title() + ".")
print("\n")

#Use .remove() to delete a element by the value

liquids = ["nasty" , "interestellar" , "mr ape"]
print(liquids)
liquids.remove("nasty")
print(liquids)
print("\n")

motorcycles = ["honda" , "yamaha" , "suzuki" , "ducati"]
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print("A " + too_expensive.title() + " is too expensive for me." )
