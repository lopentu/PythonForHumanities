## 歌詞擷取自盧廣仲《魚仔》
## I. Data Section
lyrics = """去學校的路很久沒走
最近也換了新的工作
所有的追求是不是缺少了什麼
想像著生活風平浪靜
打開了窗戶突然想起
你在的世界會不會很靠近水星"""

## II. Cloze sentence generation (P)
sentence_list = lyrics.split("\n")
sentence_list.sort()
sentence_x = sentence_list.pop()
char_bag = list(sentence_x)
char_bag.sort()
cloze_char = char_bag.pop()
cloze_sentence = sentence_x.replace(cloze_char, "__")

## III. Display the cloze (O)
print("\n--- 歌詞填空產生器 ---")
print(cloze_sentence)

## IV. User Input (I)
ans_char = input("請填入空格中的字是：")

## V. Check the answer (P)
if ans_char == cloze_char:
    print("答對了！")
else:
    print("答案應該是「{}」".format(cloze_char))
