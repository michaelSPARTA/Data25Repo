def calculate_total_price(prices, discount):
    largest = prices[0]
    total = 0
    if 0 <= discount <= 100 and 0 < len(prices) < 100:
        for i in prices:
            total += i
            if 100000 > i > largest:
                largest = i
        print(largest)
        return ((largest * (100 - discount)) / 100) + (total - largest)
    else:
        return


price = [100, 400, 200000]
discount_val = 10
print(calculate_total_price(price, discount_val))
