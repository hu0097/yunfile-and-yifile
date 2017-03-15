# #coding=utf-8
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from PIL import Image
import time
import requests

head = {
	'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:49.0) Gecko/20100101 Firefox/49.0",
	'Host':"page2.dfpan.com",
}
baseurl = "http://dl16.dfpan.com/"

def get_post_url(page_source):
	pattern = r'form\.action = saveCdnUrl\+\"(.*?)\"'
	posturl = re.findall(pattern,page_source)
	return baseurl + posturl[0]


def get_post_data(page_source):
	soup = BeautifulSoup(page_source,'lxml')
	tform = soup.select("[class~=tform]")

	pattern = r'value=\"(.*?)\"\/'
	result = re.findall(pattern,str(tform))

	pattern = r'form\.fileId\.value = \"(.*?)\"'
	fileId = re.findall(pattern,str(soup))

	pattern = r'vericode = \"(.*?)\"'
	vid = re.findall(pattern,str(soup))

	postdata = {
		'module' : result[0],
		'userId' : result[1],
		'fileId' : fileId[0],
		'vid'    : vid[0],
		'vid1'   : result[4],
		'md5'    : result[5],
	}

	return postdata

def get_page_source(url):
	driver = webdriver.PhantomJS(executable_path='/usr/local/bin/PhantomJS')
	driver.get(url)
	#获得验证码
	element = driver.find_element_by_id('inputDownWait').find_element_by_class_name('slow_button')
	element.click()
	time.sleep(1)
	#关闭弹窗
	driver.find_element_by_id('login_registBox2').find_element_by_class_name('ui_dialog_close').click()
	driver.get_screenshot_as_file('./img_src/img_src1.png')
	#输入验证码
	print '请输入验证码：'
	intval = raw_input()
	driver.find_element_by_id('vcode').send_keys(intval)
	#发送验证码并等待页面刷新
	driver.find_element_by_id('slow_button').click()
	time.sleep(40)
	page_source = driver.page_source.encode('utf-8')
	#获得post数据
	postdata = get_post_data(page_source)
	print postdata
	#获得posturl
	posturl = get_post_url(page_source)
	print posturl
	file = open('./page_source/page_source99.html','w')
	file.write(page_source)
	file.close()

	#使用requests下载
	session = requests.Session()
	cookies = driver.get_cookies()

	for cookie in cookies:
		session.cookies.set(cookie['name'],cookie['value'])

	response = session.post(posturl,data = postdata,headers = head)

	filename = postdata['fileId'] + '.rar'
	with open(filename,'wb') as file:
		file.write(response.content)

	# return page_source




if __name__ == '__main__':
	# url = 'http://page2.dfpan.com/fs/6For0you220188b6b65'
	print('请输入yunpan链接：')
	url = raw_input()
	get_page_source(url)
	# postdata = get_post_data(page_source)
	# print postdata


















