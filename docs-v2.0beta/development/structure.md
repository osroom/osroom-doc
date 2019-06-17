### 结构图解

![OSROOM](../imgs/dev/structure.png)

### 代码结构

### osroom/

```
.
├── apps # 应用程序主目录
├── LICENSE　# 版权说明
├── logs　# 日志目录
├── osr-tool.py　# 离线工具脚本
├── README.md
├── requirements.txt　# python需求包文件
├── start.py # 系统启动目录
├── test
└── tools　# 离线工具脚本

```

### osroom/apps/

```
.
├── admin_pages # 管理端静态文件(html,js,css...)
├── app.py # 系统初始化程序
├── configs # 系统配置文件目录
├── core　# 核心程序目录
├── init_core_module.py # 初始化核心模块脚本
├── __init__.py
├── modules　# 功能模块主目录,功能模块都在此，比如user,post,comment等
├── plugins　# 插件模块主目录(安装的插件会在此目录)
├── routing　# 路由控制模块目录
├── static   # 其他系统必须静态文件目录
├── sys_startup_info.py　# 系统启动时打印信息脚本
├── themes　# 主题主目录(安装的主题会在此目录)
├── transations　# 各语言翻译目录
└── utils　# 通用程序


```

#### &nbsp;&nbsp;osroom/apps/configs

```
.
├── config.py # 配置文件,此文件内容可以在系统管理的控制
├── db_config.py # 数据库配置文件(未上传到代码库)
├── db_config_sample.py　# 配置文件db_config.py的样例
├── __init__.py
├── mdb_collection.py
├── __pycache__
└── sys_config.py # 一些固定敏感的配置

```