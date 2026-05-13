def is_valid_email(email):
    if not email:
        return False
    return True

def is_quantity_fits(quantity, stock):
    return quantity > 0 and quantity < stock

def calculate_price(product_price, quantity):
    return product_price * quantity

def get_discount_price(full_price, quantity):
    if quantity >= 50:
        return full_price * 0.85
    if quantity >= 10:
        return full_price * 0.9
    return full_price

def update_stock(stock, quantity):
    return stock - quantity

def print_invalid_message(invalid_data):
    print (f'invalid {invalid_data}')

def print_order_info(order_user, order_product, order_quantity, order_total, order_status):
    print(f"Order {order_status}: {order_user} bought {order_quantity}x {order_product} for ${order_total}")


def handle_purchase(user_email, product_name, product_price, stock, quantity):
    if not is_valid_email(user_email):
        print_invalid_message("user")
        return None
    if not is_quantity_fits(quantity, stock):
        print_invalid_message("quantity")
        return None

    price = calculate_price(product_price, quantity)
    price = get_discount_price(price, quantity)

    stock = update_stock(stock, quantity)

    order_user = user_email
    order_product = product_name
    order_quantity = quantity
    order_total = price
    order_status = "confirmed"
    print_order_info(order_user, order_product, order_quantity, order_total, order_status)
    return order_user, order_product, order_quantity, order_total, order_status
