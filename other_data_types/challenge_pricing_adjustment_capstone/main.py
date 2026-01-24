grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)}

egg_category, egg_price, egg_stock = grocery_inventory["Eggs"]
if egg_price > 5:
    grocery_inventory["Eggs"] = (egg_category, egg_price - 1, egg_stock)
    print("Eggs are too expensive, reducing the price by $1.", egg_price)
else:
    print("The price of Eggs is reasonable.")

grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print("Inventory after adding Tomatoes: ",grocery_inventory)

milk_category, milk_price, milk_stock = grocery_inventory["Milk"]
if milk_stock < 10:
    milk_stock += 20
    grocery_inventory["Milk"] = (milk_category, milk_price, milk_stock)
    print("Milk needs to be restocked. Increasing stock by 20 units.", milk_stock)
else:
    print("Milk has sufficient stocked.")

apple_category, apple_price, apple_stock = grocery_inventory["Apples"]
if apple_price > 2:
    grocery_inventory.pop("Apple")
    print("Apples removed from inventory due to high price.")

print("Updated inventory: ", grocery_inventory)
    