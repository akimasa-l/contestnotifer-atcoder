import requests
from bs4 import BeautifulSoup
import time
import datetime
import re
import json


def get_from_posts():
    url="https://atcoder.jp/posts/?lang=ja"
    r=requests.get(url)
    b=BeautifulSoup(r.text,"html.parser")
    c=[]
    for info in b.select(".panel-default"):
        cname=info.find("a").text
        if not(re.match(".*告知",cname)):
            continue
        cname=cname.replace(" 告知","")
        li=info.text.split("- ")
        pronum=li[4].split()
        writers=li[5][7:]
        #print(writers)
        ws=[writer.text for writer in BeautifulSoup(writers,"html.parser").find_all("span")]
        point=re.search("配点は .* です。",info.text).group()#[4:-4]
        #print(cname,pronum,ws,point)
        c.append({"name":cname,"problemnumber":pronum,"writer":ws,"point":point})
    #print(c)
    return c

print(get_from_posts())