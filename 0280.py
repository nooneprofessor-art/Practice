def sell_house(house_price = 5000000, market = 8000000):
    invest = house_price > market
    return invest

print(sell_house())