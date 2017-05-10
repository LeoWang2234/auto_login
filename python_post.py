'''
用于测试python  的 post 请求
'''
import requests

login_url = "http://172.20.3.81:801/include/auth_action.php"
headers = {'Host':'172.20.3.81:801'}
post_data = {'action':'login','username':'Y30150635@free','password':'{B}d2FuZ2NoZW5n','ac_id':'3','user_ip':'172.21.196.132','nas_ip':'','user_mac':'98:7f:27:22:0e:c8','ajax':'1'}
post = requests.post(login_url,headers=headers,data=post_data)
print(post.text)  
# action=login&username=Y30150635@free&password={B}d2FuZ2NoZW5n&ac_id=3&user_ip=172.21.195.123&nas_ip=&user_mac=f0:e8:4d:8b:70:35&ajax=1