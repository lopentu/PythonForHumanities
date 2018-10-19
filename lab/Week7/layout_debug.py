## poem變項內容擷取自鄭愁予《錯誤》

poem = """
東風不來，三月的柳絮不飛
你的心如小小寂寞的城
恰若青石的街道向晚
跫音不響，三月的春帷不揭
你的心是小小的窗扉緊掩
"""

print("[DEBUG] line_buffer: {!r}".format(poem))
line_buffer = ". "
for ch in poem:
    print("[DEBUG] Loop start (ch: {!r})".format(ch))
    if ch in ("\n", "，"):
        print("[DEBUG] newline case encountered")
        print("[DEBUG] print line_buffer: ")
        print(line_buffer)
        line_buffer = ". "
        print("[DEBUG] Reset line_buffer")
    else:
        print("[DEBUG] other character encountered")
        space = ord(ch) % 3
        print("[DEBUG] codepoint: {}, space: {}".format(ord(ch), space))
        line_buffer += " " * space
        line_buffer += ch
print("")
        