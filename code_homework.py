# # PROBLEM 1

# ticker_1 = "AAPL"  # first ticker declaration
# ticker_2 = "TSLA"  # second ticker declaration
# ticker_3 = "NQ"
# entry_price_1 = 185.50  # entry price 1-3 from line 6-8
# entry_price_2 = 245.00
# entry_price_3 = 24037.60
# exit_price_1 = 192.30  # exit price 1-3 from line 9-11
# exit_price_2 = 238.75
# exit_price_3 = 24382.40
# shares_ticker_1 = 100  # shares for all tickers bought lines 12-14
# shares_ticker_2 = 50
# shares_ticker_3 = 2

# pnl_1 = (exit_price_1 - entry_price_1) * (shares_ticker_1)
# pnl_2 = (exit_price_2 - entry_price_2) * (shares_ticker_2)
# pnl_3 = (exit_price_3 - entry_price_3) * (shares_ticker_3)
# total_pnl = pnl_1 + pnl_2 + pnl_3
# print("QUESTION 1:")
# print("=== PORTFOLIO SUMMARY ===")
# print(
#     f"Trade 1: {ticker_1} | Entry: ${entry_price_1:.2f} | Exit: ${exit_price_1:.2f} | Shares: {shares_ticker_1} | P&L: ${pnl_1:.2f}"
# )
# print(
#     f"Trade 2: {ticker_2} | Entry: ${entry_price_2:.2f} | Exit: ${exit_price_2:.2f} | Shares: {shares_ticker_2} | P&L: ${pnl_2:.2f}"
# )
# print(
#     f"Trade 3: {ticker_3} | Entry: ${entry_price_3:,.2f} | Exit: ${exit_price_3:,.2f} | Shares: {shares_ticker_3} | P&L: ${pnl_3:.2f}"
# )
# print(f"Total P&L: ${total_pnl:,.2f}")
# print("=============================================================")
email = "kumar.sharma@trading.com"
position = email.find(
    "@"
)  # finds position of the '@' in the email and saves the position of the @ in the position variable.
# print(position)
print("QUESTION 2:")
print(f"Email:  {email}")
print(
    f"Username: {email[position+1:]}"
)  # prints the email of user up to the @ and saves it as the username
print("=============================================================")

# price = 152.75
# volume = 75000
# above_vwap = True
# rsi = 55.3
# print("QUESTION 3:")
# print("=== TRADE SCREENER ===")
# print(f"Price above $100: {price>100}")
# print(f"Volume above 50,000: {volume > 50000}")
# print(f"Above VWAP: {above_vwap}")
# print(f"RSI between 30-70: {30<=rsi<=70}")
# print("---")
# print(f"Valid setup: {(price>100) and (volume > 50000) and (above_vwap) and (30<=rsi<=70)}")
