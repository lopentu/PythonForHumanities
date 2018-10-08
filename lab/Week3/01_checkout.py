## --- Input Section ---
## Subtask: 使用者輸入最多三項之金額
item1 = input("請輸入金額 - 物品1: ")
item2 = input("請輸入金額 - 物品2: ")
item3 = input("請輸入金額 - 物品3: ")

## --- Program Section ---
## Subtask: 計算總金額
total = int("0"+item1) + int("0"+item2) + int("0"+item3)

## --- Output Section ---
## Subtask: 顯示金額
print("總額：" + str(total) + "元")