import urllib
import urllib2
import re

f = open('store.txt','w')

class BDTB:

	def __init__(self, baseUrl, seeLZ):
		self.baseUrl = baseUrl
		self.seeLZ = '?see_lz='+str(seeLZ)

	def getPage(self, pageNum):
		try:
			url = self.baseUrl + self.seeLZ + '&pn=' + str(pageNum)
			request = urllib2.Request(url)
			response = urllib2.urlopen(request)
			f.write(response.read())
			return response
		except urllib2.URLError,e:
			if hasattr(e, "reason"):
				print "fail to connect tieba, reason is:", e.reason
				return None

	
	def getTitle(self):
		f= open('title.txt','w')
		page = self.getPage(1).read()
		pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>',re.S)
		result = re.search(pattern,page)
		if result:
			f.write(result.read())
			return result.group(1).strip()
		else:
			f.write('reurn None')
			return None

	def getContent(self, page):
		f = open('content.txt','w')
		pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
		items = re.findall(pattern, str(page))
		for item in items:
			f.write(item)


baseUrl = "http://tieba.baidu.com/p/3138733512"
bdtb = BDTB(baseUrl, 1)

bdtb.getTitle()
bdtb.getContent(1)

