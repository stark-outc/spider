# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 10:05:12 2020

@author: 徐钦华
"""

import requests
from pprint import pprint
import json
from datetime import datetime,timedelta
import pandas as pd

today = datetime.today()
gap = 15
beginTime = (today-timedelta(days=gap)).strftime('%Y-%m-%d')
endTime = (today-timedelta(days=3)).strftime('%Y-%m-%d')
save_path = 'D://银行日报相关//'

# 挖财
bank = '恒丰银行'
limit = 300
userName_wc = ""
password_wc = ""
data_login_wc = {"userName": userName_wc,"password": password_wc}
data_target_wc = {"beginTime": beginTime, "endTime": endTime,"name":bank, "limit": str(limit), "pageNum": "1","type": "card"}
login_url_wc = 'https://dianshi.wacai.com/ssp/api/ad-merchant/api/v1/user/login'
target_url_wc = 'https://dianshi.wacai.com/ssp/api/ad-merchant/api/v1/user/settlement-data'
headers_wc = {'Accept': 'application/json, text/plain, */*',
 'Accept-Encoding': 'gzip, deflate, br',
 'Accept-Language': 'zh-CN,zh;q=0.9',
 'Connection': 'keep-alive',
 'Content-Type': 'application/json;charset=UTF-8',
 'Host': 'dianshi.wacai.com',
 'Origin': 'https://dianshi.wacai.com',
 'Referer': 'https://dianshi.wacai.com/ssp/user/login',
 'Sec-Fetch-Dest': 'empty',
 'Sec-Fetch-Mode': 'cors',
 'Sec-Fetch-Site': 'same-origin',
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
               '(KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
 'x-requested-with': 'XMLHttpRequest'}

key_list_wc=['visitNum','entryNum','oneEntryNum','validEntryNum','firstCheckNum','oneFirstCheckNum','effectiveFirstCheckNum',
          'middleFirstCheckNum','highFirstCheckNum','awardCardNum','commonCardNum','uncommonCardNum','goldCardNum','newUserNum','activationNum','firstBrushNum',
          'finalCheckNum','highQualityCustomerANum','highQualityCustomerBNum']
key_list_hsl=['time','url_code','bank_name','company_name','submit','valid_submit','first_trial','check','new_check','activate','first_brush','artificial','refused']

#豪斯莱
bank_map = {'恒丰银行':'87'}
login_url_hsl = "http://ccard.yingbei365.com/index.php/Login/getLogin"
target_url_hsl = "http://ccard.yingbei365.com/index.php/Settlement/day_list"
data_login_hsl = {'u': '','p': ''}
data_target_hsl = {'bank_id': bank_map['恒丰银行'],'page': '1','datemin': beginTime,'datemax': endTime,type: 0}
headers_hsl ={'Host': 'ccard.yingbei365.com',
'Connection': 'keep-alive',
'Accept': 'application/json, text/plain, */*',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
'Content-Type': 'application/x-www-form-urlencoded',
'Origin': 'http://ccard.yingbei365.com',
'Referer': 'http://ccard.yingbei365.com/web/',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9'}

