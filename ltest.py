def colacalcu():
    print("Good day, please input 50 cents to get your cola. This machine only accepts " + str((25, 10, 5)))
    cost = 50
    while cost > 0:
        validIn = (25, 10, 5)
        userIn = int(input("Insert Coin: "))
        if userIn in validIn:
            cost = cost - userIn
            if 0 > cost:
                print("Your change: " + str(cost * -1))
            elif 0 == cost:
                pass
            else:
                print("Amount due: " + str(cost))
        else:
            print("This machine only accepts " + str(validIn))
    print("Thank you for purchasing!")

colacalcu()