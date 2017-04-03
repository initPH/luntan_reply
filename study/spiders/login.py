# -*- coding:utf-8 -*-
from scrapy.spiders import Spider
from scrapy import Request
from scrapy.conf import settings #导入设置里的cookie
from scrapy import FormRequest
import random #随机评论

class Login(Spider):
	name = "login" #爬虫名字
	allowed_domains = ["bbs.fishc.com"]
	start_urls =["http://bbs.fishc.com/thread-76536-1-1.html"]#回复的网址
	
	cookie = settings["COOKIE"]
	print(cookie)
	headers = {
	'Connection':'keep-alive',
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
	}#加头部
	
	meta = {
	'dont_redirect':True,
	'handle_httpstatus_list':[301,302]
	}
	
	def start_requests(self):
		yield Request(self.start_urls[0],callback=self.parse,cookies = self.cookie,
		headers=self.headers,meta = self.meta)
		
	
	def parse(self,response):
		print("in parse")
		# with open("check.html","wb") as f:
			# f.write(response.body)
		form_action = response.xpath('//*[@id="fastpostform"]/@action').extract()[0]
		print("1")
		print(form_action)
		print("2")
		action = "http://"+self.allowed_domains[0]+'/'+form_action+"&inajax=1"
		print(action)
		print('http://bbs.fishc.com/forum.php?mod=post&action=reply&fid=173&tid=84530&extra=page%3D1&replysubmit=yes&infloat=yes&handlekey=fastpost&inajax=1')
		replys = [b'\xc2\xa5\xd6\xf7\xba\xc3\xc0\xf7\xba\xa6',
					b'\xc0\xf7\xba\xa6\xb5\xc4\xd2\xbb\xc5\xfa'
		]
		reply = replys[random.randint(0,1)]
		formdata ={
			'posttime':response.xpath('//*[@id="posttime"]/@value').extract()[0],
			'formhash':response.xpath('//*[@id="fastpostform"]/table/tr/td[2]/input[2]/@value').extract()[0],
			'usesig':response.xpath('//*[@id="fastpostform"]/table/tr/td[2]/input[3]/@value').extract()[0],
			'subject':response.xpath('//*[@id="fastpostform"]/table/tr/td[2]/input[4]/@value').extract()[0],
			'message':reply
		}
		print(3)
		yield FormRequest(action,callback=self.finish,
		headers = self.headers,cookies=self.cookie,
		meta=self.meta,formdata=formdata)
		print(4)
		return
		
	def finish(self,response):
		print(5)
		print("reply success")