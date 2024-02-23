import requests
from config import APIKEY

url = f"https://rest.coinapi.io/v1/assets/?apikey={APIKEY}"
r = requests.get(url)

if r.status_code != 200:
    raise Exception("Error in code query:{}".format(r.status_code))
       
        

   

dic_coins = r.json()
crypto_coins = []
real_coins= []

for dic in dic_coins:
    if dic["type_is_crypto"] == 1:
       crypto_coins.append(dic["asset_id"])
    else:
        real_coins.append(dic["asset_id"])

all_coins = crypto_coins + real_coins 



#print("Number of all coins: ",len(all_coins))
#print("Number of crypto coins: ",len(crypto_coins))
#print("Real coins: ",len(all_coins) - len(crypto_coins))
#print("All the crypto:", crypto_coins)


###################################


coin_from = input("insert a coin to exchange from:").upper()#makes the input to be always uppercase


while coin_from != "" or not coin_from.isalpha(): 
    if coin_from in all_coins:#this search in the list of crypto_coins if the input from coin_from exists inside
        url = f"https://rest.coinapi.io/v1/exchangerate/{coin_from}?apikey={APIKEY}"#this is the request to acces the link
        r = requests.get(url)#this is the request to acces the link

        coin_to = input("insert a coin to exchange to:").upper()

        while coin_to != "" or not coin_from.isalpha():
            if coin_to in all_coins:
                exchangeRate_url = f"https://rest.coinapi.io/v1/exchangerate/{coin_from}/{coin_to}?apikey={APIKEY}"#this is the request to acces the link
                r = requests.get(exchangeRate_url)#this is the request to acces the link

                #1st exercise
                dic_link = r.json()#adds the data from json to the dic variable

                #2nd exercise
                if r.status_code == 200:
                    print("rate: {:.5f}€".format(dic_link["rate"]))#this prints the value of the key rate with two decimal
                    
                    break
                else:
                    print("error",dic_link["error"])#this if the link is wrong it will give a specific error that it´s already programed in the data of json
            coin_to = input("insert a coin to exchange from: ").upper()    
         
    coin_from = input("insert a coin to exchange from: ").upper()

         

        
    




"""            
print("http request code:",r.status_code)
print("headers:",r.headers['content-type'])
print("enconding:",r.encoding)
print("estring request:",r.text)
print("json request:",r.json())#the result of this is a dictionary

"""

