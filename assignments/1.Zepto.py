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
#------------------#------------------------#

# 1. int – User ID
user_id = 102345

# 2. str – User name
user_name = "Sirimilla Swetha "

# 3. float – Wallet balance
wallet_balance = 1500.75

# 4. list – Transaction history
transaction_history = ["Recharge ₹199", "Bill Payment ₹450"]

# 5. tuple – Bank account details (fixed data)
bank_details = ("SBI Bank", "XXXX1234")

# 6. set – Unique offers applied
offers_applied = {"Cashback10", "NewUserOffer"}

# 7. dict – PhonePe user profile
phonepe_profile = {
    "User ID": user_id,
    "Name": user_name,
    "Balance": wallet_balance,
    "Bank": bank_details
}

# Display user details
print("📱 PhonePe Application")
print("----------------------")
print("User ID:", phonepe_profile["User ID"])
print("User Name:", phonepe_profile["Name"])
print("Linked Bank:", phonepe_profile["Bank"])
print("Wallet Balance: ₹", phonepe_profile["Balance"])

print("\nTransaction History:")
for transaction in transaction_history:
    print("-", transaction)

print("\nOffers Applied:")
for offer in offers_applied:
    print("-", offer)
