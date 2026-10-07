# E-Commerce Core Logic - PrinceGFO
# Lesson 1: Products & Checkout

products = [
    {"id": 1, "name": "Coleman 1.5mm Cable", "price": 25000, "stock": 50},
    {"id": 2, "name": "Dangote Cement 42.5R", "price": 8500, "stock": 200},
    {"id": 3, "name": "12mm Iron Rod", "price": 9500, "stock": 0},
]

def get_available_products():
    return [p for p in products if p["stock"] > 0]

def checkout(cart):
    """cart = [{"price": 25000, "qty": 2}]"""
    return sum(item["price"] * item["qty"] for item in cart)

# Demo
cart = [{"price": 25000, "qty": 2}, {"price": 8500, "qty": 5}]
print("Available:", get_available_products())
print(f"Total: ₦{checkout(cart)}")
