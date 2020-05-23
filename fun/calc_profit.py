"""original problem: https://edabit.com/challenge/YfoKQWNeYETb9PYpw"""
import math
def profit(items):
    for key in ['cost_price', 'sell_price', 'inventory']:
         if key not in items:
            raise ValueError("Ill dictionary format")
    return math.ceil( (items['sell_price'] - items['cost_price']) * items['inventory'])



if __name__ == "__main__":
    tests = [
        {
        "cost_price": 32.67,
        "sell_price": 45.00,
        "inventory": 1200
        },

        {
        "cost_price": 225.89,
        "sell_price": 550.00,
        "inventory": 100
        },
        
        {
        "cost_price": 2.77,
        "sell_price": 7.95,
        "inventory": 8500
        }
    ]
    expected_vals = [14796, 32411, 44030]
    error_message = 'Should be %d but got %d'
    for test, expected_val in zip(tests, expected_vals):
        total = profit(test)
        assert total == expected_val, error_message % (expected_val, total)
    print('All test cases passed.')
