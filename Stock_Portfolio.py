def stock_tracker():
    stock_prices = {"AAPL": 180, "TSLA": 250, "GOOG": 2800, "MSFT": 300}
    portfolio = {}

    print("📊 Stock Portfolio Tracker")
    while True:
        stock = input("Enter stock symbol (or 'done' to finish): ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print("❌ Stock not found! Available:", list(stock_prices.keys()))
            continue
        qty = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + qty

    total = sum(stock_prices[s] * q for s, q in portfolio.items())
    print("\nYour Portfolio:", portfolio)
    print(f"💰 Total Investment Value: ${total}")

    # Save to file
    with open("portfolio.txt", "w") as f:
        f.write("Stock Portfolio Summary\n")
        for s, q in portfolio.items():
            f.write(f"{s}: {q} x {stock_prices[s]} = {stock_prices[s]*q}\n")
        f.write(f"Total Investment: ${total}\n")

    print("✅ Portfolio saved to portfolio.txt")

if __name__ == "__main__":
    stock_tracker()