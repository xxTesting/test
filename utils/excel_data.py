#!/use/bin/env python
#coding:utf-8 

#Author:WuYa


class ExcelVariable:
	caseID=0
	url=2
	request_data=3
	expect=4
	result=5

def getCaseID():
	return ExcelVariable.caseID

def getUrl():
	return ExcelVariable.url

def get_request_data():
	return ExcelVariable.request_data

def getExpect():
	return ExcelVariable.expect

def getResult():
	return ExcelVariable.result

def getHeadersValue():
	'''获取请求头'''
	headers={
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
		'Cookie':'_ga=GA1.2.1237290736.1534169036; user_trace_token=20180813220356-b7e42516-9f01-11e8-bb78-525400f775ce; LGUID=20180813220356-b7e428ad-9f01-11e8-bb78-525400f775ce; index_location_city=%E5%85%A8%E5%9B%BD; _gid=GA1.2.675811712.1540794503; JSESSIONID=ABAAABAAAGFABEF93F47251563A52306423D37E945D2C54; _gat=1; LGSID=20181029213144-fa3c8e13-db7e-11e8-b51c-525400f775ce; PRE_UTM=; PRE_HOST=www.bing.com; PRE_SITE=https%3A%2F%2Fwww.bing.com%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1539529521,1539785285,1540794503,1540819902; SEARCH_ID=ae3ae41a58d94802a68e848d36c30711; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1540819909; LGRID=20181029213151-fe7324dc-db7e-11e8-b51c-525400f775ce',
		'Referer':'https://www.lagou.com/jobs/list_%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88?labelWords=sug&fromSearch=true&suginput=%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95'}
	return headers
