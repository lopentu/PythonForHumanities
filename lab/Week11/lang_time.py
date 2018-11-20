import re
from datetime import datetime

def get_intent(input_text):
    m_dow = re.search("禮拜幾|星期幾", input_text)
    m_daydiff = re.search("離.*?天", input_text)

    if m_dow:
        intent = "ASK_WEEKDAY"
    elif m_daydiff:
        intent = "ASK_DAYDIFF"
    else:
        intent = "UNKNOWN"

    return intent

def get_date_slot(input_text):
    m_date = re.search(r"\d+/\d+/\d+", input_text)
    m_now = re.search(r"(今天|現在)", input_text)

    if m_date:
        date_str = m_date.group()
        ret_dt = datetime.strptime(date_str, "%Y/%m/%d").date()
    else:        
        if m_now:
            ret_dt = datetime.today().date()
        else:
            ret_dt = None
    return ret_dt

def compute_response(input_text):
    intent = get_intent(input_text)
    dt = get_date_slot(input_text)

    if intent == "ASK_WEEKDAY":
        response = dt.strftime("%A")

    elif intent == "ASK_DAYDIFF":
        today = datetime.now().date()
        day_diff = (dt - today).days
        if day_diff < 0:
            response = "{}天前".format(-day_diff)
        else:
            response = "{}天後".format(day_diff)
    else:
        response = "(unsupported)"

    return response

def main():    
    print("-- 日期計算 --")
    print("你可以問的事情像是：")
    print("- 2018/2/6是禮拜幾？")
    print("- 2018/11/24離現在幾天？")
    print("- 今天星期幾？")
    while True:
        user_input = input(">> ")
        if not user_input:
            break
        resp = compute_response(user_input)
        print(resp)

if __name__ == "__main__":
    print("")
    main()
    print("")
