# Taking inputs from user
Zepto_order_id = int(input("Enter Zepto order id: "))
Zepto_customer_name = input("Enter customer name: ")
Zepto_item_name = input("Enter item name: ")
Zepto_delivery_location = input("Enter delivery location: ")
Zepto_delivery_date = input("Enter delivery date: ")
Zepto_item_quantity = int(input("Enter item quantity: "))

# list
Zepto_order_details_list = [
    Zepto_order_id,
    Zepto_customer_name,
    Zepto_item_name,
    Zepto_delivery_location,
    Zepto_delivery_date,
    Zepto_item_quantity
]

# tuple
Zepto_order_details_tuple = (
    Zepto_order_id,
    Zepto_customer_name,
    Zepto_item_name,
    Zepto_delivery_location,
    Zepto_delivery_date,
    Zepto_item_quantity
)

# set
Zepto_order_details_set = {
    Zepto_order_id,
    Zepto_customer_name,
    Zepto_item_name,
    Zepto_delivery_location,
    Zepto_delivery_date,
    Zepto_item_quantity
}

# dictionary
Zepto_order_details_dict = {
    "Zepto_order_id": Zepto_order_id,
    "Zepto_customer_name": Zepto_customer_name,
    "Zepto_item_name": Zepto_item_name,
    "Zepto_delivery_location": Zepto_delivery_location,
    "Zepto_delivery_date": Zepto_delivery_date,
    "Zepto_item_quantity": Zepto_item_quantity
}

# Output
print("\n🛒 Zepto Order Details 🛒")
print("Zepto Order Details in List:", Zepto_order_details_list)
print("Zepto Order Details in Tuple:", Zepto_order_details_tuple)
print("Zepto Order Details in Set:", Zepto_order_details_set)
print("Zepto Order Details in Dictionary:", Zepto_order_details_dict)