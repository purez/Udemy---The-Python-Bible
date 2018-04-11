known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]

while True:
    print("Hi! My names is Travis")
    name = input(str("What is your name? ").strip().capitalize())

    if name in known_users:
        print("Hello {}!".format(name))
        remove = input(str("Would you like to be removed from the system? (y/n) ")).strip().lower()

        if remove == "y":
            known_users.remove(name)

        elif remove == "n":
            print("no problem, I didn't want you to leave anyway!")
    else:
        print("Hmmm I don't think I have met you yet {}".format(name))
        add_me = input(str("Would you like to be added to the system? (y/n)").strip().lower())
        if add_me == "y":
            known_users.append(name)
        
        elif add_me == "n":
            print("No worries, see you around!")
