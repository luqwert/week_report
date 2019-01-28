#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
# @Author  : lusheng

import mysteel
import asiametal
import cnfeol
import platts


# platts指数
weblist = {
    'platts': [platts.platts,'',''],
    'mysteel': [mysteel.mysteel,'hnxgscb', 'xg8659291'],
    '钢之家': [mysteel.steelhome,'xmx', 'xiemx'],
    '亚洲金属网': [asiametal.asiametal,'sinometal', '50808266'],
    '铁合金在线': [cnfeol.cnfeol,'sinometal', '20091228'],
}

for name in weblist.keys():
    try:
        username = weblist[name][1]
        password = weblist[name][2]
        weblist[name][0](username, password)
        print('%s数据已下载完成' % name)
    except EnvironmentError as e:
        print('%s数据没有下载完成' % name)
        print('错误信息：', e)
