# -*- coding: UTF-8 -*-

import json
import urllib
import urllib2
import random
import time

try:
	tmp = open("store_parameter.txt", "r")
	tmp.close()
except:
	tmp = open("store_parameter.txt", "w")
	tmp.write("0\n")
	tmp.write("0\n")
	tmp.close()
i_flag = 1
j_flag = 1
read_cnt = open("store_parameter.txt", "r")
tags = ["美食","宾馆","购物","汽车服务","生活服务","结婚","丽人","金融","休闲娱乐","运动健身","医疗","旅游景点","教育","培训机构","交通设施","房地产","自然地物","行政区划","政府机构","公司企业","门址","道路","交通线"]
apikey = "x14xrPrUuRk422dyN5yKCZIf"
min_lng = 118.403
min_lat = 29.2059
lng_total_gap = 2.291
lat_total_gap = 1.3531
lng_gap = 0.006
lat_gap = 0.006
for cnt in range (0, 23):
	if cnt == 8:
		tag = tags[cnt]
		print tag
		file_name = tag+".txt"
		f = open(file_name, "a")
		i = 0.0
		if i_flag == 1:
			i_flag = 0
			i = float(read_cnt.readline())
		while i < lng_total_gap:
			j = 0.0
			if j_flag == 1:
				j_flag = 0
				j = float(read_cnt.readline())
			while j < lat_total_gap:
				time.sleep(random.random()*2)
				small_lng = min_lng + i
				small_lat = min_lat + j
				large_lng = small_lng + lng_gap
				large_lat = small_lat + lat_gap
				location = str(small_lat)+","+str(small_lng)+","+str(large_lat)+","+str(large_lng)
				url = "http://api.map.baidu.com/place/v2/search?&query="+tag+"&bounds="+location+"&output=json&page_num=0&ak="+apikey
				data = json.load(urllib2.urlopen(url))
				f.write(str(data["total"]) + "\t")
				j = j + lat_gap
				store_cnt = open("store_parameter.txt", "w")
				store_cnt.write(str(i)+"\n")
				store_cnt.write(str(j)+"\n")
				store_cnt.close()
				print i
				print j
				print "end"
			i = i + lng_gap
			store_cnt = open("store_parameter.txt", "w")
			store_cnt.write(str(i)+"\n")
			store_cnt.write(str(j)+"\n")
			store_cnt.close()
			f.write("\n")
		f.close()
