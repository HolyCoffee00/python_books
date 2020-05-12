#3-4
guests = ["rivas" , "coso" , "gabriel" , "gabo"]
print("Come to my party, message to: " + guests[0].title())
print("Come to my party, message to: " + guests[1].title())
print("Come to my party, message to: " + guests[2].title())
print("Come to my party, message to: " + guests[3].title() + "\n")
#3-5
print("Gabo can't go to my party so i will invite other person")
guests[3] = "orlando"
print("Come to my party, message to: " + guests[0].title())
print("Come to my party, message to: " + guests[1].title())
print("Come to my party, message to: " + guests[2].title())
print("Come to my party, message to: " + guests[3].title() + "\n")
#3-6
print("I can invite more people")
guests.insert(0,"roger")
guests.insert(2,"ricky")
guests.append("manuel")
print("Come to my party, message to: " + guests[0].title())
print("Come to my party, message to: " + guests[1].title())
print("Come to my party, message to: " + guests[2].title())
print("Come to my party, message to: " + guests[3].title())
print("Come to my party, message to: " + guests[4].title())
print("Come to my party, message to: " + guests[5].title())
print("Come to my party, message to: " + guests[6].title() + "\n")
#3-7
print("I'm so sorry i only can bring 3 people")
manuel_popped = guests.pop()
ricky_popped = guests.pop(2)
roger_popped = guests.pop(0)
orlando_popped = guests.pop(3)
print("I'm sorry you can't come today, i am out of espace, message to: " + manuel_popped.title())
print("I'm sorry you can't come today, i am out of espace, message to: " + ricky_popped.title())
print("I'm sorry you can't come today, i am out of espace, message to: " + roger_popped.title())
print("I'm sorry you can't come today, i am out of espace, message to: " + orlando_popped.title() + "\n")

print("You still invited to my party tonight " + guests[0].title())
print("You still invited to my party tonight " + guests[1].title())
print("You still invited to my party tonight " + guests[2].title() + "\n")

del guests[0]
del guests[0]
del guests[0]

print(guests)

