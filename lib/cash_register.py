#!/usr/bin/env python3


# Purpose: A Cash Register that can:
# 1.Add items of varying quantities and prices
# 2.Calculate discounts
# 3.Keep track of what's been added to it
# 4.Void the last transaction - will remove the last transaction from the total


class CashRegister:
    def __init__(self, discount=0):
        """
        Initialize the cash register with a discount and an empty cart.
        """
        self.discount = discount
        self.items = []  # Store items as a list of dictionaries
        self.total = 0

    def add_item(self, title, price, quantity=1):
        """Add items to items with their title, price and quantity"""
        self.items.append({"title": title, "price": price, "quantity": quantity})
        self.total += price * quantity

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.2f}")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            last_item = self.items.pop()  # Get the last item's details
            last_item_price = last_item["price"]
            last_item_quantity = last_item["quantity"]
            self.total -= last_item_price * last_item_quantity
        else:
            print("No items to void.")
