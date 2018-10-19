## 此程式碼僅包含作業提示，本身不是一個有效的Python程式。
## 請記得完成作業內容。
## poem變項內容擷取自鄭愁予《錯誤》

poem = """
東風不來，三月的柳絮不飛
你的心如小小寂寞的城
恰若青石的街道向晚
跫音不響，三月的春帷不揭
你的心是小小的窗扉緊掩
"""

layout_dict = {
    "心": '❤️', '城': '🏰', '晚': '🌙',
    "小": 'drift', "向": 'drift',
    "的": 'drift', "月": 'drift'
}

line_buffer = ""
for ch in poem:
    if ch in ("\n", "，"):
        print(line_buffer)
        line_buffer = ""
    else:
        # [Hint] layout_code是要從layout_dict裡，以ch變項內容當作key，取出其對應的value。
        # 但不是所有的字元在layout_dict裡都有鍵值對。所以請使用一個dict的物件方法，
        # （參考 https://docs.python.org/3.7/library/stdtypes.html#mapping-types-dict）
        # 此方法可以在layout_dict的keys包含ch內容時，取出ch內容所對應的值；
        # 但當keys不包含ch的內容時，傳回一個預設值。
        # 這裡的預設值可以用一個空字串（""）。
        layout_code = layout_dict.

        # [Hint] 接下來是一些條件判斷，如果layout_code是'drift'就用字串的format方法，
        # 讓該字元前空一格。
        if layout_code == :
            # [Hint] 這是一個字串物件的format方法，format中放入要顯示的變項。
            line_buffer += "{:>2}".format()

        # [Hint] 如果layout_code是一個emoji，其字串長度就會大於0，
        # 此時就可呈現layout_code。因為螢幕顯示的關係，所以我們用"{:<4}.format"，
        # 給emoji比較大的呈現空間（亦即emoji本身靠左呈現，有4個字元空間）。
        elif len(layout_code) > :
            # [Hint] 同樣記得在format中需要放入要顯示的變項。
            line_buffer += "{:<4}".format()

        # [Hint] 如果以上兩個條件都不符合，那ch應該就是一個一般字元，不需特別的排版呈現，
        # 所以就直接接進line_buffer即可。
        else:
            line_buffer +=             
