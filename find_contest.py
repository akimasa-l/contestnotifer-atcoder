import requests
from bs4 import BeautifulSoup
import time
import re

url="https://atcoder.jp/contests/?lang=en"

r=requests.get(url)
b=BeautifulSoup(r.text,"html.parser")
table=b.find(id="contest-table-upcoming")
for tr in table.find_all("tr"):
    contest=tr.find_all("td")
    if not contest:
        continue
    cname=contest[1].find("a").text
    ctime=contest[0].find("time").text
    cdtime=contest[2].text
    rated=contest[3].text
    year,month,day,hour,minutes,se,plus=re.split(r"[\-:\+ ]",ctime)
    dhour,dminutes=cdtime.split(":")
    print(cname,ctime,cdtime,rated)