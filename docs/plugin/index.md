### 插件开发

#### &nbsp;&nbsp;原理

osroom系统提供部分功能的hook, 供插件开发使用.
如比如osroom文件上传功能的hookname为"file_upload". 当程序执行文件上传时,
会检查是否存在hookname为"file_upload", 并且已经激活的插件. 如果存在, 且已
激活, 则调用此插件完成文件上传, 插件需要按规定返回规定格式的结果.


#### &nbsp;&nbsp;目录结构

```

- plugin_test # 为你的插件名称, 可自定义
| - main.py # 调用主程序
| - config.py # 插件配置
| - conf.yaml # 插件安装配置，比如名称之类的
| - README.md # 说明

```

#### &nbsp;&nbsp;conf.yaml

> conf.yaml示范

```

# 插件名称必须和主目录名称一致
alias_name: plugin_test
author: Allen Woo
author_uri: www.xxx.com/plugin
plugin_uri: www.xxx.com/plugin
introduce: 这里是简单介绍.
version: v0.1
license: BSD-3
hook_name: file_storage
startup_file_name: main.py
execution_func_name: main


```

#### &nbsp;&nbsp;config.py

> config.py示范

```

# 插件名称
PLUGIN_NAME = "plugin_test"

# 插件配置格式
CONFIG = {
    "TEST1":{
        "info":"我是示范配置",
        "value_type":"string",
        "value":"test",
        "reactivate":True
    },
    "TEST2":{
        "info":"我是示范配置２",
        "value_type":"password",
        "value":"123456",
        "reactivate":True
    },
    "TEST3":{
        "info":"我是示范配置3",
        "value_type":"int",
        "value":123,
        "reactivate":False
    },
｝

```

####　&nbsp;&nbsp;mian.py

> main.py示范, 包括import_plugin_config, get_plugin_config的使用

```python

# -*-coding:utf-8-*-

# 导入插件里的其他程序方法
from apps.core.plug_in.config_process import import_plugin_config, get_plugin_config
from apps.plugins.plugin_test.upfile_cloud import fun_test
from apps.plugins.plugin_test.config import CONFIG, PLUGIN_NAME

'''
osroom提供了插件设置导入函数
import_plugin_config(<plugin name>, <config:dict>)
可以用于把插件的一些设置导入到osroom系统保存, 方便调用.
比如密码之类数据.
之后可以调用get_plugin_config(<plugin name>, <str>)获取导入的dict数据中
'''

# 导入插件的设置
import_plugin_config(PLUGIN_NAME, CONFIG)

# 调用插件插件的设置
get_plugin_config(PLUGIN_NAME, "TEST1")

def main(**kwargs):

    '''
    主函数
    :param kwargs:
    :return:
    '''

    # 这里可以调用其他程序方法来完成工作...
    ...

    # 最后返回结果
    return data

```

#### &nbsp;&nbsp;实例参考

[https://github.com/osroom-plugins](https://github.com/osroom-plugins)
[https://github.com/osroom-plugins/aliyun_oss_plugin](https://github.com/osroom-plugins/aliyun_oss_plugin)


### hook

目前osroom提供以下hook

#### &nbsp;&nbsp;file_storage

```
功能: 主要用于接入第三方图床/文集储存, 如aliyun oss, 七牛云存储. 解决集群部署图片等文件保存问题.

hookname: file_storage

1.上传
插件接受参数:
    action："upload"
    localfile_path：<str> 服务器本地文件路径
    filename： <str>,要保存的文件名
    prefix：<str>,要保存的文件名前缀

返回结果格式:
{type:"<你的储存平台名>", ...其他任意需要保存的信息}
如{"type":"aliyun_oss", "bucket_name":"demo_osr"}


2. 复制文件
插件接受参数:
    action："copy_file"
    file_url_obj:<dict> 在使用插件上传时, 插件返回的结果dict
    new_filename:<str>, 新文件名

返回结果格式:
复制的副本文件的{type:"<你的储存平台名>", ...其他需要保存的信息}


3.删除文件
插件接收参数:
    action："delete"
    file_url_obj:<dict>  在使用插件上传或复制时, 插件返回的结果dict

返回的结果格式：
   bool值, 删除成功：True， 删除失败False


4.重命名
插件接收参数:
    action："rename"
    file_url_obj:<dict> 在使用插件上传或复制时, 插件返回的结果dict
    new_filename:<str>, 新名称

返回的结果格式：
    bool值, 删除成功：True， 删除失败False

5. 获取文件url
插件接收参数:
    action："get_file_url"
    file_url_obj:<dict> 在使用插件上传或复制时, 插件返回的结果dict

返回的结果格式：
    成功：return url
    失败：return None
```


#### &nbsp;&nbsp;短信发送send_msg

```

功能: 发送短信

hookname: send_msg

1.短信发送
插件接受参数:
    to_numbers：<list> 发送到哪些号码,这是一个list
    content：<str>,发送的内容

需要返回的结果格式：
    bool值, 成功：True， 失败False

```

#### &nbsp;&nbsp;send_email

功能: 邮件发送
hookname：send_email

1.邮件发送
插件接受参数:
    recipients:<list>收件人, 数组类型如:["xxxxx.xx@osroom.com"]
    send_independently:<bool> 如果为Ture,给每个收件人独立发送, 不一次性发送给多个，导致收件人邮件中可以看到此邮件发送给了多少人,
    subject：<str> 邮件标题
    html：<str> html格式邮件
    text：<str> text格式邮件
    attach : <str> 附件文件路径

需要返回的结果格式：
    bool值, 成功：True， 失败False

```

#### &nbsp;&nbsp;内容安全检测

```
功能: 用于检测内容安全, 比如鉴定文本, 图片等文件敏感信息.

1. 文本安全鉴定
hookname: content_inspection_text
插件接受参数:
    content:<str>, 需要检查的文本

需要返回的结果格式:
    dict: {"lable":"<鉴定结果的类型>", "score":<int or float>}
    score范围是1到100分，违规越可疑，分值越高. 如果无法判断是否正常或违规,那就返回
    {"suggestion”:"review",  "lable":"<鉴定结果的类型>"， score":0}

2. 图片安全鉴定
hookname: content_inspection_image

插件接受参数:
    url:<str>, 可获取的图片url

需要返回的结果格式:
    dict: {"lable":"<鉴定结果的类型>", "score":<int or float>}
    score范围是1到100分，违规越可疑，分值越高. 如果无法判断是否正常或违规,那就返回
    {"suggestion”:"review",  "lable":"<鉴定结果的类型>"， score":0}

2. 视频安全鉴定
hookname: content_inspection_video

插件接受参数:
    url:<str>, 可获取的视频url

需要返回的结果格式:
    dict: {"lable":"<鉴定结果的类型>", "score":<int or float>}
    score范围是1到100分，违规越可疑，分值越高. 如果无法判断是否正常或违规,那就返回
    {"suggestion”:"review",  "lable":"<鉴定结果的类型>"， score":0}

2. 音频安全鉴定
hookname: content_inspection_audio

插件接受参数:
    url:<str>, 可获取的音频url

需要返回的结果格式:
    dict: {"lable":"<鉴定结果的类型>", "score":<int or float>}
    score范围是1到100分，违规越可疑，分值越高. 如果无法判断是否正常或违规,那就返回
    {"suggestion”:"review",  "lable":"<鉴定结果的类型>"， score":0}

```

#### &nbsp;&nbsp;ip geo

```
功能:　根据IP获取geo(地理位置), osroom中用于鉴定用户登录地区, 识别用户登录是否异常等功能中
hookname: ip_geo

插件接受参数:
    ip: ip地址

需要返回的结果格式：
    dict
    {
        "continent":{
            "code":"<code>",
            "name":"<名称>",
            "names":"<其他语言名称>"
        },
        "country":{
            "iso_code":"<iso code>",
            "name":"<名称>",
            "names":"<其他语言名称>"
        },
        "subdivisions":{
            "iso_code":"<iso code>",
            "name":"<名称>",
            "names":"<其他语言名称>"
        },
        "coordinates":{
            "lat":"<location latitude>",
            "lon":"<location longitude>",
            "accuracy_radius":"<accuracy radius>",
            "time_zone":"<time zone>"
        },
        "post":{
            "code":"< code>"
        }
    }

```


#### &nbsp;&nbsp;第三方登录

```
功能:　通过第三方平台验证登录, 如wechat,qq
hookname: wechat_login
hookname: qq_login
hookname: github_login
hookname: sina_weibo_login
hookname: alipay_login
hookname: facebook_login
hookname: twitter_login

插件接受参数:
    request_argget_all：<obj>, 一个获取第三方平台登录验证后,回调osroom系统url时传过来的数据.

登录回调地址：
    http://youdomain/open-api/sign-in/third-party/<platform>/callback
    比如:微信登录可以这样回调:/open-api/sign-in/third-party/wechat/callback

第三方平台回调地址后, 系统会根据地址执行相关的登录插件
    如:/open-api/sign-in/third-party/wechat/callback 则执行wechat登录插件

request_argget_all使用:
    在插件中可以使用osroom传入的request_argget_all对象获取登录回调地址参数
     使用方式: request_argget.all("unionid"), 获取用户唯一标识

插件需要返回结果格式:
{
    "unionid":<用户唯一标示>  # 必须返回
    "nickname": <用户昵称>,
    "gender" :<性别>,        # 只能是 "secret", "m", "f"中的一个，分别代表保密, 男, 女
    "email" :<email>,
    "avatar_url":<头像地址>,
    "province" :<地址区>,
    "city": <地址城市>,
    "country":<地址国家>
}

```