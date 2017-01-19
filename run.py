import itchat
import cl

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    print(msg['Text'],msg['FromUserName'])
    return cl.wzcl(msg['Text'],msg['FromUserName'])

@itchat.msg_register(itchat.content.TEXT,isGroupChat = True)
def groupchat_reply(msg):
    print(msg['Text'],msg['FromUserName'])
    print(cl.wzcl(msg['Text'], msg['FromUserName']))
    return cl.wzcl(msg['Text'],msg['FromUserName'])

@itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
def atta_reply(msg):
    return ({ 'Picture': u'图片', 'Recording': u'录音',
        'Attachment': u'附件', 'Video': u'视频', }.get(msg['Type']) +
        u'已下载到本地') # download function is: msg['Text'](msg['FileName'])

@itchat.msg_register(['Map', 'Card', 'Note', 'Sharing'])
def mm_reply(msg):
    if msg['Type'] == 'Map':
        return u'收到位置分享'
    elif msg['Type'] == 'Sharing':
        return u'收到分享' + msg['Text']
    elif msg['Type'] == 'Note':
        return u'收到：' + msg['Text']
    elif msg['Type'] == 'Card':
        return u'收到好友信息：' + msg['Text']['Alias']

@itchat.msg_register('Friends')
def add_friend(msg):
    itchat.add_friend(**msg['Text'])
    itchat.send_msg(u'功能:\n电费查询「df 宿舍号」', msg['RecommendInfo']['UserName'])

itchat.auto_login(hotReload=True)
itchat.run()