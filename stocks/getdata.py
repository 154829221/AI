#!/bin/python
import urllib, urllib2, sys
import os
import time
import random
import sys

code = sys.argv[2]
stock_type = sys.argv[1]

years = ["2010","2011","2012","2013","2014","2015","2016","2017","2018","2019"]

months = ["01","02","03","04","05","06","07","08","09","10","11","12"]

def create_dir_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

for y in years:
    for m in months:
        create_dir_if_not_exists("data/%s" % stock_type)
        create_dir_if_not_exists("data/%s/%s" % (stock_type,code))
        filename=("data/%s/%s/%s_%s.json" % (stock_type,code,y,m))
        if not os.path.exists(filename):
            time.sleep(5)
            time.sleep(random.random()*6)
            time.sleep(random.random()*6)
            time.sleep(random.random()*6)
            host = 'http://stock.market.alicloudapi.com'
            path = '/sz-sh-stock-history'
            method = 'GET'
            appcode = '1fea94e11c824500b9d9e558330bbf83'
            querys = 'begin='+y+'-'+m+'-01&code='+code+'&end='+y+'-'+m+'-31'
            bodys = {}
            url = host + path + '?' + querys
            print url
            request = urllib2.Request(url)
            request.add_header('Authorization', 'APPCODE ' + appcode)
            response = urllib2.urlopen(request)
            content = response.read()
            if (content):
                with open(filename,'w') as load_f:
                    load_f.write(content)
