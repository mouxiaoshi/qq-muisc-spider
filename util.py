#! /usr/local/bin/python3.8
# -*- coding: UTF-8 -*-

import random
import execjs
import re
import json

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
    "Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/4E423F",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36 Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1500.55 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36",
    "Mozilla/5.0 (X11; NetBSD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14"
]


# 获取浏览器认证头
def get_user_agents():
    return random.choice(USER_AGENTS)


# 读取js
def load_js(name):
    f = open(name, 'r', encoding='utf-8')
    js_text = ''
    while True:
        readline = f.readline()
        if readline:
            js_text += readline
        else:
            break
    return js_text


# 读取sign.js
def get_sign_js():
    return load_js('sign.js')


# pt_js.js
def get_pt_js():
    return load_js('pt_data.js')


# others.js
def get_others_js():
    return load_js('others.js')


# 获取签名
def get_sign(requestDate):
    # 加载js
    execjs_execjs = execjs.compile(get_sign_js())
    return execjs_execjs.call('getSign', requestDate)


# 获取pt
def get_pt():
    # 加载js
    execjs_execjs = execjs.compile(get_pt_js())
    return execjs_execjs.call('getPt', None)


# 获取ptqrtoken
def get_ptqrtoken(qrsign):
    # 加载js
    execjs_execjs = execjs.compile(get_others_js())
    return execjs_execjs.call('hash33', qrsign)


# 获取g_tk
def get_g_tk(p_skey):
    # 加载js
    execjs_execjs = execjs.compile(get_others_js())
    return execjs_execjs.call('getToken', p_skey)


# 获取callback数据
def get_callback_data(call_fun):
    # 加载js
    execjs_execjs = execjs.compile(get_others_js())
    return execjs_execjs.call('getData', call_fun)


# generate golobally unique identifier
def guid():
    # 加载js
    execjs_execjs = execjs.compile(get_others_js())
    return execjs_execjs.call('guid')


# 保存图片到本地
def save_file(response, fileName):
    with open(fileName, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            f.write(chunk)


# 查找返回url中的code
def get_code(url):
    pattern = re.compile(r'[A-Za-z0-9]{16,}')  # 查找
    result = pattern.findall(url)
    return result[0]


# 转json不带空格
def dumps_without_space(data):
    return json.dumps(data, separators=(',', ':'))


# json转dict
def json_to_dict(str_data):
    return json.loads(str_data)


if __name__ == '__main__':
    # str_data = '{"code":0,"ts":1611562430406,"start_ts":1611562430393,"req_0":{"code":0,"data":{ "expiration": 80400, "login_key": "", "midurlinfo": [ { "auth_switch": 0, "common_downfromtag": 0, "ekey": "", "errtype": "", "filename": "C400003QLRda0tLCuz.m4a", "flowfromtag": "", "flowurl": "", "hisbuy": 0, "hisdown": 0, "isbuy": 0, "isonly": 0, "onecan": 0, "opi128kurl": "", "opi192koggurl": "", "opi192kurl": "", "opi30surl": "", "opi48kurl": "", "opi96kurl": "", "opiflackurl": "", "p2pfromtag": 0, "pdl": 0, "pneed": 0, "pneedbuy": 0, "premain": 0, "purl": "C400003QLRda0tLCuz.m4a?guid=8611065755&vkey=67A37A0B28144B41BCE3AE2A19C027111C8B46B99673F4C0D7B2677A3F5F18C0CE21E9C7FE0978EFCCEEBF053B217A4060BA6C972CFE8802&uin=5367&fromtag=66", "qmdlfromtag": 0, "result": 0, "songmid": "000amRvH3wxv56", "tips": "", "uiAlert": 0, "vip_downfromtag": 0, "vkey": "67A37A0B28144B41BCE3AE2A19C027111C8B46B99673F4C0D7B2677A3F5F18C0CE21E9C7FE0978EFCCEEBF053B217A4060BA6C972CFE8802", "wififromtag": "", "wifiurl": "" } ], "msg": "218.66.11.123", "retcode": 0, "servercheck": "89f397c5444ebdbff3f8cf1c6e9e17bc", "sip": [ "http:\/\/ws.stream.qqmusic.qq.com\/", "http:\/\/isure.stream.qqmusic.qq.com\/" ], "testfile2g": "C400003mAan70zUy5O.m4a?guid=8611065755&vkey=207E666363C68AF88F199BA08AAE04624612DEC9563A4DAEFE8E995A023AE2B02B032A8AFA852AF6F637F4645892A9CFECFEBB6EFED666AD&uin=&fromtag=3", "testfilewifi": "C400003mAan70zUy5O.m4a?guid=8611065755&vkey=207E666363C68AF88F199BA08AAE04624612DEC9563A4DAEFE8E995A023AE2B02B032A8AFA852AF6F637F4645892A9CFECFEBB6EFED666AD&uin=&fromtag=3", "thirdip": [ "", "" ], "uin": "", "verify_type": 0 }}}'
    # to_dict = json_to_dict(str_data)
    # print()
    # print(to_dict['req_0']['data']['sip'][0] + to_dict['req_0']['data']['midurlinfo'][0]['purl'])
    load_js('others.js')
    execjs_execjs = execjs.compile(get_others_js())
    call = execjs_execjs.call('getData',
                              'callback({"code":0,"data":{"keyword":"我们的歌","priority":0,"qc":[],"semantic":{"curnum":0,"curpage":1,"list":[],"totalnum":0},"song":{"curnum":15,"curpage":1,"list":[{"albumid":32295,"albummid":"002Zwh5p4HgecI","albumname":"改变自己","albumname_hilight":"改变自己","alertid":24,"belongCD":0,"cdIdx":5,"chinesesinger":0,"docid":"3608193620978857916","grp":[],"interval":247,"isonly":1,"lyric":"","lyric_hilight":"","media_mid":"0009QnRd4czHGM","msgid":15,"newStatus":2,"nt":2508226582,"pay":{"payalbum":0,"payalbumprice":0,"paydownload":1,"payinfo":1,"payplay":1,"paytrackmouth":1,"paytrackprice":200},"preview":{"trybegin":70827,"tryend":96435,"trysize":960887},"pubtime":1184256000,"pure":0,"singer":[{"id":265,"mid":"001JDzPT3JdvqK","name":"王力宏","name_hilight":"王力宏"}],"size128":3965376,"size320":9912683,"sizeape":0,"sizeflac":28901210,"sizeogg":6050968,"songid":102193483,"songmid":"000NqZLy2lfXjT","songname":"我们的歌","songname_hilight":"<em>我们的歌</em>","strMediaMid":"0009QnRd4czHGM","stream":1,"switch":628481,"t":1,"tag":11,"type":0,"ver":0,"vid":"q0013x75hkk"},{"albumid":16475794,"albummid":"001jMudH3aMmc1","albumname":"中国梦之声·我们的歌第二季 第12期","albumname_hilight":"中国梦之声·<em>我们的歌</em>第二季 第12期","alertid":23,"belongCD":0,"cdIdx":6,"chinesesinger":0,"docid":"4610586117815101236","grp":[],"interval":311,"isonly":1,"lyric":"","lyric_hilight":"","media_mid":"003PgofS1NIenG","msgid":16,"newStatus":1,"nt":21341824,"pay":{"payalbum":0,"payalbumprice":0,"paydownload":1,"payinfo":1,"payplay":0,"paytrackmouth":1,"paytrackprice":200},"preview":{"trybegin":59569,"tryend":145059,"trysize":960887},"pubtime":1609077960,"pure":0,"singer":[{"id":4284,"mid":"004DFS271osAwp","name":"陈小春","name_hilight":"陈小春"},{"id":1121441,"mid":"004LV0lb4fOw89","name":"GAI周延","name_hilight":"GAI周延"}],"size128":4978961,"size320":12446644,"sizeape":0,"sizeflac":41196720,"sizeogg":7256168,"songid":291397478,"songmid":"001AGqzU3a3aHj","songname":"万里长城永不倒 (Live)","songname_hilight":"万里长城永不倒 (Live)","strMediaMid":"003PgofS1NIenG","stream":1,"switch":636675,"t":1,"tag":10,"type":0,"ver":3,"vid":"j0035gwpj55"},{"albumid":16185176,"albummid":"000Gc7Hx0NOVh3","albumname":"中国梦之声·我们的歌第二季 第10期","albumname_hilight":"中国梦之声·<em>我们的歌</em>第二季 第10期","alertid":23,"belongCD":0,"cdIdx":4,"chinesesinger":0,"docid":"3050303729339594969","grp":[],"interval":292,"isonly":1,"lyric":"","lyric_hilight":"","media_mid":"0023bMd31rT6FH","msgid":16,"newStatus":1,"nt":511727550,"pay":{"payalbum":0,"payalbumprice":0,"paydownload":1,"payinfo":1,"payplay":0,"paytrackmouth":1,"paytrackprice":200},"preview":{"trybegin":71793,"tryend":115596,"trysize":960887},"pubtime":1607869112,"pure":1,"singer":[{"id":235,"mid":"003nS2v740Lxcw","name":"李克勤","name_hilight":"李克勤"},{"id":199509,"mid":"003fA5G40k6hKc","name":"周深","name_hilight":"周深"}],"size128":4682644,"size320":11705873,"sizeape":0,"sizeflac":36171665,"sizeogg":6336943,"songid":289711616,"songmid":"0023bMd31rT6FH","songname":"爱情转移 (Live)","songname_hilight":"爱情转移 (Live)","strMediaMid":"0023bMd31rT6FH","stream":1,"switch":636675,"t":1,"tag":12,"type":0,"ver":3,"vid":"l0035j083ug"},{"albumid":15927057,"albummid":"002IyYs84DHdOp","albumname":"中国梦之声·我们的歌第二季 第9期","albumname_hilight":"中国梦之声·<em>我们的歌</em>第二季 第9期","alertid":23,"belongCD":0,"cdIdx":5,"chinesesinger":0,"docid":"3317306288335256412","grp":[],"interval":300,"isonly":1,"lyric":"","lyric_hilight":"","media_mid":"002uzsf10XD0Ch","msgid":16,"newStatus":1,"nt":856328625,"pay":{"payalbum":0,"payalbumprice":0,"paydownload":1,"payinfo":1,"payplay":0,"paytrackmouth":1,"paytrackprice":200},"preview":{"trybegin":0,"tryend":0,"trysize":0},"pubtime":1607263837,"pure":0,"singer":[{"id":14197,"mid":"002kJDgu1KMVQP","name":"常石磊","name_hilight":"常石磊"},{"id":161301,"mid":"000IBYF50SRnXP","name":"王源","name_hilight":"王源"}],"size128":4807190,"size320":12017613,"sizeape":0,"sizeflac":37414739,"sizeogg":6510961,"songid":288082570,"songmid":"002uzsf10XD0Ch","songname":"逆光 (Live)","songname_hilight":"逆光 (Live)","strMediaMid":"002uzsf10XD0Ch","stream":1,"switch":17413891,"t":1,"tag":12,"type":0,"ver":3,"vid":"a0035e8sb1c"},{"albumid":16185176,"albummid":"000Gc7Hx0NOVh3","albumname":"中国梦之声·我们的歌第二季 第10期","albumname_hilight":"中国梦之声·<em>我们的歌</em>第二季 第10期","alertid":23,"belongCD":0,"cdIdx":5,"chinesesinger":0,"docid":"3749580517421738170","grp":[],"interval":290,"isonly":1,"lyric":"","lyric_hilight":"","media_mid":"0012T2HR2Cznzn","msgid":16,"newStatus":1,"nt":3306940018,"pay":{"payalbum":0,"payalbumprice":0,"paydownload":1,"payinfo":1,"payplay":0,"paytrackmouth":1,"paytrackprice":200},"preview":{"trybegin":63678,"tryend":206956,"trysize":960887},"pubtime":1607869880,"pure":0,"singer":[{"id":167,"mid":"0000mFvh1jtLcz","name":"张信哲","name_hilight":"张信哲"},{"id":1726831,"mid":"003x3ppP1EIkaN","name":"太一","name_hilight":"太一"}],"size128":4647118,"size320":11617123,"sizeape":0,"sizeflac":36367106,"sizeogg":6441544,"songid":289711620,"songmid":"0012T2HR2Cznzn","songname":"口是心非 (Live)","songname_hilight":"口是心非 (Live)","strMediaMid":"0012T2HR2Cznzn","stream":1,"switch":636675,"t":1,"tag":12,"type":0,"ver":3,"vid":"g00357ek7a4"},{"albumid":15691214,"albummid":"003D7OSN32RQev","albumname":"中国梦之声·我们的歌第二季 第7期","albumname_hilight":"中国梦之声·<em>我们的歌</em>第二季 第7期","alertid":23,"belongCD":0,"cdIdx":5,"chinesesinger":0,"docid":"13156823387344280148","grp":[],"interval":349,"isonly":1,"lyric":"","lyric_hilight":"","media_mid":"000zF70n0nDFeE","msgid":16,"newStatus":1,"nt":201872326,"pay":{"payalbum":0,"payalbumprice":0,"paydownload":1,"payinfo":1,"payplay":0,"paytrackmouth":1,"paytrackprice":200},"preview":{"trybegin":0,"tryend":0,"trysize":960887},"pubtime":1606055731,"pure":1,"singer":[{"id":4284,"mid":"004DFS271osAwp","name":"陈小春","name_hilight":"陈小春"},{"id":14197,"mid":"002kJDgu1KMVQP","name":"常石磊","name_hilight":"常石磊"},{"id":1121441,"mid":"004LV0lb4fOw89","name":"GAI周延","name_hilight":"GAI周延"},{"id":161301,"mid":"000IBYF50SRnXP","name":"王源","name_hilight":"王源"}],"size128":5587502,"size320":13967979,"sizeape":0,"sizeflac":41829375,"sizeogg":7657034,"songid":285433777,"songmid":"000zF70n0nDFeE","songname":"乱世巨星 (Live)","songname_hilight":"乱世巨星 (Live)","strMediaMid":"000zF70n0nDFeE","stream":1,"switch":17413891,"t":1,"tag":12,"type":0,"ver":3,"vid":"e0035iy0zhj"},{"albumid":9075966,"albummid":"001lTYI21MP0Di","albumname":"中国梦之声·我们的歌 第2期","albumname_hilight":"中国梦之声·<em>我们的歌</em> 第2期","alertid":24,"belongCD":0,"cdIdx":3,"chinesesinger":0,"docid":"16596013984183050217","grp":[],"interval":290,"isonly":1,"lyric":"","lyric_hilight":"","media_mid":"002Lw55p3SdaQQ","msgid":15,"newStatus":2,"nt":3178292508,"pay":{"payalbum":0,"payalbumprice":0,"paydownload":1,"payinfo":1,"payplay":1,"paytrackmouth":1,"paytrackprice":200},"preview":{"trybegin":235454,"tryend":269401,"trysize":960887},"pubtime":1572710400,"pure":1,"singer":[{"id":235,"mid":"003nS2v740Lxcw","name":"李克勤","name_hilight":"李克勤"},{"id":199509,"mid":"003fA5G40k6hKc","name":"周深","name_hilight":"周深"}],"size128":4657121,"size320":11642473,"sizeape":0,"sizeflac":30937851,"sizeogg":6128176,"songid":244261498,"songmid":"002Lw55p3SdaQQ","songname":"月半小夜曲 (Live)","songname_hilight":"月半小夜曲 (Live)","strMediaMid":"002Lw55p3SdaQQ","stream":1,"switch":628481,"t":1,"tag":12,"type":0,"ver":3,"vid":"e0032go9489"},{"albumid":15333365,"albummid":"00397Jhs10CKrJ","albumname":"中国梦之声·我们的歌第二季 第4期","albumname_hilight":"中国梦之声·<em>我们的歌</em>第二季 第4期","alertid":23,"belongCD":0,"cdIdx":2,"chinesesinger":0,"docid":"16244783382706560346","grp":[],"interval":259,"isonly":1,"lyric":"","lyric_hilight":"","media_mid":"0017U3pE4ZdzHU","msgid":16,"newStatus":1,"nt":4218340527,"pay":{"payalbum":0,"payalbumprice":0,"paydownload":1,"payinfo":1,"payplay":0,"paytrackmouth":1,"paytrackprice":200},"preview":{"trybegin":82716,"tryend":140795,"trysize":960887},"pubtime":1604237505,"pure":0,"singer":[{"id":4284,"mid":"004DFS271osAwp","name":"陈小春","name_hilight":"陈小春"},{"id":1121441,"mid":"004LV0lb4fOw89","name":"GAI周延","name_hilight":"GAI周延"}],"size128":4150990,"size320":10377119,"sizeape":0,"sizeflac":27915689,"sizeogg":5668459,"songid":282621243,"songmid":"0017U3pE4ZdzHU","songname":"没那种命 (Live)","songname_hilight":"没那种命 (Live)","strMediaMid":"0017U3pE4ZdzHU","stream":1,"switch":636675,"t":1,"tag":12,"type":0,"ver":3,"vid":"i0034j9ezjv"},{"albumid":16475794,"albummid":"001jMudH3aMmc1","albumname":"中国梦之声·我们的歌第二季 第12期","albumname_hilight":"中国梦之声·<em>我们的歌</em>第二季 第12期","alertid":23,"belongCD":0,"cdIdx":2,"chinesesinger":0,"docid":"1190147825448274492","grp":[],"interval":243,"isonly":1,"lyric":"","lyric_hilight":"","media_mid":"004Vgac33KtZtl","msgid":16,"newStatus":1,"nt":3520312885,"pay":{"payalbum":0,"payalbumprice":0,"paydownload":1,"payinfo":1,"payplay":0,"paytrackmouth":1,"paytrackprice":200},"preview":{"trybegin":0,"tryend":0,"trysize":960887},"pubtime":1609074974,"pure":1,"singer":[{"id":235,"mid":"003nS2v740Lxcw","name":"李克勤","name_hilight":"李克勤"},{"id":199509,"mid":"003fA5G40k6hKc","name":"周深","name_hilight":"周深"}],"size128":3892707,"size320":9731388,"sizeape":0,"sizeflac":33104764,"sizeogg":5740980,"songid":291397486,"songmid":"004Vgac33KtZtl","songname":"突如其来的爱情 (Live)","songname_hilight":"突如其来的爱情 (Live)","strMediaMid":"004Vgac33KtZtl","stream":1,"switch":636675,"t":1,"tag":12,"type":0,"ver":3,"vid":"y0035xmmcch"},{"albumid":16381943,"albummid":"004VOQeB1EY7oL","albumname":"中国梦之声·我们的歌第二季 第11期","albumname_hilight":"中国梦之声·<em>我们的歌</em>第二季 第11期","alertid":23,"belongCD":0,"cdIdx":3,"chinesesinger":0,"docid":"13876213832483367695","grp":[],"interval":325,"isonly":1,"lyric":"","lyric_hilight":"","media_mid":"0029cipi2tWMW5","msgid":16,"newStatus":1,"nt":2467844211,"pay":{"payalbum":0,"payalbumprice":0,"paydownload":1,"payinfo":1,"payplay":0,"paytrackmouth":1,"paytrackprice":200},"preview":{"trybegin":143530,"tryend":179074,"trysize":960887},"pubtime":1608472794,"pure":0,"singer":[{"id":4284,"mid":"004DFS271osAwp","name":"陈小春","name_hilight":"陈小春"},{"id":1121441,"mid":"004LV0lb4fOw89","name":"GAI周延","name_hilight":"GAI周延"}],"size128":5215962,"size320":13039531,"sizeape":0,"sizeflac":39493185,"sizeogg":7495322,"songid":290795362,"songmid":"0029cipi2tWMW5","songname":"神啊 救救我 (Live)","songname_hilight":"神啊 救救我 (Live)","strMediaMid":"0029cipi2tWMW5","stream":1,"switch":636675,"t":1,"tag":10,"type":0,"ver":3,"vid":"q0035l1arph"},{"albumid":16475794,"albummid":"001jMudH3aMmc1","albumname":"中国梦之声·我们的歌第二季 第12期","albumname_hilight":"中国梦之声·<em>我们的歌</em>第二季 第12期","alertid":23,"belongCD":0,"cdIdx":3,"chinesesinger":0,"docid":"3044552796404474583","grp":[],"interval":305,"isonly":1,"lyric":"","lyric_hilight":"","media_mid":"00363L8N0OcvCM","msgid":16,"newStatus":1,"nt":1782987667,"pay":{"payalbum":0,"payalbumprice":0,"paydownload":1,"payinfo":1,"payplay":0,"paytrackmouth":1,"paytrackprice":200},"preview":{"trybegin":0,"tryend":0,"trysize":960887},"pubtime":1609075909,"pure":0,"singer":[{"id":167,"mid":"0000mFvh1jtLcz","name":"张信哲","name_hilight":"张信哲"},{"id":1726831,"mid":"003x3ppP1EIkaN","name":"太一","name_hilight":"太一"}],"size128":4894964,"size320":12237044,"sizeape":0,"sizeflac":38430282,"sizeogg":6708257,"songid":291397476,"songmid":"00363L8N0OcvCM","songname":"用情 (Live)","songname_hilight":"用情 (Live)","strMediaMid":"00363L8N0OcvCM","stream":1,"switch":636675,"t":1,"tag":10,"type":0,"ver":3,"vid":"h0035xu1rij"},{"albumid":15801316,"albummid":"004X8h9B13o3dt","albumname":"中国梦之声·我们的歌第二季 第8期","albumname_hilight":"中国梦之声·<em>我们的歌</em>第二季 第8期","alertid":23,"belongCD":0,"cdIdx":5,"chinesesinger":0,"docid":"16637192108520368463","grp":[],"interval":343,"isonly":1,"lyric":"","lyric_hilight":"","media_mid":"0038nyIo0ZCwGt","msgid":16,"newStatus":1,"nt":4018757705,"pay":{"payalbum":0,"payalbumprice":0,"paydownload":1,"payinfo":1,"payplay":0,"paytrackmouth":1,"paytrackprice":200},"preview":{"trybegin":115660,"tryend":144970,"trysize":960887},"pubtime":1606660227,"pure":0,"singer":[{"id":4284,"mid":"004DFS271osAwp","name":"陈小春","name_hilight":"陈小春"},{"id":14197,"mid":"002kJDgu1KMVQP","name":"常石磊","name_hilight":"常石磊"},{"id":1121441,"mid":"004LV0lb4fOw89","name":"GAI周延","name_hilight":"GAI周延"},{"id":161301,"mid":"000IBYF50SRnXP","name":"王源","name_hilight":"王源"}],"size128":5499333,"size320":13747966,"sizeape":0,"sizeflac":40959153,"sizeogg":7477378,"songid":286704269,"songmid":"0038nyIo0ZCwGt","songname":"岁月留声 (Live)","songname_hilight":"岁月留声 (Live)","strMediaMid":"0038nyIo0ZCwGt","stream":1,"switch":17413891,"t":1,"tag":10,"type":0,"ver":3,"vid":"d0035za2ghe"},{"albumid":15077391,"albummid":"0044pR9106u4s5","albumname":"中国梦之声·我们的歌第二季 第2期","albumname_hilight":"中国梦之声·<em>我们的歌</em>第二季 第2期","alertid":23,"belongCD":0,"cdIdx":4,"chinesesinger":0,"docid":"10416415150913906831","grp":[],"interval":246,"isonly":1,"lyric":"","lyric_hilight":"","media_mid":"003NHdn50EgGhu","msgid":16,"newStatus":2,"nt":6094769,"pay":{"payalbum":0,"payalbumprice":0,"paydownload":1,"payinfo":1,"payplay":0,"paytrackmouth":1,"paytrackprice":200},"preview":{"trybegin":76084,"tryend":111464,"trysize":960887},"pubtime":1603029025,"pure":0,"singer":[{"id":167,"mid":"0000mFvh1jtLcz","name":"张信哲","name_hilight":"张信哲"},{"id":1726831,"mid":"003x3ppP1EIkaN","name":"太一","name_hilight":"太一"}],"size128":3937817,"size320":9844207,"sizeape":0,"sizeflac":29067880,"sizeogg":5464496,"songid":280494286,"songmid":"003NHdn50EgGhu","songname":"太想爱你 (Live)","songname_hilight":"太想爱你 (Live)","strMediaMid":"003NHdn50EgGhu","stream":1,"switch":636675,"t":1,"tag":12,"type":0,"ver":3,"vid":"w00346oe5k1"},{"albumid":15691214,"albummid":"003D7OSN32RQev","albumname":"中国梦之声·我们的歌第二季 第7期","albumname_hilight":"中国梦之声·<em>我们的歌</em>第二季 第7期","alertid":23,"belongCD":0,"cdIdx":1,"chinesesinger":0,"docid":"16241595254814687443","grp":[],"interval":268,"isonly":1,"lyric":"","lyric_hilight":"","media_mid":"003yd2Pk26hTRg","msgid":16,"newStatus":1,"nt":2188911409,"pay":{"payalbum":0,"payalbumprice":0,"paydownload":1,"payinfo":1,"payplay":0,"paytrackmouth":1,"paytrackprice":200},"preview":{"trybegin":72999,"tryend":106287,"trysize":960887},"pubtime":1606052399,"pure":0,"singer":[{"id":167,"mid":"0000mFvh1jtLcz","name":"张信哲","name_hilight":"张信哲"},{"id":118,"mid":"001uXFgt1kpLyI","name":"容祖儿","name_hilight":"容祖儿"},{"id":1726831,"mid":"003x3ppP1EIkaN","name":"太一","name_hilight":"太一"},{"id":1518533,"mid":"000PJRig3WnHYX","name":"硬糖少女303希林娜依·高","name_hilight":"硬糖少女303希林娜依·高"}],"size128":4302701,"size320":10755629,"sizeape":0,"sizeflac":34196949,"sizeogg":5904045,"songid":285433782,"songmid":"003yd2Pk26hTRg","songname":"难以抗拒你容颜 (Live)","songname_hilight":"难以抗拒你容颜 (Live)","strMediaMid":"003yd2Pk26hTRg","stream":1,"switch":636675,"t":1,"tag":12,"type":0,"ver":3,"vid":"n00355fvaun"},{"albumid":16475794,"albummid":"001jMudH3aMmc1","albumname":"中国梦之声·我们的歌第二季 第12期","albumname_hilight":"中国梦之声·<em>我们的歌</em>第二季 第12期","alertid":23,"belongCD":0,"cdIdx":7,"chinesesinger":0,"docid":"11380786028102219803","grp":[],"interval":266,"isonly":1,"lyric":"","lyric_hilight":"","media_mid":"001MWHZz3gqWpL","msgid":16,"newStatus":1,"nt":3841370983,"pay":{"payalbum":0,"payalbumprice":0,"paydownload":1,"payinfo":1,"payplay":0,"paytrackmouth":1,"paytrackprice":200},"preview":{"trybegin":0,"tryend":0,"trysize":960887},"pubtime":1609078490,"pure":0,"singer":[{"id":138,"mid":"0019iLuN2glWFi","name":"孙楠","name_hilight":"孙楠"},{"id":2696301,"mid":"0010ZEtk1CMl32","name":"郑云龙","name_hilight":"郑云龙"}],"size128":4270953,"size320":10676597,"sizeape":0,"sizeflac":32486093,"sizeogg":5924417,"songid":291397477,"songmid":"001MWHZz3gqWpL","songname":"你快回来 (Live)","songname_hilight":"你快回来 (Live)","strMediaMid":"001MWHZz3gqWpL","stream":1,"switch":636675,"t":1,"tag":10,"type":0,"ver":3,"vid":"h0035pc1q7y"}],"totalnum":600},"tab":0,"taglist":[],"totaltime":0,"zhida":{"chinesesinger":0,"type":0}},"message":"","notice":"","subcode":0,"time":1611565471,"tips":""})')
    print(call)
