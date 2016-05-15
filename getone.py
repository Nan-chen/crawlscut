#-*-coding:utf8-*-


import urllib
import urllib2
import re
from bs4 import BeautifulSoup
import requests
import os
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')
#中文也是可以的这样


f1=open('store.txt','w')
f2=open('img.txt','w')
f3=open('description.txt','w')

for page in range(1000,1050):
	url = 'http://wufazhuce.com/one/'+str(page)
	try:
		response = requests.get(url)
		soup = BeautifulSoup(response.text,"html.parser")
	except:
		print 'page'+str(page)+'download fail!'
		continue

	f2.write(soup.find_all('img')[1]['src']+'\n')
	#下载图片,保存在当前目录的one_image文件夹下
	image_path='one_image'
	if os.path.exists(image_path) is False:
		os.mkdir(image_path)
	temp= image_path + '/%s.jpg' % str(page)
	print u'正在下载第%s页的图片' % str(page)
	try:
		urllib.urlretrieve(urllib2.urlopen(soup.find_all('img')[1]['src']).geturl(),temp)
	except:
		print '第%s页的图片下载失败' % str(page)

	f3.write(soup.title.string[:]+'--') #写编号
	for meta in soup.select('meta'):  #写描述
		if meta.get('name') == 'description':
			f3.write(meta.get('content')+'\n')
	print 'http://wufazhuce.com/one/'+str(page)+u'下载完毕'
			
