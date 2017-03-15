# -*- coding: utf-8 -*-
import requests
import re
import urllib2
import cookielib
import urllib

# head = {'User-Agent':"User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"}
# s = requests.Session()
# url = "https://www.yifile.com/file/V4Pzf3bPxVzcihwW7Q.html"

# r = s.get(url,headers = head)
# print r.text
# pattern = r"data : '(.*?)',"
# text = re.findall(pattern,r.text)
# print text[0]
# posturl = "https://www.yifile.com/jsa/api.php"
# req = s.request(posturl,text[0])
# data = urlopen(req).read()


head = {
	'User-Agent':"User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
	'Host':"www.yifile.com",
	'Accept':"text/plain, */*; q=0.01",
}
s = requests.Session()
s.cookies = cookielib.LWPCookieJar('yifilecookes')
# s.cookies.load(ignore_discard=True)

def abc(a,b,c):
	'''''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
   	'''
	per = 100.0 * a * b / c
	if per > 100:
		per = 100
	print '%.2f%%' % per

def getyifile(url):
	r = s.get(url,headers = head)
	pattern = r"data : 'action=yifile_down&file_id=(.*?)',"
	text = re.findall(pattern,r.text)
	posturl = "https://www.yifile.com/ajax.php"
	data = {
		'action':'yifile_down',
		'file_id':text[0],
	}
	rpost = s.post(posturl,data)
	# print rpost.text
	# print text[0]
	s.cookies.save()
	# string = "true|http://dl3.yifile.com:81/file/2016/12/22/05b65d5039b7b14790f0295f3a464bb3.zip/st-j1UkxNNdbog6ucFeep5M7A/e-1482518323/xcode-fe682e8e7ed5b59bb823bad129275867928d3ce7f05177e80b2977702d3e6764fe682e8e7ed5b59bb823bad129275867928d3ce7f05177e80b2977702d3e6764fe682e8e7ed5b59bb823bad129275867928d3ce7f05177e80b2977702d3e6764fe682e8e7ed5b59bb823bad129275867928d3ce7f05177e80b2977702d3e6764fe682e8e7ed5b59bb823bad129275867928d3ce7f05177e80b2977702d3e6764fe682e8e7ed5b59bb823bad129275867928d3ce7f05177e80b2977702d3e6764fe682e8e7ed5b59bb823bad129275867928d3ce7f05177e80b2977702d3e6764fe682e8e7ed5b59bb823bad129275867928d3ce7f05177e80b2977702d3e6764fe682e8e7ed5b59bb823bad129275867928d3ce7f05177e80b2977702d3e6764fe682e8e7ed5b59bb823bad129275867928d3ce7f05177e80b2977702d3e6764fe682e8e7ed5b59bb823bad129275867928d3ce7f05177e80b2977702d3e6764fe682e8e7ed5b59bb823bad129275867928d3ce7f05177e80b2977702d3e6764fe682e8e7ed5b59bb823bad129275867928d3ce7f05177e80b2977702d3e6764fe682e8e7ed5b59bb823bad129275867928d3ce7f05177e80b2977702d3efe682e8e7ed5b59bb823bad129275867928d3ce7f05177e80b2977702d3efe682e8e7ed5b59bb823bad129275867928d3ce7f05177e80b2977702d3e/122225.zip"
	x = rpost.text.split('|')
	print x[1]
	pattern = r'.*/(.*?)\.zip'
	t = re.findall(pattern,rpost.text)
	print t[0]
	filename = './'+t[0]+'.zip'
	urllib.urlretrieve(x[1],filename,abc)

if __name__ == '__main__':
	print('请输入yifile链接：')
	url = raw_input()
	getyifile(url)











