#!/bin/python
import json
import os
import sys

import config


def averagenum(num):
    nsum = 0
    for i in range(len(num)):
        nsum += num[i]
    return nsum / len(num)


def mediannum(num):
    listnum = [num[i] for i in range(len(num))]
    listnum.sort()
    lnum = len(num)
    if lnum % 2 == 1:
        i = int((lnum + 1) / 2) - 1
        return listnum[i]
    else:
        i = int(lnum / 2) - 1
        return (listnum[i] + listnum[i + 1]) / 2


def publicnum(num, d=0):
    dictnum = {}
    for i in range(len(num)):
        if num[i] in dictnum.keys():
            dictnum[num[i]] += 1
        else:
            dictnum.setdefault(num[i], 1)
    maxnum = 0
    maxkey = 0
    for k, v in dictnum.items():
        if v > maxnum:
            maxnum = v
            maxkey = k
    return maxkey


def compute_type_data(stock_type, day_range, test_day, result_day):
    stocks_data_list = []
    for stock in os.listdir(data_dir + os.sep + stock_type + os.sep):
        single_stock_data_list = []
        for i in os.listdir(data_dir + os.sep + stock_type + os.sep + stock):
            if ".json" in i:
                with open(data_dir + os.sep + stock_type + os.sep + stock + os.sep + i, "r") as f:
                    d = json.loads(f.read())
                    if len(d["showapi_res_body"]["list"]) != 0:
                        for day_data in d["showapi_res_body"]["list"]:
                            if day_data["date"] in day_range:
                                single_stock_data_list.append(float(day_data["diff_rate"].encode("utf-8")))
        if len(single_stock_data_list) == test_day + result_day:
            stocks_data_list.append(averagenum(single_stock_data_list))
    if len(stocks_data_list) == 0:
        return False, 0
    else:
        return True, averagenum(stocks_data_list)


def sortedDictByKeys(adict):
    items = adict.items()
    items.sort()
    return [value for key, value in items]


def compute_stock_data(stock_types, day_range, test_day, result_day, stock_code):
    stock_result_d = {}
    for stock_type in stock_types:
        for stock in os.listdir(data_dir + os.sep + stock_type + os.sep):
            for i in os.listdir(data_dir + os.sep + stock_type + os.sep + stock):
                if ".json" in i:
                    with open(data_dir + os.sep + stock_type + os.sep + stock + os.sep + i, "r") as f:
                        d = json.loads(f.read())
                        if len(d["showapi_res_body"]["list"]) != 0:
                            for day_data in d["showapi_res_body"]["list"]:
                                if day_data["date"] in day_range:
                                    if stock_code == stock:
                                        stock_result_d[day_data["date"]] = [day_data["open_price"],
                                                                            day_data["close_price"]]
            if len(stock_result_d) == test_day + result_day:
                d = sortedDictByKeys(stock_result_d)
                return d
                break
    return []

if __name__ == "__main__":
    test_day = 5
    result_day = 2
    data_dir = "data"
    index = 0
    types = [i for i in os.listdir(data_dir + os.sep)]
    stock_code = sys.argv[1]
    day_range = sys.argv[2]
    data = []
    for t in types:
        ctdata = compute_type_data(t, day_range, config.test_day, config.result_day)
        if ctdata[0]:
            data.append(ctdata[1])

    day_range_stock_result = compute_stock_data(types, day_range, config.test_day, config.result_day, stock_code)
    stock_result = -1
    print(day_range_stock_result)
    if len(day_range_stock_result) == config.test_day + config.result_day:
        stop = float(day_range_stock_result[config.test_day + config.result_day - 1][1].encode("utf-8"))
        start = float(day_range_stock_result[config.test_day + config.result_day - 2][0].encode("utf-8"))

        if start == 0:
            stock_result = 0
        if (stop - start) / start * 100 > 5:
            stock_result = 1
        else:
            stock_result = 0
    print([data, stock_result])

