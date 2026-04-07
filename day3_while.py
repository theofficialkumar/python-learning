# account_balance = 1050
# trade_number = 1

# while account_balance > 0:
#     loss = 150
#     account_balance -= loss
#     print(f"Trade {trade_number}: balance =${account_balance:.2f}")
#     trade_number += 1
# print(f"Account blown after {trade_number - 1} trades")
# prices = [185.50, 192.30, 310.75, 178.90, 195.75]
# for price in prices:
#     if price > 300:
#         print(f"${price:.2f} - price is too high, stopping scan")
#         # break
#     print(f"${price:.2f} - scanning...")

# print("Scan Complete")

#CONTINUE LOOP EXAMPLE

# prices = [185.50, -10.00, 192.30, 0, 178.90]

# for price in prices:
#     if price <= 0:
#         print(f"Invalid price: ${price} - skipping")
#         continue
#     print(f"Processing ${price:.2f}")

# print("Done Processing")

# max_attempts = 3
# attempts = 0

# while True:
#     attempts += 1
#     print(f"Attempt {attempts}...")

#     if attempts >= max_attempts:
#         print("Max attempts reached. Stopping.")
#         break

balance = 10000
num_trades = 0
final_balance = 0
pnls = [1000, 2000, 0, 233, -52]#making new list of pnls
for pnl in pnls:# for every pnl in the pnls list
    if balance>=8000:# first check if the balance is at least 8000
        if pnl == 0: #if the pnl you are looking at is 0 then skip it with continue
            continue
        else:#else update the balance and counter for number of trades
            balance += pnl
            num_trades += 1
        if balance < 8000:
            print("Daily loss limit hit on last trade")#message shows the second your account
            #balance goes below 8000 on last trade
    else:
        print("Daily loss limit hit")#message shows the second your account balance goes below 8000
        break
print(f"Final Balance: ${balance}")#update balance
print(f"Number of Trades: {num_trades}")#update number of trades taken

