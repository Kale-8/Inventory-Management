
# Inventory Manager in Python 🛒

This is a simple Python program to help manage a store's inventory. It lets you add, search, update, and delete products, and also calculate the total value of everything in stock. It's a great little project for learning how to use lists, dictionaries, tuples, and functions in Python!

## 🔧 What Can You Do With This?

- **Add new products**: Just enter the name, price, and quantity. Done!
- **Search for products**: Type the name and get all the details.
- **Update prices**: Change the price of any product already in the inventory.
- **Delete products**: Remove products that are no longer available.
- **See total inventory value**: Quickly get the total worth of your stock.

## 📦 How It Works

The inventory is stored as a list of dictionaries. Each product is saved like this:

```python
{"apple": (1.50, 10, 15.00)}  # name: (price, quantity, subtotal)
```

The subtotal (price × quantity) is updated whenever changes are made.

We also use a few **lambda functions** for calculating totals and showing colored alerts in the terminal (just for fun and clarity).

## 🧠 Structure of the Code

- `add_product`: Adds a new product.
- `search_product`: Looks for a product by its name.
- `update_price`: Lets you change the price of a product.
- `delete_product`: Deletes a product from the inventory.
- `calculate_total_value`: Uses a lambda to sum everything up.
- `main`: Runs the program with a menu so you can choose what to do.

Everything is wrapped in functions, and it’s interactive — the user chooses what they want to do from a menu.

## 🚨 Error Handling

We’ve included some friendly checks to make sure:
- You only enter numbers where needed.
- You can’t search or delete something that isn’t there.
- You get clear, colored messages when something goes wrong or right.

## ▶️ How to Run

1. Open your terminal or IDE.
2. Run the Python file:
   ```bash
   python inventory_manager.py
   ```
3. Follow the menu prompts!

## 📝 Notes

- This project is meant for beginners to intermediate learners.
- Make sure to test it with different scenarios to see how it reacts.
- If you'd like to improve it, maybe try saving the data to a file or adding a GUI.

Have fun managing your inventory!