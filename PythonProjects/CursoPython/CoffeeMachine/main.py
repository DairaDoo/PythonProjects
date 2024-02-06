from coffee_menu import MENU

machine_still_working = True

# Coffee dispenser data
water = 300
milk = 200
coffee = 100
money = 0

# List of coffee to search for
coffee_list = [
    "espresso",
    "latte",
    "cappuccino",
]

while machine_still_working:

    user_coffee = input(" What would you like? (espresso/latte/cappuccino): ").lower()

    if user_coffee == "off":
        print("Machine turned off.")
        break

    elif user_coffee == "report":
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${round(money, 2)}")
        continue  # the program begins a new iteration.

    elif user_coffee not in coffee_list:
        print("Invalid option! Please enter a valid one.")
        continue  # the program begins a new iteration.

    print("Please insert coins.")

    try:
        quarter = float(input("How many quarter: ")) * 0.25  # 25 cents.
        dime = float(input("How many dime: ")) * 0.10  # 10 cents.
        nickles = float(input("How many nickles: ")) * 0.05  # 5 cents.
        pennies = float(input("How many pennies: ")) * .01  # 1 cents.

    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    user_money = quarter + dime + nickles + pennies

    if user_coffee == "espresso":
        if water < 50:
            print("Sorry there is not enough water.")
        if coffee < 18:
            print("Sorry there is not enough coffee.")
        if user_money < 1.5:
            print("Sorry that's not enough money. Money refunded.")
            user_money = 0

        if water >= 50 and coffee >= 18 and user_money >= 1.50:
            water -= MENU["espresso"]["ingredients"]["water"]
            coffee -= MENU["espresso"]["ingredients"]["coffee"]
            user_money -= MENU["espresso"]["cost"]
            money += user_money
            user_money = round(user_money, 2)

            if user_money > 0:
                print(f"Here is your ${round(user_money, 2)} change.")

            print("Here is your espresso ☕. Enjoy!! ")

    elif user_coffee == 'latte':
        if water < 200:
            print("Sorry there is not enough water.")
        if coffee < 24:
            print("Sorry there is not enough coffee.")
        if milk < 150:
            print("Sorry there is not enough milk.")
        if user_money < 2.5:
            print("Sorry that's not enough money. Money refunded.")
            user_money = 0

        if water >= 200 and milk >= 150 and coffee >= 24 and user_money >= 2.50:
            water -= MENU["latte"]["ingredients"]["water"]
            coffee -= MENU["latte"]["ingredients"]["coffee"]
            milk -= MENU["latte"]["ingredients"]["milk"]
            user_money -= MENU["latte"]["cost"]
            money += user_money
            user_money = round(user_money, 2)

            if user_money > 0:
                print(f"Here is you're ${round(user_money, 2)} change.")

            print("Here is your latte ☕. Enjoy!!")

    elif user_coffee == 'cappuccino':
        if water < 250:
            print("Sorry there is not enough water.")
        if coffee < 24:
            print("Sorry there is not enough coffee.")
        if milk < 100:
            print("Sorry there is not enough milk.")
        if user_money < 3.0:
            print("Sorry that's not enough money. Money refunded.")
            user_money = 0

        if water >= 250 and milk >= 100 and coffee >= 24 and user_money >= 3.0:
            water -= MENU["cappuccino"]["ingredients"]["water"]
            coffee -= MENU["cappuccino"]["ingredients"]["coffee"]
            milk -= MENU["cappuccino"]["ingredients"]["milk"]
            user_money -= MENU["cappuccino"]["cost"]
            money += user_money
            user_money = round(user_money, 2)

            if user_money > 0:
                print(f"Here is you're ${round(user_money, 2)} change.")

            print("Here is your cappuccino ☕. Enjoy!!")
