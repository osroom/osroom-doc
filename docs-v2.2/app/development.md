# 本地开发运行

### &nbsp;&nbsp; 运行:

```bash

python start.py runserver

```

*参数:*

 - -h/--host 绑定ip, 默认 127.0.0.1
 
 - -p/--poer 绑定端口, 默认 5000
 
 - -D/--debug, 调试方式运行
 

> *重要: --debug 开启与不开启功能区别

```base

python start.py runserver -h 0.0.0.0 -p 5000 --debug
# 与
python start.py runserver -h 0.0.0.0 -p 5000

```
<br>


- 区别1：使用 --debug参数将 不执行 以下功能:

	1. mongodb数据库collections更新(主要用于建立新添加的collection，无新coll无需更新)
	
	2. 自动获取网页路由和API更新到 路由&API权限管理数据库（未添加新页面   或API时可以不更新，或者开发环境无需使用API权限设置可不更新）



