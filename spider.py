# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 10:08:54 2020

@author: 徐钦华
"""
import requests
from pprint import pprint
import json
from datetime import datetime,timedelta
import pandas as pd
from config import *
class get_table_spider(object):
    def __init__(self):
        self.beginTime = beginTime
        self.endTime = endTime
    def get_data(self,partner=None,headers=None,data_login=None,data_target=None,login_url=None,target_url=None):
        session = requests.Session()
        if partner== 'wc':
            res0 = session.post(login_url,data=json.dumps(data_login),headers=headers,verify=False)
            token = res0.json().get('tokenId')
            session.headers.update({'token':token})
            res = session.post(target_url, data=json.dumps(data_target), headers=headers,verify=False)
            return res.json()
        elif partner == 'hsl':
            res0 = session.post(login_url, data=data_login, headers=headers)
            res0.encoding = res0.apparent_encoding
            session3rd = res0.json().get('data')['session3rd']
            data_target['session3rd'] = session3rd
            res = session.post(target_url,data = data_target,headers=headers)
            res.encoding = res.apparent_encoding
            num = res.json().get('data')['count']
            page_num = int(num) // 10 + 1
            lst=[]
            for n in range(1, page_num + 1):
                data_target['page'] = n
                res1 = session.post(target_url,data = data_target,headers=headers)
                res1.encoding = res.apparent_encoding
                lst.append(res1.json())
            return lst


    def parse_data_wc(self):
        data = self.get_data(partner='wc',headers=headers_wc,data_login=data_login_wc,data_target=data_target_wc,login_url=login_url_wc,target_url=target_url_wc)
        card = data.get('objects')
        lst=[]
        for i in card:
            dic = dict()
            dic['stat_date'] = i['settlementDate']
            dic['bank'] = i['financeOrg']['shortName']
            dic['channelCode'] = i['channelCode']
            for j in key_list_wc:
                dic[j] = i[j]
            lst.append(dic)
        final_data = pd.DataFrame(lst)
        final_data['stat_date'] = final_data['stat_date'].map(lambda x: str(x)[:10])
        return final_data
    def parse_data_hsl(self):
        data = self.get_data(partner='hsl', headers=headers_hsl, data_login=data_login_hsl, data_target=data_target_hsl,login_url=login_url_hsl, target_url=target_url_hsl)
        group_lst = list()
        for i in data:
            lst = list()
            card = i.get('data')['list']
            for j in card:
                dic = dict()
                for q in key_list_hsl:
                    dic[q] = j[q]
                lst.append(dic)
            group_lst.extend(lst)
        final_data = pd.DataFrame(group_lst)
        # final_data['time'] = final_data['time'].map(lambda x: str(x)[:10])
        return final_data
def save_data(save_data=None,save_partner=None):
        re_date = today.strftime('%m%d')
        save_data.to_csv(save_path+f'{save_partner}_form'+re_date+'.csv',encoding='utf_8_sig',index=False,line_terminator="\n")
        return print(f'{save_partner}_form{re_date}.csv 成功写入')

if __name__=='__main__':
    save_data_wc =get_table_spider().parse_data_wc()
    save_data(save_data=save_data_wc,save_partner='wc')