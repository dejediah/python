def wordbank():
    bank = []
    userin = "y"
    count = 0

    while (userin.lower() == "y" ):
        word =  input("Enter a word: ")
        bank.append(word)
        userin = input("Try again? Y/y or N/n ")
        count = count + 1

    print(bank)
    print(f"Total words: {count}")

wordbank()
