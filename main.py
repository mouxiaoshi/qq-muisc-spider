#! /usr/local/bin/python3.8
# -*- coding: UTF-8 -*-
from qq_music import SpiderSession, Login, QqMusicUtil

if __name__ == '__main__':
    spider_session = SpiderSession()

    login = Login(spider_session)
    # login.login()

    music_util = QqMusicUtil()
    search_music = input('请输入要搜索的歌曲:')
    response = music_util.search_music(search_music)
    list_ = music_util.get_music_list(response)
    for index, item in enumerate(list_):
        print(str(index + 1) + ':' + item['songname'] + '-' + item['singer'][0]['name'])
    choice_function = input('请选择要获取链接的歌曲编号:')
    if int(choice_function) > len(list_) or int(choice_function) < 1:
        print('请输入正确的歌曲编号')
    response = music_util.get_music_url(list_[int(choice_function) - 1]['songmid'])
    print(music_util.get_music_down_url(response))
