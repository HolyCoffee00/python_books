million = [value for value in range(1,1000001)]
maximum_number = max(million)
minimum_number = min(million)
adding_number = sum(million)
result = [maximum_number , minimum_number , adding_number]
print(result)
print("\n")

for oddnumber in range(1,21,2):
	print(oddnumber)
print("\n")

for threes in range(3,31,3):
	print(threes)
print("\n")

cubes = []
for value in range(1,11):
	cube = value**3
	cubes.append(cube)
print(cubes)
