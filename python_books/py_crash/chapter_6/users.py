user_0 = {
    "username": "efermi",
    "first name": "enrico",
    "last name": "fermi",
}
user_1 = {
    "username": "carlosmal",
    "first name": "carlos",
    "last name": "maldonado",
}
user_2 = {
    "username" : "danigonz",
    "first name": "daniela",
    "last name": "gonzales",
}
people = [user_0 , user_1 , user_2]
for users in people:
    for k, v in users.items():
        if k == "username":
            print("users data:".upper())
        if k == "username":
            print("  " + k.title() + ":")
            print("\t" + v + ".")
        else:
            print("  " + k.title() + ":")
            print("\t" + v.title() + ".")
    if k == "last name":
        print("\n")
#for k, v in user_0.items():
#    print("\nKey: " + k.title())
#    print("Value: " + v.title())

#for key, value in user_0.items():
#    print("\nKey: " + key.title())
#    print("Value: " + value.title())