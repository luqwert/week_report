#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Author  : lusheng


from selenium import webdriver
import time


url = 'http://www.cnfeol.com/'
headers = {
    'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
    'Accept-Encoding':'gzip,deflate',
    'Accept-Language': 'zh-CN,zh;q = 0.9',
    'Connection': 'keep - alive',
    'Cookie': 'bdshare_firstime=1465884234301; ls_token=047ada6b-ce18-47ca-8ead-4ca01a9632f2; evercookie_png=047ada6b-ce18-47ca-8ead-4ca01a9632f2; evercookie_etag=047ada6b-ce18-47ca-8ead-4ca01a9632f2; evercookie_cache=047ada6b-ce18-47ca-8ead-4ca01a9632f2; cnfeol_mn=D4DF29036A2136C443B2919FB212EE01; cnfeol_smn=F6AD58D36D91CDBC5C420224F8B16EEF; Hm_lvt_7d36fb642594f3133d486f18ce21e9fd=1546045906,1546481945,1546583487,1546827489; ASP.NET_SessionId=41mdf3ymnpjv3p55lk4vp045; cnfeol_mn=; cnfeol_smn=; cnfeol_mkoc=false; cnfeol_mt_2015=40AE7CC5E559216E884991B0798EFF24EE6FE5E85F21D846639F5F1F77E0AA7D74BD1109697898835575B93FB7EEF1C91CE773EE0380698565D4F12AA5E0E9B79A321C3273916310A1BB877C95303361138E1025CC1D080BCA1562E12ED01D4E64C99D8AEC332DD06A2060250A4D1ACA9A9901E0EF454EAC23E5788B65729EB924B828C631A991169DB3913329CE75EFB99949469E253D7BD7A8268E8F46482DAD86718D20FCCD0279ADD1585D5D8CF955A1E8BE4A5212EC845D89EE7AC30D99526FB66F0AE6E1F23FE823BA3B4DA770ED27B2A5C915081697C67D870D9067FC3D3CA281F577CAAAB1CAEF448B335604E5675CBAB0CD4A23BF66E5BD26CB16C07EA410FDA0BEBE7274566ECB86487058D390FFCEEA38D659C104E87E77588E42BF5A7E15F6536BD2E8E1596856D64C06529CA768592BBA29A68E7A5E5D9644090D9A514935283A98C7DE15028F00D0306041690F905EC2284860891E4D4DA78CBF68759B35D2D246AA83254B7C6B9B6957D268248E5C0117D81FE191AA23CCC1; cnfeol_mt=bC2tT9Z9wi/dBNNEng0GvySuhBY74ZKx0x+ZcgnhqsYmfrB+GGMCeSV6zOMXz6OhJz2F4hbWFkoSNfOz/8GTcb8ut1Zou7B7h4H5xnDN2XrNauw1N5H9NRpGrgSAJBZbBVAEVtPh4/ADG7knE+psX95/kZLVtKhV7KrHGTxHpOWhdT8HLFFhUb/s44zJRy1uWMJp9eQD7s53lRgX3Vy9nV2HgcgMKwn2J0OJyMohG0CZkIoeu5kOdlVl3yNY8XdGX3q6FcxddJ/Vg+5L5Lpfm229IGheukgIGDxlSmUTrwZnpXJg+zSwlBAdeW0EL22sNW8g5i+4deQ=; Hm_lpvt_7d36fb642594f3133d486f18ce21e9fd=1546827496',
    'Host':'www.cnfeol.com',
    'If-Modified-Since':'Fri, 28 Dec 2018 07:43:31 GMT',
    'If-None-Match': 'c6e3467819ed41:0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
}
headers2 = 'bdshare_firstime=1465884234301; ls_token=047ada6b-ce18-47ca-8ead-4ca01a9632f2; evercookie_png=047ada6b-ce18-47ca-8ead-4ca01a9632f2; evercookie_etag=047ada6b-ce18-47ca-8ead-4ca01a9632f2; evercookie_cache=047ada6b-ce18-47ca-8ead-4ca01a9632f2; cnfeol_mn=D4DF29036A2136C443B2919FB212EE01; cnfeol_smn=F6AD58D36D91CDBC5C420224F8B16EEF; ASP.NET_SessionId=x2btdfb3r5hpmz45a3i5viue; Hm_lvt_7d36fb642594f3133d486f18ce21e9fd=1545881694,1545983116,1546045906,1546481945; Hm_lpvt_7d36fb642594f3133d486f18ce21e9fd=1546481945; cnfeol_mn=; cnfeol_smn=; cnfeol_mkoc=false; cnfeol_mt_2015=40AE7CC5E559216E884991B0798EFF24EE6FE5E85F21D846639F5F1F77E0AA7D74BD1109697898835575B93FB7EEF1C91CE773EE0380698565D4F12AA5E0E9B76D24EA4A16A9056A33A0E501F8AD79C8E2BB738E8E69F8AB936F8524CCAC87498208FF86F735681FC291FB10ADDDF52F07A8E6E7F32D14C76B3CF5B509701FC31DC4D09E9FA2A4E879350312602A66142FBEE94C9C9D09B6B0AB045211019A1D23D80A66AE4AC345A13800CC7F51B272A620E5FDEFAC1C4F6E7E0129E4FE66DBD0712F4232365B64E704C811FE38DB0FBCA79FBEE6EBD16283ABCE58CE069A5F1AEF01ABFEB308B7D252792A28F1237E68E2932A8D4F3A7A6C728D9E9D2694672D41E8F2B3F852949F7873BEBC6B23DAABCDE1415AD790EA64A02C5BFAD90DE8BBB289ADF6A708DDE818B87D5198D927C69480BE5AEBCB0C88EDAF9F5CB9AB53D6411DD49762C5D90BC5D5A17AEF5BD2AC4F4BDC030806101000F1C979AC20D60ACDF44BF5E80D24141A1D210898708C5EBFAF49E81E26473BB08DACB6393B1A; cnfeol_mt=bC2tT9Z9wi/dBNNEng0GvySuhBY74ZKx0x+ZcgnhqsYmfrB+GGMCeSV6zOMXz6OhJz2F4hbWFkoSNfOz/8GTcb8ut1Zou7B7h4H5xnDN2XrNauw1N5H9NRpGrgSAJBZbBVAEVtPh4/ADG7knE+psX5sjGAe9CgTI+zunTKNNQ9yFqEoennPlTNIxfnu3sM5PUp63s/xd3T9xr87EP59U+0s5CNk/la7MAMECBnszHZilnFRKS3PWWFVl3yNY8XdGcy1tLzgrk5nVg+5L5Lpfm2lpCfHs9xmIK8lJ5UuiVZFnpXJg+zSwlBAdeW0EL22sNW8g5i+4deQ='

options = webdriver.ChromeOptions()
options.add_argument(headers2)
browser = webdriver.Chrome(chrome_options=options)
browser.get(url)
input_username = browser.find_element_by_id('Signin_MemberName')
input_username.send_keys('sinometal')
input_password = browser.find_element_by_id('Signin_MemberPassword')
input_password.send_keys('20091228')
signin = browser.find_element_by_id('Signin_Submit')
signin.click()
time.sleep(5)


#进入锰矿/硅锰页面
mengkuangurl = 'http://www.cnfeol.com/mengkuang/'
guimengurl = 'http://www.cnfeol.com/guimeng/'
browser.get(mengkuangurl)
reports = browser.find_element_by_id('summarytabimage')
reports.click()
time.sleep(5)
    #获取周分析报告列表
lists = browser.find_elements_by_class_name('listbig')
link = ''
# print(lists)
for list in lists:
    if '锰矿周评'in list.get_attribute('title'):
        global title
        link = list.get_attribute('href')
        title = list.get_attribute('title')
        print(link,title)
        break

#解析目标周报网页
browser.get(link)
time.sleep(3)

# try:
#     page_text = browser.find_elements_by_xpath('//*[@id="contentdetail_info_detail"]/p')
#     print(page_text)
# except:
#     print('需要重新登录')
#     browser.find_element_by_xpath('//*[@id="BoxLogin_LoginBox_Signin"]/a/img').click()
#     browser.find_element_by_xpath('//*[@id="TextBoxScreenName"]').send_keys('sinometal')
#     browser.find_element_by_xpath('//*[@id="TextBoxPassword"]').send_keys('20091228')
#     browser.find_element_by_xpath('//*[@id="ButtonLogin"]').click()
#     time.sleep(3)
#     kucuntext = browser.find_element_by_xpath('//*[@id="text"]/p[1]').text
#     print(kucuntext)

#获取需要的部分内容
page_text = browser.find_elements_by_xpath('//*[@id="contentdetail_info_detail"]/p')
table_content1 = browser.find_element_by_xpath('//*[@id="contentdetail_info_detail"]/table[1]').text
table_content2 = browser.find_element_by_xpath('//*[@id="contentdetail_info_detail"]/table[2]').text
# print(page_text)
text = title + '\n'
for paragraph in page_text:
    text = text + paragraph.text + '\n'

print(text)
print(table_content1)
print(table_content2)
#保存获得的内容
f_mengkuang = open('C:\\Users\\LUS\\Desktop\\锰矿.txt', 'w', encoding='utf-8')
f_mengkuang.write(text + '\n\n')
f_mengkuang.write(table_content1 + '\n\n')
f_mengkuang.write(table_content2)
f_mengkuang.close()

#获取硅锰分析周报
guimengurl = 'http://www.cnfeol.com/guimeng/'
browser.get(guimengurl)
reports = browser.find_element_by_id('summarytabimage')
reports.click()
time.sleep(3)
    #获取周分析报告列表
lists = browser.find_elements_by_class_name('listbig')
link = ''
# print(lists)
for list in lists:
    if '硅锰周评'in list.get_attribute('title'):
        link = list.get_attribute('href')
        title = list.get_attribute('title')
        print(link,title)
        break



#解析目标周报网页
browser.get(link)
time.sleep(5)

#获取需要的部分内容
page_text = browser.find_elements_by_xpath('//*[@id="contentdetail_info_detail"]/p')
# print(page_text)
text = title + '\n'
for paragraph in page_text:
    text = text + paragraph.text + '\n'

table_content3 = browser.find_element_by_xpath('//*[@id="contentdetail_info_detail"]/table[1]').text
print(text)
print(table_content3)

#关闭浏览器
browser.close()

#保存获得的内容
f_guimeng = open('C:\\Users\\LUS\\Desktop\\硅锰.txt', 'w', encoding='utf-8')
f_guimeng.write(text + '\n\n')
f_guimeng.write(table_content3)
#关闭文件
f_guimeng.close()