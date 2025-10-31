def dictionary_operations(fruit_prices: dict, fruits: list):
    # add the fruit fruits[0] to fruit_prices with cost 3
    fruit_prices[fruits[0]] = 3
    order_print(fruit_prices)

    # modify the cost of fruits[1] as 2 in fruit_prices
    fruit_prices[fruits[1]] = 2
    order_print(fruit_prices)

    # increase the cost of fruits[2] by 2 in fruit_prices
    fruit_prices[fruits[2]] += 2
    order_print(fruit_prices)

    # delete both key and value for fruits[3] from fruit_prices
    fruit_prices.pop(fruits[3], None)
    order_print(fruit_prices)

    # print the price of fruits[4]
    print(fruit_prices[fruits[4]])

    # print the names of fruits in fruit_prices as a list sorted in ascending order
    print(sorted(fruit_prices.keys()))

    # print the prices of the fruits as a list sorted in ascending order.
    print(sorted(fruit_prices.values()))


def increase_prices(fruit_prices: dict) -> None:
    '''
    Increase the prices of every fruit by 20 percent and round to two decimal places
    '''
    fruit_prices.update({k: round(v * 1.2, 2) for k, v in fruit_prices.items()})


def dict_from_string(string: str, key_type, value_type):
    '''
    Given a string where each line has a comma-separated key-value pair, 
    create a dictionary out of it. Convert key and values to the given types.
    '''
    return {key_type(k): value_type(v) for k, v in (line.split(',') for line in string.strip().split('\n'))}


def dict_to_string(D: dict) -> str:
    '''
    Convert the given dictionary back to the string format produced by dict_from_string.
    '''
    return '\n'.join([f"{k},{v}" for k, v in D.items()])
