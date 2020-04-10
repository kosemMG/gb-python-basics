products = []
i = 1
analytics = {
    'name': [],
    'price': [],
    'quantity': [],
    'units': []
}

while True:
    print('Please, fill the product information. Enter "space" for "name" to finish:')
    name = input('Enter the product name: ')
    if name == '':
        break
    price = input('Enter the product price: ')
    quantity = input('Enter the product quantity: ')
    units = input('Enter the the product units: ')

    product = {
        'name': name,
        'price': price,
        'quantity': quantity,
        'units': units
    }

    products.append((i, product))
    i += 1

    for value in product:
        analytics[value].append(product[value])

print(products)
print(analytics)

