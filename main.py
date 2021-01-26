#! /usr/local/bin/python3.8
# -*- coding: UTF-8 -*-
from qq_music import SpiderSession, Login, QqMusicUtil

if __name__ == '__main__':
    spider_session = SpiderSession()

    login = Login(spider_session)
    # login.login()

    music_util = QqMusicUtil()
    done = False
    while not done:
        search_music = input('请输入要搜索的歌曲:')
        response = music_util.search_music(search_music)
        list_ = music_util.get_music_list(response)
        for index, item in enumerate(list_):
            print(str(index + 1) + ':' + item['songname'] + '-' + item['singer'][0]['name'])
        choice_function = input('请选择要获取链接的歌曲编号:')
        if int(choice_function) > len(list_) or int(choice_function) < 1:
            print('请输入正确的歌曲编号')
        choose_music = list_[int(choice_function) - 1]
        response1 = music_util.get_music_url(choose_music['songmid'])
        url = music_util.get_music_down_url(response1)
        print(url)
        music_util.down_music(url, choose_music['songname'], choose_music['singer'][0]['name'],
                              music_util.get_music_suffix(response1))
        print('下载成功')
        choose_1 = ''
        while choose_1 != '1' and choose_1 != '0':
            choose_1 = input('继续搜索请输入1，退出输入0:')
        if int(choose_1) == 0:
            done = True
        if int(choose_1) == 1:
            done = False
