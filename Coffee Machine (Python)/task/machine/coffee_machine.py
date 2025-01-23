WATER_PER_CUP = 200
MILK_PER_CUP = 50
BEANS_GRAM_PER_CUP = 15

def coffee_cups_remaining(water, milk, coffee):
    water_cups = water // WATER_PER_CUP
    milk_cups = milk // MILK_PER_CUP
    coffee_beans = coffee // BEANS_GRAM_PER_CUP
    return min(water_cups, milk_cups, coffee_beans)

water_remaining = int(input("Write how many ml of water the coffee machine has: "))
milk_remaining = int(input("How many ml of milk the coffee machine has: "))
coffee_beans_remaining = int(input("Write how many grams of coffee beans the coffee machine has: "))

total_remaining_coffee_cups = coffee_cups_remaining(water_remaining, milk_remaining, coffee_beans_remaining)
coffee_cups_requested = int(input("Write how many cups of coffee you will need: "))

if total_remaining_coffee_cups == coffee_cups_requested:
    print("Yes, I can make that amount of coffee")
elif total_remaining_coffee_cups > coffee_cups_requested:
    print(f"Yes, I can make that amount of coffee (and even {total_remaining_coffee_cups - coffee_cups_requested} more than that)")
else:
    print(f"No, I can make only {total_remaining_coffee_cups} cups of coffee")