usernames = ["deadstar" , "crazyboy01" , "dabid" , "admin" , "putita01"]

if usernames:
    print()
else:
    print("We need to find some users")

for usernames in usernames:
    if usernames == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + usernames + ", thanks for logging in again")
print("\n")

current_users = ["Deadstar".lower() , "crazYboy01".lower() , "daBid".lower() , "admin".lower() , "putita01".lower()]
new_users = ["deadstar".lower() , "brother".lower() , "daddy".lower() , "ricoaqui".lower() , "Dabid".lower()]

for new_users in new_users:
    if new_users in current_users:
        print("This username already exist: " + new_users)
    else:
        print("This username is available: " + new_users)

cordinal_numbers = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]

for cordinal_numbers in cordinal_numbers:
    if cordinal_numbers == 1:
        print("1st")
    elif cordinal_numbers == 2:
        print("2nd")
    elif cordinal_numbers == 3:
        print("3rd")
    else:
        print(str(cordinal_numbers) + "th")


