
from urllib import parse
url='https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_10308414147640445854%22%7D&n_type=-1&p_from=-1'
result=parse.urlparse(url)
a=str(result)
print(a)