#!/bin/python
import string
import sys

import dbconn

sys.setdefaultencoding('utf8')


def get_days():
    days = []
    sql = "select date from stocks group by date order by date;"

    result = ai_conn.get_data_result(sql)
    if result[0] != True:
        return days
    else:
        for r in result[1]:
            days.append(r[0].encode("utf-8"))
    return days


def get_day_list_count(all_days):
    day_list_count = []
    i = 0
    while i < len(all_days):
        tmp_days = all_days[i:test_day + result_day + i]
        i += 1
        if len(tmp_days) == test_day + result_day:
            day_list_count.append(tmp_days)
    return day_list_count


def count_stocks_data(days, test_day, result_day, stock_code):
    all_type_data = {}
    all_stock_data = {}
    daylist = "'"
    index = 1
    for day in days:
        if index < len(days):
            index += 1
            daylist += day + "','"
        else:
            daylist += day + "'"

    sql = "select stock_type,stock_code,date,open_price,close_price,diff_rate from stocks where date in (%s) order by stock_type,stock_code,date;" % daylist

    result = ai_conn.get_data_result(sql)
    if result[0] != True:
        pass
    else:
        stock_types = {}
        for i in result[1]:
            stock_type = i[0].encode("utf-8")
            if not stock_types.has_key(stock_type):
                stock_types[stock_type] = {}
            else:
                pass
        for i in result[1]:
            stock_type = i[0].encode("utf-8")
            stock_code = i[1].encode("utf-8")
            date = i[2].encode("utf-8")
            open_price = i[3]
            close_price = i[4]
            diff_rate = i[5]
            if open_price == 0 or close_price == 0:
                continue
            if not stock_types[stock_type].has_key(stock_code):
                stock_types[stock_type][stock_code] = []
                stock_types[stock_type][stock_code].append([date, open_price, close_price, diff_rate])
            else:
                stock_types[stock_type][stock_code].append([date, open_price, close_price, diff_rate])

    type_count_data = {}

    stock_result_data = {}
    for t in stock_types:
        type_count_data[t] = -1
        stock_data = {}
        for stock in stock_types[t]:
            if len(stock_types[t][stock]) != test_day + result_day:
                pass
            else:
                day2 = stock_types[t][stock][-1][2]
                day1 = stock_types[t][stock][-2][2]

                if day1 == day2:
                    stock_result_data[stock] = 0
                if (day2 - day1) / day1 > 0.02:
                    stock_result_data[stock] = 1
                else:
                    stock_result_data[stock] = 0

                stock_data[stock] = count_single_stock(stock_types[t][stock])

        if len(stock_data) != 0:
            type_count_data[t] = count_stocks(stock_data)

    if len(type_count_data) == 66:
        all_type_data[days[0]] = type_count_data
    all_stock_data[days[0]] = stock_result_data
    result = search_and_get_data(days[0], stock_code, all_type_data, all_stock_data)

    if result is not False:
        goout(result[0], result[1])


def goout(source, dst):
    tmp_list = []
    for i in source:
        tmp_list.append(str(i))
    print(','.join(tmp_list) + ',' + str(dst))


def search_and_get_data(day, stock_code, all_type_data, all_stock_data):
    if all_type_data.has_key(day) and all_stock_data.has_key(day):
        if all_stock_data[day].has_key(stock_code):
            test_record_list = sortedDictByKeys(all_type_data[day])
            return test_record_list, all_stock_data[day][stock_code]
    return False


def count_single_stock(data):
    # [['2010-01-05', 6.94, 6.99, 0.72],
    # ['2010-01-06', 6.99, 6.99, 0.0],
    # ['2010-01-07', 6.95, 6.79, -2.86],
    # ['2010-01-08', 6.79, 6.86, 1.03],
    # ['2010-01-11', 6.9, 6.92, 0.87],
    # ['2010-01-12', 6.9, 7.19, 3.9],
    # ['2010-01-13', 7.08, 7.1, -1.25]]
    seven_days_data = []
    for day_data in data:
        seven_days_data.append(day_data[3])
    return averagenum(seven_days_data)


def count_stocks(data):
    stocks_data = []
    for day_data in data:
        stocks_data.append(data[day_data])
    return averagenum(stocks_data)


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


def sortedDictByKeys(adict):
    items = adict.items()
    items.sort()
    return [value for key, value in items]


if __name__ == "__main__":
    test_day = 5
    result_day = 2
    ai_conn = dbconn.ai_conn
    all_days = get_days()

    stock_code = "000404"
    if len(all_days) == 0:
        pass
    else:
        day_list = get_day_list_count(all_days)
        for d in day_list:
            count_stocks_data(d, test_day, result_day, stock_code)

