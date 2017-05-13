#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
此程序用于修改Mac地址后，调用登陆函数，自动登录，
获取蓝灯免费流量，

'''
import os
import login
import restart_lantern
import sys
# 修改Mac地址
def change_mac_address():
	status = os.popen('./mac_script.sh').read()
	mac_list = status.split('\n')

	# print(mac_list)
	if len(mac_list[0]) != 17 or len(mac_list[1]) != 23:
		print('取到的mac地址有误')
		return False

	new_mac = mac_list[0]
	mac_in_use = mac_list[1][6:]
	# print len(mac_list[0])
	# print len(mac_list[1])
	if new_mac==mac_in_use:
		return True
	else:
		print("mac 地址修改失败")
		return False

if __name__=='__main__':
	change_mac_address()