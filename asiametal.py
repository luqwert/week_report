#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
# @Author  : lusheng
import datetime
import requests
from selenium import webdriver
import time


#主页
url = 'http://www.asianmetal.cn/'
browser = webdriver.Chrome()
browser.get(url)
time.sleep(5)

browser.get(url)
js = "document.getElementById('txtUser_Pwd').style.display='block'"#编写JS语句
browser.execute_script(js)#执行JS
browser.find_element_by_xpath('//*[@id="txtUser_LoginName"]').send_keys('sinometal')
print(browser.find_element_by_xpath('//*[@id="txtUser_Pwd"]').is_displayed())
browser.find_element_by_xpath('//*[@id="txtUser_Pwd"]').send_keys('50808266')
browser.find_element_by_xpath('//*[@id="loginHead"]/li[1]/a').click()
time.sleep(5)

print(browser.find_element_by_xpath('//*[@id="showBut"]/input[1]'))
browser.find_element_by_xpath('//*[@id="showBut"]/input[1]').click()
time.sleep(1)
print(browser.find_element_by_xpath('//*[@id="showBut"]/input'))
browser.find_element_by_xpath('//*[@id="showBut"]/input').click()

#获取近一年价格变化图
today = datetime.datetime.now().strftime('%Y-%m-%d')
print(today)
strday = (datetime.datetime.now()-datetime.timedelta(days=365)).strftime("%Y-%m-%d")
print(strday)
strday_year = str((datetime.datetime.now()-datetime.timedelta(days=365)).strftime("%Y"))
strday_month = str((datetime.datetime.now()-datetime.timedelta(days=365)).strftime("%m"))
strday_day = str((datetime.datetime.now()-datetime.timedelta(days=365)).strftime("%d"))
today_year = str(datetime.datetime.now().strftime("%Y"))
today_month = str(datetime.datetime.now().strftime("%m"))
today_day = str(datetime.datetime.now().strftime("%d"))

selectdate = 'strYear=%s&strMonth=%s&strDay=%s&year=%s&month=%s&day=%s' % (strday_year, strday_month, strday_day, today_year, today_month, today_day)
picurl = 'http://www.asianmetal.cn/price/productPriceChart.am?isProduct=true&priceParamId=349&priceFlag=5&' + selectdate
print(picurl)
browser.get(picurl)
piclink = browser.find_element_by_xpath('//*[@id="a_349"]/img').get_attribute('src')
print(piclink)

cookies={}
for cookie in browser.get_cookies():
    cookies[cookie['name']]=cookie['value']
h = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'}

response = requests.get(piclink,headers=h,cookies=cookies)
print(response)
with open('C:\\Users\\LUS\Desktop\\锰片价格.png', 'wb') as f:
    f.write(response.content)
    f.close()

#进入锰系页面
browser.get('http://www.asianmetal.cn/product/164.html')
report_link = browser.find_element_by_xpath('//*[@id="mainContent"]/div[14]/div[2]/ul/li[1]/span[1]/a').get_attribute('href')
report_title = browser.find_element_by_xpath('//*[@id="mainContent"]/div[14]/div[2]/ul/li[1]/span[1]/a').get_attribute('title')
print(report_link,report_title)
response = requests.get(report_link,headers=h,cookies=cookies)
print(response)
f = open('C:\\Users\\LUS\Desktop\\' + report_title + '.pdf','wb')
f.write(response.content)      # r.content -> requests中的二进制响应内容：以字节的方式访问请求响应体，对于非文本请求
f.close()
browser.close()







