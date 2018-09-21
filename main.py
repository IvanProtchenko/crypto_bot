#!/usr/bin/python3
import logging
import time
import config
import function
def main():
    correct_time=time.time()
    print(correct_time)
    logging.basicConfig(format = u'%(asctime)s [%(levelname)-8s] %(message)s',filename=config.LOGFILE, level=logging.INFO)
    list_item=function.select_items("select * from items")
    dict_info=function.get_info_bitforex(list_item,correct_time)
    if len(dict_info)>0:
        for item in dict_info:
            print(item)
            value_insert=""
            flag=0
            for data in dict_info[item]['data']:
                if flag==0:
                    flag=1
                    pass    
                else:
                    value_insert+=","
                value_insert+="('"+item+"',"+str(data['amount'])+","+str(data['price'])+","+str(data['time'])[:-3]+")"
            function.insert("insert into history (name,amount,price,time) value "+value_insert)
    depth_info=function.get_depth(1,correct_time)
    if len(depth_info)>0:
        function.insert("insert into history_depth (name,amount,time) value ('asks',"+str(depth_info['asks'])+","+str(correct_time)+"),('bids',"+str(depth_info['bids'])+","+str(correct_time)+")")
    

if __name__ == "__main__":
    interval=1
    while(True):
        main()
        time.sleep(1)
