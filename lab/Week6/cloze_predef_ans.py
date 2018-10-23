## Data Section
lyrics = """路,去學校的路很久沒走
換,最近也換了新的工作
缺,所有的追求是不是缺少了什麼
平,想像著生活風平浪靜
想,打開了窗戶突然想起
水,你在的世界會不會很靠近水星"""

## Cloze sentence generation (P)
sentence_list = lyrics.split("\n")
sentence_list.sort()
line = sentence_list.pop()

### [Hint] 
### 1. item_pair是一個有兩個元素的清單，第一個元素item_pair[0]是要挑空的字，
###    第二個元素item_pair[1]是句子本身。
### 2. 在lyrics字串中，每行句子已經符合上述結構，且那兩個元素是用半形逗號(,)分隔，
###    我們只需要用.split(",")把句子切開，即可得到這兩個元素的清單。
item_pair = line.split(",")
sentence_x = item_pair[1]
cloze_char = item_pair[0]
cloze_sentence = sentence_x.replace(cloze_char, "__")

## Display the cloze (O)
print("--- 歌詞填空產生器 ---")
print(cloze_sentence)

## User Input (I)
ans_char = input("請填入空格中的字是：")

## Check the answer (P)
if ans_char == cloze_char:
    print("答對了！")
else:
    print("答案應該是「{}」".format(cloze_char))
