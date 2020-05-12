#Using .sort we can ordenate the list elements alphabetically
cars = ["bmw" , "audi" , "toyota" , "subaru"]
print(cars)
cars.sort()
print(cars)

print("\nreverse".upper())
cars.sort(reverse = True)
print(cars)

#Using sorted() we can order it temporaly
cars = ["bmw" , "audi" , "toyota" , "subaru"]

print("\nHere is the original order: ")
print(cars)
print("\nHere is ordered: ")
print(sorted(cars))
print("\nHere is the original order again: ")
print(cars)
#Reverse order .reverse
print("\nreverse\n".upper())
print(cars)
cars.reverse()
print(cars)
len(cars)

