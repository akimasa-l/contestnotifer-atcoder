import requests
from bs4 import BeautifulSoup
import time
import re
import json


def get_contest(lang):
    c=[]
    url="https://atcoder.jp/contests/?lang="+lang
    
    r=requests.get(url)
    b=BeautifulSoup(r.text,"html.parser")
    table=b.find(id="contest-table-upcoming")
    for tr in table.find_all("tr"):
        contest=tr.find_all("td")
        if not contest:
            continue
        cname=contest[1].find("a").text
        curl="https://atcoder.jp"+contest[1].find("a").get("href")
        ctime=contest[0].find("time").text
        cdtime=contest[2].text
        rated=contest[3].text
        year,month,day,hour,minute,second,gmt=re.split(r"[\-:\+ ]",ctime)
        dhour,dminute=cdtime.split(":")
        #print(cname,ctime,cdtime,rated,curl)
        contestdict={
            "name":cname,
            "date":{
                "year":year,
                "month":month,
                "day":day,
                "hour":hour,
                "minute":minute,
                "second":second,
                "gmt":gmt
            },
            "dtime":{
                "hour":dhour,
                "minute":dminute
            },
            "rated":rated,
            "url":curl
        }
        c.append(contestdict)
    return c

print(*get_contest("en"))#