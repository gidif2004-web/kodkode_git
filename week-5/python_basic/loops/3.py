products = []
while True:
    product = input('enter a product')
    if product == 'done':
        break
    products.append(product)
print (products)


for i in range(1,4):
    for j in range(1,4):
        if (j==2):
            break
        print(i,j)