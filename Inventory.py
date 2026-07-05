import sqlite3

# Connect Database
conn = sqlite3.connect("raja.db")
cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL,
    quantity INTEGER
)
""")

conn.commit()


# Add Product
def add_product():
    name = input("Enter Product Name: ")
    price = float(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))

    cursor.execute(
        "INSERT INTO products(name, price, quantity) VALUES (?, ?, ?)",
        (name, price, quantity)
    )

    conn.commit()
    print("Product Added Successfully")


# View Products
def view_products():
    cursor.execute("SELECT * FROM products")

    products = cursor.fetchall()

    if len(products) == 0:
        print("No Products Found")
    else:
        print("\n--- Product List ---")
        for product in products:
            print(product)


# Search Product
def search_product():
    name = input("Enter Product Name: ")

    cursor.execute(
        "SELECT * FROM products WHERE name = ?",
        (name,)
    )

    result = cursor.fetchall()

    if len(result) == 0:
        print("Product Not Found")
    else:
        for product in result:
            print(product)


# Update Stock
def update_stock():
    product_id = int(input("Enter Product ID: "))
    quantity = int(input("Enter New Quantity: "))

    cursor.execute(
        "UPDATE products SET quantity = ? WHERE id = ?",
        (quantity, product_id)
    )

    conn.commit()

    print("Stock Updated Successfully")


# Delete Product
def delete_product():
    product_id = int(input("Enter Product ID: "))

    cursor.execute(
        "DELETE FROM products WHERE id = ?",
        (product_id,)
    )

    conn.commit()

    print("Product Deleted Successfully")


# Reports
def reports():

    cursor.execute("SELECT COUNT(*) FROM products")
    total_products = cursor.fetchone()[0]

    cursor.execute("SELECT SUM(quantity) FROM products")
    total_quantity = cursor.fetchone()[0]

    print("\n--- Reports ---")
    print("Total Products:", total_products)
    print("Total Quantity:", total_quantity)


# Main Menu
while True:

    print("\n===== Raja Inventory Management System =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Stock")
    print("5. Delete Product")
    print("6. Reports")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        view_products()

    elif choice == "3":
        search_product()

    elif choice == "4":
        update_stock()

    elif choice == "5":
        delete_product()

    elif choice == "6":
        reports()

    elif choice == "7":
        print("Thank You")
        break

    else:
        print("Invalid Choice")

conn.close()