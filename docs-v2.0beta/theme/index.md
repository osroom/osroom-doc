
### 主题结构(可参考osr-style)

#### &nbsp;&nbsp;目录结构

```

- theme-name # 为你的主题名称, 可自定义
| - pages    # 存放html页面的目录, 名称必须是pages.
  | - about-us
    | - index.html
    ...
  | - contcat
    | - index.html
    | - weixin.html
    ...

  | - login.html
  | - index.html
  ...
| - static  # 存放其他静态文件的目录, 名称必须是static.
  | - css
  | - js
  ...

| - conf.yaml　# 主题配置文件
| - init_setting.json　# 主题初始化数据文件
| - readme.md　# 主题介绍


```

#### &nbsp;&nbsp;结构解释

- theme-name主题主目录, 名称可自定义

- theme-name目录下的pages和static两个目录名称不可自定义

- pages下是自定义区, 可根据自己的需求设计路由

- static下主页用于存放css, js ,img等静态文件

#### &nbsp;&nbsp;路由

pages目录下的所有html文件的 "路由" 都和目录结构层次一样, 路由从pages下的第一级目录开始.

路由上无需带上".html"后缀. 比如需要访问theme-name/pages/contcat/weixin.html, 路由则是/contcat/weixin.

如果路由只写到目录层(未写到具体文件名), 则会响应此目录下的index.html文件.如果该目录下无index.html文件, 则响应404

比如：访问路由为/about-us和/about-us/index都会响应同一个about-us/index.html文件

#### &nbsp;&nbsp;conf.yaml 使用说明(格式)

```yaml

# 主题名必须和主题主目录一致
theme_name: Your theme's name
author: Allen Woo
theme_uri: yoursite.com
introduce: 这里是主题的简单介绍
cover_path: static/sys_imgs/cover.png
version: v0.1
license: BSD-2

```

#### &nbsp;&nbsp;init_setting.json 初始化配置文件

> 此配置文件可以用于初始化主题的设置，每个主题独立拥有一份设置

> 配置是一个json文件, 格式与参数

```

[
    {
        name: <str>
        type: <str>
        category: <str>
        title: <str>
        link: <str>
        switch: <int:0 or 1>
        code_type: <str:'html' or 'json'>
        code: <str or json>
        text: <str>
        text_html: <str>
    }
]
```

> 示范
```json

[{
    	"name": "about_us",
		"category": "文本信息",
		"type": "text",
		"link":"",
		"code_type":"html",
		"code":"",
		""
		"text": "这里展示关于我们信息",
		"title": "关于我们"
	},
	{
		"name": "contact",
		"category": "文本信息",
		"type": "text",
		"text": "Email:xxx@xxx.com",
		"title": "联系"
	},
	{
		"name": "contact",
		"category": "文本信息",
		"type": "image",
		"text": "Email:xxx@xxx.com",
		"title": "联系"
	},
	{
		"name": "photo-page-nav",
		"category": "Photo导航",
		"type": "text",
		"link": "",
		"title": "Photo页面导航",
		"code":["城市","风光"],
		"code_type":"json",
		"text_html": "导航是[多媒体>图库]中的任一[分类名称]",
		"text": "导航是[多媒体>图库]中的任一[分类名称]"
	},
	{
		"name": "display_tag",
		"category": "首页展示",
		"type": "text",
		"title": "Home页面文章Tags展示开关, 不需要展示则关闭开关",
		"switch":1,
		"link": "",
		"text": "管理端->主题展示设置->图文里添加或修改，删除"
	}
]

```

### 全局变量

#### &nbsp;&nbsp;全局变量 g

- 在html中使用osroom提供的全局变量 g 可以获取站点的一些公开设置与数据(使用方法见[模板引擎Jinjia2]("#jinjia2"))

#### &nbsp;&nbsp;全局遍历current_user

- 在html中使用osroom提供的全局变量cureent_user(提供当前用户的一些可公布信息与方法), 使用方法见[模板引擎Jinjia2]("#jinjia2")


> current_user 提供的方法有

```python

# 判断当前用户是否已验证登录
current_user.is_authenticated

# 判断当前用户是否是匿名用户(未登录用户)
current_user.is_anonymous


# 判断用户是否拥有某个权限
current_user.can()
已登录用户可用
参数：
　permissions:<int>, 权限值


# 判断当前用户是否拥有某些page路由的权限
current_user.page_permission_check()
已登录用户可用
参数：
　urls:<array>,
使用示范:
    current_user.page_permission_check(['/account', '/account/email'])


# 判断当前用户是否是网站工作人员
current_user.is_staff
已登录用户可用

# 判断当前用户是否是激活用户
current_user.is_active
已登录用户可用


# 获取当前用户的角色名称
current_user.get_role_name()
已登录用户可用

```

> current_user提供的用户信息有(获取以下信息前请判断用户是否登录)


```python
current_user.id
current_user.str_id
current_user.username
current_user.email
current_user.mphone_num
current_user.custom_domain
current_user.gender
current_user.avatar_url
current_user.role_id
current_user.active
current_user.is_delete
current_user.create_at
current_user.update_at
current_user.editor
current_user.jwt_login_time
current_user.user_info

```

#### &nbsp;&nbsp;　注意

- 以上全局变量只适合在OSROOM主题上使用, 未经过OSROOM系统的html等, 可以调用API: /api/global来获取全局数据了.

```

API: /api/global
获取当前全局数据,包括站点的公开设置, 当前登录用户的基本可公开信息.

```

### 模板引擎Jinjia2使用

- 使用模板引擎可以将数据渲染在html中

#### &nbsp;&nbsp;示范1: 获取全局变量g

```html

<!--获取site配置的LOGO路由-->
<img class="osr-logo" src="{{g.site_global.site_config.LOGO_IMG_URL}}" alt="Logo">

<!--想知道g会包含哪些数据可以将它在html页面中全部显示出来,如下-->
{{ g }}

<!--想知道网站的全局数据site_global,如下-->
{{ g.site_global }}

<!--这样也可以,如下-->
<script>

var current_lang = '{{g.site_global.language.current}}';
alert(current_lang);

</script>


```


#### &nbsp;&nbsp;示范2: 获取cureent_user


```html

<!--判断是否已登录-->

{% if current_user.is_authenticated %}
    <a>
        <img class="osr-img-circle-b" src="{{current_user.avatar_url}}" alt="User Avatar"/>
    </a>

{% else %}
    <a href="/sign-in">
        登录
    </a>

{% endif %}


<!--又比如. 选择使用网站名还是Logo-->
<a href="/">
{% if g.site_global.site_config.MB_LOGO_DISPLAY == "logo" %}

    <img src="{{g.site_global.site_config.LOGO_IMG_URL}}" alt="Logo"/>

{% else %}

    <strong>{{g.site_global.site_config.APP_NAME}}</strong>

{% endif %}
</a>

```

#### &nbsp;&nbsp;更多的Jinjia2的语法

- 了解了OSROOM提供的相关信息后就可以开发自己的主题了, 当然你要先去学习下Jinjia2使用.


[docs.jinkan.org/docs/jinja2](http://docs.jinkan.org/docs/jinja2/)


### 其他公共数据

- 最后我们要通过Api获取和提交其他数据,比如登录, 注册, 发表等, 具体有哪些Api请看Api文档


#### &nbsp;&nbsp;主题设置数据

> 这里要强调的是一个多媒体数据获取API:

```
/api/global/theme-data/display
```

- 主题的很多设置可以在Admin管理的主题展示设置中设置

- 比如图片设置页面中: 127.0.0.1/osr-admin/theme-setting/display/image

> 例子:

在管理的主题展示设置中上传3张图片, 比如名称改为home-carousel-1, home-carousel-1, home-rec1-1
那么我可以使用api 获取这两张图片信息, 展示在html页面中


``` js
var conditions = [
     {
        type:"image",
        name_regex:"home-carousel-[0-9]+",
        result_key:"home_carousel"
     },
     {
        type:"image",
        name_regex:"home-rec1-[0-9]+",
        result_key:"rec_1"
     }
];
var d ={
    conditions:JSON.stringify(conditions)

}

// js请求api
var result = $.request("GET","/api/global/theme-data/display", d);
result.then(function (r) {
    var carousel = r.data.medias.home_carousel;
    var rec_1 = r.data.medias.rec_1;
});


```


- /api/global/theme-data/display的具体使用方式可以见api文档, 以下文档不一定是最新的


```
/api/global/theme-data/display　调用说明
GET:
    1.获取主题展示用的多媒体数据
    conditions:<array:dict>, Such as:[{'type':<str>, 'names':<array>, 'name_regex':''}]
        说明:
            type-可以是"text", "image", "video", "audio"
            names-数组,指定要获取数据的name
            name_regex-字符串,获取匹配此正则的media,如果为空值，则不使用正则匹配(空置包括null, None,False, "")
            注意:name 与name_regex不能同时使用,当name_regex非空时，查询自动忽略names
        使用示例：前提在管理端多媒体中存在的内容
        如:首页轮播图片和获取”关于我们“页面的文字内容
        [
            {"type":"image", "names":["home-carousel-1", "home_carousel-2"]},
            {"type":"text", "names":["about-me"]},
            {"type":"image", "name_regex":"test-[0-9]+"}
        ]


```

### 多语言翻译

#### &nbsp;&nbsp;标记文本

> 在html中标记要翻译的文本, 示范:

- 使用{{_()}}标记

```html

<div>
{{_('这里是需要翻译的文本')}}
</div>

```

#### &nbsp;&nbsp;提取文本

> 提取文本使用osroom下的翻译提取脚本具体请看transations_tool提取

> 工具文档
```shell

# 获取提取工具帮助文档(osroom根目录下)
python tools/transations/transations_tool.py -h

```

> 步骤:每个步骤操作请看transations_tool.py -h 文档

- 1.初始化语言目录(注意: 第一次提取前使用)

- 2.update: 更新内容（提取最新的文本）

- 3.翻译.po文本, 在语言目录(初始化后会自动建立)下, 比如osroom/apps/transations/theme/en_US/LC_MESSAGES/messages.po

- 4.发布翻译

> 如果无需翻译, 就无需使用此工具

### End 后续再补充
