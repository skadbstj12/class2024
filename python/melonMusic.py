import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd

head = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
res = req.get("https://www.melon.com/chart/index.htm", headers=head)

# print(res.status_code) #406
# print(res.text)

soup = bs(res.text, "lxml")

#데이터 선택
ranking = soup.select("tbody .wrap.t_center > .rank")
title = soup.select("tbody .wrap_song_info > .ellipsis.rank01 span > a")
artist = soup.select("tbody .wrap_song_info > .ellipsis.rank02 span > a:nth-child(1)")

# print(len(ranking))
# print(len(title))
# print(len(artist))

# rankingList = []
# titleList = []
# artistList = []

# for i in range(len(ranking)) :
#     rankingList.append(ranking[i].text)
#     titleList.append(title[i].text)
#     artistList.append(artist[i].text)

# print(artistList)
# print(titleList)
# print(rankingList)


rankingList = [rank.text.strip() for rank in ranking]
titleList = [t.text.strip() for t in title]
artistList = [a.text.strip() for a in artist]

chart_df = pd.DataFrame({
    'Ranking' : rankingList,
    'Title': titleList,
    'Artist': artistList
})

# JSON 파일로 저장
chart_df.to_json("melonChart100.json", force_ascii=False, orient="records")