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
import my_sleep_time as time
# alter_mac = False
def restart_lantern_and_relogin():
	restart_lantern.kill_lantern()
	# 修改完成后登陆
	state = login.login_ten_times() 
	if state=='success' or state == 'already_login':
		time.sleep(1)
		print('登录成功，即将重启蓝灯，可能需要您输入密码')
		state = restart_lantern.restart_lantern()
		print(state)
		time.sleep(1)
		if state == 'lanten_restart_success':
			print('重启蓝灯成功！')
		else:
			print('重启蓝灯失败')
	else:
		print(state)
		print('登录函数返回值异常')
# 修改Mac地址
# 拿到脚本的输出值
def alter_mac_and_relogin():
	status = os.popen('./mac_script.sh').read()
	mac_list = status.split('\n')

	new_mac = mac_list[0]
	mac_in_use = mac_list[1][6:]

	if new_mac==mac_in_use:
		restart_lantern_and_relogin()
	else:
		print("mac 地址修改失败")
		print('  new_mac  = ' + new_mac)
		print('mac_in_use = ' + mac_in_use)

if __name__=='__main__':
	alter_mac_and_relogin()