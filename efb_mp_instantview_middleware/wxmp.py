from telegraph import Telegraph
from sql import dbManager
from datetime import datetime
def recursivewrite(c,content):
    if isinstance(c,list):
        for i in c:
            if isinstance(i,str):
                content.append(i)
            elif isinstance(i,dict) and 'children' in i:
                recursivewrite(i['children'],content)
    elif isinstance(c, dict):
        c = c['children']
        recursivewrite(c,content)
    elif isinstance(c,str):
        content.append(c)
def savempeassy(url: str,token: str=''):
    content=[]
    date = datetime.today().strftime('%Y-%m-%d')
    #token = "624ce1cc14d827544a397043c4e2ca3a544ac1bec289b43604ef171608c9"
    #url = "https://mp.weixin.qq.com/s?__biz=MzAwMjI0ODk0NA==&mid=2451950599&idx=1&sn=9170e61b1aa56727a14e92ed506b3dcc&chksm=8d1c3598ba6bbc8e8a323a148b20c379e598f2e5347de898ecb164b870717157489f0b8d1b6a&scene=0&xtrack=1#rd"
    telegraph_processor = Telegraph(token,'')
    page = telegraph_processor.process_url(url)
    wxmp = dbManager("wxmp",'INFGate')
    for c in page['content']:
        recursivewrite(c,content)
        content=''.join(content)
        wxmp.cur.execute("INSERT INTO essays (author,title,content,date) VALUES (%s,%s,%s,%s)",(page['author'],page['title'],content,date))


#storeMPEassy('','')