from config import APIKEY
from CryptoApp.modelsV2Kidu import *
import datetime

#checking for all coins
all_coins = AllCoinsApiIO()
all_coins.getAllCoins(APIKEY)

date = datetime.date.today()
time = datetime.datetime.now().strftime('%H:%M:%S')


print("Date: ", date)
print("Time: ", time)


#print("Number of all coins: ",len(all_coins.total_coins))
#print("Number of crypto coins: ",len(all_coins.crypto_coins))
#print("Real coins: ",len(all_coins.real_coins))

###################################


coin_from = input("Enter a coin to exchange from: ").upper()#makes the input to be always uppercase


while coin_from != "" or not coin_from.isalpha():
    if coin_from in all_coins.total_coins:
        quantity_from = input("Enter quantity to exchange from: ")

        while quantity_from != "" or not quantity_from.isnumeric():
            if quantity_from.isnumeric():
                quantity_from = float(quantity_from)

                coin_to = input("Enter a coin to exchange to: ").upper()

                while coin_to != "" or not coin_to.isalpha():
                    if coin_to in all_coins.total_coins:
                        exchange = Exchange(coin_from, coin_to)
                        try:
                            exchange.updateExchange(APIKEY)
                            quantity_to =  quantity_from * exchange.rate
                            print ("Quantity exchanged to: {:.5f}€".format(quantity_to))
                            break
                        except ModelError as error:
                            print(error)

                    coin_to = input("Enter a coin to exchange to: ").upper()
                break                   
            quantity_from = input("Enter quantity to exchange from: ")
      
    coin_from = input("Enter a coin to exchange from: ").upper()




