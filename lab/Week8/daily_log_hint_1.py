from datetime import datetime
## Data Section
## =============


events = [
    ("2018/10/25", "寫日記", 30),
    ("2018/10/23", "7-11", 1),
    ("2018/9/27", "寫日記", 30),
    ("2018/9/28", "寫日記", 20),
    ("2018/9/29", "寫日記", 40),
    ("2018/9/29", "總圖", 3),
    ("2018/9/30", "寫日記", 25),
    ("2018/10/21", "7-11", 2),
    ("2018/10/22", "總圖", 3),
    ("2018/10/23", "總圖", 2)
]

event_info = {
    "寫日記": {
        "detail": "寫日記花的時間",
        "unit": "分鐘"},
    "7-11": {
        "detail": "在7-11蒐集到的點數",
        "unit": "點"},
    "總圖": {
        "detail": "在總圖唸書的時間",
        "unit": "小時"}
}


## -----------------------
##   Function Definition
## -----------------------
def group_last_time(ev_data, ev_info):
    ## [Optional] 為了讓我們理解「傳進」函數的引數是什麼，你可以選擇用debugger看
    ## ev_data或ev_info的內容，或直接用print把這兩個變項印出來。
    
    ltime_dict = {}
    for ev_x in ev_data:

        ## 請在ev_x裡找出代表類別的元素，例如「7-11」、「總圖」、「捷運」這些事件。
        ev_category = 

        ## [Hint]: 從ltime_dict.get方法，從dict中取出目前ev_category變項
        ## 內容所儲存的內容，並把該內容指派給ltime_day。
        ## 如果ltime_dict裡還沒有ev_category所對應的內容，那就用36500（天）
        ## 當作預設值。這樣的用意是讓接下來取最小值時，這個預設（初始）值很容易被
        ## 真實資料所取代。
        ltime_day = ltime_dict.get(, 36500)

        ## [Hint]: 請在這一行把字串剖析成日期(datetime)物件
        ## 在這個檔案一開始已經幫同學做好引入，也就是第一行的
        ## `from datetime import datetime`
        ## 請找出如何使用datetime.strptime方法（可參考strptime的說明文件） 
        date_x = 

        ## [Hint]: 用現在時間減掉資料裡的時間`date_x`，date_diff代表「時間的差異」。
        date_diff = datetime.now() - date_x

        ## [Hint] date_diff是「時間的差異」，date_diff.days是
        ## 以天數表達這個時間差異。
        ## 我們希望找出距離現在最近的日期，當作最近一次活動距離現在的天數，
        ## 也就是我們要找出最小的date_diff.days。
        ## 你可能可以用條件式，或用min函數比較ltime_day和date_diff.days完成這個目的。
        ltime_min = 
        
        ## [Hint] 最後把ltime_min寫回ltime_dict物件，請填寫要寫入ltime_dict的鍵（key） 
        ## 以及其所對應的值（value）
        ltime_dict[] = 

    output_text = format_group_message(
        "[{category}]，最近一次是{value}天前\n", ltime_dict, ev_info)
    return output_text

def group_sum(ev_data, ev_info):
    sum_dict = {}
    for ev_x in ev_data:
        ev_category = ev_x[1]
        sum_val = sum_dict.get(ev_category, 0)
        sum_val += int(ev_x[2])
        sum_dict[ev_category] = sum_val

    output_text = format_group_message(
        "{detail}，總共{value}{unit}\n", sum_dict, ev_info)
    return output_text

def group_max(ev_data, ev_info):
    max_dict = {}
    for ev_x in ev_data:
        ev_category = ev_x[1]
        max_val = max_dict.get(ev_category, 0)
        max_val = max(max_val, ev_x[2])
        max_dict[ev_category] = max_val

    output_text = format_group_message(
        "{detail}，最高紀錄是{value}{unit}\n", max_dict, ev_info)
    return output_text

def format_group_message(template, group_dict, ev_info):
    output_text = ""
    for group_cat, group_val in group_dict.items():
        group_detail = ev_info[group_cat]["detail"]
        group_unit = ev_info[group_cat]["unit"]
        output_text += template.format(
            category=group_cat,
            detail=group_detail,
            value=group_val,
            unit=group_unit
        )
    return output_text
    
## ---------------------
##  Main Entry Function
## ---------------------

def main():

    while True:
        ## Ask for user input (I)
        print("-- 我的生活日誌 --")
        print("1. 各活動加總")
        print("2. 各活動最高紀錄")
        print("3. 各活動的最近一次")
        option_x = input("選擇分析選項（或Enter結束）：")

        ## Carryout selected action (P)
        if option_x == "1":
            outStr = group_sum(events, event_info)
        elif option_x == "2":
            outStr = group_max(events, event_info)
        elif option_x == "3":
            outStr = group_last_time(events, event_info)
        elif option_x == "":
            print("Bye")
            break
        else:
            print("unrecognized option")
            continue

        ## Output resulting string (O)
        print("-----")
        print(outStr)

## Calling main() function
main()
