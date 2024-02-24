import requests
from config import APIKEY

class ModelError(Exception):
    pass

class AllCoinsApiIO:
    def __init__(self):
        self.url=""
        self.crypto_coins=[]
        self.real_coins =[]
        self.diclist_coins = []
        self.total_coins = []


    def getAllCoins(self, apikey):
        self.url = f"https://rest.coinapi.io/v1/assets/?apikey={APIKEY}"
        r = requests.get(self.url)
        if r.status_code != 200:
            raise Exception("Error in code query:{}".format(r.status_code))
        
        self.diclist_coins = r.json()
        

        for dic in self.diclist_coins:
            if dic["type_is_crypto"] == 1:
                self.crypto_coins.append(dic["asset_id"]) 
            else:
                self.real_coins.append(dic["asset_id"])

        self.total_coins = self.crypto_coins + self.real_coins

class Exchange:
    def __init__(self, coinFrom, coinTo):
        self.rate = None
        self.coin_from = coinFrom
        self.coin_to = coinTo
        self.status_code = None


    def updateExchange(self,apikey):
        url = f"https://rest.coinapi.io/v1/exchangerate/{self.coin_from}/{self.coin_to}?apikey={APIKEY}"#this is the request to acces the link
        r = requests.get(url)#this is the request to acces the link
        self.status_code = r.status_code
        #1st exercise
        dic = r.json()#adds the data from json to the dic variable

        #2nd exercise
        if r.status_code == 200:
            self.rate = dic["rate"]
            
        else:
           raise ModelError(f"status:{r.status_code}, error: {dic['error']}")
        