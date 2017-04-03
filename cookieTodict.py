class transCookie:
	def __init__(self,cookie):
		self.cookie = cookie
		"""
		pgv_pvid=6048341432; pt2gguin=o0949898050; 
		RK=VPuO5rpLVa; 
		ptcz=a0d01abe740fca2ac5628f3cc3e090a565a9034a894857f3cc33e9bff0b3470b; 
		_qz_referrer=i.qq.com;
		pgv_pvi=9715714048; 
		pgv_si=s5326641152;
		_qpsvr_localtk=0.3871737558646893;
		pgv_info=ssid=s3528572020
		"""
	def stringToDict(self):
		itemDict = {}
		items = self.cookie.split(";")
		for item in items:
			key = item.split("=")[0].replace(' ','').replace('//n',"")
			value = item.split("=")[1]
			itemDict[key] = value
		return itemDict
	