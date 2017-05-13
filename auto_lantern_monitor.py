#!/usr/bin/env python
#-*- coding:utf-8 -*-
from lxml import etree
import login
import os
import login_for_auto_traffic_monitor
import regex
import time
import datetime
import my_sleep_time as time
import restart_lantern
import change_mac_address
from selenium import webdriver
from lxml.html.soupparser import fromstring
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def login_ecust():
	# 若是校园网，则自动登录，若不是，则跳过登录
	if(os.popen('ipconfig getifaddr en0').read()[0:6]=='172.21'):
		# 登录开始
		print('您连接的是校园网')
		while True:
			state = login.auto_login()
			if state == 'success' or state == 'already_login':
				break
			else:
				print('登录失败，正在发起新的请求.......')
				time.sleep(5)
				continue
	else:
		print("未监测到网络连接，或者您连的不是校园网")
		# 登录结束
	
def start():
	# 流量小于 10 M 时，自动重新登录
	traffic_low_limit = 10
	# set phantomJS's agent to Firefox
	dcap = dict(DesiredCapabilities.PHANTOMJS)
	dcap["phantomjs.page.settings.userAgent"] = \
	    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 "
	# system path you need to config by yourself
	phantomjsPath = "/Users/cheng/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs"
	driver = webdriver.PhantomJS(executable_path=phantomjsPath, desired_capabilities=dcap)

	driver.set_window_size(1440, 900)
	# 限制重试次数为 3 次
	RETRY_TIME = 3
	retry_time = 0

	while True:
		# 首先判断用户是否在线，若不在，则直接退出

		try:
			# 拿到 html 数据
			driver.get('http://localhost:50833/?1')
			driver.set_page_load_timeout(5)
			# 解析 html. 数据，拿到含有流量大数据 
			capdata = driver.find_element_by_id("capdata")
			# 转换编码
			remained_traffic = capdata.text.encode('ascii','ignore')

			# print remained_traffic
			# 拿到剩余流量并转换成 int 类型
			traffic =  int(regex.findall('\d+', remained_traffic)[0])
			print('当前流量：' + str(traffic))
		except Exception as e:
			# print str(e)
			# print(traffic)
			print('未拿到有效数据,请确定是否已经开启了蓝灯,或者已联网')
			if retry_time <= RETRY_TIME:
				retry_time = retry_time + 1
				print('正在尝试重新获取流量数据')
				time.sleep(2)
				continue
			retry_time = 0
			print('正在尝试帮您重新联网并开启蓝灯.......')
			login_ecust()
			restart_lantern.kill_and_restart_lantern()
			print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			print('开启成功，正在监控流量')
			time.sleep(30)
			continue
		else:
			pass
		finally:
			pass
		if traffic <= traffic_low_limit:
			print("流量趋近枯竭")
			while True:
				# 流量快用完时，自动修改 mac 地址，并重启蓝灯
				if change_mac_address.change_mac_address():
					print('mac 地址已修改生效')
					print('正尝试重新登录')
					# 修改了mac地址后不要那么着急就登录
					time.sleep(10)
					login_ecust()
					print('正尝试重新开启蓝灯')
					restart_lantern.kill_and_restart_lantern()
					print('开启蓝灯成功')
					break
				else:
					print('正在尝试重新修改 Mac 地址')
					continue
			print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			time.sleep(30)
			continue
		else:
			if traffic >= 200:
				print('流量还有很多')
			elif traffic >= 100:
				print('流量还有不到一半')
			elif traffic >= 50:
				print('流量不多啦')
			else:
				print('流量即将告急')
			print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			time.sleep(traffic/5)
			print('--*--*--*--*--*--*--')
			continue
	driver.quit()


if __name__ == '__main__':
	start()