MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18, }, "cost": 1.5, },
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24, }, "cost": 2.5, },
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24, }, "cost": 3.0, }
}

resources = {"water": 300,
             'milk': 200,
             'coffee': 100,
             'money': 0}


def money(q, d, n, p):
    return (q * 0.25) + (d * 0.10) + (n * 0.05) + (p * 0.01)


def calculate(ow, drink_price):
    if ow > drink_price:
        change = ow - drink_price
        final = "{:.2f}".format(change)
        if final != 0.00:
            print(f"Here is ${final} in change.\n")
        else:
            print("You don't have any change.")
        return drink_price
    elif ow == drink_price:
        return drink_price
    else:
        return 0


def costa(c, r, ing):
    for i in ing:
        if ing[i] > r[i] or r[i] == 0:
            if i != 'money':
                print(f"Sorry, there is no enough {i}.")
        else:
            print('Please insert coins. \n[Warning: Only numbers(in numeric format) are allowed].\n')
            quarters = input("How many quarters?: ")
            dimes = input("How many dimes?: ")
            nickels = input("How many nickels?: ")
            pennies = input("How many pennies?: ")
            if quarters.isdigit() and dimes.isdigit() and nickels.isdigit() and pennies.isdigit():
                owo = money(int(quarters), int(dimes), int(nickels), int(pennies))
                if owo >= c:
                    r[i] = r[i] - ing[i]
                    print(f'Here is your {option.upper()}, Enjoy!!!')
                    r['money'] += calculate(owo, cost)
                else:
                    print("Sorry, that's not enough money.\nMoney refunded.")
                    break
                break
            else:
                print('You did enter the correct input format for one [or more] of the coins.'
                      ' Please try again.\n')


checking = {}

cost = 0
continual = True
print("WELCOME TO MY COFFEE MACHINE!!!!")
print("{If you wish to switch it off, just type 'off'.}")
print("{You can also get a report of the amount of ingredients remaining by typing 'report'}")

try:
    while continual:
        option = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if option in MENU.keys():
            checking = MENU[option]['ingredients']
            cost = MENU[option]['cost']

            costa(cost, resources, checking)

        elif option == 'report':
            for k in resources:
                if k == 'coffee':
                    print(f"{k}: {resources[k]}g")
                elif k == 'money':
                    print(f"{k}: ${resources[k]}")
                else:
                    print(f"{k}: {resources[k]}ml")

        elif option == 'off':
            continual = False
            print("Thank you for using my coffee machine. GoodBye.")

        else:
            print("You did not select a valid option!!!")
except KeyboardInterrupt:
    pass
