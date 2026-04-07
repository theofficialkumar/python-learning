# # clear\Initialization
# name = "Kumar"
# ticker = "nq_mini"
# entry_price = 24037.61
# pnl = 3444.82

# # f-string basics
# print(f"Trader: {name}")
# print(f"Enterered {ticker} at {entry_price}")
# print({f"P&L: ${pnl}"})

# # You can do math within the curly braces with the f-strings
# print(f"P&L after fees: ${(pnl- 125.43):.2f}")

# # Formatting decimals -.2f means 2 decimal places
# print(f"Entry: ${entry_price:.2f}")

# # Formatting percentages
# win_rate = 0.6742332
# print(f"Win rate: {win_rate:.0%}")
# print(f"Win rate: {win_rate:.1%}")

# # String methods
# setup = "  Breakout Pullback on NQ      "

# print(setup.lower())  # all lower-case
# print(setup.upper(setup[3:7]))  # all upper-case

# print(setup.strip())  # removes whitespaces from both ends
# print(setup.replace("NQ", "ES"))
# print(setup.split())
# print(setup.startswith("  B"))
# print(setup.count("l"))
# # Checking string content
# ticker = "AAPL"
# print(ticker.isalpha())  # bool that checks if string is all lettes
# print("12345".isdigit())  # bool that checks is string is all nums
# print("1232jjsjkn".isalnum())  # bool that checks if string has nums and letters

# # Slicing - grabbing parts of a string

# ticker = "NQ_MINI_2026"

# print(ticker[0])
# print(ticker[0:2])
# print(ticker[-4:])
# print(ticker[3:7])
# print(len(ticker))


# EXCERCISE 2

ticker = "NQ_MINI"
entry = 24037.60
tp = 24382.40
result = "WINNER"
notes = "Clean breakout, followed the plan"
print("=== TRADE SUMMARY ===")
print(f"Ticker: {ticker}")
print(f"Entry: ${entry:,.2f}")
print(f"Exit: ${tp:,.2f}")
print(f"P&L: ${(tp-entry):,.2f}")
print(f"Result: {result}")
print(f"Notes: {notes}")
