try:
    print("Hi! I'm going to help you calculate your net salary.")
    gross = input("What is your gross salary?")
    gross = float(gross)
    children = input("How many children do you have?")
    children = int(children)
except ValueError:
    print("One of the numbers was invalid :(")
    exit(1)
else:
    if gross < 0:
        print("You cannot have negative salary :O")
        exit(1)
    elif children < 0:
        print("I would be impressed if you had negative children :O")
        exit(1)
    elif gross < 1000.0:
        net = gross*(0.9 + children/100)
        if (0.9 + children/100) > 1:
            net = gross  # you cannot get profit from tax deduction even if you have a lot of children
        print("Your net salary is", net)
    elif gross < 2000.0:
        net = gross*(0.88 + children/100)
        if (0.88 + children/100) > 1:
            net = gross  # you cannot get profit from tax deduction even if you have a lot of children
        print("Your net salary is", net)
    elif gross < 4000.0:
        net = gross*(0.86 + children/200)
        if (0.86 + children/200) > 1:
            net = gross  # you cannot get profit from tax deduction even if you have a lot of children
        print("Your net salary is", net)
    else:  # gross > 4000
        net = gross*(0.82 + children/200)
        if (0.82 + children/200) > 1:
            net = gross  # you cannot get profit from tax deduction even if you have a lot of children
        print("Your net salary is", net)
finally:
    print("Thanks! Hope I helped you :)")