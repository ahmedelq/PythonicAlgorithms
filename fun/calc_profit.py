def profit(items):
    for key in ['cost_price', 'sell_price', 'inventory']:
         if key not in items:
            raise ValueError("Ill dictionary format")
    return (items['cost_price'] - items['sell_price']) * items['inventory']




if __name__ == '__main__':
    assert profit({
    "cost_price": 32.67,
    "sell_price": 45.00,
    "inventory": 1200
    }), 14796

    assert profit({
    "cost_price": 225.89,
    "sell_price": 550.00,
    "inventory": 100
    }), 32411

    assert profit({
    "cost_price": 225.89,
    "sell_price": 550.00,
    "inventory": 100
    }), 44030