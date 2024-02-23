import requests #this imports the library requests
from config import APIKEY

coin_from = input("insert a coin to exchange from:").upper()#makes the input to be always uppercase

 
while coin_from == "" and coin_from.isalpha():
    url = f"https://rest.coinapi.io/v1/exchangerate/{coin_from}/EUR?apikey={APIKEY}"#this is the request to acces the link
    r = requests.get(url)#this is the request to acces the link

    #1st exercise
    dic = r.json()#adds the data from json to the dic variable

    #2nd exercise
    if r.status_code == 200:
        print("rate: {:.2f}€".format(dic["rate"]))#this prints the value of the key rate with two decimal
        
        break
    else:
        print("error",dic["error"])#this if the link is wrong it will give a specific error that it´s already programed in the data of json
        
    coin_from = input("insert a coin to exchange from: ").upper()


"""            
print("http request code:",r.status_code)
print("headers:",r.headers['content-type'])
print("enconding:",r.encoding)
print("estring request:",r.text)
print("json request:",r.json())#the result of this is a dictionary

"""

