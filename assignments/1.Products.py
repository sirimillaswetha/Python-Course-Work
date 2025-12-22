# Take input from user

product_id = int(input("Product ID: "))
product_name = input("Product Name: ")
price = float(input("Price: "))

categories = input("Categories (comma separated): ").split(",")

available = int(input("Available Stock: "))
sold = int(input("Sold Stock: "))
stock = (available, sold)
# Float
discount = float(input("Discount Percentage: "))
# Set
features = set(input("Product Features (comma separated): ").split(","))

supplier_name = input("Supplier Name: ")
supplier_contact = input("Supplier Contact: ")
supplier_location = input("Supplier Location: ")
# Dictionary
supplier = {
    "Name": supplier_name,
    "Contact": supplier_contact,
    "Location": supplier_location
}

print("\n--- Product Details ---\n")

# Comma separation
print("ID, Name, Price", product_id, product_name, price, sep=", ")

# Percentage formatting
print("Discount: %.2f%%" % discount)

# f-string
print(f"Product: {product_name}")
print(f"Price: ₹{price}")
print(f"Available Stock: {stock[0]}")

# format() method
print("Supplier: {}, {}, {}".format(
    supplier["Name"],
    supplier["Contact"],
    supplier["Location"]
))
