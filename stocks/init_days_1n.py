#!/bin/python
import os
import json

test_day = 5
result_day = 2

data_dir="data"
types = [ i for i in os.listdir(data_dir+os.sep)]


day_dict = {}

for type in types:
    codes = [code for code in os.listdir(data_dir+os.sep+type+os.sep)]
    for code in codes:
        for i in os.listdir(data_dir+os.sep+type+os.sep+code+os.sep):
            if ".json" in i:
                with open(data_dir+os.sep+type+os.sep+code+os.sep+i,"r") as f:
                    d = json.loads(f.read())
                    if len(d["showapi_res_body"]["list"]) != 0:
                        for day_data  in d["showapi_res_body"]["list"]:
                            day_dict[day_data["date"]]=""

def sortedDictByKeys(adict): 
    items = adict.keys() 
    items.sort() 
    return [key.encode("utf-8") for key in items] 

day_list = sortedDictByKeys(day_dict)


def get_day_list_count():
    day_list_count=[]
    i = 0
    while i < len(day_list):
        tmp_days = day_list[i:test_day + result_day + i]
        i += 1
        if len(tmp_days) == test_day + result_day:
            day_list_count.append(tmp_days)
    return day_list_count
