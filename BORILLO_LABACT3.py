name = input("Good day! What is your name? ")
print("Welcome " + name.upper() + "!")
userinp = input("Would you like to buy apples at a rate of 20.0? ")
userinp = userinp.upper()
if userinp == "YES":
    apples = float(input("How many? "))
else:
    apples = 0
    print("")
userinp = input("Would you like to buy mangoes at a rate of 15.0? ")
userinp = userinp.upper()
if userinp == "YES":
    mangoes = float(input("How many? "))
else:
    mangoes = 0
    print("")
userinp = input("Would you like to buy oranges at a rate of 10.0? ")
userinp = userinp.upper()
if userinp == "YES":
    oranges = float(input("How many? "))
else:
    oranges = 0
    print("")
price = (apples*20) + (mangoes*15) + (oranges*10)
apprice = (apples*20)
manprice = (mangoes*15)
orprice = (oranges*10)
if price >= 200:
    discount = (price*0.20)
    final = price - discount
else:
    discount = 0
    final = price
    print("")

print("Here is the list of the items you bought!"
      "\n" + str(apples) + " pcs. of apples --------------- " + "Php " + str(apprice))
print(str(mangoes) + " pcs. of mangoes --------------- " + "Php " + str(manprice))
print(str(oranges) + " pcs. of oranges --------------- " + "Php " + str(orprice))
print("=====================================")
print("Total: " + str(price))
print("")
print("Hello " + name.upper())
print("Total Amount: ======================= " + str(final))
if discount <= 0:
    print()
else:
    print("Discount: ======================= " + str(discount))
pay = float(input("Cash Tendered: ======================= "))
change = pay - final


if change >= 0:
    print("Change: ======================= " + str(change))
    print("Thanks for buying!")
else:
    print("That's not enough money. Please buy again.")
