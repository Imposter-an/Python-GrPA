def total_price(fruit_prices: dict, purchases) -> float:
    '''
    Compute the fruit prices give the quantity of each fruit. Do not use the sum function.
    '''
    total = 0
    for fruit, qty in purchases:
        total += fruit_prices[fruit] * qty
    return total


def total_price_no_loops(fruit_prices: dict, purchases) -> float:
    '''
    Compute the total price without loops.
    '''
    return sum(fruit_prices[f] * q for f, q in purchases)


def find_cheapest_fruit(fruit_prices: dict) -> str:
    '''
    Find the cheapest fruit from the fruit_prices dict, do not use min function
    '''
    cheapest_fruit = None
    cheapest_price = float('inf')
    for fruit, price in fruit_prices.items():
        if price < cheapest_price:
            cheapest_price = price
            cheapest_fruit = fruit
    return cheapest_fruit


def find_cheapest_fruit_no_loops(fruit_prices: dict) -> str:
    '''
    Find the cheapest fruit using min function. Do not use loops
    '''
    return min(fruit_prices, key=fruit_prices.get)


def group_fruits(fruits: list):
    '''
    Group the fruits based on the first letter of the names. Assume first letters will be upper case.
    '''
    return {ch: sorted([f for f in fruits if f[0] == ch]) for ch in sorted({f[0] for f in fruits})}


def bin_fruits(fruit_prices):
    '''
    Classify the fruits as cheap, affordable and costly based on the fruit prices.
    '''
    return {
        "cheap": {f for f, p in fruit_prices.items() if p < 3},
        "affordable": {f for f, p in fruit_prices.items() if 3 <= p <= 6},
        "costly": {f for f, p in fruit_prices.items() if p > 6}
    }
