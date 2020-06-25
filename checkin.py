
import requests, time, re, rsa, json, base64, argparse
from urllib import parse
# server酱开关，填0不开启(默认)，填1只开启cookie失效通知，填2同时开启cookie失效通知和签到成功通知
sever = '2'
# 填写server酱sckey,不开启server酱则不用填

sckey = 'SCU89402Tf98b7f01ca3394b9ce9aa5e2ed1abbae5e6ca42796bb9'
# 填入glados账号对应cookie
cookie = '__cfduid=d3459ec306384ca67a65170f8e2a5bd561593049467; _ga=GA1.2.766373509.1593049472; _gid=GA1.2.1338236108.1593049472; koa:sess=eyJ1c2VySWQiOjQxODMwLCJfZXhwaXJlIjoxNjE4OTY5NTI4MzY4LCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=6qG8SyMh_5KpSB6LBc9yRviaPvI'

def start():
  res = requests.get("https://glados.live/console/checkin", headers={'cookie': cookie })
  if 'leftDays' in res.text:
    print(res.text)
    if sever == '2':
      if res.json()['result'] == 'ok':
        requests.get('https://sc.ftqq.com/' + sckey + '.send?text=签到成功，你还有'+leftDays+'天可用')
  else:
    if sever != '0':
      requests.get('https://sc.ftqq.com/' + sckey + '.send?text=cookie过期')

def main_handler(event, context):
  return start()

if __name__ == '__main__':
  start()

