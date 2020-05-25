prompt = "\nTell me something and i will print it back to you!:"
prompt += "\nEnter quit to end the program.\n"
prompt += ">>>"
message = ""

while message != "quit":
    message = input(prompt)
    if message != "quit":
        print("\n>>>" + message)

#FLAG USING
prompt = "\nTell me something and i will print it back to you!:"
prompt += "\nEnter quit to end the program.\n>>>"

active = True
while active:
    message = input(prompt)
    if message == "quit":
        active = False
    else:
        print(message)