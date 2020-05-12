favourite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
    "sergio": "python"
}
0
for name, language in favourite_languages.items():
    print(name.title() + "'s favourite language is " +
          language.title())
print("\n")

friends = ["phil" , "sarah" , "sergio"]
for name in favourite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() +
              ", i see your favourite lenguage is " +
              favourite_languages[name].title() + "!")
if "erin" not in favourite_languages.keys():
    print("\nErin please take our poll")
print("\n")

for names in sorted(favourite_languages):
    print(names.title() + ", thank you for taking the poll!")

print("\nThe following languages has been mentioned:")
for languages in set(favourite_languages.values()):
    print(languages.title())
###############################################
#Nesting
favourite_languages = {
    "jen": ["python" , "ruby"],
    "sarah": ["c"],
    "edward": ["ruby" , "c"],
    "phil": ["python", "java"],
    "sergio": ["python"]
}
for name, lang in favourite_languages.items():
    print("\n" + name.title() + "'s favorite language is ")
    for fav_lang in lang:
        print("\t" + fav_lang.title())


###############################################
print("\n")
rivas = {
    "first_name": "jesus",
    "last_name": "rivas",
    "age": "22",
    "aka": "el mocho"
}
print("My friends name is: " +
      rivas["first_name"].title() + " " +
      rivas["last_name"].title() + ", " +
      "he is " + rivas["age"] + " years old"
      " and his AKA is " + rivas["aka"].upper()
      )
