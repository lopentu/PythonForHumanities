
## --- Input Section ---
print("支援幣別: USD/HKD/GBP/JPY/EUR/KRW/MYR/CNY")
currency_label = input("以台幣兌換之幣別: ")
value_str = input("兌換金額（目標幣別）: ")


## --- Program Section ---
# currency retrieved on 2018-09-06
# https://rate.bot.com.tw/xrt?Lang=zh-TW
# 現金買入
USD = 30.37     # 美金
HKD = 3.756     # 港幣
GBP = 38.56     # 英磅
JPY = 0.2673    # 日圓
EUR = 34.97     # 歐元
KRW = 0.02569   # 韓元
MYR = 6.331     # 馬來幣
CNY = 4.4       # 人民幣

## --- Output Section ---
value = int("0" + value_str)
rate = eval(currency_label)
exchanged = value * rate
print("需台幣" + str(exchanged) + "元")
