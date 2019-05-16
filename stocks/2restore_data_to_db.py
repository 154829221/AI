#!/bin/python
import json
import os
import sys

import dbconn

sys.setdefaultencoding('utf8')


def get_and_restore_data(types, conn):
    for stock_type in types:
        for stock in os.listdir(data_dir + os.sep + stock_type + os.sep):
            for i in os.listdir(data_dir + os.sep + stock_type + os.sep + stock):
                if ".json" in i:
                    with open(data_dir + os.sep + stock_type + os.sep + stock + os.sep + i, "r") as f:
                        d = json.loads(f.read())
                        if len(d["showapi_res_body"]["list"]) != 0:
                            for i in d["showapi_res_body"]["list"]:
                                date_s = i["date"].encode("utf-8")
                                stock_type = stock_type.encode("utf-8")
                                stock_code = stock.encode("utf-8")
                                open_price = float(i["open_price"].encode("utf-8"))
                                close_price = float(i["close_price"].encode("utf-8"))
                                max_price = float(i["max_price"].encode("utf-8"))
                                min_price = float(i["min_price"].encode("utf-8"))
                                trade_money = float(i["trade_money"].encode("utf-8"))
                                diff_money = float(i["diff_money"].encode("utf-8"))
                                diff_rate = float(i["diff_rate"].encode("utf-8"))
                                if i["swing"].encode("utf-8") == "":
                                    swing = float(0)
                                else:
                                    swing = float(i["swing"].encode("utf-8"))
                                turnover = float(i["turnover"].encode("utf-8"))
                                market = i["market"].encode("utf-8")

                                sql = "insert into stocks (`date`,`stock_type`,`stock_code`,`open_price`,`close_price`,`max_price`,`min_price`,`trade_money`,`diff_money`,`diff_rate`,`swing`,`turnover`,`market`) values ('%s','%s','%s',%s,%s,%s,%s,%s,%s,%s,%s,%s,'%s')" % (
                                    date_s,
                                    stock_type,
                                    stock_code,
                                    open_price,
                                    close_price,
                                    max_price,
                                    min_price,
                                    trade_money,
                                    diff_money,
                                    diff_rate,
                                    swing,
                                    turnover,
                                    market)
                                print(sql)

                                result = ai_conn.transaction(sql)
                                if result[0] != True:
                                    print(result[1])
                                    continue
                                else:
                                    print(result[1])


if __name__ == "__main__":
    data_dir = "data"
    types = [i for i in os.listdir(data_dir + os.sep)]
    data = []
    ai_conn = dbconn.ai_conn
    get_and_restore_data(types, ai_conn)

