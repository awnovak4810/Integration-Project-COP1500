"""Anthony Novak's Integration Project for COP1500"""
__author__ = "Anthony Novak"

# Anthony Novak, COP1500, 1:30pm Class
# My program is effectively a fun interaction with the AI known as BeepBoop
# As well as other functions to show my progress in the class.

# Import math library for later use
import math


def getIntInput():
    """
    The purpose of this function is to ensure that the user enters an
    integer when asked, in order to prevent errors from crashing the program.
    user_input is used generically for any inputs requiring an integer,
    and therefore makes this a value-returning function.
    """
    control = True
    while control:
        try:
            user_input = int(input())
            control = False
        except:
            print("Invalid input. Please enter a valid number.")
    return user_input


# Introduction
print("Hello! My name is BeepBoop and you have just been selected")
print("to participate in a brief survey for $100!", end="\n\n")

firstName = str(input("What is your first name? "))
lastName = str(input("What is your last name? "))

print("\nIt's nice to meet you", firstName, lastName + "!", end="\n\n")

print("What is your age in human years?")
userAgeHumanYears = getIntInput()

# Calculates user's human year age into dog years
userAgeDogYears = (userAgeHumanYears * 7)
print("\nWow!", format(userAgeHumanYears, "0.0f"), "in human years is")
print(format(userAgeDogYears, "0.0f"), "years old if you were a dog!",
      end="\n\n")

favColor = input("What is your favorite color? ")

print("\nSo you're", format(userAgeHumanYears, ".0f"), "human years old")
print("and your favorite color is",
      favColor + ".\nI find that incredibly interesting!", end="\n\n")

# The user is given money for a shopping interaction
walletAmount = 100.00
print("Thank you for answering my survey! I'm giving you $100!")
print("Let's use it to go shopping for a new outfit!", end="\n\n")

# Defining the store's prices
hawaiianShirtCost = 15
shortsCost = 12

# Prompts user for number of hawaiian shirts they want
print("This very nice Hawaiian Shirt costs $15")
print("How many would you like to buy? ")
numberShirts = getIntInput()

# Calculates how much money will be spent on hawaiian shirts alone
totalShirts = (hawaiianShirtCost * numberShirts)

# Prompts user for number of pairs of shorts they want
print("This pair of shorts only costs $12! What a steal!")
print("How many would you like to buy?")
numberShorts = getIntInput()

# Calculates how much money will be spent on pairs of shorts alone
totalShorts = (shortsCost * numberShorts)

# Calculates the total cost of hawaiian shirts and pairs of shorts together
totalCost = (totalShirts + totalShorts)

# Checkout process commences here
print("\nYou have", int(numberShirts), "hawaiian shirt(s) and")
print(int(numberShorts), "pair(s) of shorts in your cart.", end="\n\n")
print("Your balance due is: $" + format(totalCost, "0.2f"), end="\n\n")

# Determines if the user has enough money in their wallet for the purchase
if totalCost < walletAmount:

    # Various basic calculations that define new values for later use
    print("How much money will you give the cashier? ")
    amountTendered = getIntInput()
    balanceAmount = (totalCost - amountTendered)
    changeAmount = (amountTendered - totalCost)
    newWalletBalance = (walletAmount - totalCost)

    # Handles when the user tries to use more money than is in their wallet
    if amountTendered > walletAmount:
        print("Hey! I never gave you that much money!", end="\n\n")

    # Continues the transaction smoothly
    else:

        # If the user pays off their balance immediately
        if balanceAmount == 0:
            print("\nThank you for your purchase! Enjoy your new outfit!",
                  end="\n\n")
            print("You currently have $" + format(newWalletBalance, "0.2f") +
                  " left to spend!", end="\n\n")

        # If the user has a balance remaining, this is their last chance to pay
        elif balanceAmount > 0:
            print("\nYou only gave the cashier $",
                  format(amountTendered, "0.2f"), ".", sep="")
            print("Your balance due is: $", format(balanceAmount, "0.2f"),
                  end="\n\n", sep="")
            print("Please pay your remaining balance now.")
            print("How much will you pay?")
            lastChanceBalance = getIntInput()

            # If the user refuses to pay the full balance,
            # BeepBoop becomes angry and starts making irrational decisions
            if lastChanceBalance != balanceAmount:
                print("You have made the great BeepBoop ANGRY!!")
                print("You are going straight to jail!!")
                print("And your grade on this assignment is now a zero!!!",
                      end="\n\n")

            # If the user pays off their full balance,
            # BeepBoop is pleased and the user gets to live to see another day
            else:
                print("Thank you for your purchase!")
                print("I was starting to get worried that you")
                print("weren't going to pay off your remaining balance.",
                      end="\n\n")
                print("Trust me, you don't want to know")
                print("what would have happened otherwise :)", end="\n\n")
                print("*NERVOUS LAUGHTER*\n" * 5)

        # If the user decides to leave a generous tip
        else:

            # Calculates the tip amount
            tipAmount = (amountTendered - totalCost)
            print("\nHey thanks for the $", format(tipAmount, "0.2f"),
                  " tip, ", str(firstName), end="\n\n", sep="")

            # Allows calculation of the tip amount into the total spent
            if tipAmount > 0:

                # Calculates new amounts remaining
                totalSpent = (totalCost + tipAmount)
                newWalletAmount = (walletAmount - totalSpent)

                print("\nYou spent $" + format(totalSpent, "0.2f") +
                      " and currently have")
                print(
                    "$" + format(newWalletAmount, "0.2f") + " left to spend!")

            # Only possible if the user entered a negative number
            else:
                print("It seems you entered a negative at some point. Shame!")

# Kicks the user out of the store if they don't have enough money
else:
    print("Oh no! It appears you don't have the money to buy these items!\n")
    print("Thank you!\nHave a nice day!", end="\n\n")

# Math operations beginning
print("\nWow that shopping spree was fun!")
print("But I have a much more fun activity for us to do!")
print("We are going to experiment around with some number calculations!",
      end="\n\n")

# Exponent operator, while loop, OR
print("Let's take two numbers and find the exponent value of them.")

print("Please enter a positive whole number between 1-10:")
exponentValue1 = getIntInput()
while exponentValue1 < 1 or exponentValue1 > 10:
    print("Your number is invalid.")
    print("Please enter a positive whole number between 1-10:")
    exponentValue1 = getIntInput()

print("Please enter a second positive whole number between 2-4:")
exponentValue2 = getIntInput()
while exponentValue2 < 2 or exponentValue2 > 4:
    print("Your number is invalid.")
    print("Please enter a second positive whole number between 2-4:")
    exponentValue2 = getIntInput()
newExponentValue = float(exponentValue1 ** exponentValue2)
print("You entered ", format(exponentValue1, "0.0f"), " to the power of ",
      format(exponentValue2, "0.0f"), sep="")
print("That equals ", format(newExponentValue, "0.0f"), sep="", end="\n\n")

# Division operator
totalMonkeys = 25
print(
    "25 monkeys want to jump on the bed,")
print("but the bed can only hold 5 monkeys at once.")
print("The monkeys must be split into even groups.")
print("How many groups will there be?")
numberMonkeysPerGroup = getIntInput()

if (totalMonkeys / numberMonkeysPerGroup) == 5:
    print("\nThat is correct! Good Job!", end="\n\n")
else:
    print("\nI'm sorry that's the incorrect answer!", end="\n\n")

# Remainder operator
print("Since we divided 25 monkeys in to 5 even groups of 5,")
print("How many monkeys were remaining?")
howManyMonkeys = getIntInput()

if howManyMonkeys == (totalMonkeys % numberMonkeysPerGroup):
    print("\nThat is correct! Good job!", end="\n\n")
else:
    print("\nI'm sorry that's the incorrect answer!", end="\n\n")

# Floor Division operator
newMonkeyAmount = 19
print("Let's say there were only 19 monkeys,")
print("How many even groups of 5 monkeys will there be this time?")
evenGroupsNumber = getIntInput()

if evenGroupsNumber == (newMonkeyAmount // numberMonkeysPerGroup):
    print("That is correct! Good job!", end="\n\n")
else:
    print("I'm sorry that's the incorrect answer!", end="\n\n")


# Parameter passing and function definition
def getQuadratic(a, b):
    """
    This function serves to calculate the square root using the math library
    :param a: first value entered
    :param b: second value entered
    :return: the square root of the two numbers entered.
    """
    square = a ** 2 + b ** 2
    squareRoot = math.sqrt(square)
    return squareRoot


def main():
    """
    This function is static, in a way, by which the values are not entered
    by the user, but just serve to display that I know how to use the
    functions in Python for my project
    :return: the square root of the numbers 420 and 69.
    """
    print("Fun fact! The square root of the sum of squares of 420 and 69 is:",
          format(getQuadratic(420, 69), "0.2f"))


main()

# For, In, and Range loop
print("\nWould you like me to display your name 10 times?")
userInput = str(input("Please type 'y' for yes, or 'n' for no. "))
if userInput == 'y':
    for name in range(10):
        print(firstName, lastName)
elif userInput == 'n':
    print("Aw, you're no fun. But that's okay.", end="\n\n")
else:
    print("It seems you didn't understand the prompt, but that's okay.")
    print("We'll just have to find something else for you to do!", end="\n\n")

# Shortcut operator
salary = 80000
bonus = 15000

print("\nYour salary is $", format(salary, '0.2f'), sep="")
print("And your annual bonus is $", format(bonus, '0.2f'), sep="")
salary += bonus
print("Therefore, your total annual income is $", format(salary, '0.2f'),
      sep="")

# And and not boolean operators

print("What's the last score you received on an assignment out of 100%?")
grade = getIntInput()
if grade > 90 and grade <= 100:
    print("Wow you're an excellent student! Congratulations!")
elif grade > 80 and grade < 90:
    print("What a good grade! You did so well! Good job!")
elif grade > 70 and grade < 80:
    print("You passed with an average score, good job!")
elif not (grade != 69):
    print("Nice.")
elif grade > 60 and grade < 70:
    print("It seems you need to study more, but congratulations on passing!")
else:
    print("You failed your assignment, you'll do great next time!")

print("You have reached the end of my COP1500 integration project.")
print("I hope you enjoyed your time and that you didn't find any issues")
print("with my code. I hope you have a great day!")
print("\n\n*BeepBoop has left the chat*")
