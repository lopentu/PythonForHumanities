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
print("char_bag: {}".format(char_bag))
char_bag.sort()
print("after sorting: {}".format(char_bag))
cloze_char = char_bag.pop()
print("cloze_char: {}".format(cloze_char))
cloze_sentence = sentence_x.replace(cloze_char, "__")
print("cloze_sentence: {}".format(cloze_sentence))

## III. Display the cloze (O)

## IV. User Input (I)

## V. Check the answer (P)

