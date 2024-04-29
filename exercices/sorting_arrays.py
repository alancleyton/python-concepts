products = [
    { 'name': 'Product 06', 'price': 10.00 },
    { 'name': 'Product 07', 'price': 22.32 },
    { 'name': 'Product 22', 'price': 10.11 },
    { 'name': 'Product 41', 'price': 105.87 },
    { 'name': 'Product 05', 'price': 69.90 },
    { 'name': 'Product 01' , 'price': 17.29 },
]

products_with_discount = [
    {**product, 'price': product['price'] + (10 * product['price']) / 100 }
    for product in products
]

products_sorted_by_name = sorted(
    products,
    key=lambda product: product['name'],
    reverse=True
)

products_sorted_by_price = sorted(
    products,
    key=lambda product: product['price'],
    reverse=True
)

print(products_with_discount)
print(products_sorted_by_name)
print(products_sorted_by_price)