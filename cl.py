# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import re
import itchat

def wzcl(b,c):
    text = b.split(' ', 1)
    if(text[0] == 'df'):
        df = cx(text[1])
        return "房间编号：" + df[0] + "\n使用电量：" + df[1] + "\n剩余电量：" + df[2] + "\n抄表日期：" + df[3]
    if(text[0] == '@bot'):
        return 'a'
    else:
        return text

def cx(a):
    d = {'10':'48','11':'39','12':'1','13':'10','14':'18','15':'32','16':'56','17':'63','18':'70','19':'77',
         '20':'88','21':'95','22':'102','23':'109','24':'116','27':'84','28':'123','29':'149','34':'185',
         '40':'157','43':'158','45':'132','46':'133','47':'159','48':'160'}
    get = {}
    get['Apartid']=d[a[:2]]
    get['Roomname']=a
    values=urllib.parse.urlencode(get)
    url="http://dian.gdlgxy.com/RoomSelect/GetRoomInfo?"
    furl=url+values
    #url = "http://dian.gdlgxy.com/RoomSelect/GetRoomInfo?Apartid=39&Roomname=11602"
    wy = urllib.request.urlopen(furl).read()
    wy = wy.decode('UTF-8','ignore')
    pa = re.findall(r'infolab\"\>([\s\S]*?)\<\/',wy)
    sz = [pa[0].strip(),pa[1].strip(),pa[2].strip(),pa[3].strip()]
    return sz