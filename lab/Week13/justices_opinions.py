import re
from collections import Counter
import requests
import requests_cache
from bs4 import BeautifulSoup

requests_cache.install_cache()

def load_moj_justice(url):
    resp = requests.get(url)
    print("[INFO] retrieved from cache: {}".format(resp.from_cache))
    if resp.status_code != 200:
        return ""
    html = resp.text
    return html

def parse_moj_justice(html):
    soup = BeautifulSoup(html, "html.parser")
    trs = soup.find_all("tr")
    td_abs = trs[1].select_one("td")
    print("[DEBUG] {}".format(td_abs.text))
    td_links = trs[4].select_one("td")
    link_texts = extract_a_text(td_links)

    return link_texts

def extract_a_text(elem):
    a_elems = elem.find_all("a")
    links = []
    for a in a_elems:
        links.append(a.text)
    return links

def group_opinions(titles):
    opinions = parse_opinion_titles(titles)
    opinion_freq = Counter(opinions)

    return opinion_freq

def parse_opinion_titles(titles):
    opinions = []
    for title_x in titles:
        mat_title = re.search("之([部分協不同]+)意見書", title_x)
        if not mat_title:
            continue
        opinion_type = mat_title.group(1)
        # print("[DEBUG] {}: {}".format(title_x, opinion_type))
        opinions.append(opinion_type)
    return opinions

def print_opinion_freq(ofreq_data):
    otypes = ["協同", "部分協同", "部分協同部分不同",
              "部分不同部分協同", "部分不同", "不同"]
    print("{:\u3000>8}|{:^4}|".format("類型", "次數"))
    print("---------------:|:----:|")
    for otype in otypes:
        ofreq = ofreq_data[otype]
        print("{:\u3000>8}|{:^6}|".format(
            otype, ofreq))

def main():
    # Data Section
    # URLs to retrieve
    urls = [
        "https://law.moj.gov.tw/News/news_detail.aspx?msgid=144494",
        "https://law.moj.gov.tw/News/news_detail.aspx?msgid=143948",
        "https://law.moj.gov.tw/News/news_detail.aspx?msgid=143280",
        "https://law.moj.gov.tw/News/news_detail.aspx?msgid=141876",
        "https://law.moj.gov.tw/News/news_detail.aspx?msgid=141599"
    ]

    # Load and parse URLs above
    title_list = []
    for url_x in urls:
        import time; time.sleep(1);
        html_x = load_moj_justice(url_x)
        file_titles = parse_moj_justice(html_x)
        title_list.extend(file_titles)        
    
    # Data analysis (Program)
    opinion_freq = group_opinions(title_list)

    # Print the parsed data (Output)
    print_opinion_freq(opinion_freq)


if __name__ == "__main__":
    main()
