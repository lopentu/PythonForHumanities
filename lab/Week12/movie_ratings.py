import re

def load_movie_data(data_path):
    fmovie = open(data_path, "r", encoding="UTF-8")
    movies = {}
    for line in fmovie.readlines():
        mat = re.search(r"(.+)<(\d+)>: (.+)", line)
        if not mat:
            continue
        movie_name = mat.group(1)
        movie_year = int(mat.group(2))
        movie_rating = float(mat.group(3))
        movies[movie_name] = {"year": movie_year, "rating": movie_rating}
    fmovie.close()
    return movies

def query_ratings(query_x, data):
    results = ""
    for title_x in data:
        if query_x.lower() in title_x.lower():
            movie_info = data[title_x]
            movie_year = movie_info["year"]
            movie_rating = movie_info["rating"]
            results += "{}({}): {}\n".format(title_x, movie_year, movie_rating)
    return results

def main():
    movie_data = load_movie_data("movie_ratings.txt")    
    print("== 查詢IMDB電影評分 ==")
    print("已載入{:,}部電影評分資料（2008年以後）".format(len(movie_data)))    
    counter = 0
    from datetime import datetime
    t0 = datetime.now()
    while True:
        # query = input("輸入英文片名: ")
        query = "ZDFAKLSJER"
        if not query:
            break
        results = query_ratings(query, movie_data)        
        counter += 1
        if counter > 1e3: break
        # print(results)
    print(f"{(datetime.now() - t0)} seconds")

if __name__ == "__main__":
    print("")
    main()
    print("")