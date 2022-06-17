from django.shortcuts import render
from django.http import HttpResponse
import requests
import pyupbit as ub
import pandas as pd
import gc
import datetime

def index(request):
    gc.collect(generation=2)

    now = datetime.datetime.now().strftime('%H:%M:%S')
    open1 = ub.get_ohlcv(ticker="KRW-BTC", interval="day", count = 1)
    open2 = ub.get_ohlcv(ticker="KRW-ETH", interval="day", count = 1)
    open3 = ub.get_ohlcv(ticker="KRW-NEO", interval="day", count = 1)
    open4 = ub.get_ohlcv(ticker="KRW-MTL", interval="day", count = 1)
    open5 = ub.get_ohlcv(ticker="KRW-LTC", interval="day", count = 1)

    scal1 = ub.get_ohlcv(ticker="KRW-BTC", interval="minute30", count = 1)
    scal2 = ub.get_ohlcv(ticker="KRW-ETH", interval="minute30", count = 1)
    scal3 = ub.get_ohlcv(ticker="KRW-NEO", interval="minute30", count = 1)
    scal4 = ub.get_ohlcv(ticker="KRW-MTL", interval="minute30", count = 1)
    scal5 = ub.get_ohlcv(ticker="KRW-LTC", interval="minute30", count = 1)

    sca1 = ub.get_ohlcv(ticker="KRW-BTC", interval="minute15", count = 1)
    sca2 = ub.get_ohlcv(ticker="KRW-ETH", interval="minute15", count = 1)
    sca3 = ub.get_ohlcv(ticker="KRW-NEO", interval="minute15", count = 1)
    sca4 = ub.get_ohlcv(ticker="KRW-MTL", interval="minute15", count = 1)
    sca5 = ub.get_ohlcv(ticker="KRW-LTC", interval="minute15", count = 1)

    tickers = ub.get_tickers(fiat='KRW', verbose=True)
    coin1 = ub.get_current_price('KRW-BTC')
    coin2 = ub.get_current_price('KRW-ETH')
    coin3 = ub.get_current_price('KRW-NEO')
    coin4 = ub.get_current_price('KRW-MTL')
    coin5 = ub.get_current_price('KRW-LTC')

    p1 = (1 - coin1/pd.DataFrame(open1.open)) * (-100) 
    p2 = (1 - coin2/pd.DataFrame(open2.open)) * (-100)
    p3 = (1 - coin3/pd.DataFrame(open3.open)) * (-100)
    p4 = (1 - coin4/pd.DataFrame(open4.open)) * (-100)
    p5 = (1 - coin5/pd.DataFrame(open5.open)) * (-100)

    s1 = (1 - coin1/pd.DataFrame(scal1.open)) * (-100) 
    s2 = (1 - coin2/pd.DataFrame(scal2.open)) * (-100) 
    s3 = (1 - coin3/pd.DataFrame(scal3.open)) * (-100) 
    s4 = (1 - coin4/pd.DataFrame(scal4.open)) * (-100) 
    s5 = (1 - coin5/pd.DataFrame(scal5.open)) * (-100) 

    sc1 = (1 - coin1/pd.DataFrame(sca1.open)) * (-100) 
    sc2 = (1 - coin2/pd.DataFrame(sca2.open)) * (-100) 
    sc3 = (1 - coin3/pd.DataFrame(sca3.open)) * (-100) 
    sc4 = (1 - coin4/pd.DataFrame(sca4.open)) * (-100) 
    sc5 = (1 - coin5/pd.DataFrame(sca5.open)) * (-100) 


    context = {'name1':tickers[0]['korean_name'], 'trade_price1':round(coin1), 'close1':round(p1.iloc[0][0], 2), 'scal1':round(s1.iloc[0][0], 2), 'sca1':round(sc1.iloc[0][0], 2),
                'name2':tickers[1]['korean_name'], 'trade_price2':round(coin2), 'close2':round(p2.iloc[0][0], 2), 'scal2':round(s2.iloc[0][0], 2), 'sca2':round(sc2.iloc[0][0], 2),
                'name3':tickers[2]['korean_name'], 'trade_price3':round(coin3), 'close3':round(p3.iloc[0][0], 2), 'scal3':round(s3.iloc[0][0], 2), 'sca3':round(sc3.iloc[0][0], 2),
                'name4':tickers[3]['korean_name'], 'trade_price4':round(coin4), 'close4':round(p4.iloc[0][0], 2), 'scal4':round(s4.iloc[0][0], 2), 'sca4':round(sc4.iloc[0][0], 2),
                'name5':tickers[4]['korean_name'], 'trade_price5':round(coin5), 'close5':round(p5.iloc[0][0], 2), 'scal5':round(s5.iloc[0][0], 2), 'sca5':round(sc5.iloc[0][0], 2),
                'now':now
                }

    return render(request, 'coin_price/index.html', context)