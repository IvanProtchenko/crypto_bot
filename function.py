#!/usr/bin/python3
import time
import logging
import pymysql
import config
import requests

def select(sql):
    db = pymysql.connect(config.MYSQLHOST,config.MYSQLUSER,config.MYSQLPASS,config.MYSQLDB )
    cursor = db.cursor()
    cursor.execute(sql)
    logging.info("query "+sql)
    data = cursor.fetchall()
    db.close()
    #print (data)
    return data

def select_items(sql):
    db = pymysql.connect(config.MYSQLHOST,config.MYSQLUSER,config.MYSQLPASS,config.MYSQLDB )
    cursor = db.cursor()
    cursor.execute(sql)
    logging.info("query "+sql)
    data = cursor.fetchall()
    db.close()
    list_items=[]
    for i in data:
        for ii in i:
            list_items.append(ii)
    #print (list_items)
    return list_items


def insert(sql):
    db = pymysql.connect(config.MYSQLHOST,config.MYSQLUSER,config.MYSQLPASS,config.MYSQLDB )
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        logging.info("query "+sql)
    except:
        db.rollback()
        logging.warning("query rollback "+sql)
    db.close()

def get_info_time(item):
    period=2678400
    correct_time=int(time.time())
    start=correct_time-period
    end=correct_time
    r = requests.get("https://poloniex.com/public?command=returnTradeHistory&currencyPair="+item+"&start="+str(start)+"&end="+str(end))
    rr=eval(r.text)
    return rr
    print('ok')

def get_info(list_item):
    item_res={}
    correct_time=int(time.time())
    interval=10
    if correct_time % interval == 0:
        r = requests.get("https://poloniex.com/public?command=returnTicker")
        logging.info("get https://poloniex.com/public?command=returnTicker")
        for item in list_item:
            rr=eval(r.text)
            item_res[item]={'value':rr[item]['last'],'clock':str(correct_time)}
            #print(rr[item]['last'])
        return item_res
    else:
        return {}

def get_info_bitforex(list_item,correct_time):
    true=1
    false=0
    item_res={}
    correct_time=int(correct_time)
    interval=10
    if correct_time % interval == 0:
        for item in list_item:
            r = requests.get("https://api.bitforex.com/api/v1/market/trades?symbol="+item+"&size=600")
            logging.info("GET https://api.bitforex.com/api/v1/market/trades?symbol="+item+"&size=600")
            #print(r.text)
            rr=eval(r.text)
            try:
                item_res[item]={'data':rr['data']}
                
            except:
                logging.warning(rr)
                return {}
        return item_res
    else:
        return {}

def get_depth(count,correct_time):
    true=1
    false=0
    correct_time=int(correct_time)
    interval=10
    if correct_time % interval == 0:
        r = requests.get("https://api.bitforex.com/api/v1/market/depth?symbol=coin-usdt-btc&size=200")
        logging.info("GET https://api.bitforex.com/api/v1/market/depth?symbol=coin-usdt-btc&size=200")
        rr=eval(r.text)
        count_asks=len(rr['data']['asks'])
        count_bids=len(rr['data']['bids'])
        #print({'asks':count_asks,'bids':count_bids})
        return {'asks':count_asks,'bids':count_bids}
    else:
        return {}

        

