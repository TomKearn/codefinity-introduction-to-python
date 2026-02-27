# List of products with their initial stock levels at the start of the week
products = [
    ["Apples", 150],  
    ["Bananas", 200],
    ["Oranges", 100],
    ["Mangoes", 120]
]

# List of products sold by the end of the week
units_sold = [["Apples", 30], ["Bananas", 45], ["Oranges", 20], ["Mangoes", 10]]

# New shipment received at the end of the week
shipment_received = [["Apples", 50], ["Bananas", 70], ["Oranges", 30], ["Mangoes", 40]]

# Task
for i in range(len(products)):
    name = products[i][0]
    start_stock = products[i][1]
    sold = units_sold[i][1]

    products[i][1] = start_stock - sold

for i in range(len(products)):
    name = products[i][0]
    mid_stock = products[i][1]
    restocked = shipment_received[i][1]

    products[i][1] = mid_stock + restocked

    print(f"Final stock levels for all products: {products}")
    
print("--------")

for item in products:
    print(item)
    

