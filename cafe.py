print("---Welcome to Oat's coffee---")
show_menu = input("\nPlease type 1 to show menu: ")

if show_menu == "1":
    print("\n---Choose the menu--- \n1. Espresso \n2. Cappucino \n3. Latte")
    choose_menu = input("\nSelect coffee: ")
    
    if choose_menu == "1":
        print("\n---Choose the type of the coffee--- \n1. Hot 55 baht \n2. Cold 60 baht")
        choose_type = input("\nSelect type: ")
        if choose_type == "1":
            print("---You chose hot Espresso 55 baht---")
            pay = int(input("\nInput your money: "))
            if pay >= 55:
                recieved = pay - 55
                print("You recieved a change of %d baht \n---Thank you---" % recieved)
            else:
                print("Not enough money \n---Please try again---")
        elif choose_type == "2":
            print("---You chose cold Espresso 60 baht---")
            pay = int(input("\nInput your money: "))
            if pay >= 60:
                recieved = pay - 60
                print("You recieved a change of %d baht \n---Thank you---" % recieved)
            else:
                print("Not enough money \n---Please try again---")

    elif choose_menu == "2":
        print("\n---Choose the type of the coffee--- \n1. Hot 55 baht \n2. Cold 60 baht")
        choose_type = input("\nSelect type: ")
        if choose_type == "1":
            print("---You chose hot Cappucino 55 baht---")
            pay = int(input("\nInput your money: "))
            if pay >= 55:
                recieved = pay - 55
                print("You recieved a change of %d baht \n---Thank you---" % recieved)
            else:
                print("Not enough money \n---Please try again---")
        elif choose_type == "2":
            print("---You chose cold Cappucino 60 baht---")
            pay = int(input("\nInput your money: "))
            if pay >= 60:
                recieved = pay - 60
                print("You recieved a change of %d baht \n---Thank you---" % recieved)
            else:
                print("Not enough money \n---Please try again---")

    elif choose_menu == "3":
        print("\n---Choose the type of the coffee--- \n1. Hot 55 baht \n2. Cold 60 baht")
        choose_type = input("\nSelect type: ")
        if choose_type == "1":
            print("---You chose hot Latte 55 baht---")
            pay = int(input("\nInput your money: "))
            if pay >= 55:
                recieved = pay - 55
                print("You recieved a change of %d baht \n---Thank you---" % recieved)
            else:
                print("Not enough money \n---Please try again---")
        elif choose_type == "2":
            print("---You chose cold Latte 60 baht---")
            pay = int(input("\nInput your money: "))
            if pay >= 60:
                recieved = pay - 60
                print("You recieved a change of %d baht \n---Thank you---" % recieved)
            else:
                print("Not enough money \n---Please try again---")

else:
    print("Sorry, something went wrong")
