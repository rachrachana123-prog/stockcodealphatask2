
prices = {
    "INFY": 1500,
    "TCS": 3600,
    "RELIANCE": 2500,
    "HDFCBANK": 1700,
    "ITC": 450
}

portfolio_data = []
grand_total = 0

print("----- STOCK PORTFOLIO TRACKER -----")


count = int(input("How many different stocks do you want to enter? "))

for i in range(count):
    print(f"\nStock {i+1}:")
    name = input("Enter stock name: ").upper()
    
    if name not in prices:
        print("This stock is not available in our list.")
        continue
    
    qty = int(input("Enter quantity: "))
    
    cost = prices[name] * qty
    grand_total += cost

    
    portfolio_data.append((name, qty, prices[name], cost))


print("\n----- YOUR PORTFOLIO -----")
for item in portfolio_data:
    print(f"{item[0]} | Qty: {item[1]} | Price: {item[2]} | Value: {item[3]}")

print(f"\nTotal Investment = {grand_total}")


with open("my_portfolio.txt", "w") as f:
    f.write("My Stock Portfolio\n")
    f.write("-------------------------\n")
    
    for item in portfolio_data:
        f.write(f"{item[0]} - {item[1]} shares @ {item[2]} = {item[3]}\n")
    
    f.write(f"\nTotal Investment: {grand_total}")


with open("my_portfolio.csv", "w") as f:
    f.write("Stock,Quantity,Price,Value\n")
    
    for item in portfolio_data:
        f.write(f"{item[0]},{item[1]},{item[2]},{item[3]}\n")
    
    f.write(f"\nTotal,,,{grand_total}")

print("\nFiles saved successfully (TXT & CSV).")