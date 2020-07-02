def displayInventory(inventory):
  totItems = 0
  print("Inventory:")

  for k, v in inventory.items():
    print(f"{v} {k}")
    totItems += v
  print(f"Total number of items: {totItems}")


def addToInventory(inventory, addedItems):
  for i in addedItems:
    if i not in inventory:
      inventory[i] = 1
    else:
      inventory[i] += 1
  return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)

displayInventory(inv)

