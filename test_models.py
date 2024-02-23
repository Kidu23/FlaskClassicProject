from CryptoApp.models import AllCoinsApiIO, Exchange, ModelError
from config import APIKEY
import pytest

def test_allcoins():
    lists = AllCoinsApiIO()#creating an object of the class AllCoinsApiIo
    lists.getAllCoins(APIKEY)#call of the method getAllCoins
    assert lists != None#True
    quantity = len(lists.crypto_coins) + len(lists.real_coins)
    assert quantity == 18564#True

def test_exchange():
    change = Exchange("BTC")
    change.updateExchange(APIKEY)
    assert change.rate > 0 #True
    assert change.rate != None #True

def test_exchange_error():
    change = Exchange("ÑÑÑ")
    
    with pytest.raises(ModelError) as exceptionInfo:
        change.updateExchange(APIKEY)
    assert str(exceptionInfo.value) == f"status:{change.status_code}, error: You requested specific single item that we don\u0027t have at this moment."
    assert change.status_code



