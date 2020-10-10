# このドキュメントは何

私が作った[AtCoder IDを入力すると自動で有効か無効か判断してくれるスプレッドシート][0]の公式API Referenceです。

# APIの使い方

Example:

```
GET https://script.google.com/macros/s/AKfycbx7DEcey_KAI24uYy8ICdPhT-ZRSNrVjpSkqSdXrkNet04hi_4/exec
```

Expected Responce:

```json:responce.json
["akimasa_l","tourist","chokudai","blacky555","yudai0418","sasanoha","orangecolor","2plus2equal57"]
```

### Example in Python

```python:getAtCoderIdList.py

import requests
import json
url="https://script.google.com/macros/s/AKfycbx7DEcey_KAI24uYy8ICdPhT-ZRSNrVjpSkqSdXrkNet04hi_4/exec"
a=requests.get(url)
print(a.status_code)
d=json.loads(a.text)
print(d)

```

Example out:

```
200
["akimasa_l","tourist","chokudai","blacky555","yudai0418","sasanoha","orangecolor","2plus2equal57"]
```

[0]:https://docs.google.com/spreadsheets/d/1qB4jgvLTkp_-7ggA0j4uZ4tC-dmwLwym_oPQXX2q6rQ/edit?usp=sharing