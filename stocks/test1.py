import urllib, urllib2, sys


code = 600004

years = ["2010","2011","2012","2013","2014","2015","2016","2017","2018","2019"]

months = ["01","02","03","04","05","06","07","08","09","10","11","12"]

#for y in years:
#    for m in mouths:
host = 'http://stock.market.alicloudapi.com'
path = '/sz-sh-stock-history'
method = 'GET'
appcode = '1fea94e11c824500b9d9e558330bbf83'
querys = 'begin=2010-07-01&code=600004&end=2010-07-31'
bodys = {}
url = host + path + '?' + querys

request = urllib2.Request(url)
request.add_header('Authorization', 'APPCODE ' + appcode)
response = urllib2.urlopen(request)
content = response.read()
if (content):
    print(content)
