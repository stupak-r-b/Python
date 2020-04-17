"""
You are given the current stock prices. You have to find out which stocks cost more.

Input: The dictionary where the market identifier code is a key and the value is a stock price.
Output: The market identifier code (ticker symbol) as a string.
"""

def best_stock(a):
    
    # Sort the stock values
    sorted_dict = sorted(a.items(), key=lambda item: item[1], reverse=True)
    
    # If the dictionary is empty then return 0.0 else return the key
    return sorted_dict[0][0] if len(sorted_dict) > 0 else 0.0                               


if __name__ == '__main__':
    assert best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}) == "ATX"
    assert best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}) == "TASI"
    print("Coding complete? Click 'Check' to earn cool rewards!")
