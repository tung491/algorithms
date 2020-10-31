def max_profit(prices):
        if not prices:
            return 0
        profits = [0 for _ in range(len(prices) + 1)]
        for i, buy_price in enumerate(prices, start=1):
            for i1, sell_price in enumerate(prices[i:], start=i+1):
                if buy_price > sell_price:
                    continue
                profits[i1] = max(profits[i1 - 1], sell_price - buy_price, profits[i1])
        return profits[-1]


if __name__ == "__main__":
    print(max_profit([2,4,1]))