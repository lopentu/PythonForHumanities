# Movie rating data
movie_1 = "Avengers: Infinity War"
movie_2 = "The Shape of Water"
movie_3 = "Mamma Mia! Here We Go Again"
rating_1 = "8.6"
rating_2 = "7.4"
rating_3 = "7.2"

## --- Input Section ---
print("== 請選擇影片 1~3 == ")
print("1. " + movie_1)
print("2. " + movie_2)
print("3. " + movie_3)
movie_index = input("影片編號(1~3): ")

## --- Program Section ---
movie_label = eval("movie_" + movie_index)
movie_rating = eval("rating_" + movie_index)

## --- Output Section ---
print("Rating of '" + movie_label + "' is: " + movie_rating)
