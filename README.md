# wechatAI

Using Artificial Intelligence into we chat application.

itchat is an open source api for WeChat, a commonly-used Chinese social networking app.

Accessing your personal wechat account through itchat in python has never been easier.

## Installation

itchat can be installed with this little one-line command:

```python
pip install itchat
```

## Simple uses

With itchat, if you want to send a message to filehelper, this is how:

```python
import itchat

itchat.auto_login()

itchat.send('Hello, filehelper', toUserName='filehelper')
```

And you only need to write this to reply personal text messages.

```python
import itchat

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return msg.text

itchat.auto_login()
itchat.run()
```

## Have a try
- image classification wechat robot
- auto replay wechat robot
- auto translate wechat robot
