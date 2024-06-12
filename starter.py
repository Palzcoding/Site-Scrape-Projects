import urllib.request

## Open website and get response
url = 'http://www.baidu.com'
resp = urllib.request.urlopen(url)

with open('taobao1.html',mode='w',encoding='utf-8') as a: # set encode style while opening
    a.write(resp.read().decode('utf-8'))

print('Over!')
