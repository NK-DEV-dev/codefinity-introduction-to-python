vegetables = ["tomatoes", "potatoes", "onions"]
vegetables.remove("onions")
vegetables.append("carrots")
vegetables.append("cucumbers")
print("Updated Vegetable Inventory: ", vegetables)
vegetables.sort()

if "carrots" in vegetables:
    print("Carrots are already in the list.")
if "cucumbers" in vegetables:
    print("Cucumbers are already in the list.")



# only add if not present
if "carrots" not in vegetables:
    vegetables.append("carrots")
else:
    print("Carrots are already in the list.")

if "cucumbers" not in vegetables:
    vegetables.append("cucumbers")
else:
    print("Cucumbers are already in the list.")
