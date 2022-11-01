#Anthony Novak, COP1500, 1:30pm Class
#My program is effectively a fun interaction with the AI known as BeepBoop.
#I plan to expand this much more in further iterations


#This section serves as an introduction and collects some basic information from the user and recalls it
print("Hello! My name is BeepBoop and you have just been selected\nto participate in a brief survey for $100!", end="\n\n")

firstName = str(input("What is your first name? "))
lastName = str(input("What is your last name? "))

print("\nIt's nice to meet you", firstName, lastName + "!", end="\n\n", sep=" ")

userAgeHumanYears = float(input("What is your age in human years? "))

#Calculates user's human year age into dog years
userAgeDogYears = (userAgeHumanYears * 7)
print("\nWow!", format(userAgeHumanYears,"0.0f"), "in human years is", format(userAgeDogYears,"0.0f"), "years old if you were a dog!", end="\n\n")

favColor = str(input("What is your favorite color? "))

print("\nSo you're", format(userAgeHumanYears,".0f"), "human years old and your favorite color is", favColor + ".\nI find that incredibly interesting!", end="\n\n", sep=" ")

#In this section, the user is given money for the following shopping interaction
walletAmount = 100.00
print("Thank you for answering my survey! I'm giving you $100!\nLet's use it to go shopping for a new outfit!", end="\n\n")

#Defining the store's prices
hawaiianShirtCost = 15
shortsCost = 12

#Prompts user for number of hawaiian shirts they want
numberShirts = float(input("\nThis very nice Hawaiian Shirt costs $15.00.\n\nHow many would you like to buy? "))

#Calculates how much money will be spent on hawaiian shirts alone
totalShirts = (hawaiianShirtCost * numberShirts)

#Prompts user for number of pairs of shorts they want
numberShorts = float(input("\nThis high quality pair of shorts only costs $12! What a steal!\n\nHow many would you like to buy? "))

#Calculates how much money will be spent on pairs of shorts alone
totalShorts = (shortsCost * numberShorts)

#Calculates the total cost of hawaiian shirts and pairs of shorts together
totalCost = (totalShirts + totalShorts)

#Checkout process commences here
print("\nYou have", int(numberShirts), "hawaiian shirt(s) and", int(numberShorts), "pair(s) of shorts in your cart.", end="\n\n")
print("Your balance due is: $" + format(totalCost,"0.2f"), end="\n\n")

#Conditional statement to determine if the user has enough money in their wallet for the purchase
if totalCost < walletAmount:

    #Various basic calculations that define new values for later use
    amountTendered = float(input("How much money will you give the cashier? "))
    balanceAmount = (totalCost - amountTendered)
    changeAmount = (amountTendered - totalCost)
    newWalletBalance = (walletAmount - totalCost)

    #Handles the condition where the user attempts to tender more money than exists in their wallet
    if (amountTendered > walletAmount):
        print("\nHey! I never gave you that much money!", end="\n\n")
        print("Please leave the store by closing out of this program and restarting it.\nThank you!\nHave a nice day!")

    #Continues the transaction smoothly
    else:
        
        #If the user pays off their balance immediately
        if (balanceAmount == 0):
            print("\nThank you for your purchase! Enjoy your new outfit!", end="\n\n")
            print("You now currently have $" + format(newWalletBalance,"0.2f") + " left to spend!", end="\n\n")
        

        #If the user still has a balance remaining, this is their last chance to pay it
        elif (balanceAmount > 0):
            print("\nYou only gave the cashier $", format(amountTendered,"0.2f"), ". Your balance due is: $", format(balanceAmount,"0.2f"), end="\n\n", sep="")
            lastChanceBalance = float(input("Please pay your remaining balance now. It is your very last chance!\n\nHow much will you pay? "))

            #If the user refuses to pay the full remaining balance, BeepBoop becomes very angry and starts making irrational decisions
            if (lastChanceBalance != balanceAmount):
                print("\nYou have made the great BeepBoop ANGRY!!", end="\n\n")
                print("You are going straight to jail!!", end="\n\n")
                print("And your grade on this assignment is now a zero!!!", end="\n\n")
    
            #If the user pays off their full balance, BeepBoop is pleased and the user gets to live to see another day
            else:
                print("\nThank you for your purchase! I was starting to get worried that you\nweren't going to pay off your remaining balance.", end="\n\n")
                print("Trust me, you don't want to know what would have happened otherwise :)", end="\n\n")
                print("*NERVOUS LAUGHTER*\n" * 5)

        #If the user decides to leave a generous tip
        else:
            
            #Calculates the tip amount
            tipAmount = (amountTendered - totalCost)
            print("\nHey thanks for the $", format(tipAmount,"0.2f"), " tip, ", str(firstName), end="\n\n", sep="")

            #Allows calculation of the tip amount into the total that was spent
            if tipAmount > 0:

                #Calculates new amounts remaining
                totalSpent = (totalCost + tipAmount)
                newWalletAmount = (walletAmount - totalSpent)

                print("\nWow you spent $" + format(totalSpent,"0.2f") + " and currenly have $" + format(newWalletAmount,"0.2f") + " left to spend!")
                
            #Only possible if the user entered a negative number, aka tried to rob the store.
            else:
                print("It seems you must have entered a negative value at some point. Please restart the program and try again!")

#Kicks the user out of the store if they don't have enough money
else:   
    print("Oh no! It looks like you don't have enough money to purchase these items!\n\n")
    print("Please leave the store by closing out of this program and restarting it.\nThank you!\nHave a nice day!", end="\n\n")

#Math operations beginning
print("\nWow that shopping spree was fun!", end="\n\n")
print("But I have a much more fun activity for us to do!", end="\n\n")
print("We are going to experiment around with some number calculations!", end="\n\n")

#Exponent operator
exponentValue1 = float(input("Please enter a positive whole number between 1-10: "))
exponentValue2 = float(input("Please enter a second positive whole number between 2-4: "))
newExponentValue = float(exponentValue1 ** exponentValue2)
print("You entered ", format(exponentValue1,"0.0f"), " to the power of ", format(exponentValue2,"0.0f"), sep="")
print("Your new number is: ", format(newExponentValue,"0.0f"), sep="", end="\n\n")

#Division operator
totalMonkeys = 25
print("There are 25 monkeys who would like to jump on the bed, but the bed can only hold 5 monkeys at a time.")
numberMonkeysPerGroup = float(input("The monkeys must be split into even groups. How many groups will there be? "))

if (totalMonkeys / numberMonkeysPerGroup) == 5:
    print("\nThat is correct! Good Job!", end="\n\n")
else:
    print("\nI'm sorry that's the incorrect answer!", end="\n\n")

#Remainder operator
print("Since we divided 25 monkeys in to 5 even groups of 5,")
howManyMonkeys = float(input("How many monkeys were reamining? "))

if (howManyMonkeys == (totalMonkeys % numberMonkeysPerGroup)):
    print("\nThat is correct! Good job!", end="\n\n")
else:
    print("\nI'm sorry that's the incorrect answer!", end="\n\n")

#Floor Division operator
newMonkeyAmount = 19
print("Let's say there were only 19 monkeys this time,")
evenGroupsNumber = float(input("How many even groups of five will there be this time? "))

if (evenGroupsNumber == (newMonkeyAmount // numberMonkeysPerGroup)):
    print("That is correct! Good job!", end="\n\n")
else:
    print("I'm sorry that's the incorrect answer!", end="\n\n")





