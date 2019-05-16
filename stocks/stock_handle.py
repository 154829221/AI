#!/bin/python
import os
import json
import config

stock_dir="data/"
data_dir="data/jisuanjiyingyong/000034/"
type_dir="data/jisuanjiyingyong/"

def concat_stock_data(data_dir):
    data_list_sort=[]
    if os.path.exists(data_dir):
        day_list=[]
        data_list=[]
        data_list_sort=[]
        for i in os.listdir(data_dir):
            if ".json" in i:
                with open(data_dir+i,"r") as f:
                    d = json.loads(f.read())
                    if len(d["showapi_res_body"]["list"]) != 0:
                        for day_data  in d["showapi_res_body"]["list"]:
                            day_list.append(day_data["date"])
                            data_list.append(day_data)
        day_list.sort()
        for i in day_list:
            for j in data_list:
                if i == j["date"]:
                    data_list_sort.append(j)
        return data_list_sort
    else:
        return data_list_sort


data_dict={}
data_list=[]
def get_data_days():
    for type in os.listdir(stock_dir):
        for stock in os.listdir(stock_dir+type+"/"):
            i =  concat_stock_data(stock_dir+type+"/"+stock+"/")
            for j in i:
                data_dict[j["date"]] = 0

    for i in  data_dict.keys():
        data_list.append(i)
    data_list.sort()
    return data_list


def get_test_days_list():
    test_day_size = config.test_day + config.result_day
    days_list=[]
    i = 0
    while i< (len(config.days)-test_day_size):
        i += 1
        days_list.append(config.days[i:i+test_day_size])
    return days_list


def get_test_datas():
    types = os.listdir(stock_dir)
    for type in types:
        for stock in os.listdir(stock_dir+type+"/"):
            i =  concat_stock_data(stock_dir+type+"/"+stock+"/")


def get_test_lenth():
    return len(get_test_days_list())



def compute1(data_list,test_day):
    start = 0
    end = 0
    for i in range(len(data_list)):
        if i == 0:
            start = data_list[i]["open_price"]
        if i == test_day - 1:
            end = data_list[i]["close_price"]
    return (float(end)-float(start))/float(start)

def get_point(stock_type,many_day):
    d = float(0)
    size = float(0)
    for stock in os.listdir(stock_dir+stock_type+"/"):
        datas = concat_stock_data(stock_dir+stock_type+"/"+stock+"/")
        stock_size = 0
        stock_data = []
        for day in many_day:
            for data in datas:
                if data["date"] == day:
                    stock_size += 1
                    stock_data.append(data)
        if len(many_day) == stock_size:
            #print("Stock %s is get to compute." % stock)
            #print("Stock data is %s" % stock_data)
            t = compute1(stock_data,config.test_day)
            d += t
            size += 1
    return (d/size)


for many_day in get_test_days_list():
    types = os.listdir(stock_dir)
    print(many_day)
    for stock_type in types:
        print("Type %s  : %f" % (stock_type,get_point(stock_type,many_day)))

