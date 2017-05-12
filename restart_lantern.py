#-*- coding:utf-8 -*-
'''
重新启动蓝灯 
'''
import os
import time 

# 重启蓝灯
def restart_lantern():
	try:
		print('restart.....')
		time.sleep(2)
		os.popen('open -a Lantern.app')
		time.sleep(1)
	except Exception as e:
		print('exception.....')
		raise
	else:
		print('return.......')
		return 'lanten_restart_success'
def kill_lantern():
	pids = os.popen('ps -A | grep Lantern').read()
	# id_list = pids.split('\n')
	# lantern_pid = id_list[0][1:5]
	# print(pids.split(' '))
	id_list = [int(s) for s in pids.split(' ') if s.isdigit()]
	try:
		os.popen('sudo kill ' + str(id_list[0]))
		pass
	except Exception as e:
		raise
	else:
		return 'lantern_has_been_killed'
def kill_and_restart_lantern():
	kill_lantern()
	time.sleep(2)
	restart_lantern()

if __name__=="__main__":
	kill_lantern()
