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
    output_text = "(function not implemented)"
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
