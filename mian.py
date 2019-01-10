#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
# @Author  : lusheng

import mysteel
import asiametal
import cnfeol
import platts


#platts指数
try:
    platts.platts()
    print('platts数据已下载完成')
except EnvironmentError as e:
    print('platts数据没有下载完成')
    print('错误信息：', e)

#mysteel
try:
    mysteel.mysteel('hnxgscb', 'xg8659291')
    print('mysteel数据已下载完成')
except EnvironmentError as e:
    print('mysteel数据没有下载完成')
    print('错误信息：', e)

#钢之家
try:
    mysteel.steelhome('xmx', 'xiemx')
    print('钢之家数据已下载完成')
except EnvironmentError as e:
    print('钢之家数据没有下载完成')
    print('错误信息：', e)

#亚洲金属网
try:
    asiametal.asiametal('sinometal', '50808266')
    print('亚洲金属网金属锰数据已下载完成')
except EnvironmentError as e:
    print('亚洲金属网数据没有下载完成')
    print('错误信息：', e)

#铁合金在线
try:
    headers2 = 'bdshare_firstime=1465884234301; ls_token=047ada6b-ce18-47ca-8ead-4ca01a9632f2; evercookie_png=047ada6b-ce18-47ca-8ead-4ca01a9632f2; evercookie_etag=047ada6b-ce18-47ca-8ead-4ca01a9632f2; evercookie_cache=047ada6b-ce18-47ca-8ead-4ca01a9632f2; cnfeol_mn=D4DF29036A2136C443B2919FB212EE01; cnfeol_smn=F6AD58D36D91CDBC5C420224F8B16EEF; ASP.NET_SessionId=r30jw255aehzn555olesvxno; Hm_lvt_7d36fb642594f3133d486f18ce21e9fd=1546481945,1546583487,1546827489,1547088554; Hm_lpvt_7d36fb642594f3133d486f18ce21e9fd=1547088554'  #没有备案过的浏览器，需要手机验证，无法手机验证，因此手动输入更新的cookis
    cnfeol.cnfeol(headers2, 'sinometal', '20091228')
    print('铁合金在线网数据已下载完成')
except EnvironmentError as e:
    print('铁合金在线数据没有下载完成')
    print('错误信息：', e)
