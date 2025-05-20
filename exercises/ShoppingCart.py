# MIT License
# Copyright (c) 2025 Emir Baha Yıldırım
# Please see the LICENSE file for more details.

class ShoppingCart:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def add(self, name, price, quantity): # Add item to cart with name, price, quantity as properties.

        count = 0
        item = [name, price, quantity] # Create a tmp list using the properties given.

        for i in self.items: # Iterates through items already in the cart.

            if item[0] == i[0]: # Checks if the item exists.

                i[2] += item[2] # Adds the given quantity to previous one.
                count += 1
                break

        if count == 0: # Adds item if it doesn't exist already.

            self.items.append(item)

    def remove(self, name, quantity): # Remove item with name and quantity as properties.

        if not self.isEmpty(): # Checks if the ccart is empty.

            for item in self.items: # Iterates through the list to find the index.

                if (item[0] == name and
                    item[2] > quantity):
                    # Checks if the given quantity is less than the total in the list.
                    item[2] -= quantity # Removes said amount of items.
                    break

                elif item[0] == name and item[2] <= quantity:
                    self.items.remove(item) # Removes the item completely. Error handling.
                    break

        else:
            return "Cart empty."

    def total(self): # Calculates the total of the shopping cart.

        total = 0

        for item in self.items: # Iterates through all items.
            total += item[1] * item[2] # Calculates the total using the price of one and the quantity in cart.

        return total

    def show(self): # Shows what's in the cart.

        if not self.isEmpty(): # Checks if empty.
            return self.items # Returns cart as nested list.
        
        else: # Error handling.
            return "Cart empty."

"""
# Example Use:

cart = ShoppingCart()

cart.add("Apple", 3.5, 5)
cart.add("Papaya", 15, 1)
cart.add("Guava", 25, 1)
cart.add("Orange", 1.25, 1)
cart.add("Orange", 1.25, 2)
cart.add("Orange", 1.25, 5)
print(cart.show())
print(cart.total())
cart.remove("Orange", 2)
print(cart.show())
print(cart.total())
cart.remove("Papaya", 2)
print(cart.show())
print(cart.total())
cart.remove("Apple", 5)
print(cart.show())
print(cart.total())
cart.remove("Guava", 1)
cart.remove("Orange", 6)
cart.remove("Bus", 1)
print(cart.show())
print(cart.total())
"""
