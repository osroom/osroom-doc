## Api文档说明


#### Admin-message-sms

**Api**:/api/admin/message/sms

**Methods**:GET, DELETE

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
GET:
        获取系统发送出去的邮件或短信记录
        status:<str>, 状态, normal, abnormal, error
        pre:<int>,每页获取几条数据,默认10
        page:<int>,第几页,默认1
    DELETE:
        删除消息(此接口只能删除由系统发出的消息user_id==0的)
        ids:<array>,消息id
    :return:
```
***

#### Admin-message-on-site

**Api**:/api/admin/message/on-site

**Methods**:GET, PUT, DELETE

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
GET:
        获取用户消息
        is_sys_msg:<int>,获取系统消息? 1表示是, 0表示否
        pre:<int>,每页获取几条数据,默认10
        page:<int>,第几页,默认1
        type:<array>,消息类型, 比如["notice", "comment", "audit"]
    DELETE:
        删除消息(此接口只能删除由系统发出的消息user_id==0的)
        ids:<array>,消息id
    :return:
```
***## Api文档说明


#### User-message

**Api**:/api/user/message

**Methods**:GET, PUT, DELETE

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
GET:
        获取用户的消息
        type:<array>,消息类型, 比如["notice", "private_letter"]
        label:<array>, 消息label, 默认全部label, 比如['comment', 'audit_failure', 'sys_notice']
        pre:<int>,每页获取几条数据,默认10
        page:<int>,第几页,默认1
        status_update:<str>,获取后的消息状态更新. 可以为: "have_read"
    PUT:
        更新消息状态
        ids:<array>,消息id
        status_update:<str>,获取后的消息状态更新. 可以为: "have_read"
    DELETE:
        删除消息
        ids:<array>,消息id
    :return:
```
***

#### Admin-message-send

**Api**:/api/admin/message/send

**Methods**:POST

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
POST
        发送消息
        title:<title>,标题
        content:<str>,正文
        content_html:<str>,正文html
        send_type:<array>,发送类型on_site, email, sms . 如:["email"], 也可以同时发送多个个["email", "on_site"]
        username:<array>, 接收信息的用户名, 如["test", "test2"]
    :return:
```
***

#### Inform-content

**Api**:/api/inform/content

**Methods**:PUT

**Permission**:unlimited

**Login auth**:

**Request and parameters:**

```
PUT:
        内容违规举报
        ctype:<str>, 内容的类型可选:post(文章), comment(评论), media(多媒体), user(用户)
        cid:<str>, 内容的id
        category:<str>, 举报内容违规类型, 可选: ad, junk_info, plagiarize, other
        details：<str>, 违规详情(选填)
```
***## Api文档说明


#### Admin-comment

**Api**:/api/admin/comment

**Methods**:GET, POST, PUT, PATCH, DELETE

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
GET:
        获取评论
        status:<str>,"is_issued"（正常发布） or "not_audit"（等待审核） or "unqualified"（未通过审核） or "user_remove"(用户删除的)
        keyword:<str>,搜索关键字
        sort:<array>,排序, 1表示升序, -1表示降序.如:
            按时间降序 [{"issue_time":-1}]
            按时间升序 [{"issue_time": 1}]
            先后按赞(like)数降序, 评论数降序,pv降序, 发布时间降序
            [{"like": -1},{"issue_time": -1}]
            默认时按时间降序, 也可以用其他字段排序
        page:<int>,第几页，默认第1页
        pre:<int>, 每页查询多少条, 默认是config.py配制文件中配制的数量
        :return:
    PATCH or PUT:
        1.人工审核comment, 带上参数score
        op:<str>, "audit"
        ids:<array>, comment id
        score:<int>, 0-10分
        2.恢复comment, 只能恢复管理员移入待删除的comment, is_delete为2的comment
        op:<str>,  "restore"
        ids:<array>, comment id
    DELETE:
        删除comment
        ids:<array>, comment id
        pending_delete:<int>, 1: is_delete为2, 标记为永久删除, 0:从数据库删除数据
        :return:
```
***## Api文档说明


#### Comment

**Api**:/api/comment

**Methods**:GET

**Permission**:unlimited

**Login auth**:

**Request and parameters:**

```
GET:
        获取文章的评论
        target_id:<str>, 目标id,比如文章post id
        target_type:<str>, 目标类型,比如文章就是"post"
        status:<str>,"is_issued"（正常发布） or "not_audit"（等待审核） or "unqualified"（未通过审核） or "user_remove"(用户删除的)
        sort:<array>,排序, 1表示升序, -1表示降序.如:
            按时间降序 [{"issue_time":-1}]
            按时间升序 [{"issue_time": 1}]
            先后按赞(like)数降序, 评论数降序,pv降序, 发布时间降序
            [{"like": -1},{"issue_time": -1}]
            默认时按时间降序, 也可以用其他字段排序
        page:<int>,第几页，默认第1页
        pre:<int>, 每页查询多少条, 默认是config.py配制文件中配制的数量
        :return:
```
***

#### Comment

**Api**:/api/comment

**Methods**:POST, PUT, PATCH, DELETE

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
POST:
        评论发布
        target_id:<str>, 目标id,比如文章post id
        target_type:<str>, 目标类型,比如文章就是"post"
        reply_id:<str>, 被回复的comment id.
        如果是回复评论中的评论,如:在评论a下面有一个评论a1，我需要回复a1, 这个时候需要提供的reply_id依然是a评论的，　而不是a1的
        reply_user_id:<str>, 被回复的comment 的用户的user id，
        如果是回复评论中的评论,如:在评论a下面有一个评论a1，我需要回复a1, 这个时候需要提供的reply_user_id是a１评论的
        reply_username:<str>, 被回复的comment 的用户的username，
        如果是回复评论中的评论,如:在评论a下面有一个评论a1，我需要回复a1, 这个时候需要提供的reply_username是a１评论的
        content:<str>, 内容(比如:富文本的html内容),将会保存到数据库中
        如果是游客评论,则需要以下两个参数(需要再后台配置中开启游客评论开关):
        username:<str>, 游客昵称
        email:<str>,游客邮箱
        :return:
    DELETE:
        评论删除
        ids:<array>, comment ids
```
***

#### Comment-like

**Api**:/api/comment/like

**Methods**:PUT

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
PUT:
        给评论点赞
        id:<str>
    :return:
```
***

#### Admin-url-permission

**Api**:/api/admin/url/permission

**Methods**:GET, POST, PUT, DELETE

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
GET:
        获取系统的web url
        type:<array>,类型, 可选api, static, page
        pre:<int>,每页获取几条数据,默认10
        page:<int>,第几页,默认1
        keyword:<str>,搜索关键字
    POST:
        添加页面路由
        url:<str>, 只用于添加页面路由
    PUT:
        更新权限
        id:<str>,id
        method:<str>
        custom_permission:<array>, 如[1, 512, 128]
        login_auth:<int>, 0 或　１, 是否需要登录验证(如果原代码路由中未指定需要登录请求, 则按照此配置)
    DELETE:
        删除手动添加的页面路由
        ids:<array>
    :return:
```
***## Api文档说明


#### Admin-permission

**Api**:/api/admin/permission

**Methods**:GET, POST, PUT, DELETE

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
GET:
        1.获取系统的权限数据详情
        pre:<int>,每页获取几条数据,默认10
        page:<int>,第几页,默认1
        keyword:<str>,搜索关键字
        is_details:<int>, 必须是1
        2.只获取系统的全部权限的value, name, explain, 以及已使用的权重位置
        不填任何参数
    POST:
        添加一个权限
        name:<str>, 名称
    　　 position:<int>, 二进制中的位置
    　　 explain:<str>,说明
        is_default:<int>, 0表示不作为默认权限, 1表示作为默认权限之一
    PUT:
        更新权限
        id:<str>,id
        name:<str>, 名称
    　　 position:<int>, 二进制中的位置
    　　 explain:<str>,说明
        is_default:<int>, 0表示不作为默认权限, 1表示作为默认权限之一
    DELETE:
        删除手动添加的页面路由
        ids:<array>
    :return:
```
***

#### Admin-audit-rule-key

**Api**:/api/admin/audit/rule/key

**Methods**:GET

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
GET:
        获取审核规则的所有key与说明, 也就config设置中的audit
        :return:
```
***

#### Admin-audit-rule

**Api**:/api/admin/audit/rule

**Methods**:GET, POST, PUT, PATCH, DELETE

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
GET:
        1. 获取所有验证规则
        project:<str>, "username", "post_category",
        keyword:<str>,不能使用的关键词,支持正则
        page:<int>, 第几页, 默认1
        pre:<int>, 每页返回pre条数据，默认10
        :return:
    POST:
        添加验证规则
        project:<str>, "username", "post_category"
        rule:<str>
        :return:
    DELETE:
        删除规则
        ids:<array>, rule ids
        :return:
```
***## Api文档说明


#### Sign-up

**Api**:/api/sign-up

**Methods**:POST

**Permission**:unlimited

**Login auth**:

**Request and parameters:**

```
POST:
        1.普通用户使用邮箱注册a
        emial:<emial>, 邮箱
        username: <str>, 用户名
        password: <str>,密码
        password2: <str>,再次确认密码
        code:<str>, 邮箱收取到的code
        2.普通用户使用手机注册a
        mobile_phone_number:<int>手机号码
        username: <str>, 用户名
        password: <str>,密码
        password2: <str>,再次确认密码
        code:<str>, 手机收取到的code
        :return:
```
***

#### Sign-in

**Api**:/api/sign-in

**Methods**:PUT

**Permission**:unlimited

**Login auth**:

**Request and parameters:**

```
PUT:
        1.普通登录
        username: <str>, 用户名或邮箱或手机号码
        password: <str>,密码
        remember_me:<bool>,是否保存密码
        next:<str>, 登录后要返回的to url, 如果为空,则返回设置中的LOGIN_TO
        use_jwt_auth:<int>, 是否使用jwt验证. 0 或 1,默认为0不使用
        当多次输入错误密码时，api会返回open_img_verif_code:true,
        表示需要图片验证码验证,客户端应该请求验证码/api/vercode/image,
         然后后再次提交登录时带下如下参数
        再次提交登录时需要以下两个参数
        code:<str>, 图片验证码中的字符
        code_url_obj:<json>,图片验证码url 对象
        :return:
        2.第三方登录
        待开发插件入口
```
***

#### Sign-in-third-party-<platform>-callback

**Api**:/api/sign-in/third-party/<platform>/callback

**Methods**:GET, PUT, POST

**Permission**:unlimited

**Login auth**:

**Request and parameters:**

```
PUT & POST & GET:
        第三方平台授权登录回调
        platform: 平台名称：可以是wechat, qq, github, sina_weibo, alipay, facebook, twitter等
                可在sys_config.py文件中配置LOGIN_PLATFORM
        :return:
```
***

#### Sign-out

**Api**:/api/sign-out

**Methods**:GET, PUT

**Permission**:unlimited

**Login auth**:

**Request and parameters:**

```
GET or PUT:
        用户登出api
        use_jwt_auth:<int>, 是否使用jwt验证. 0 或 1,默认为0不使用.
                     如果是jwt验证登录信息的客户端use_jwt_auth应为1
        :param adm:
        :return:
```
***

#### Account-email

**Api**:/api/account/email

**Methods**:PUT

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
PUT
        账户邮件修改
        email:<email>, 要绑定的新邮箱
        new_email_code:<str>, 新邮箱收取到的验证码,用于保证绑定的邮箱时用户自己的
        current_email_code:<str>, 当前邮箱收取的验证码,用于保证邮箱修改是用户自己发起
        password:<str>, 账户的登录密码
        :return:
```
***## Api文档说明


#### Account-data-availability

**Api**:/api/account/data/availability

**Methods**:GET

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
GET:
        查看用户名，email,个性域是否可以使用
        field:<str>, username or email or custom_domain
        vaule:<str>
        :return:
```
***

#### Account-self

**Api**:/api/account/self

**Methods**:GET

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
GET:
        提供一个user id, 获取是否时当前登录用户
        user_id:<str>
        :return:
```
***

#### Account-password-reset

**Api**:/api/account/password/reset

**Methods**:PUT

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
PUT:
        账户密码重设
        now_password:<str>,目前使用的密码
        password:<str>, 新密码
        password2:<str>, 再次确认新密码
        :return:
```
***

#### Account-password-retrieve

**Api**:/api/account/password/retrieve

**Methods**:PUT, POST

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
PUT:
        忘记密码,重设
        获取验证码,只需要传回参数email,return回一个{code:{'_id':'', str:'',time:'' }}
        设置新密码,需要全部参数
        email_code:<str>, 邮件中收到的验证码
        email:<str>, 邮箱
        password:<str>, 新密码
        password2:<str>, 再次确认密码
        :return:
```
***

#### Account-profile-public

**Api**:/api/account/profile/public

**Methods**:GET

**Permission**:unlimited

**Login auth**:

**Request and parameters:**

```
GET:
        获取用户公开信息
        user_id:<str>
        is_basic:<int>, 0或1,默认1. 为１时只获取最基本的用户信息
        :return:
```
***

#### Account-basic

**Api**:/api/account/basic

**Methods**:PUT

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
用户基础设置
    PUT:
        编辑用户基础设置
        username:<str>, 新的用户名
        custom_domain:<str>, 个性域名
        editor:<str>, 'rich_text' or 'markdown' 如果你有多个文本编辑器的话，可以加入这个选项
    :return:
```
***

#### Account-profile

**Api**:/api/account/profile

**Methods**:GET, PUT

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
用户资料
    GET:
        获取当前登录用户的信息
        is_basic:<int>, 0或1,默认1. 为１时只获取最基本的用户信息
    PUT
        更新用户资料
        gender:<str>, m or f or secret
        birthday:<int or str>, The format must be "YYYYMMDD" ,such as: 20170101
        address:<dict>, The format must be: {countries:'string', provinces:'string',
                                             city:'string', district:'string', detailed:'string'}
        info:<str>
    :return:
```
***## Api文档说明


#### Admin-role

**Api**:/api/admin/role

**Methods**:GET, POST, PUT, DELETE

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
GET:
        1. 获取指定ID的角色
        id:<str> ,role id
        2.分页获取全部角色
        page:<int>,第几页，默认第1页
        pre:<int>, 每页查询多少条
    POST:
        添加一个角色
        name:<str>
        instructions:<str>
        default:<int or bool>, 0 or 1
        permissions:<array>, 数组，可以给角色指定多个权重, 如[1, 2, 4, 128]
    PUT:
        修改一个角色
        id:<str>, role id
        name:<str>
        instructions:<str>
        default:<int>, 0 or 1
        permissions:<array>, 数组，可以给角色指定多个权重, 如[1, 2, 4, 128]
    DELETE:
        删除角色
        ids:<arry>, role ids
```
***

#### Account-upload-avatar

**Api**:/api/account/upload/avatar

**Methods**:PUT

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
PUT
        头像上传
        注意:虽然服务的提供图片裁剪功能，由于耗费服务器资源,非必要情况下请不要使用，请再客户端裁剪好再上传.
        为了防止恶意使用裁剪功能，可以在管理端中设置(upload)中关闭上传文件裁剪功能
        *提供2种上传方式*
        1.以常规文件格式上传
        upfile:<img file>，头像文件
        preview_w:<int>, 图片预览宽度
        tailoring:<dict>, (裁剪功能开启后才能使用),裁剪尺寸，格式:{x:12, y:12, height:100, width:100, rotate:0}
            x和ｙ为裁剪位置，x距离左边距离, y距离上边距离, width截图框的宽，　height截图框的高
        2.以base64编码上传
        imgfile_base:<str>,以base64编码上传文件
    :return:
```
***

#### Admin-user

**Api**:/api/admin/user

**Methods**:GET, PUT, DELETE

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
GET:
        1. 获取指定ID的用户基本信息
        id:<str> , user id
        2.分页获取所有用户
        status:<str>,用户状态，"normal"　or "inactive" or "cancelled"
        page:<int>,第几页，默认第1页
        pre:<int>, 每页查询多少条
        keyword:<str>, Search keywords, 搜索的时候使用
    PUT:
        1.编辑用户
        id:<str>, user id
        role_id:<str>, role id
        active:<int>, 0 or 1
        2.激活或冻结用户
        op:<str>, 为"activation"
        active:<int>, 0 or 1, 0为冻结, 1为激活
        ids:<array>
        3.恢复用户,将状态改为未删除
        op:<str>, 为"restore"
        ids:<array>
    DELETE:
        删除用户,非数据库删除
        ids:<array>
```
***

#### Admin-user-del

**Api**:/api/admin/user/del

**Methods**:DELETE

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
DELETE:
        永久删除用户,数据库中删除
        ids:<array>
        permanent:<int> 0 or 1, 0:非数据库删除,只是把状态改成"删除状态",为1:表示永久删除,
```
***## Api文档说明


#### Token-access-token

**Api**:/api/token/access-token

**Methods**:GET

**Permission**:unlimited

**Login auth**:

**Request and parameters:**

```
GET:
        客户端获取/刷新AccessToken (必须使用SecretToken验证通过)
        如果请求头中带有ClientId 则使用客户端提供的ClientId, 否则创建新的ClientId
    :return:
```
***

#### Admin-token-secret-token

**Api**:/api/admin/token/secret-token

**Methods**:GET, POST, PUT, DELETE

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
客户端访问使用的secret token管理
    GET:
        获取所有secret token
    POST:
        创建一个secret token
    PUT:
        激活或禁用一个id
        token_id:<id>,token id
        action:<str>,如果为"activate"则激活token, 为"disable"禁用token
    DELETE:
        删除一个token
        token_id:<id>,token id
    :return:
```
***## Api文档说明


#### Content-category-info

**Api**:/api/content/category/info

**Methods**:GET

**Permission**:unlimited

**Login auth**:

**Request and parameters:**

```
获取指定category id的category信息
    :return:
```
***

#### Content-category

**Api**:/api/content/category

**Methods**:GET, POST, PUT, DELETE

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
GET:
        action:<str>, 可以为get_category, get_category_type, 默认get_category
        1.获取当前用户指定的type的所有category
            action:<str>, 为get_category
            type:<str>, 你设置的那几个类别中的类别,在config.py文件中category, 可在网站管理端设置的
        2. 获取所有的type: config.py文件中category的所有CATEGORY TYPE
            action:<str>, 为get_category_type
        解释:
            在分类中(category)又分为几种类型(type)
            如: type为post有几个category
    POST:
        添加文集
        name:<str>
        type:<str>, 只能是你设置的那几个类别,在config.py文件中category, 或者网站管理设置
    PUT:
        修改文集
        id:<str>, post category id
        name:<str>
    DELETE:
        删除文集名称
        ids:<array>, post category ids
```
***

#### Admin-content-category

**Api**:/api/admin/content/category

**Methods**:GET, POST, PUT, DELETE

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
Admin管理端category管理
    GET:
        1.获取指定的type的所有分类
        type:<str>, 你设置的那几个类别中的类别,在config.py文件中category, 或者网站管理设置
        2.获取所有的type
        get_type:<int>, get_type为1
    POST:
        添加文集
        name:<str>
        type:<str>, 只能是你设置的那几个类别,在config.py文件中category, 或者网站管理设置
    PUT:
        修改文集
        id:<str>, post category id
        name:<str>
    DELETE:
        删除文集名称
        ids:<array>, post category ids
```
***## Api文档说明


#### Global

**Api**:/api/global

**Methods**:GET

**Permission**:unlimited

**Login auth**:

**Request and parameters:**

```
GET:
        获取当前全局数据,包括站点的公开设置, 当前登录用户的基本可公开信息
        :return:
```
***

#### Global-media

**Api**:/api/global/media

**Methods**:GET

**Permission**:unlimited

**Login auth**:

**Request and parameters:**

```
GET:
        1.获取指定的多媒体数据
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
        2.获取指定category的多媒体
        category_name:<array> category name, 可同时指定多个category name, 使用数组
        category_user_id:<str>, 为空则表示获取站点官方的多媒体
        category_type:<str>, 可选"text", "image", "video", "audio"
        page:<int>, 第几页, 默认1
        pre:<int>, 每页几条数据, 默认8
        3.根据id 获取
        media_id:<str>
        :return:
```
***

#### Admin-static-file

**Api**:/api/admin/static/file

**Methods**:GET, POST, PUT, DELETE

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
GET:
        1.获取静态文件内容
        file_path:<str>,静态文件所在目录
        filename:<str>,文件名
        2.获取静态文件名列表
        page:<int>, 第几页, 默认1
        pre:<int>, 第几页, 默认15
        keyword:<str>,关键词搜索用
        type:<str>, "all" or "default" or "custom"
    PUT:
        编辑静态文件内容
        file_path:<str>,静态文件所在目录
        filename:<str>,文件名
        content:<str>, 内容
```
***## Api文档说明


#### Admin-theme-page

**Api**:/api/admin/theme/page

**Methods**:GET, POST, PUT, DELETE

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
POST:
        添加页面
        routing:<str>,路由
        content:<str>, 内容
    DELETE:
        删除自己添加的页面
        file_path:<str>,页面html文件所在目录
        filename:<str>,页面html文件名
```
***

#### Admin-theme

**Api**:/api/admin/theme

**Methods**:GET, POST, PUT, DELETE

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
主题管理
    GET:
        获取当前所有主题
    POST:
        主题安装
        upfile:<file>, 上传的主题文件
    PUT:
        切换主题
        theme_name:<str>, 主题名称
    DELETE:
        删除主题
        theme_name:<str>, 主题名称
    :return:
```
***## Api文档说明


#### User-follow

**Api**:/api/user/follow

**Methods**:GET

**Permission**:unlimited

**Login auth**:

**Request and parameters:**

```
GET:
        获取用户关注的用户
        user_id:<str>, 用户ID
        action:<str>,　为followed_user
        获取当前的登录用户的粉丝
        action:<str>,　为fans
    :return:
```
***

#### User-follow

**Api**:/api/user/follow

**Methods**:POST, DELETE

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
POST:
        当前登录用户关注另一个用户用户
        ids:<array>,需关注用户的user id
    DELETE:
        当前登录用户取消关注一个用户
        ids:<array>,不再关注的用户的user id
    :return:
```
***

#### Admin-plugin-setting

**Api**:/api/admin/plugin/setting

**Methods**:GET, POST, PUT

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
插件设置
    GET:
        获取插件设置
        plugin_name:<str>, 插件名
    POST:
        刷新当前插件配置(当插件配置代码被修改后,如果未重新激活，系统保存的配置是不会更新的，所有可以使用此方法刷新)
        plugin_name:<str>, 插件名
    PUT:
        修改设置
        plugin_name:<str>, 插件名
        key:<str>,KEY
        value:<可多种类型的数据>, 值
    :return:
```
***

#### Admin-plugin-setting-install-requirement

**Api**:/api/admin/plugin/setting/install-requirement

**Methods**:PUT

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
插件需求包安装
    PUT:
        插件需求包安装
        plugin_name:<str>, 插件名
    :return:
```
***## Api文档说明


#### Admin-plugin

**Api**:/api/admin/plugin

**Methods**:GET, POST, PUT, DELETE

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
插件管理
    GET:
        获取所有插件
        page:<int>,第几页, 默认1
        pre:<int>,每页个数, 默认10
        keyword:<str>, 搜索用
    POST:
        插件安装
        upfile:<file>,上传的插件压缩包
    PUT:
        操作插件
        action:<str>, start:激活插件 stop:停用插件
        name:<str>, 插件名称
    :return:
```
***

#### Admin-upload-media-file

**Api**:/api/admin/upload/media-file

**Methods**:GET, POST, PUT, DELETE

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
GET
        1.获取多个多媒体信息
        file_type:<str>, 文件类型,可选"image", "video", "audio", "other"
        category_id:<str>, 分类id, 获取默认分类使用"default"作为category_id, 不传入此参数则表示获取全部
        keyword:<str>,搜索用
        page:<int>, 第几页, 默认1
        pre:<int>, 每页几条数据, 默认12
        sort:<array>,排序, 1表示升序, -1表示降序.如:
            按时间降序 [{"time":-1}]
            按时间升序 [{"time", 1}]
            默认时按时间降序, 也可以用其他字段排序
        2.获取1个信息
        id:<str>,id
    POST
        添加媒体
        name:<str>, 名字
        link:<str>, 链接, 用于展示的时候跳转链接
        link_name:<str>,链接名字
        link_open_new_tab:<str>,链接是否打开新标签
        title:<str>, 展示的标题
        name:<str>, 展示时需要显示的文字
        text:<str>
        text_html:<str>, text的html格式(富文本)
        type:<str>, 文件类型,可选"image", "video", "audio", "text","other"
        category_id:<str>, 分类id
        **如果需要上传文件,还需要一下参数:
        batch:<int>, 0 or 1, default:0, 为1表示批量上传.
        return_url_key: <str>, 自定义返回数据的urls的key, 默认'urls'
        return_state_key:<str>, 自定义返回数据的状态的key, 默认'state'
        return_success:<str or int>, 自定义返回数据成功的状态的值, 默认'success'
        return_error:<str or int>, 自定义返回数据错误的状态的值, 默认'error'
         **注意: 如果后台获取有文件上传，则表示只上传文件
        上传文件返回数据格式默认如下:
        {'urls':[<url>, ...,<url>],
         'state':<'success' or 'error'>,
         'msg_type':<'s' or e'>,
         'msg':''
         }
    PUT
        编辑多媒体信息
        id:<str>,要编辑的media id
        category_id:<str>,要编辑的文件的分类id, 如果不修改分类可以不提交
        name:<str>
        link:<str>, 链接
        link_name:<str>,链接名字
        link_open_new_tab:<str>,链接是否打开新标签
        title:<str>
        text:<str>
        text_html:<str>, text的html格式(富文本)
        **如果只更新文件(如图片),还需要一下参数:
        batch:<int>, 0 or 1, default:0, 为1表示批量上传.
        return_url_key: <str>, 自定义返回数据的urls的key, 默认'urls'
        return_state_key:<str>, 自定义返回数据的状态的key, 默认'state'
        return_success:<str or int>, 自定义返回数据成功的状态的值, 默认'success'
        return_error:<str or int>, 自定义返回数据错误的状态的值, 默认'error'
        **注意: 如果后台获取有文件上传，则表示只上传文件
        上传文件返回数据格式默认如下:
        {'urls':[<url>, ...,<url>],
         'state':<'success' or 'error'>,
         'msg_type':<'s' or e'>,
         'msg':''
         }
    DELETE
        删除多媒体文件
        ids:<array>,要删除的文件的id
        :return:
```
***## Api文档说明


#### Upload-file

**Api**:/api/upload/file

**Methods**:POST

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
POST
        文件上传
        api返回json数据,格式默认如下:
        {'urls':[<url>, ...,<url>],
         'state':<'success' or 'error'>,
         'msg_type':<'s' or e'>,
         'msg':''
         }
        return_url_key: <str>, 自定义返回数据的urls的key, 默认'urls'
        return_state_key:<str>, 自定义返回数据的状态的key, 默认'state'
        return_success:<str or int>, 自定义返回数据成功的状态的值, 默认'success'
        return_error:<str or int>, 自定义返回数据错误的状态的值, 默认'error'
        prefix:<str>, 默认为“generic/”, 则会将文件放入到generic目录下
        save_temporary_url：<0 or 1>,默认为1, 如果
        :return:
```
***

#### Admin-setting-sys-config-version

**Api**:/api/admin/setting/sys/config/version

**Methods**:GET, PUT

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
GET:
        获取所有的系统配置版本, 和网站服务器主机
    PUT:
        切换单个节点网站的配置版本
        switch_version:<str>, 需要切换的版本号
        diable_update:<int> , 0 or 1
        host_ip:<str>, 主机ip
    :return:
```
***

#### Admin-setting-sys-config

**Api**:/api/admin/setting/sys/config

**Methods**:GET, PUT

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
GET:
        根据project获取当前最新配置(特殊配置将不会返回,如不允许再页面编辑的,即那些不带有"__restart__"key的)
        project:<array>, 能同时获取多个project的数据.不使用此参数则表示获取全部配置
        keyword:<str>, 搜索匹配关键字的结构
        only_project_field:<int>, 只需要project字段. 0 or 1.默认为0
    PUT:
        key:<str>, 要设置的配制参数的key
        project:<str>, 项目,比如这个key是comment下的，则project为comment
        value:<str or int or bool or list or dict or tuple>, key对应的值
        info:<str>, 说明
    :return:
```
***## Api文档说明


#### Admin-setting-sys-log

**Api**:/api/admin/setting/sys/log

**Methods**:GET

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
GET:
        获取文件日志
        name:<str>,日志名称
        ip:<str>,要获取哪个主机的日志
        page:<int>
        :return:
```
***

#### Admin-setting-sys-host

**Api**:/api/admin/setting/sys/host

**Methods**:GET, POST, PUT, DELETE

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
GET:
        获取主机的信息
        ip:<str>,要获取哪个主机的日志
        :return:
    PUT:
        设置主机连接信息与重启命令
        username:<str>,主机用户名
        password:<str>,主机密码
        host_ip:<str>,要获取哪个主机的日志
        host_port:<int>,主机端口
        cmd:<str>, 命令, 注释使用#
```
***

#### Admin-setting-sys-host-cmd-execute

**Api**:/api/admin/setting/sys/host/cmd-execute

**Methods**:PUT

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
PUT:
        命令执行
        host_ip:<str>
        cmd:<str>, 要执行的Linux 命令,如果没有则自动执行主机保存的常用命令
    :return:
```
***

#### Admin-setting-sys-host-connection-test

**Api**:/api/admin/setting/sys/host/connection-test

**Methods**:PUT

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
PUT:
        服务器连接测试
        host_ip:<str>
    :return:
```
***## Api文档说明


#### Session-language-set

**Api**:/api/session/language-set

**Methods**:PUT

**Permission**:unlimited

**Login auth**:

**Request and parameters:**

```
PUT :
        修改当前语言
        language:<str>, 如en_US, zh_CN
    :return:
```
***

#### Search

**Api**:/api/search

**Methods**:GET

**Permission**:unlimited

**Login auth**:

**Request and parameters:**

```
GET:
        搜索(暂不支持全文搜索), 只能搜索文章, 用户
        keyword:<str>, Search keywords
        target:<str>, 可选"post" 或 "user". 不使用此参数则搜索所有可选目标
        page:<int>,第几页，默认第1页
        pre:<int>, 每页多少条
```
***## Api文档说明


#### Admin-post

**Api**:/api/admin/post

**Methods**:GET, POST, PUT, PATCH, DELETE

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
GET:
        1. 根据条件获取文章
        sort:<array>,排序, 1表示升序, -1表示降序.如:
            按时间降序 [{"issue_time":-1},{"update_time",-1}]
            按时间升序 [{"issue_time", 1},{"update_time",1}]
            先后按赞(like)数降序, 评论数降序,pv降序, 发布时间降序
             [{"like", -1}, {"comment_num", -1}, {"pv", -1},{"issue_time", -1}];
            默认时按时间降序, 也可以用其他字段排序
        page:<int>,第几页，默认第1页
        pre:<int>, 每页查询多少条
        status:<int> , "is_issued"（正常发布） or "draft"（草稿） or "not_audit"（等待审核） or "unqualified"（未通过审核） or "recycle"(用户的回收站) or "user_remove"
            （user_remove是指用户永久删除或被管理删除的）
        keyword:<str>, Search keywords, 搜索的时候使用
        fields:<array>, 需要返回的文章字段,如["title"]
        unwanted_fields:<array>, 不能和fields参数同时使用,不需要返回的文章字段,如["content"]
        :return:
        2.获取一篇文章
        post_id:<str>,post id
        status:<str>,状态, 可以是"is_issued" or "draft" or "not_audit" or "unqualified" or "recycle"
    PATCH or PUT:
        1.人工审核post
        op:<str>, 为"audit"
        ids:<str>, posts id
        score:<int>, 0-10分
        2.恢复post, 只能恢复管理员移入待删除的文章is_delete为3的post
        op:<str>, 为"restore"
        ids:<array>, posts id
    DELETE:
        删除post
        ids:<array>, posts id
        pending_delete:<int>, 1: 标记is_delete为3, 对于post属于的用户永久删除, 0:从数据库删除数据
        :return:
```
***

#### User-post

**Api**:/api/user/post

**Methods**:POST, PUT, PATCH, DELETE

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
POST:
        内容发布
        title:<str>, 标题
        content:<str>, 内容(比如:富文本的html内容),将会保存到数据库中
        conetent_text:<str>, 纯文本内容
        editor:<str>, 使用的编辑器类型, "markdown" or "rich_text"
        tags:<array>, 标签
        category:<str>, post category id. post分类
        cover_url:<str>,文章封面图url,默认为空
        issue_way:<str>, 可选'issue' or 'save'.　发布或者保存为草稿
    PUT or PATCH:
        1.内容修改
        id:<str>, 编辑已有的文章需要传入id, 新建文章不需要
        title:<str>, 标题
        content:<str>, 内容(比如:富文本的html内容),将会保存到数据库中
        conetent_text:<str>, 纯文本内容
        editor:<str>, 使用的编辑器类型, "markdown" or "rich_text"
        tags:<array>, 标签
        category:<str>, post category id. post分类
        issue_way:<str>, 可选'issue' or 'save'.　发布或者保存为草稿
        2.恢复回收站的post
        op:<str>, restore
        ids:<array>, posts id
    DELETE:
        删除post
        ids:<array>, posts id
        recycle:<int>,1 or 0,　1：则移入回收站, 0: 则直接标记为永久删除, 管理员才可见
```
***## Api文档说明


#### Post

**Api**:/api/post

**Methods**:GET

**Permission**:unlimited

**Login auth**:

**Request and parameters:**

```
GET:
        1.获取一篇文章
        post_id:<str>,post id
        2.根据条件获取文章
        sort:<array>,排序, 1表示升序, -1表示降序.如:
            按时间降序 [{"issue_time":-1},{"update_time":-1}]
            按时间升序 [{"issue_time": 1},{"update_time": 1}]
            先后按赞(like)数降序, 评论数降序,pv降序, 发布时间降序
            [{"like": -1}, {"comment_num": -1}, {"pv": -1},{"issue_time": -1}]
            默认时按时间降序, 也可以用其他字段排序
        status:<int> , "is_issued"（正常发布） or "draft"（草稿） or "not_audit"（等待审核） or "unqualified"（未通过审核） or "recycle"(用户的回收站) or "user_remove"
            （user_remove是指用户永久删除或被管理删除的）
        matching_rec:<str>,可选，提供一段内容, 匹配一些文章推荐
        time_range:<int>,可选,单位为天,比如最近7天的文章
        page:<int>,第几页，默认第1页
        pre:<int>, 每页查询多少条
        keyword:<str>, Search keywords, 搜索使用
        fields:<array>, 需要返回的文章字段,如["title"]
        unwanted_fields:<array>, 不能和fields参数同时使用,不需要返回的文章字段,如["user_id"]
        user_id:<str>, 如需获取指定用户的post时需要此参数
        category_id:<str>, 获取指定文集的post时需要此参数
```
***

#### Post

**Api**:/api/post

**Methods**:PUT

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
PUT:
        喜欢文章
        action:<str>, 可以是like(点赞文章)
        id:<str>, post id
```
***

#### Admin-post-access

**Api**:/api/admin/post/access

**Methods**:GET

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
GET:
        获取post数据统计
        days:<int>
```
***## Api文档说明


#### Admin-report-basic

**Api**:/api/admin/report/basic

**Methods**:GET

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
GET:
        获取网站的最基本报表数据
        project:<array>,默认全部,可以是post, comment, user, message, plugin, media, inform
```
***

#### Admin-comment-access

**Api**:/api/admin/comment/access

**Methods**:GET

**Permission**:unlimited

**Login auth**:Yes

**Request and parameters:**

```
GET:
        获取comment数据统计
        days:<int>
```
***