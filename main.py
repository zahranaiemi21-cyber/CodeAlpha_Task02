stock_price={"AAPL":180,"TSLA":250,"GOOG":150,"AMZN":140}
total_investment=0
portfolio=[]
while True:
    stock = input("Enter stock name (or 'DONE' to finish):").upper()
    if stock=="DONE":
        break
    if stock not  in stock_price:
        print(" stock not found.Try again")
        continue
    try:
       quantity = int(input(f"Enter quantity of {stock}:"))
       if quantity<=0:
            print("Quantity must be positive!")
            continue
    except ValueError:
        print("please enter a valid number")
        continue

    investment=stock_price[stock]*quantity
    portfolio.append((stock,quantity,investment))
    total_investment+=investment
    print(f"Total:{total_investment}")
    with open ("portfolio.txt","a") as f:
       f.write(f"{stock},{quantity},{investment}\n")
    with open("portfolio.txt", "a") as f:
     f.write(f" The total_investment is :${total_investment}")
     f.write("\n")
print("✅ Portfolio saved successfully!")




