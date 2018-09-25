# dynasty year span data
# retrieved from 
# https://zh.wikipedia.org/wiki/%E4%B8%AD%E5%9B%BD%E5%8E%86%E5%8F%B2%E5%B9%B4%E8%A1%A8
唐 = "690-705"
宋 = "960-1279"
元 = "1271-1368"
明 = "1368-1644"
清 = "1636-1912"

# program starts here
dynasty = input("輸入朝代名: ")
year_span = eval(dynasty)
print("朝代起迄（西元年）：")
print(year_span)
