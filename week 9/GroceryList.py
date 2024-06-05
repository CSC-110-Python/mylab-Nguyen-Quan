class GroceryItemOrder:
    def __init__(self, name, quantity, price_per_unit):
        self.name = name
        self.quantity = quantity
        self.price_per_unit = price_per_unit

    def cost(self):
        return self.quantity * self.price_per_unit

    def __str__(self):
        return f"{self.quantity} x {self.name} and ${self.price_per_unit:.2f} for each"

    def get_quantity(self):
        return self.quantity

class GroceryList:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    @property
    def total_cost(self):
        return sum(item.cost() for item in self.items)

    def __str__(self):
        return '\n'.join(str(item) for item in self.items)

# Create grocery items
item1 = GroceryItemOrder("Oranges", 4, 0.5)
item2 = GroceryItemOrder("Bread", 2, 2.5)
item3 = GroceryItemOrder("Chicken", 1, 17.99)
item4 = GroceryItemOrder("Beef", 3, 7.99)
item5 = GroceryItemOrder("Vegetable", 2, 8.39)
item6 = GroceryItemOrder("Butter", 1, 1.99)
item7 = GroceryItemOrder("Ice-cream", 5, 1.99)
item8 = GroceryItemOrder("Pineapple", 2, 2.99)
item9 = GroceryItemOrder("Boba-tea", 1, 4.99)

# Create a grocery list and add items to it
grocery_list = GroceryList()
grocery_list.add(item1)
grocery_list.add(item2)
grocery_list.add(item3)
grocery_list.add(item4)
grocery_list.add(item5)
grocery_list.add(item6)
grocery_list.add(item7)
grocery_list.add(item8)
grocery_list.add(item9)

# Print out the items, quantities, cost per item, and total cost
print(grocery_list)
print(f"Total cost: ${grocery_list.total_cost:.2f}")


