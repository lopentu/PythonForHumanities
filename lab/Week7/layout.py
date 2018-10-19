## poem變項內容擷取自鄭愁予《錯誤》

poem = """
東風不來，三月的柳絮不飛
你的心如小小寂寞的城
恰若青石的街道向晚
跫音不響，三月的春帷不揭
你的心是小小的窗扉緊掩
"""

line_buffer = ". "
for ch in poem:
    if ch in ("\n", "，"):
        print(line_buffer)
        line_buffer = ". "
    else:
        space = ord(ch) % 3
        line_buffer += " " * space
        line_buffer += ch
print("")
        