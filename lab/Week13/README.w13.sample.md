期末專案構想：生活事件
===================

## 專案公開資訊

### 專案題目（格式：程式名稱/專案題目，30中文字以內，2個英文字母算1個中文字）
MyDays/記錄個人的生活事件

### 簡述（100字內）
MyDays是生活事件的追蹤程式。它想讓人們能在自己電腦裡安心地記錄自己的生活軌跡。程式會幫助使用者彙總各項活動事件，並計算出活動趨勢，讓使用者能藉此調整生活習慣、訂定生活目標。

---

## 目的/功能說明（約500字即可）
這個程式想要幫助使用者記錄每天發生的事情。人們每天都發生很多事。例如，今天去總圖唸書（睡覺）多久，在7-11蒐集到多少點數等等。
有些事可能無關緊要，但有些事如果能長久記錄下來，就可以記錄累積數量，甚至計算發生趨勢。這些訊息能讓人們更清楚自己的生活軌跡，甚至幫助調整生活習慣、訂定生活目標。

記錄上述事件有許多可能的替代方案，例如Google Document、Sheet，或特定的行動應用程式（App）。然而，這些程式雖然方便，但把自己的私人的生活事件交給第三方服務，可能讓使用者無法放心，進而限制使用者願意記錄的事件類型。其他的本機方法，例如用單純的記事本記錄等，雖然較沒有資料隱私的考量，卻會受限於記事本只是純文字檔，無法進一步對事件資料進行彙總、計算、分析等功能。所以本專案希望能提供使用者很單純的Python單機程式。此程式沒有網路功能，故沒有資料共享的風險，它僅記錄、儲存、管理、分析使用者交付記錄的生活事件。

這個程式的功能透過文字介面讓使用者輸入事件資料，程式會協助儲存、管理生活事件。使用者同樣可透過文字介面完成合併彙算、分析等功能。在此期末專案的範圍中，此程式將提供四項分析功能：（1）各活動類別加總、（2）各活動最高記錄、（3）各活動的最近一次記錄以及（4）各活動最長連續記錄。各分析結果也同樣使用文字介面呈現出來。未來本專案將試圖改善輸出介面成為排版較佳的HTML頁面格式，並計算各事件的發生週期並做出預測供使用者參考。

## 你覺得可能會遇到的困難，請盡量清楚地條列敘述。
1. 本專案為求實作單純，故以文字介面與使用者互動。但為讓使用者輕易和本程式互動，則需系統性構思如何設計互動流程。
2. 如何儲存、讀取使用者過去所交付的生活事件。甚至是否可能讓使用者加密保護其資料。
3. 如何操作各事件類別的分群與彙總。
4. 如何格式化文字輸出

## 如何達成此專案的功能
1. 介面互動

    使用者將以文字介面和程式互動。程式的輸入使用input()函式、輸出則用print()函式。所有的使用者輸入都會有程式提示既定選項，故僅需非常少量的（或不需要）語句剖析。

2. 資料儲存與管理

    本專案將把使用者所輸入的資料以CSV格式儲存。Python有內建的[csv][link_csv]套件可以儲存和讀取CSV檔，但在程式裡，可能仍須另外實作兩個函式負責把事件資料結構寫入CSV，和從CSV載入事件資料結構。

    由於此專案的目的之一是保護使用者隱私，即便此程式僅會將資料儲存於本機，但畢竟只是一個明碼（plain text）儲存的文字檔（CSV）。故未來計畫在寫入檔案時將檔案內容加密。Python有眾多加密套件可供選擇，其中[pyCryptodome][link_crypto]是使用社群較廣且程式介面方便、說明文件完整的加密工具。

    [link_csv]: https://docs.python.org/3/library/csv.html
    [link_crypto]: https://www.pycryptodome.org/en/latest/
  
3. 資料處理與彙總

    本專案提供的「各活動類別加總」、「各活動最高記錄」、「最近一次記錄」，以及「最長連續記錄」皆可自行實作。實作方式大致上是以迴圈一個個走過目前使用者所儲存的事件，並按照每個事件的類型，記錄其數值到相對應的暫存變項，並在每次迭代中對該暫存變項的值做運算（如加總、最大值等）。

4. 格式化輸出

    在專案初期僅提供一般文字介面的輸出回饋，所有的文字顯示都使用內建的print()和內建的[格式化字串語法][fstr_link]即可完成。

    未來專案將提供HTML輸出介面。要達成HTML的格式輸出可能有兩個套件可以參考：

    1. [mako][link_mako]：好處是直接在範本語言中寫HTML，可詳細控制HTML的格式；但缺點是語法較多，開發過程較複雜。
    2. [markdown2][link_md]：程式可直接用Markdown語法格式化結果，並藉此套件轉換成HTML；但最後的呈現樣式仍須在HTML檔頭指定。

    [fstr_link]:https://docs.python.org/3/library/string.html#format-string-syntax
    [link_mako]:https://www.makotemplates.org/
    [link_md]:https://github.com/trentm/python-markdown2

## 實作時間表

### W14 12/12  Checkpoint 1

* 寫出使用者介面

    使用者可透過文字選單和程式互動，包含輸入資料、選擇分析或彙總功能、輸出資料、或儲存成HTML檔案。程式互動介面會在主迴圈內完成，使用者可以重複和選單互動，或者不輸入任何選擇，直接按Enter跳出程式。

    在主迴圈中，程式會依照使用者選擇呼叫4個函式： `print_main_ui_menu()` 負責印出程式功能的主選單， `handle_user_data()` 負責引導使用者輸入自己的事件資料，`handle_analysis_request()` 負責讓使用者選擇要進行的分析，`handle_export()` 負責顯示使用者目前事件分析的文字報表，或可以直接輸出成HTML檔。

    本週進度要完成上述4個函式中與使用者互動的部分，亦即顯示選單，以及讓使用者能輸入資料的`input()`函式等。但所有真正的程式檔案存取、分析工作將會在之後的checkpoints完成。

```python
while True:
    user_input = input("請輸入選項：")
    print_main_ui_menu()
    if not user_input:
        break
    if user_input == "A":
        handle_user_data()
    elif user_input == "B":
        handl_analysis_request()
    elif user_input == "C":
        handle_export()
```

### W15 12/19  Checkpoint 2

* 完成`handle_user_data`

    完成handle_user_data裡的功能，包含引導使用者輸入事件的日期、類型、名稱、和對應數值。

* 完成檔案I/O

    當使用者把事件內容輸入之後，程式會自動將新資料儲存進檔案。並且當程式下次執行時，自動把資料從檔案中讀取進來。在這週也會實作檔案IO相關函式，例如：

```python
    def load_data_from_file(file_path):
        pass  # function to be implemented
        
    def save_data_to_file(file_path):
        pass  # function to be implemented
```

* 完成分析結果的文字輸出

    本週將事先寫定一組測適用的分析結果，並用該結果先撰寫輸出結果的函式。

```python
# a test analysis result dictionary
ev_dict = {"7-11": 2.5, "總圖": 4}
event_info = {
    "7-11": {
        "detail": "在7-11蒐集到的點數",
        "unit": "點"},
    "總圖": {
        "detail": "在總圖唸書的時間",
        "unit": "小時"}
}
def format_event_dict(ev_dict, ev_info):
    # format ev_dict into a text string, with information in ev_info
    outStr = ""   # the resulting string
    return outStr
```

### W16 12/26  Checkpoint 3

* 完成資料分析功能 `handle_analysis_request()`

    此函式會負責分析使用者的各項事件彙總或趨勢。本專案預計實作的有「各活動類別加總」、「各活動最高記錄」、「最近一次記錄」，以及「最長連續記錄」。

    每個分析功能都盡可能遵循相同函式特徵（signature）以方便開發維護，它們都必須以使用者的活動資料（一個tuple所構成的清單）當作第一個參數，函式的回傳是一個以活動類型當作鍵（key），彙總結果當作值（value）的字典（dict）。例如：

```python
    def analyze_activity_sum(ev_data):        
        # process ev_data to build ev_map        
        # ev_dict:Dict[ActCategory, ActValue]
        # ev_dict is of type Dict, its key type is ActCategory and value type is ActValue
        ev_dict = {}
        return ev_dict
```

## W17 01/02  口頭報告 / beta release

* 測試程式功能

* 調整其他程式小問題

## 未來開發計畫

* 檔案加密

* 將使用者互動方式改成圖形化使用者介面

* 與行動裝置整合串連。按照生活事件記錄在行動裝置上顯示通知，例如提醒運動、提醒休息等等。

