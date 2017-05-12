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
# alter_mac = False
def restart_lantern_and_relogin():
	restart_lantern.kill_lantern()
	# 修改完成后登陆
	state = login.login_ten_times() 
	if state=='success' or state == 'already_login':
		print('登录成功，即将重启蓝灯，可能需要您输入密码')
		state = restart_lantern.restart_lantern()
		if state == 'lanten_restart_success':
			print('重启蓝灯成功！')
		else:
			print('重启蓝灯失败')
	else:
		print(state)
		print('登录函数返回值异常')
# 修改Mac地址
def change_mac_address():
	status = os.popen('./mac_script.sh').read()
	mac_list = status.split('\n')

	print(mac_list)
	new_mac = mac_list[0]
	mac_in_use = mac_list[1][6:]

	if new_mac==mac_in_use:
		return True
	else:
		print("mac 地址修改失败")
		print('  new_mac  = ' + new_mac)
		print('mac_in_use = ' + mac_in_use)
		return False
# 拿到脚本的输出值
def alter_mac_and_relogin():
	print("确实要修改Mac地址吗？还有流量未用完，请杜绝浪费")
	print('修改请输入 yes ,只是重启蓝灯并重新登录请输入 no ,任意键退出')
	answer = str(raw_input("请输入你的决定："))
	# print(answer)
	if answer!='yes' and answer!='no':
		answer='exit'
	# 确定修改时
	# print(answer)
	if answer=='yes':
		# print("条件为真")
		# return
		path = os.path.dirname(sys.argv[0])
		print(path)
		os.chdir(path)
		while True:
			if change_mac_address():
				restart_lantern_and_relogin()
				break
			print('正在尝试重新修改 Mac 地址')
	# 重新登录并重启蓝灯
	elif answer=='no':
		# print('你输入的是no')
		restart_lantern_and_relogin()
	elif answer=='exit':
		print("程序退出")
		sys.exit(0)
		return

if __name__=='__main__':
	alter_mac_and_relogin()