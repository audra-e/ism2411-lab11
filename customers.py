# ISM2411 Lab 11 - Customer Dictionary & Lookup

# REFLECTION 1:
# I would use .get() when a key might not exist because it allows
# the program to return a default value instead of crashing.
# I would use bracket notation when I know the key exists and
# need to access its value directly.

# REFLECTION 2:
# This pattern reminds me of using SUMIF in Excel because it adds
# values based on categories. Python is more useful for large
# datasets because it can automatically organize and calculate
# information from many records.


# EXERCISE 1 - One Customer

print("\nEXERCISE 1 - One Customer")

customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1200
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print(customer)


# EXERCISE 2 - Update and Add

print("\nEXERCISE 2 - Update and Add")

customer["phone"] = "555-123-4567"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)


# EXERCISE 3 - Safe Lookup

print("\nEXERCISE 3 - Safe Lookup")

email = customer.get("email", "no email on file")
print(email)

try:
    print(customer["email"])
except KeyError:
    print("KeyError: email does not exist")


# EXERCISE 4 - Iterate

print("\nEXERCISE 4 - Iterate")

for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), the loop only gives us the dictionary keys.
for key in customer:
    print(key)


# EXERCISE 5 - Lookup Table

print("\nEXERCISE 5 - Lookup Table")

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

tier = customer["tier"]
discount = tier_discounts.get(tier, 0)

purchase_price = 200
final_price = purchase_price * (1 - discount)

print(f"Tier: {tier}")
print(f"Discount rate: {discount:.0%}")
print(f"Final price: ${final_price:.2f}")


# EXERCISE 6 - List of Dictionaries

print("\nEXERCISE 6 - List of Dictionaries")

dict1 = {
    "name": "Alice",
    "tier": "platinum"
}

dict2 = {
    "name": "Bob",
    "tier": "gold"
}

dict3 = {
    "name": "Charlie",
    "tier": "silver"
}

customers = [dict1, dict2, dict3]

for person in customers:
    tier = person["tier"]
    discount = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount

    print(
        f"{person['name']} | Tier: {tier} | "
        f"Discount: ${discount_amount:.2f}"
    )


# EXERCISE 7 - Nested Catalog

print("\nEXERCISE 7 - Nested Catalog")

catalog = {
    "Widget A": {
        "price": 9.99,
        "stock": 150
    },
    "Gadget C": {
        "price": 49.99,
        "stock": 8
    }
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(
            f"LOW STOCK: {product} - "
            f"{details['stock']} remaining"
        )


# EXERCISE 8 - Sales by Region

print("\nEXERCISE 8 - Sales by Region")

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_summary = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    sales_summary[region] = sales_summary.get(region, 0) + amount

for region in sorted(sales_summary):
    print(f"{region}: ${sales_summary[region]}")