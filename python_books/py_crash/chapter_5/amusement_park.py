age_input = input("Welcome to the museum, i will register you, How old are you?: ")
age = age_input

if int(age) < 4:
    print("Your admission cost is 0$")
elif int(age) < 18:
    print("Your admission cost is 5$")
elif int(age) < 65:
    print("Your admission cost is 10$")
else:
    print("Your admission cost is 0$")
print("\n")

age_input = input("Welcome to the museum, i will register you, How old are you?: ")
age = age_input

if int(age) < 4:
    price = 0
elif int(age) < 18:
    price = 5
elif int(age) < 65:
    price = 10
else:
    price = 0

print("Your admission cost is: " + str(price) + "$")


