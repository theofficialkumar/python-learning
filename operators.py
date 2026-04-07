# a = 10
# b = 3
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a**b)

# comparison
# x = 5
# y = 10
# print(x == y)  # equal to
# print(x != y)
# print(x > y)
# print(x < y)
# print(x >= 5)
# print(x <= 4)

# logical operators
from operator import truediv

# print(True and True)
# print(True and False)
# print(True or False)
# print(False or False)
# print(not True)
# print(not False)

entry_price = 23456.43
stop_loss = 23256.43
take_profit = 23856.43
risk_reward_ratio = 2.0
risk = entry_price - stop_loss
reward = take_profit - entry_price

calculated_r = reward / risk

# print(calculated_R)
print(f"Trade meets your minimum R:R: {(calculated_R)>=(risk_reward_ratio)}")
