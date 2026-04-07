# watchlist = ["NQ", "ES", "TSLA", "MSFT"]

# for ticker in watchlist:
#     print(f"Scanning {ticker}...")


# #EXAMPLE 2

# for i in range(5):
#     print(f"Trade #{i}")


# # EXAMPLE 3
# for i in range(1, 6):
#     print(f"Trade #{i}")

# prices = [185.50, 192.30, 178.90, 195.75, 188.40]
# total = 0
# for price in prices:
#     total = total + price
# average = total / len(prices)
# print(f"Total: ${total}")
# print (f"Average price: ${average}")

# EXAMPLE 4

tickers = ["NQ", "ES", "AAPL", "TSLA"]

for index, ticker in enumerate(tickers):
    print(f"{index}: {ticker}")

# ZIP() EXAMPLE:

# tickers = ["AAPL", "TSLA", "NQ"]
# prices = [192.3, 238.75, 24382.40]
# for ticker, price in zip(tickers, prices):
#     print(f"{ticker}: ${price:,.2f}")


#Combining if statements and for loops

# prices = [185.50, 192.30, 78.90, 295.75, 45.20, 188.40]

# for price in prices:
#     if price > 100:
#         print(f"${price:.2f} - tradeable")
#     else:
#         print(f"${price:.2f} - too cheap, skip")


#EXERCISE PRACTICE LOOPS
# tickers = ["YM","NQ", "ES", "TSLA", "AAPL"] #decalaration of tickers in list
# daily_pnl = [23453.32, 5132.28, -8122.42, -923.65, 4678.34] #declaration of pnls of each tickers respectively in list
# total = 0 #initialization of total, winner and loser
# winner= 0
# loser = 0
# for ticker, pnl in zip(tickers, daily_pnl):# loop uses zip to combine tickers and pnls
#     # winner = 0
#     total+=pnl
#     if pnl > 0: #if the pnl is greater than 0 it is a winner; winner counter will be iterated and total will be added
#         print(f"{ticker} ${pnl:,.2f} WINNER")#print ticker, pnl and win
#         winner += 1
#     else:#else the pnl is  it is a loser; loser counter will be iterated and total will be added
#         print(f"{ticker} ${pnl:,.2f} LOSE") #print ticker, pnl and lose
#         loser+=1
# #display results for winner/loser count and total
# print(f"\nYou have {winner} Winners")
# print(f"You have {loser} Losers")
# print(f"\nYour total P&L is : ${total:,.2f}")

