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
print("before sorting: {}".format(sentence_list))
sentence_list.sort()
print("after sorting: {}".format(sentence_list))
sentence_x = sentence_list.pop()
print("sentence_x: {}".format(sentence_x))

## III. Display the cloze (O)

## IV. User Input (I)

## V. Check the answer (P)

