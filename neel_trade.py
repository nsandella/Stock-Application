#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
import time
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators


def retrieveAPIKey(keyToken):
    key_counter = open('keys.txt', 'r')
    allKeys = key_counter.readlines()
    apiKey = allKeys[keyToken]
    key_counter.close()
    return apiKey


def getCallPosition():
    call_counter = open('keys_configurable.txt', 'r')
    call_line = call_counter.readlines()
    call_line = call_line[0].split('=')
    call_position = int(call_line[1])
    call_counter.close()
    if call_position < 30:
        call_position += 1
        call_editor = open('keys_configurable.txt', 'w')
        call_editor.write('current_call_position = ' + str(call_position))
        call_editor.close()
        return call_position
    else:
        call_position = 0
        call_editor = open('keys_configurable.txt', 'w')
        call_editor.write('current_call_position = ' + str(call_position))
        call_editor.close()
        return call_position


def quote():
    t = TimeSeries('key')
    realtimedata = t.get_quote_endpoint(symbol=stock)
    print(realtimedata)


def simp180():
    savg = TechIndicators('key')
    s = savg.get_sma(symbol = stock, interval = '1min', time_period=180, series_type='close') 
    print(s)

 
def ex9day():
    eavg = TechIndicators('key')
    e = eavg.get_ema(symbol = stock, interval = '1min', time_period=9, series_type = 'close') 
    print(e)


def vwap():
    vwap = TechIndicators('key')
    v = vwap.get_vwap(symbol = stock, interval='1min') 
    print(v)

def MACD():
    macd = TechIndicators('key')
    d = macd.get_macd(symbol = stock, fastperiod = 12, slowperiod = 26, signalperiod = 9)
    print(d)

def rsi():
    rsi = TechIndicators('key')
    r = rsi.get_rsi(symbol = stock, interval = '1min', time_period = 16, series_types = 'close')
    print(r)
    
def rsi():
    rsi = TechIndicators('key')
    r = rsi.get_rsi(symbol = stock, interval = '1min', time_period = 16, series_types = 'close')
    print(r)
   

starttime = time.time()
while True:
    callPosition = getCallPosition()
    if callPosition < 6:
        key = retrieveAPIKey(0)
        print('key1' + ': ' + key)
    elif callPosition > 5 and callPosition < 11:
        key = retrieveAPIKey(1)
        print('key2' + ': ' + key)
    elif callPosition > 10 and callPosition < 16:
        key = retrieveAPIKey(2)
        print('key3' + ': ' + key)
    elif callPosition > 15 and callPosition < 21:
        key = retrieveAPIKey(3)
        print('key4' + ': ' + key)
    elif callPosition > 20 and callPosition < 26:
        key = retrieveAPIKey(4)
        print('key5' + ': ' + key)
    elif callPosition > 25 and callPosition < 31:
        key = retrieveAPIKey(5)
        print('key6' + ': ' + key)
    
    stock = 'aapl'
    quote()
    print('tick')
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))
    