def get_order(order):
    menu = ['burger', 'fries', 'chicken', 'pizza', 'sandwich', 'onionrings', 'milkshake', 'coke']
    order_sorted = []

    for item in menu:
        index = 0
        while not ((index == len(order))):
            if order[index:index+len(item)] == item:
                order_sorted.append(order[index:index+len(item)].title())
            index += 1
    
    return ' '.join(order_sorted)


print(get_order("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"))