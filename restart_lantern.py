#-*- coding:utf-8 -*-
'''
重新启动蓝灯 
'''
import os
import time 

# 重启蓝灯
def restart_lantern():
	try:
		os.popen('open -a Lantern.app')
	except Exception as e:
		raise
	else:
		return 'lanten_restart_success'
def kill_lantern():
	pids = os.popen('ps -A | grep Lantern').read()
	id_list = pids.split('\n')
	lantern_pid = id_list[0][1:5]
	try:
		os.popen('sudo kill ' + lantern_pid)
	except Exception as e:
		raise
	else:
		return 'lantern_has_been_killed'
def kill_and_restart_lantern():
	kill_lantern()
	time.sleep(2)
	restart_lantern()

if __name__=="__main__":
	kill_and_restart_lantern()
