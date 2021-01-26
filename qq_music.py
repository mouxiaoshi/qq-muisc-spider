#! /usr/local/bin/python3.8
# -*- coding: UTF-8 -*-

import requests
from requests.cookies import RequestsCookieJar

import util
import random
import time
import os
import pickle

from urllib import parse
from PIL import Image


class SpiderSession:
    """session"""

    def __init__(self):
        self.cookie_path = 'cookies/'
        self.session = requests.session()
        # pt数据
        self.pt = util.get_pt()

    def get_session(self):
        return self.session

    def get_pt(self):
        return self.pt

    def get_cookies(self):
        return self.session.cookies

    def set_cookie(self, cookies):
        return self.session.cookies.update(cookies)

    def save_cookies_to_local(self, cookie_file_name):
        """
        保存Cookie到本地
        :param cookie_file_name: 存放Cookie的文件名称
        :return:
        """
        path = self.cookie_path
        filepath = path + cookie_file_name + '.cookie'
        if not (os.path.exists(path)):
            os.makedirs(path)
        with open(filepath, 'wb') as f:
            pickle.dump(self.get_cookies(), f)

    def load_cookies_from_local(self):
        """
        从本地加载Cookie
        :return:
        """
        path = self.cookie_path
        if os.path.exists(path):
            for file_name in os.listdir(path):
                if file_name.endswith('.cookie'):
                    cookie_file_name = file_name
                    filepath = path + cookie_file_name
                    load_cookie = pickle.load(open(filepath, 'rb'))
                    self.set_cookie(load_cookie)

    def get_user_id(self):
        return self.get_cookies().get('uin')


class Login:
    """二维码扫码登陆"""

    def __init__(self, spider_session=SpiderSession):
        self.spider_session = spider_session
        self.session = self.spider_session.get_session()
        self.pt = self.spider_session.get_pt()

    # 获取跳转链接
    def _get_polling_url(self, str_p):
        c = self.pt
        t = 'https://ssl.' if c['ptui']['isHttps'] else 'http://'
        t = t + 'ptlogin2.' + c['ptui']['domain'] + '/' + str_p + '?'
        t += 'appid=' + c['ptui']['appid'] + '&e=2&l=M&s=3&d=72&v=4&t=' + str(random.random())
        if c['ptui']['daid']:
            t += '&daid=' + c['ptui']['daid']
            # if s.isTim:
            # t += '&tim=1'
        if c['ptui']['pt_3rd_aid']:
            t += '&pt_3rd_aid=' + c['ptui']['pt_3rd_aid']
        return t

    # 获取ptlogin2的地址
    def ptlogin2(self):
        client_id = '100497308'
        s_url = 'https://graph.qq.com/oauth2.0/login_jump'
        s_url = 'https://xui.ptlogin2.qq.com/cgi-bin/xlogin?appid=716027609&daid=383&style=33&theme=2&login_text=%E6%8E%88%E6%9D%83%E5%B9%B6%E7%99%BB%E5%BD%95&hide_title_bar=1&hide_border=1&target=self&s_url=' + parse.quote(
            s_url, safe='')
        s_url += '&pt_3rd_aid=' + parse.quote(client_id, safe='')
        dm_host = ''
        feed_back_link = 'https://support.qq.com/products/77942?customInfo=' + parse.quote(dm_host,
                                                                                           safe='') + '.appid' + client_id
        s_url += ('&pt_feedback_link=' + parse.quote(feed_back_link, safe=''))
        return self.session.get(s_url)

    # 获取二维码登陆图片地址
    def get_qrlogin_pic(self):
        heads = {
        }
        url = self._get_polling_url('ptqrshow')
        response = self.session.get(url)
        util.save_file(response, "login_qr.png")

    def check(self):
        pt_login_sig = self.session.cookies.get('pt_login_sig')
        if pt_login_sig is None:
            pt_login_sig = self.pt['ptui']['login_sig']
        qrsig = self.session.cookies.get('qrsig')
        login_url = 'https://ssl.' if self.pt['ptui']['isHttps'] else 'http://'
        login_url += 'ptlogin2.' + self.pt['ptui']['domain'] + '/'
        t = 'ptqrlogin'
        login_url += t + '?'
        login_url += 'u1=' + parse.quote(self.pt['ptui']['s_url'], safe='')
        login_url += '&ptqrtoken=' + str(util.get_ptqrtoken(qrsig))
        login_url += '&ptredirect=' + str(self.pt['ptui']['target'])
        login_url += '&h=1&t=1&g=1&from_ui=1'
        login_url += '&ptlang=' + self.pt['ptui']['lang']
        login_url += '&action=0-0-' + str(int(time.time()))
        login_url += '&js_ver=' + self.pt['ptui']['ptui_version']
        login_url += '&js_type=1'
        login_url += '&login_sig=' + pt_login_sig
        login_url += '&pt_uistyle=' + self.pt['ptui']['style']
        login_url += '&aid=' + self.pt['ptui']['appid']
        login_url += '&daid=' + self.pt['ptui']['daid']
        login_url += '&pt_3rd_aid=' + self.pt['ptui']['pt_3rd_aid']
        resp = self.session.get(login_url)
        return resp

    def authorize(self):
        c = RequestsCookieJar()
        ui = util.guid()
        c.set('ui', ui, path='/', domain='graph.qq.co')
        self.session.cookies.update(c)

        cgi_url = 'https://graph.qq.com/oauth2.0/authorize'

        headers = {
            'User-Agent': util.get_user_agents(),
            'Referer': 'https://graph.qq.com/oauth2.0/show?which=Login&display=pc&response_type=code&client_id=100497308&redirect_uri=https%3A%2F%2Fy.qq.com%2Fportal%2Fwx_redirect.html%3Flogin_type%3D1%26surl%3Dhttps%253A%252F%252Fy.qq.com%252Fportal%252Fprofile.html%2523stat%253Dy_new.top.user_pic%2526stat%253Dy_new.top.pop.logout%26use_customer_cb%3D0&state=state&display=pc',
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        payload = {
            'response_type': 'code',
            'client_id': '100497308',
            'redirect_uri': 'https://y.qq.com/portal/wx_redirect.html?login_type=1&surl=https%3A%2F%2Fy.qq.com%2F%23&use_customer_cb=0',
            'scope': '',
            'state': 'state',
            'switch': '',
            'from_ptlogin': '1',
            'src': '1',
            'update_auth': '1',
            'openapi': '80901010',
            'g_tk': util.get_g_tk(self.session.cookies.get('p_skey')),
            'auth_time': str(int(time.time())),
            'ui': ui
        }
        urlencode = parse.urlencode(payload)
        post = self.session.post(cgi_url, headers=headers, data=urlencode)
        return post

    # 获取认证的cookie
    def get_login_cookie(self, code):
        headers = {
            'User-Agent': util.get_user_agents(),
            'Referer': 'https://y.qq.com/',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        g_tk = util.get_g_tk(self.session.cookies.get('p_skey'));
        param = {
            "comm": {
                "g_tk": g_tk,
                "platform": "yqq",
                "ct": 24,
                "cv": 0
            },
            "token": {
                "module": "QQConnectLogin.LoginServer",
                "method": "QQLogin",
                "param": {
                    "code": code
                }
            }
        }
        response = self.session.post('https://u.y.qq.com/cgi-bin/musicu.fcg', headers=headers,
                                     data=util.dumps_without_space(param))
        return response

    # 登陆
    def login(self):
        # 获取登陆二维码
        self.get_qrlogin_pic()
        print('请扫描二维码登陆')
        image_open = Image.open(os.getcwd() + '/login_qr.png')
        image_open.show()
        while (True):
            check = self.check()
            values = check.cookies.values()
            if len(values) > 0:
                # 字节转化为字符串
                s = str(check.content)
                split = s.split(',')
                # 跳转返回的url(获取响应头的cookies)
                self.session.get(split[2].replace('\'', ''))
                break
            time.sleep(3)
        # 登陆认证获取cookie
        authorize = self.authorize()
        code = util.get_code(authorize.url)
        self.get_login_cookie(code)
        self.spider_session.save_cookies_to_local(self.spider_session.get_user_id())


class QqMusicUtil(object):
    """qq music工具包"""

    def __init__(self):
        self.spider_session = SpiderSession()
        # self.spider_session = spider_session
        self.spider_session.load_cookies_from_local()
        self.session = self.spider_session.session

    # 检测是否登录
    def check_login(self):
        data = {"comm":
                    {"ct": 24, "cv": 0},
                "getFavorList": {"method": "get_favor_list",
                                 "param":
                                     {"userid": self.spider_session.get_user_id(),
                                      "fav_type": 1},
                                 "module": "music.favor_system_read"}
                }
        dumps = util.dumps_without_space(data)
        payload = {
            'sign': util.get_sign(dumps),
            'data': dumps,
        }
        response = self.session.get('https://u.y.qq.com/cgi-bin/musics.fcg', params=payload)
        return response

    # 歌曲搜索
    def search_music(self, kw):
        url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
        # 页码
        p = 1
        # 每页数量
        n = 30
        # 关键字
        w = parse.quote(kw)
        print(w)
        payload = {
            'p': p,
            'n': n,
            'w': kw
        }
        response = self.session.get(url, params=payload)
        return response

    def get_music_url(self, music_id):
        url = 'https://u.y.qq.com/cgi-bin/musics.fcg'
        data = {
            'req_0': {
                'module': 'vkey.GetVkeyServer',
                'method': 'CgiGetVkey',
                'param': {'guid': '8611065755', 'songmid': [music_id],
                          'songtype': [0], 'uin': self.spider_session.get_user_id(), 'loginflag': 1, 'platform': '20'}
            }
        }
        dumps = util.dumps_without_space(data)
        payload = {
            'sign': util.get_sign(dumps),
            'data': dumps,
        }
        print(payload)
        response = self.session.get(url, params=payload)
        return response

    # 获取歌曲列表
    def get_music_list(self, response):
        data = util.get_callback_data(response.content.decode())
        data_ = data['data']
        list_ = data_['song']['list']
        return list_

    # 获取文件后缀
    def get_music_suffix(self, response):
        json_to_dict = util.json_to_dict(response.content.decode())
        file_name = json_to_dict['req_0']['data']['midurlinfo'][0]['filename']
        suffix = file_name[file_name.rfind('.'):]
        return suffix

    # 获取下载歌曲链接
    def get_music_down_url(self, response):
        json_to_dict = util.json_to_dict(response.content.decode())
        return json_to_dict['req_0']['data']['sip'][0] + json_to_dict['req_0']['data']['midurlinfo'][0]['purl']

    # 下载音乐
    def down_music(self, url, song_name, singer, suffix):
        response = self.session.get(url)
        util.save_file(response, 'files/' + song_name + '-' + singer + suffix)
