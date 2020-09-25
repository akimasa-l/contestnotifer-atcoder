import json

#なんかいろいろやる

def make_name_based_object(a):
    return {i["name"]:i for i in a}

def make_original(a):
    return a.values()
a=[{'name': 'ACL Contest 2', 'date': {'year': '2020', 'month': '09', 'day': '26', 'hour': '21', 'minute': '00', 'second': '00', 'gmt': '0900'}, 'dtime': {'hour': '02', 'minute': '30'}, 'rated': '1200 ~ 2799', 'url': 'https://atcoder.jp/contests/acl2'}, {'name': 'AtCoder Regular Contest 104', 'date': {'year': '2020', 'month': '10', 'day': '03', 'hour': '21', 'minute': '00', 'second': '00', 'gmt': '0900'}, 'dtime': {'hour': '01', 'minute': '40'}, 'rated': ' ~ 2799', 'url': 'https://atcoder.jp/contests/arc104'}, {'name': 'HHKB プログラミングコンテスト 2020', 'date': {'year': '2020', 'month': '10', 'day': '10', 'hour': '21', 'minute': '00', 'second': '00', 'gmt': '0900'}, 'dtime': {'hour': '01', 'minute': '40'}, 'rated': ' ~ 1999', 'url': 'https://atcoder.jp/contests/hhkb2020'}, {'name': 'AtCoder Regular Contest 105', 'date': {'year': '2020', 'month': '10', 'day': '11', 'hour': '21', 'minute': '00', 'second': '00', 'gmt': '0900'}, 'dtime': {'hour': '01', 'minute': '40'}, 'rated': ' ~ 2799', 'url': 'https://atcoder.jp/contests/arc105'}]#json.loads("upcomingな方")
b=[{'name': 'ACL Contest 1', 'problemnumber': ['問題数：', '6'], 'writer': ['maroonrk', 'yosupo', 'rng58_admin'], 'point': '配点は 300-600-600-800-900-1800 です。'}, {'name': 'AtCoder Beginner Contest 179', 'problemnumber': ['問題数：', '6'], 'writer': ['beet', 'kyopro_friends', 'satashun'], 'point': '配点は 100-200-300-400-500-600 です。'}, {'name': 'AtCoder Beginner Contest 178', 'problemnumber': ['問題数：', '6'], 'writer': ['ynymxiaolongbao'], 'point': '配点は 100-200-300-400-500-600 です。'}, {'name': 'AtCoder Beginner Contest 177', 'problemnumber': ['問題数：', '6'], 'writer': ['kyopro_friends', 'ynymxiaolongbao'], 'point': '配点は 100-200-300-400-500-600 です。'}, {'name': 'AtCoder Beginner Contest 176', 'problemnumber': ['問題数：', '6'], 'writer': ['kort0n', 'kyopro_friends', 'ynymxiaolongbao'], 'point': '配点は 100-200-300-400-500-600 です。'}, {'name': 'AtCoder Beginner Contest 175', 'problemnumber': ['問題数：', '6'], 'writer': ['satashun'], 'point': '配点は 100-200-300-400-500-600 です。'}, {'name': 'AtCoder Grand Contest 047', 'problemnumber': ['問題数：', '6'], 'writer': ['Errichto'], 'point': '配点は 300 - 700 - 800 - 1000 - 1800 (800) - 2200 です。'}, {'name': 'AtCoder Beginner Contest 174', 'problemnumber': ['問題数：', '6'], 'writer': ['evima', 'kyopro_friends', 'ynymxiaolongbao'], 'point': '配点は 100-200-300-400-500-600 です。'}, {'name': 'M-SOLUTIONS プロコンオープン 2020', 'problemnumber': ['問題数：', '6'], 'writer': ['E869120', 'square1001'], 'point': '配点は 100-200-300-400-500-600 です。'}]
#json.loads("upcomingじゃなくてposts")

an=make_name_based_object(a)
bn=make_name_based_object(b)
bnkeys=bn.keys()
for i in an.keys():
    ad=an[i]
    if i in bn:
        bd=bn[i]
        for j in ("writer","problemnumber","point"):
            ad[j]=bd[j]
    else:
        for j in ("writer","problemnumber","point"):
            ad[j]="null"

print(*(an.items()),sep="\n")
