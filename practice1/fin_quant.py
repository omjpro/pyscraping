# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 15:29:55 2021

@author: user
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime 

import QuantLib as ql
from bs4 import BeautifulSoup

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')

def GET_DATE():
    date = ql.Date().todaysDate()  # today's date
    one_day = ql.Period(1, ql.Days)
    last_bday = date - one_day
    
    us = ql.UnitedStates()
    
    while us.isBusinessDay(last_bday) == False:
        last_bday -= one_day
        
    date = datetime.date(last_bday.year(), 
                         last_bday.month(), 
                         last_bday.dayOfMonth())
    
    return date


def GET_QUOTE(eval_date):
    driver = webdriver.Chrome('C:\chromedriver', options=options)
    tenors = ['01M', '03M', '06M', '01Y', '02Y', '03Y', '05Y', '07Y', '10Y', '30Y']
    
    #create Empty lists
    maturities = []
    days = []
    prices = []
    coupons = [] 
    
    # get market information 
    
    for i, tenor in enumerate(tenors):
        driver.get('https://www.wsj.com/market-data/quotes/bond/BX/TMUBMUSD' + tenor + '?mod=md_home_overview_quote')
        html = driver.page_source #페이지의 소스코드
        soup = BeautifulSoup(html, 'html.parser')
        
        #price
        
        if i <= 3:
            data_src = soup.find("span", id="quote_val")
            price = data_src.text  #숫자 문자열 값을 숫자로 
            price = float(price[:-1]) # 맨 뒤에 붙은 단위삭제 
            
        else:
            data_src = soup.find("span", id="price_quote_val")
            price = data_src.text  #숫자 문자열 값을 숫자로 
            price = price.split() # 100, 0/32를 분리
            price1 = float(price[0]) # 앞 100을 숫자로 
            price = price[1].split('/') #0 / 32를 분리 
            price2 = float(price[0])
            price3 = float(price[1])
            price = price1 + price2 / price3 # 100 + 0/32

        #coupon
        data_src2 = soup.find_all("span", class_="data_data")      
        
        coupon = data_src2[2].text
        
        if coupon != '':
            coupon = float(coupon[:-1]) # 단위삭제
        else:
            coupon = 0.0
            
        #maturity date
        
        maturity = data_src2[3].text
        maturity = datetime.datetime.strptime(maturity, '%m/%d/%y').date()
        
        #send to list
        days.append((maturity - eval_date).days)
        prices.append(price)
        coupons.append(coupon)
        maturities.append(maturity)
        
    #create data frame
    df = pd.DataFrame([maturities, days, prices, coupons]).transpose()
    headers = ['maturities', 'days', 'prices', 'coupons']
    df.columns = headers
    df.set_index('maturities', inplace=True )
    
    return df


def TRESURY_CURVE(eval_date, rate_table):
    
    # divide quotes
    
    tbill = rate_table[0:4]
    tbond = rate_table[4:]
    
    #set evaluation date
    
    eval_date = ql.Date(eval_date.day, eval_date.month, eval_date.year)
    ql.Settings.instance().evaluationDate = eval_date
    
    
    #set market convention 
    
    calendar = ql.UnitedStates()
    convention = ql.ModifiedFollowing
    endOfMonth = False
    fixingDays = 1
    faceAmount = 100
    frequency = ql.Period(ql.semiannual)
    
    #construct Treasury Bill Helpers
    
    bill_helpers = [ql.DepositRateHelper(ql.QuoteHandle(ql.SimpleQuote(price/100.0)),
                                         ql.Period(maturity, ql.Days),
                                         fixingDays,
                                         calendar,
                                         convention,
                                         endOfMonth,
                                         dayCount)
                    for price, maturity in zip(tbill['price'], tbill['days'])
                    
    # construct tresury bond helpers
    bond_helpers = []
    for price, coupon, maturity in zip(tbind['price'], tbond['coupon'], tbond['days']):
        maturity_date = eval_date + ql.period(maturity, ql.Days)
        schedule = ql.Schedule(eval_Date,
                               maturity_date,
                               frequency,
                               calendar,
                               convention,
                               convention,
                               dateGeneration,
                               endOfMMonth)
        bond_helper = ql.FixedRateBondHelper(ql.QuoteHandle(ql.SimpleQuote(price)),
                                             fixingDays,
                                             faceAmount,
                                             schedule,
                                             [coupon/100.0],
                                             dayCounter,
                                             convention)
        bond_helpers.append(bond_helper)
        
    #bind helpers
    
    rate_helper = bill_helpers + bond_helpers
    
    #bill curve
    curve - ql.piecewiseLinearZero(eval_date,
                                   rate_helper,
                                   dayCounter)
    
    return curve
        



if __name__=="__main__":
    eval_date = GET_DATE()
    rate_table = GET_QUOTE(eval_date)
    curve = TREASURY_CURVE(eval_date, rate_table)
    
    
    
    
    
    
    
    
    
    
    
    