# coding: utf-8

import requests
from bs4 import BeautifulSoup
import time
import datetime
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

def make_time_based_object(lang):
    k=dict()
    for c in range(len(lang)):
        d={i:int(j)for i,j in lang[c]["date"].items()}
        da=datetime.datetime(year=d["year"],hour=d["hour"],month=d["month"],day=d["day"],minute=d["minute"],second=d["second"])
        k.setdefault(da,[]).append(lang[c])#ABC,ARC同時開催用
    return k

def get_diff_from_ja_and_en():
    ja=make_time_based_object(get_contest("ja"))
    sja=set(ja.keys())
    en=make_time_based_object(get_contest("en"))
    sen=set(ja.keys())
    both=[]#両方とも
    #for i in 


#print(get_contest("ja"))

with open("./find_contest.json",mode="w") as f:
    f.write(json.dumps(get_contest("ja"),indent=4))