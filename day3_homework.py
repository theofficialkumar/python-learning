# # PROBLEM 1:

# trade_pnls = [234.23, 3432.89,500.00, 501.00, 0, -676.00, 6767.67, -83.32, 25.90, 0  ]
# big_wins = 0
# big_loss= 0
# small_wins = 0
# small_loss = 0
# break_evens = 0
# for index, pnl in enumerate(trade_pnls):
#     if pnl == 0:
#         break_evens += 1
#         print(f"Trade {index + 1} is a BREAKEVEN trade at: ${pnl:,.2f}")
#     elif 0<pnl<=500:
#         small_wins+=1
#         print(f"Trade {index + 1} is SMALL WIN at: ${pnl:,.2f}")
#     elif 500<pnl:
#         big_wins+=1
#         print(f"Trade {index + 1} is BIG WIN at: ${pnl:,.2f}")
#     elif -500<=pnl<0:
#         small_loss+=1
#         print(f"Trade {index + 1} is SMALL LOSS at: ${pnl:,.2f}")
#     elif pnl < -500:
#         big_loss+=1
#         print(f"Trade {index + 1} is BIG LOSS at: ${pnl:,.2f}")
# print(f"TOTAL: BREAKEVENS: {break_evens} | BIG WINS: {big_wins} | SMALL WINS: {small_wins} | BIG LOSSES: {big_loss} |SMALL LOSSES: {small_loss}")



# account_balance = 50000#declaration of account balance
# risk_per_trade = account_balance *.02
# tickers = ["AAPL", "TSLA", "MSFT", "NQ", "AMZN", "GOOG"]
# stop_distance = [2.50, 5.00, 10.00, 0, 15.00, 3.75]
# # shares_calculated = 0
# for ticker, distance in zip(tickers, stop_distance):#loop will use zip function to go
#     #through every ticker and its corresponding stop distance amount
#     if distance == 0:#if distance is $0 it will skip specific ticker and send invalid message
#         print(f"{ticker} | Stop: ${distance} | SKIPPED — invalid stop")
#         continue
#     else:
#         print(f"{ticker} | Stop: ${distance:.2f} | Shares: {int(risk_per_trade/distance)}") #displays ticker,
#         #stop distance and amount of shares.

account_balance = 25000
risk_per_trade = .03 * account_balance
num_trades = 0
while account_balance > 15000:
    risk_per_trade = .03 * account_balance
    account_balance = account_balance - risk_per_trade
    num_trades += 1
    print(f"Your Loss: ${risk_per_trade:,.2f} | Remaining Balance: ${account_balance:,.2f}")

print(f"Took: {num_trades} Trades")



