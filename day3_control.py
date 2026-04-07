# price = 24037.6
# entry_price = 24037.60

# if price > entry_price:
#     print("Trade is in profit")
# elif price == entry_price:
#     print("Trade is breakeven")
# else:
#     print("Trade is in loss")
# rsi = 60.5
# volume = 120000
# above_vwap = True

# if rsi > 70:
#     print("RSI is overbought... wait for a pullback")
# elif rsi < 30:
#     print("RSI is oversold... look for a reversal")
# elif volume < 50000:
#     print("Volume is low... no trade")
# elif not above_vwap:
#     print("Below VWAP... skip this set up")
# else:
#     print("Setup looks clearn - look for entry")
# account_balance = 50000
# risk_per_trade = 0.02
# trade_cost = 5000
# if account_balance > 25000: #if account balance is greater than 25000 then you check if the risk is worth it
#     max_risk  = account_balance * risk_per_trade #checks what max risk should be based on the account size
#     if trade_cost <= max_risk:#if else statement gives approval of trade based on comparing max risk
#         #and current risk being taken
#         print(f"Trade approved. Risk: ${trade_cost} of ${max_risk:,.2f} max")
#     else:
#         print(f"Trade is too risky. Cost ${trade_cost} exceeds ${max_risk:,.2f} max")
# else:
#     print("Account is too small to trade this setup")#disqualifies trade idea based on createria

# EXERCISE 1

win = True
risk_reward = 2.1
followed_plan = False
if win and risk_reward >= 3 and followed_plan:
    print("A+ TRADE")
elif win and risk_reward >= 2:
    print("A TRADE")
elif win and risk_reward < 2:
    print("B TRADE")
elif not win and followed_plan:
    print("C TRADE")
elif not win and not followed_plan:
    print("F TRADE")
