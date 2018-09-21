#!/usr/bin/python3
import config
import function
import time

list_item=function.select_items("select * from items")
for item in list_item:
    data=function.get_info_time(item)
    for d in data:
        value=d['rate']
        clock=time.mktime(time.strptime(d['date'], '%Y-%m-%d %H:%M:%S'))
        function.insert("insert into history (name,value,clock) value ('"+item+"','"+str(value)+"','"+str(clock)+"')")


