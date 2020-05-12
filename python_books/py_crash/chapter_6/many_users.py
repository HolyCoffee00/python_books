users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princenton",
        },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
        },
    }

for username, info in users.items():
    print("\nUsername: " + username)
    full_name = info["first"] + " " + info["last"]
    location = info["location"]

    print("User full name: " + full_name.title())
    print("User location: " + location.title())