Inventory = {
    '001': {'product': 'libro','title': 'vida', 'price': 8000, 'amount': 2, 'category': 'suspenso'},
    '002': {'product': 'libro','title': 'muerte', 'price': 2500, 'amount': 2,'category': 'terror'},
    '003': {'product': 'libro','title': 'la felicidad', 'price': 3000, 'amount': 3,'category': 'suspenso'},
    '004': {'product': 'libro','title': 'cien años de soledad', 'price': 1000, 'amount': 12,'category': 'romance'},
    '005': {'product': 'libro','title': 'la cuadra', 'price': 3000, 'amount': 5,'category': 'romance'}
}

def show_inventory():
    """Muestra el menu principal del inventario."""
    print("\nInventario")
    print("1. Registrar productos")
    print("2. Consultar productos")
    print("3. Actualizar productos")
    print("4. Eliminar productos")
    print("8. Salir")


def add_product():
    """Permite al usuario añadir un nuevo producto al inventario."""
    new_id = input("Enter a unique student ID: ")
    # Check if ID already exists
    if new_id in Inventory:
        print("Este producto ya está registrado")
    else:
        product = input("Ingrese el producto: ")
        title = input("Ingrese el titulo: ")
        category = input("Ingrese la categoria: ")
        while True:
            try:
                price = int(input("Ingrese el precio: "))
                amount = int(input("Ingrese la cantidad: "))
                Inventory[new_id] = {'product': product, 'title': title, 'category': category, 'price': price, 'amount': amount}
                print(f"El producto '{product}' ha sido agregado exitosamente.")
            except ValueError:
                print("Invalid age input.")
                continue
            break 

#search product by id
def search_product_by_id():
    """Permite buscar el producto por ID."""
    id_to_search = input("Ingrese el código del producto para ver las caracterizticas del producto: ")

    if id_to_search in Inventory: # Check if ID exists.
        print(f"Producto: {Inventory[id_to_search]['product']} Titulo: {Inventory[id_to_search]['title']} Precio:{Inventory[id_to_search]['price']} Cantidad:{Inventory[id_to_search]['amount']} Categoría:{Inventory[id_to_search]['category']}") # displays the product name, price, quantity.
    else:
        print("No se encontró el producto") # Product not found
        
def update_price():
    """Permite al usuario seleccionar un producto y actualizar su precio."""
    code_update = input("Ingrese el codigo del producto cuyo precio desea actualizar: ")
    if code_update in Inventory:
        new_product_str = input(f"Ingrese el nuevo nombre para {Inventory[code_update]['product']}:")
        new_title_str = input(f"Ingrese el nuevo titulo para {Inventory[code_update]['title']}:")
        new_price_str = input(f"Ingrese el nuevo precio para {Inventory[code_update]['price']}:")
        new_amount_str = input(f"Ingrese la nueva cantidad para {Inventory[code_update]['amount']}:")
        new_category_str = input(f"Ingrese la nueva categoría para {Inventory[code_update]['category']}:")
        try:    
            Inventory[code_update]['product'] = new_product_str
            print(f"El nombre del {Inventory[code_update]['product']} ha sido actualizado a {new_product_str}.")
            
            Inventory[code_update]['title'] = new_title_str
            print(f"El titulo del {Inventory[code_update]['product']} ha sido actualizado a {new_title_str}.")
            
            Inventory[code_update]['category'] = new_category_str
            print(f"La categoria del {Inventory[code_update]['product']} ha sido actualizado a {new_category_str}.")
            
            if int(new_price_str) < 0:
                print("no se permiten numeros negativos")
                return
            new_price = int(new_price_str)
            
            Inventory[code_update]['price'] = new_price
            print(f"El precio de {Inventory[code_update]['product']} ha sido actualizado a {new_price}.")
            
            if int(new_amount_str) < 0:
                print("no se permiten numeros negativos")
                return
            new_amount = int(new_amount_str)
            
            Inventory[code_update]['amount'] = new_amount
            print(f"El precio de {Inventory[code_update]['product']} ha sido actualizado a {new_amount}.")
        except ValueError:
            print("El precio ingresado no es un numero valido.")
            
    else:
        print("Codigo de producto invalido.")
        
def delete_products():
    """permite borrar productos"""
    product_delete = input("Ingrese la ID del producto que desea Eliminar: ")
    if product_delete in Inventory:
        confirm = input("El producto existe, ¿deseas continuar con la eliminacion (si/no)?: ")
        if confirm.lower() == "si":
            Inventory.pop(product_delete) # Remove the product.
            print(f"El producto con ID {product_delete} ha sido eliminado.") # Confirmation.
        elif confirm.lower() == "no":
            print("La eliminacion ha sido cancelada.") # Deletion cancelled.
        else:
            print("Respuesta invalida. Por favor, ingresa 'si' o 'no'.") # Invalid confirmation input.
    else:
        print(f"No se encontro ningun producto con la ID {product_delete}.") # Product ID not found.


        
while True:
    show_inventory()
    option = input("Select an option: ")

    match option:
        case '1':
            add_product()
        case '2':
            search_product_by_id()
        case '3':
            update_price()
        case '4':
            delete_products()
        case '5':
            print("Exiting the program...")
            break
        case _:
            print("Invalid option. Please try again.")