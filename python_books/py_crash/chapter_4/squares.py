print("Understabable way".upper())
squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)

print("\n")

print("More efficient way".upper())
squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)
print("\n")

print("List comprenhensions".upper())
squares = [value**2 for value in range(1,11)]
print(squares)
print("\n")

print("Uses min() max() sum()".upper())
print(min(squares))
print(max(squares))
print(sum(squares))
print("\n")

print("Other way to do it".upper())
minimum_number = min(squares)
maximum_number = max(squares)
sum_number = sum(squares)
numbers = [minimum_number , maximum_number , sum_number]
print(numbers)
print("\n")


print("Other way to do it".upper())
numbers = [min(squares) , max(squares) , sum(squares)]
print(numbers)
print("\n")

print("Other way to do it with different result".upper())
numbers = [min(squares) , max(squares) , sum(squares)]
for numbers in numbers:
	print(numbers)

