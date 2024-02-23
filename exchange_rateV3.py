from config import APIKEY
from CryptoApp.models import *

#checking for all coins
all_coins = AllCoinsApiIO()
all_coins.getAllCoins(APIKEY)





print("Number of all coins: ",len(all_coins.total_coins))
print("Number of crypto coins: ",len(all_coins.crypto_coins))
print("Real coins: ",len(all_coins.real_coins))



###################################


coin_from = input("insert a coin to exchange from:").upper()#makes the input to be always uppercase


while coin_from != "" or not coin_from.isalpha():
    if coin_from in all_coins.crypto_coins:#this search in the list of crypto_coins if the input from coin_from exists inside
       exchange = Exchange(coin_from)
       try:
          exchange.updateExchange(APIKEY)
          print("rate: {:.2f}€".format(exchange.rate))
       except ModelError as error:
          print(error)
       
    coin_from = input("insert a coin to exchange from: ").upper()



