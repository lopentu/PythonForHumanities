import re
import difflib
import jieba
import jieba.analyse

def get_ratio(x, y):
    x_set = set(x)
    y_set = set(y)
    int_set = x_set.intersection(y_set)
    uni_set = x_set.union(y_set)
    return int_set, len(int_set) / len(uni_set)

def get_diff(x, y):
    seq_mat = difflib.SequenceMatcher(a=x, b=y)
    ops = seq_mat.get_opcodes()
    op_list = []
    for op_x in ops:
        tag, i1, i2, j1, j2 = op_x
        if tag == "equal": continue
        x_str = "/".join(x[i1:i2])
        y_str = "/".join(y[j1:j2])
        op_list.append("[{:7}] {} -- {}".format(tag, x_str, y_str))
    return op_list, seq_mat.ratio()

def load_ori_text(fpath):
    fin = open(fpath, "r", encoding="UTF-8")
    text = fin.read()
    text = re.sub(r"[\s\n]", "", text)
    fin.close()
    return text

def load_user_text(fpath):
    fin = open(fpath, "r", encoding="UTF-8")
    text = fin.read()
    text = re.sub(r"[\s\n]", "", text)
    tokens = text.split("/")
    fin.close()    
    return tokens

def main():
    ori_text = load_ori_text("data/news.txt")
    user_tokens = load_user_text("data/news.user.txt")

    print("--------------------")
    print("這是你的斷詞結果：")
    print(" ".join(user_tokens))
    print("--------------------\n")

    print("你覺得這篇文章的關鍵詞有哪些？")
    print("若有多個關鍵詞請以,分隔，請勿加入空白")
    user_keywords = input(">> ")
    user_keywords = user_keywords.split(",")

    ## User jieba to segment and extract keywords
    jieba_tokens = jieba.lcut(ori_text)
    jieba_keywords = jieba.analyse.textrank(ori_text)
    key_diff = get_ratio(jieba_keywords, user_keywords)
    seg_diff = get_diff(jieba_tokens, user_tokens)

    print("== 你和電腦有多像 ==")
    print("這是你的關鍵詞：")
    print(", ".join(user_keywords))
    print("--------------------")
    print("這是jieba的關鍵詞(TextRank)：")
    print(", ".join(jieba_keywords))
    print("--------------------")

    print("這是你和jieba斷詞的差異：")
    print('\n'.join(seg_diff[0]))

    print("--------------------")
    print("你和jieba斷詞的結果有{}%相似".format(int(seg_diff[1]*100)))
    print("你和jieba的關鍵詞有{}%相似".format(int(key_diff[1]*100)))
    print("--------------------")

if __name__ == "__main__":
    print("")
    main()
    print("")
