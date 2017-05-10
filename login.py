
#-*- coding:utf-8 -*-
'''
此程序用于校园网自动登录，重试十次
'''
import urllib2
import requests
import time
from bs4 import BeautifulSoup
url = 'http://login.ecust.edu.cn/&arubalp=07ab5286-6c88-4ee7-997d-1563e8afb4'

def login_ten_times():
	# 重试十次，每次间隔 5 秒
	num = 10;
	while 0 != num:
		time.sleep(5)
		state = auto_login()
		num = num -1
		if state == 'success' or state == 'already_login':
			return state

def get_response(url):
	response = ''
	try:
		request = urllib2.Request(url)
		response = urllib2.urlopen(request)
	except Exception as e:
		print('获取response失败')
	return response

def auto_login():
	# 拿到response
	response = get_response(url)
	if ''==response:
		return 'success'
	# 拿到response中的location地址，也就是重定向以后的地址
	re_url = response.geturl()
	# print(re_url)

	# 用户已经登陆啦，直接返回
	if(re_url.find('mac')==-1):
		print("yong hu yi deng lu")
		return 'already_login'
	# 用户还没用登陆，执行登陆逻辑
	# 将地址分割为字典的形式
	dictionary = dict(key.split('=') for key in re_url.split('&') )

	# 拿到服务器返回的ip 和本机的 mac 地址
	ip = dictionary.get('ip')
	mac = dictionary.get('mac')

	print('mac = ' + mac)
	print('ip = ' + ip)

	# 构造登陆请求
	login_url = "http://172.20.3.81:801/include/auth_action.php"
	headers = {'Host':'172.20.3.81:801'}
	post_data = {'action':'login','username':'Y30150635@free','password':'{B}d2FuZ2NoZW5n','ac_id':'3','user_ip':ip,'nas_ip':'','user_mac':mac,'ajax':'1'}
	
	try:
		post = requests.post(login_url,headers=headers,data=post_data)
		print('success')
	except Exception as e:
		print('尝试登录失败')
		pass

if __name__ == '__main__':
	login_ten_times()






# print('ip='+ip)
# print('mac='+mac)
# for key in keys:
	# print(key)
# print('-------------------------------')
# print(str)
# print('-------------------------------')
# soup=BeautifulSoup(str,'html.parser')

# metas = soup.find_all("meta")
# print(metas[0].attrs['content'])


# request = urllib2.Request('http://login.ecust.edu.cn/&arubalp=07ab5286-6c88-4ee7-997d-1563e8afb4')







# print(url)
# print(link.get('url'))

# print('-------------------------------')
# print(r.headers)
# print('--------------------------------')
# print(r.text)
# print('--------------------------------')
# print(response.info())
# print('--------------------------------')
# print(response.)
# print('--------------------------------')
# print(response.info()
# print(response.read())
