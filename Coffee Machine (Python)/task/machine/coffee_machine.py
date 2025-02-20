import textwrap

class CoffeeMachine:
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def get_status(self):
        status = textwrap.dedent(f"""
                 The coffee machine has:
                 {self.water} ml of water
                 {self.milk} ml of milk
                 {self.beans} g of coffee beans
                 {self.cups} disposable cups
                 ${self.money} of money
                 """)
        return status

    def reduce_supplies(self, water=0, milk=0, beans=0, cups=1):
        self.water -= water
        self.milk -= milk
        self.beans -= beans
        self.cups -= cups

    def increase_supplies(self, water=0, milk=0, beans=0, cups=0):
        self.water += water
        self.milk += milk
        self.beans += beans
        self.cups += cups

    def fill(self):
        water = int(input("Write how many ml of water you want to add: "))
        milk = int(input("Write how many ml of milk you want to add: "))
        beans = int(input("Write how many grams of coffee beans you want to add: "))
        cups = int(input("Write how many disposable cups you want to add: "))
        self.increase_supplies(water, milk, beans, cups)

    def take(self):
        money_take = self.money
        self.money = 0
        print(f"I gave you ${money_take}")

    def buy_coffee(self):
        menu_option = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: "))
        if menu_option == 1:
            self.reduce_supplies(water=250, beans=16)
            self.money += 4
        if menu_option == 2:
            self.reduce_supplies(water=350, milk=75, beans=20)
            self.money += 7
        if menu_option == 3:
            self.reduce_supplies(water=200, milk=100, beans=12)
            self.money += 6


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)

print(coffee_machine.get_status())
action = input("Write action (buy, fill, take):")
if action == "buy":
    coffee_machine.buy_coffee()
    print(coffee_machine.get_status())
if action == "fill":
    coffee_machine.fill()
    print(coffee_machine.get_status())
if action == "take":
    coffee_machine.take()
    print(coffee_machine.get_status())
