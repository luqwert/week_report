#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
# @Author  : lusheng


import requests
from selenium import webdriver
import time
import re
import globalmap as gl
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# gl._init()
#mysteel
def mysteel(username, password):
    options = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=options)
    #登录mysteel铁矿石分站
    url = 'https://tks.mysteel.com/'
    browser.get(url)
    time.sleep(3)
    # WebDriverWait(browser, 10, 0.5,ignored_exceptions='TimeoutException').until(lambda x: x.find_element_by_xpath('//*[@id="mysteel-topBar"]/div[1]/span').is_displayed())
    browser.find_element_by_xpath('//*[@id="mysteel-topBar"]/div[1]/span').click()
    # print(sign)
    #<span class="loginBtn btn">登录</span>
    input_username = browser.find_element_by_xpath('//*[@id="mysteel-topBar"]/div[1]/div/form/div[2]/input')
    #<input class="userName" type="text" required="required" placeholder="请输入用户名">
    input_username.send_keys(username)
    input_password = browser.find_element_by_xpath('//*[@id="mysteel-topBar"]/div[1]/div/form/div[3]/input[1]')
    #<input class="pasd pasdPsd hide" type="password" required="required" placeholder="请输入密码" style="display: inline-block;">
    input_password.send_keys(password)
    signin = browser.find_element_by_class_name('loginBtnBig')
    #<div class="loginBtnBig">登录</div>
    signin.click()

    # 库存情况
    kucunlink = browser.find_element_by_xpath('/html/body/ul[1]/li[8]/p/a[3]').get_attribute('href')
    kaigonglink = browser.find_element_by_xpath('/html/body/ul[1]/li[8]/p/a[5]').get_attribute('href')
    zhoupinglink = browser.find_element_by_xpath('/html/body/ul[1]/li[9]/p/a[3]').get_attribute('href')
    print(kucunlink,kaigonglink)
    #<a href="http://list1.mysteel.com/article/p-4260-------------1.html" target="_blank">港口库存</a>
    browser.get(kucunlink)
    kucunlink2 = browser.find_element_by_xpath('//*[@id="list"]/li[1]/h3/a').get_attribute('href')
    print(kucunlink2)
    #<a href="//tks.mysteel.com/18/1228/08/D46F179FC72070F8.html" title="12月28日进口矿港口库存统计与分析" target="_blank" class="ellipsis">12月28日进口矿港口库存统计与分析</a>
    browser.get(kucunlink2)
    try:
        kucuntext = browser.find_element_by_xpath('//*[@id="text"]/p[1]').text
        gl.set_value('kucun_text', kucuntext)
        print(kucuntext)
    except:
        print('需要重新登录')
        browser.find_element_by_xpath('//*[@id="userName"]').send_keys(username)
        browser.find_element_by_xpath('//*[@id="login-dialog"]/div[1]/div[2]/input[1]').send_keys(password)
        browser.find_element_by_xpath('//*[@id="login-dialog"]/div[1]/div[4]/button').click()
        time.sleep(3)
        kucuntext = browser.find_element_by_xpath('//*[@id="text"]/p[1]').text
        gl.set_value('kucun_text', kucuntext)
        print(kucuntext)
    #高炉开工率
    browser.get(kaigonglink)
    kaigonglink2 = browser.find_element_by_xpath('//*[@id="list"]/li[1]/h3/a').get_attribute('href')
    print(kaigonglink2)
    #<a href="//tks.mysteel.com/18/1228/08/D46F179FC72070F8.html" title="12月28日进口矿港口库存统计与分析" target="_blank" class="ellipsis">12月28日进口矿港口库存统计与分析</a>
    browser.get(kaigonglink2)
    kaigongtext = browser.find_element_by_xpath('//*[@id="text"]/p').text
    gl.set_value('kaigong_text', kaigongtext)
    print(kaigongtext)

    #铁矿石周评
    browser.get(zhoupinglink)
    zhoupinglink2 = browser.find_elements_by_tag_name('a')
    for i in zhoupinglink2:
        if 'Mysteel' in i.get_attribute('title'):
            zhoupinglink2 = i.get_attribute('href')
            break
    print(zhoupinglink2)
    #获取周评文本内容
    browser.get(zhoupinglink2)
    zhoupinglist = browser.find_elements_by_xpath('//*[@id="text"]//p')
    print(len(zhoupinglist))
    zhoupingtext = ''
    for li in zhoupinglist:
        zhoupingtext = zhoupingtext + li.text
    zhoupingtext1 = re.search('(?<=引言：)(.*?)(?=一)',zhoupingtext).group() + '\n' + re.search('(?<=下周市场预判)(.*?)(?=（本文数据详询)',zhoupingtext).group()
    print(zhoupingtext1)
    # print(zhoupingtext[-3].text, zhoupingtext[-2].text)
    # zhoupingtext = zhoupingtext[-3].text + zhoupingtext[-2].text
    gl.set_value('fenxi_text',zhoupingtext1)


    #废钢
    browser.get('https://feigang.mysteel.com/')
    browser.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/h4/a[2]').click()
    report_list = browser.find_elements_by_tag_name('a')
    # print(report_list)
    report_link = ''
    for report in report_list:
        if '全国废钢市场评述' in report.get_attribute('title'):
            report_link = report.get_attribute('href')
            report_title = report.get_attribute('title')
            print(report_link, report_title)
            break
    browser.get(report_link)
    feigangtext = browser.find_element_by_xpath('//*[@id="text"]/p[1]').text
    feigangpic1_title = browser.find_element_by_xpath('//*[@id="text"]/p[2]').text
    feigangpic1 = browser.find_element_by_xpath('//*[@id="text"]/p[3]/img').get_attribute('src')
    feigangpic2_title = browser.find_element_by_xpath('//*[@id="text"]/p[4]').text
    feigangpic2 = browser.find_element_by_xpath('//*[@id="text"]/p[5]/img').get_attribute('src')
    print(feigangtext)
    print(feigangpic1_title, feigangpic1)
    print(feigangpic2_title, feigangpic2)
    gl.set_value('feigang_text', feigangtext)

    response = requests.get(feigangpic1)
    print(response)
    with open('C:\\Users\\LUS\Desktop\\周报材料\\废钢指数近一年变化.png', 'wb') as f:
        f.write(response.content)
        f.close()

    response = requests.get(feigangpic2)
    print(response)
    with open('C:\\Users\\LUS\Desktop\\周报材料\\各地废钢市场价格.png', 'wb') as f:
        f.write(response.content)
        f.close()
    f_mysteel = open('C:\\Users\\LUS\\Desktop\\周报材料\\mysteel.txt', 'w', encoding='utf-8')
    f_mysteel.write(kucuntext + '\n\n')
    f_mysteel.write(kaigongtext + '\n\n')
    f_mysteel.write(zhoupingtext + '\n\n')
    f_mysteel.write(feigangtext + '\n\n')
    f_mysteel.close()
    browser.quit()


#钢之家
def steelhome(username,password):
    options = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=options)
    browser.get('http://news2.steelhome.cn/ll/col-058/var-c13/')
    report_list = browser.find_elements_by_xpath('/html/body/center/div[7]/div[2]/form/div/div/a')
    # print(report_list)
    report_link = ''
    for report in report_list:
        if '铁矿石市场一周综述' in report.get_attribute('title'):
            report_link = report.get_attribute('href')
            report_title = report.get_attribute('title')
            print(report_link,report_title)
            break
    browser.get(report_link)
    browser.find_element_by_xpath('//*[@id="username"]').send_keys(username)
    browser.find_element_by_xpath('//*[@id="password"]').send_keys(password)
    browser.find_element_by_xpath('//*[@id="loginform"]/table/tbody/tr[4]/td[2]/input[2]').click()
    time.sleep(2)
    gangzhijiatext = browser.find_element_by_xpath('//*[@id="sth_content"]').text
    # print(gangzhijiatext)
    gangzhijiatext = re.search('海运费：(.+?)美元。',gangzhijiatext).group()
    print(gangzhijiatext)
    gl.set_value('haiyunfei_text', gangzhijiatext)

#保存获得的内容
    f_mysteel = open('C:\\Users\\LUS\\Desktop\\周报材料\\mysteel.txt', 'a+', encoding='utf-8')
    f_mysteel.write(gangzhijiatext)
    #关闭文件
    f_mysteel.close()
    browser.quit()


# mysteel('hnxgscb', 'xg8659291')
