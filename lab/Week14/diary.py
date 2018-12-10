import os.path
import json
import csv
from datetime import datetime
import requests
import requests_cache

requests_cache.install_cache()

def get_taipei_weather():
    api_url = "https://www.metaweather.com/api/location/2306179/"
    print("擷取天氣中...")
    weather_resp = requests.get(api_url)
    if weather_resp.status_code == 200:
        json_data = weather_resp.json()
        cur_data = json_data["consolidated_weather"][0]
        state = cur_data["weather_state_name"]
        temp = cur_data["the_temp"]
        hum = cur_data["humidity"]
        w_str = "{}（{:.0f}℃ /{}%）".format(
            state, temp, hum)
    else:
        w_str = "(不知道)"
    return w_str

def add_diary(diary_data):
    weather = get_taipei_weather()
    now = datetime.now().strftime("%m/%d %H:%M:%S")
    header = "{}  天氣：{}\n".format(now, weather)
    header += "---------------------"
    print(header)

    print("（今天的日記，用空白行結束）")
    ln = input("> ")
    diary = header + "\n"
    while ln:
        diary += ln + "\n"
        ln = input("> ")

    diary_data.append([now, diary])

def list_diary(diary_data):
    while True:
        counter = 1
        for entry in diary_data:
            print("{}. {}".format(counter, entry[0]))
            counter += 1
        print("選擇一篇日記")
        diary_select = input(">> ")
        if diary_select:
            entry = diary_data[int(diary_select)-1]
            print(entry[1])
        else:
            break

def write_to_file(diary_data):
    fout = open("diary.json", "w", encoding="UTF-8")
    json.dump(diary_data, fout, indent=2, ensure_ascii=False)
    fout.close()

def read_from_file():
    if not os.path.exists("diary.json"):
        return []

    fin = open("diary.json", "r", encoding="UTF-8")
    json_data = json.load(fin)
    fin.close()
    return json_data

def export_to_csv(diary_data):
    fout = open("diary.csv", "w", encoding="UTF-8", newline='')
    csvwriter = csv.writer(fout)
    for entry in diary_data:
        csvwriter.writerow(entry)
    fout.close()

def print_menu():
    print("=== 我的日記 ===")
    print("1. 寫日記")
    print("2. 日記列表")
    print("3. 匯出成CSV")

def main():
    diary_data = read_from_file()
    while True:
        print_menu()
        menu_select = input(">> ")
        if menu_select == "1":
            add_diary(diary_data)
            write_to_file(diary_data)
        elif menu_select == "2":
            list_diary(diary_data)
        elif menu_select == "3":
            export_to_csv(diary_data)
        else:
            print("Bye~")
            break

if __name__ == "__main__":
    main()
