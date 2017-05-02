#coding=utf8
from __future__ import unicode_literals
import itchat, time
import re
from itchat.content import *
import requests
#import json  
from translate import Translator

#===============================================================================
# @itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
# 
# def text_reply(msg):
#     print json.dumps(msg,encoding='UTF-8',ensure_ascii=False) 
#     itchat.send('%s: %s' % (msg['Type'], msg['Text']), msg['FromUserName'])
# 
# @itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
# def download_files(msg):
#     msg['Text'](msg['FileName'])
#     return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])
# 
# @itchat.msg_register(FRIENDS)
# def add_friend(msg):
#     itchat.add_friend(**msg['Text']) # 该操作会自动将新好友的消息录入，不需要重载通讯录
#     itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])
#===============================================================================

translator= Translator(to_lang="zh")

@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    #if msg['isAt']:
    #print json.dumps(msg,encoding='UTF-8',ensure_ascii=False) 
    result = ''
    orginal_text = msg['Content'] 
    isEnglish = re.match("[a-zA-Z.,'? ]*$", orginal_text)
    print ('orginal_text' )
    print (orginal_text)
    print ('size')
    print (len(orginal_text))
    print ('is English' )
    print (isEnglish)
    if isEnglish and len(orginal_text) > 6:
        result = translation = translator.translate(orginal_text);
    if len(orginal_text)==4 and msg['isAt']: 
        r = requests.get('http://i.itpk.cn/api.php?question=@cy' + orginal_text)
        result = r.text
    print ('result' )
    print (result)
    print ('size:' )
    print (len(result))
    if len(result)>0:
        itchat.send(u'%s : %s' % (msg['ActualNickName'],result), msg['FromUserName'])
    #    itchat.send(u'@%s\u2005I received: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])

itchat.auto_login(True)
itchat.run()

