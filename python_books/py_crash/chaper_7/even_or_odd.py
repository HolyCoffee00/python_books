user_numb = input("Tell me a number and i'll tell you id is even or odd: ")
user_numb = int(user_numb)

if user_numb % 2 == 0:
    print("The number " + str(user_numb) + " is even!")
else:
    print("The number " + str(user_numb) + " is odd!")