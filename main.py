stock_price={"AAPL":180,"TSLA":250,"GOOG":150,"AMZN":140}
total_investment=0

while True:
    stock = input("Enter stock name (or 'DONE' to finish):").upper()
    if stock=="DONE":
        break
    if stock not  in stock_price:
        print(" stock not found.Try again")
        continue
    quantity = int(input(f"Enter quantity of {stock}:"))
    total_investment+=(stock_price[stock]*quantity)
    print(f" The total_investment is :${total_investment}")


