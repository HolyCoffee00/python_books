responses = {}
polling_active = True

while polling_active:
    name = input("What is your name?: ").title()
    response = input("Wich mountain would you like to climb: ").title()

    responses[name] = response

    respeat = input("Someone else wanna take this poll? (yes/no): ").lower()
    if respeat == "no":
        polling_active = False
print("------ POLL RESULTS ------")
for n, r in responses.items():
    print(n + " want's to climb the mountain " + r)
