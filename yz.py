#!/usr/bin/env python3
#
#	Python3 script scrape roix data from icodrops.
#   @Author jingkai.
#   Written for my friend.
#	

import requests
from bs4 import BeautifulSoup
import csv
import datetime

def get_html_vals(dict_of_coins):
    r = requests.get('https://icodrops.com/ico-stats/')
    soup = BeautifulSoup(r.content,'html.parser')
    ico_stat = soup.findAll('div',{'id':'ico_stats'})
    for stat in ico_stat:
        try:
            name = stat['data-ticker']
            hprice = float(stat['data-hprice'])
            erate = float(stat['data-erate'])
            brate = float(stat['data-brate'])
            c = Coin(name,hprice,erate,brate)
            dict_of_coins[name] = c
        except KeyError:
            pass

def get_json_info(dict_of_coins):
    coinjson = requests.get('https://icodrops.com/cron.json').json()
    for entry in coinjson:
        try:
            c = dict_of_coins[entry["id"]] 
            c.names = entry["name"]
            c.ticker = {"usd":float(entry["price_usd"]),"btc":float(entry["price_btc"]),"eth":float(entry["price_eth"])}
        except KeyError:
            pass

def write_to_csv(dict_of_coins):
    csv_list = [["Name","USD_ROI","ETH_ROI","BTC_ROI"]]
    for key, coin_obj in dict_of_coins.items():
        csv_list.append(coin_obj.get_csv_array())
    ct = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')
    file_name = "Roi_Report_{}.csv".format(ct)
    with open(file_name,'w') as f:
        writer = csv.writer(f)
        writer.writerows(csv_list)
        print("File {} Written".format(file_name))

class formatter():
    @classmethod
    def formatX(_,func):
        def func_method(*args):
            round_val = str(round(func(*args), 2))
            return "{}x".format(round_val)
        return func_method

class Coin():
    def __init__(self, coin_id, hprice,brate,erate):
        self.__coin_id = coin_id
        self.__name = ""
        self.__hprice = hprice
        self.__brate = brate
        self.__erate = erate
        self.__ticker = 0

    # Debugging,
    def print_obj(self):
        print("Name:"+self.__name)
        print("usd:"+self.getUsdx())
        print("eth:"+self.getEthx())
        print("btc:"+ self.getBtcx())
    
    def get_csv_array(self):
        return [self.__name,self.getUsdx(),self.getEthx(),self.getBtcx()]

    @property
    def ticker(self):
        return self.__ticker
    
    @ticker.setter
    def ticker(self,ticker):
        self.__ticker = ticker
    
    @property
    def coin_id(self):
        return self.__coin_id

    @coin_id.setter
    def coin_id(self,coin_id):
        self.__coin_id = coin_id

    @property
    def names(self):
        return self.__name

    @names.setter
    def names(self,new_name):
        self.__name = new_name

    @formatter.formatX
    def getUsdx(self):
        return self.ticker["usd"]/self.__hprice
    
    @formatter.formatX
    def getEthx(self):
        return (self.ticker["eth"]*self.__brate)/self.__hprice

    @formatter.formatX
    def getBtcx(self):
        return (self.ticker["btc"]*self.__erate)/self.__hprice


if __name__ == "__main__":
    coin_dict = {}
    print("Getting from HTML...")
    get_html_vals(coin_dict)
    print("Getting from JSON....")
    get_json_info(coin_dict)
    write_to_csv(coin_dict)

  