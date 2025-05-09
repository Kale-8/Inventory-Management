# List to store all products in the inventory
products_list:list[dict] = []

# List of lambda functions for different alert messages using ANSI color codes
# Each lambda prints a colored message for different scenarios
alerts:list = [
    lambda: print(f'\n{'\033[91m'}El numero o carácter ingresado es incorrecto, ingresalo nuevamente{'\033[97m'}'),  # Error for invalid input
    lambda: print(f'{'\n\033[91m'}El producto no se encuentra en el inventario'), # Error for product not found
    lambda name: print(f'\n{'\033[92m'}{name.capitalize()} se ha añadido'), # Success for product added
    lambda name: print(f'\n{'\033[92m'}{name.capitalize()} se ha actualizado'), # Success for product updated
    lambda name: print(f'\n{'\033[91m'}{name.capitalize()} se ha eliminado del inventario'), # Success for product deleted
    lambda: print(f'{'\n\033[91m'}Opción no disponible'), # Error for an invalid option
    lambda: print(f'{'\n\033[91m'}El producto ya existe en el inventario')
]

def validation(text:str, condition)->float:
    """Validates user numeric input with a given condition"""
    while True:
        try:
            number:float = float(input(f'\n{text}'))
            if condition(number): return number  # Returns number if the condition is met
            alerts[0]() # Shows error if condition fails
        except ValueError: alerts[0]() # Shows an error if input is not a number

def add_product(name:str,price:float,amount:float)->None:
    """Adds new product to inventory with name, price and amount"""
    if not any(next(iter(producto)) == name.lower().strip() for producto in products_list): # Validates if the product is already in products_list
        full_product:dict = {name.lower().strip(): (price, amount, price * amount)} # Creates a product with subtotal calculated
        products_list.append(full_product)
        alerts[2](name) # Shows success message
    else: alerts[6]() # Product already exists

def search_product(name:str)->dict:
    """Searches for a product by name and returns the product dict or empty dict if not found"""
    for product in products_list:
        if next(iter(product)) == name.lower().strip(): return product
    return {}

def update_price(name:str)->None:
    """Updates the price of an existing product and recalculates its subtotal"""
    flag:bool = True
    for product in products_list:
        product_name:str = next(iter(product))
        if product_name == name.lower().strip():
            product[product_name] = list(product[product_name]) # Convert tuple to list for modification
            product[product_name][0] = validation('\nIngresa el nuevo precio del producto: ', lambda x: x > 0)
            product[product_name][2] = float(product[product_name][0] * product[product_name][1]) # Recalculate subtotal
            product[product_name] = tuple(product[product_name]) # Convert back to tuple
            flag = False
    if flag: alerts[1]() # Product not found
    else: alerts[3](name) # Success message

def delete_product(name:str)->None:
    """Removes a product from the inventory"""
    flag: bool = True
    for product in products_list:
        if next(iter(product)) == name.lower().strip(): products_list.remove(product)
        flag = False
    if flag: alerts[1]() # Product not found
    else: alerts[4](name) # Success message

def calculate_total_value(value:float)->None:
    """Displays formatted inventory details including products and total value"""
    print(f'\n{'\033[96m'}')
    print('─' * 40)
    print('DETALLES DEL INVENTARIO')
    print('─' * 40)
    for product in products_list:
        product_name:str = next(iter(product))
        print(f"{'Producto':<20}{product_name.capitalize():>20}")
        print(f"{'Cantidad':<20}{product[product_name][1]:>20}")
        print(f"{'Precio unitario':<20}{f'${product[product_name][0]:.2f}':>20}")
        print(f"{'Subtotal':<20}{f'${product[product_name][2]:.2f}':>20}")
        print('─' *40)
    print(f"{'Total':<20}{f'${value:.2f}':>20}")
    print('─' * 40)

def main()->None:
    """Main program loop with a menu for inventory management"""
    print(f'\n{'\033[1m'}{'\033[93m'}Bienvenido al sistema de gestión de inventario')
    flag:bool = True
    while flag:
        try:
            # Display a menu and get a user option
            option:int = int(input(f'\n{'\033[97m'}1. Añadir producto\n2. Buscar producto\n3. Actualizar precio\n4. Eliminar producto\n5. Calcular el valor total del inventario\n{'\033[91m'}6. Salir\n\n{'\033[97m'}Ingresa una opción: '))
            match option:
                case 1: # Add a new product
                    add_product(str(input('\nIngresa el nombre del producto: ')),
                              validation('\nIngresa el precio del producto: ', lambda x: x > 0),
                              validation('\nIngresa la cantidad del producto: ', lambda x: x >= 0))
                case 2: # Search and display product
                    product:dict = search_product(str(input('\nIngresa el nombre del producto que deseas buscar: ')))
                    if product != {}:
                        print(f'{'\033[96m'}─' * 50)
                        print(f"\n{'Producto':<20}{'Precio':^10}{'Cantidad':^10}{'Subtotal':>10}")
                        print("─" * 50)
                        print(f"{next(iter(product)).capitalize():<20}{f'${product[next(iter(product))][0]:.2f}':^10}{product[next(iter(product))][1]:^10}{f'${product[next(iter(product))][2]:.2f}':>10}")
                        print('─' * 50)
                    else: alerts[1]()
                case 3: update_price(str(input('\nIngresa el nombre del producto que deseas actualizar: ')))
                case 4: delete_product(str(input('\nIngresa el nombre del producto que deseas eliminar: ')))
                case 5: # Calculate and display the total inventory value
                    total_value:float = sum(map(lambda x: x[next(iter(x))][2], products_list))
                    calculate_total_value(total_value)
                case 6: flag = False # Exit program
                case _: alerts[5]() # Invalid option
        except ValueError: alerts[0]() # Invalid input

# Program entry point
main()