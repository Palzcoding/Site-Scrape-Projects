'''因为电影天堂auto.js的反爬较难处理，所以采用了保存页面然后打开html的方式，再用正则爬取'''
## 已保存至桌面a_html.html,第一步打开html保存至html_content
import os

# 获取桌面路径
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# 指定HTML文件的完整路径
html_file_path = os.path.join(desktop_path, 'a_html.html')

# 使用gbk编码格式读取HTML文件内容
with open(html_file_path, 'r', encoding='gbk') as file:
    html_content = file.read()

'''# 输出HTML内容
print(html_content[:1000])'''

##第二步运用正则爬取想要的内容，在2024必看的栏目下寻找：1.子链接，2.电影名，3.每部电影的下载链接
import re
obj1 = re.compile('2024必看热片(?P<block>.*?)</ul>', re.S) #可以用ul命名
obj2 = re.compile('<li>.*?<a href="(?P<href>.*?)"',re.S) #<a href=""></a>是超链接

result1 = obj1.finditer(html_content)

child_href_list = []
for it in result1:
    block_content = it.group('block')
    result2 = obj2.finditer(block_content) #因为知道只有一个，所以拉出for loop
    for ite in result2:
        child_href = ite.group('href')
        child_href_list.append(child_href)
##这里子链接直接是完整的，有的网页需要 主页链接 + 子页面地址
print(child_href_list)

'''
##请求不了子链接因为auto.js
obj3 = re.compile(r'◎片　　名　(?P<title>.*?)<br />'
                  r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)"'
                  ,re.S)
for href in child_href_list: 
    child_resp = requests.get(href,verify=False)
    child_resp.encoding='gb2312'
    child_resp_content = child_resp.text
    result3 = obj3.search(child_resp_content) #有多个下载地址，只要第一个，所以是search
    print(result3.group('title'))
    print(result3.group('download'))'''

    

