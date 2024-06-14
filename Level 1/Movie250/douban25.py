import requests
import re
import csv

url = 'https://movie.douban.com/top250'
UA = 'User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 \
    (KHTML, like Gecko) Version/5.1 Safari/534.50'

header = {
    'User-Agent': UA
}

response = requests.get(url, headers=header)
page_content = response.text
obj = re.compile(
    r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
    r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?'
    r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
    r'.*?<span>(?P<num>.*?)人评价</span>'
    ,re.DOTALL) #re.S

f = open('douban2501.csv',mode='w',encoding='utf-8-sig') #utf-8-sig写中文
csvwriter = csv.writer(f)
csvwriter.writerow(['title', 'year', 'rating', 'rating_count'])
iter = obj.finditer(page_content)

for it in iter:
    dic = it.groupdict()
    dic['year'] = dic['year'].strip()
    csvwriter.writerow(dic.values())


f.close()
''' ## 不用字典直接打印的代码
for it in iter:
    print(it.group('name'))
    print(it.group('year').strip())
    print(it.group('score'))
    print(it.group('num'))'''

response.close()