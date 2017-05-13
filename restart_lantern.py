#-*- coding:utf-8 -*-
'''
重新启动蓝灯 
'''
import os
import my_sleep_time as time

# 重启蓝灯
def restart_lantern():
	try:
		# print('正在重启蓝灯.....')
		os.popen('open -a Lantern.app')
		time.sleep(5)
		# 最小化窗口
		os.popen('osascript hide.scpt')
	except Exception as e:
		print('exception.....')
		pass
	else:
		# print('return.......')
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
	time.sleep(4)
	restart_lantern()

def is_lantern_on():
	pids = os.popen('ps -A | grep Lantern').read()
	id_list = []
	for line in pids.split('\n'):
		# print line
		id_list = id_list + [int(s) for s in line.split(' ') if s.isdigit()]
	# print id_list
	# print len(id_list)
	# 小于 3 说明蓝灯未开启
	if len(id_list) < 3:
		# print('未开启')
		return False
	else:
		return True

if __name__=="__main__":
	is_lantern_on()
