## 部署OSROOM到服务器
  部署Python Web的方式有好多中, 这里只是举例其中一种方式, 使用**Nginx** + **uwsgi**部署
  先试着在自己电脑部署下也可以

### uwsgi安装与配置
> 安装

- pip 安装uwsgi(如果有建有python虚拟环境的请先进入虚拟环境再安装)
```
pip install uwsgi

```

> 配置

- 新建一个文件uwsgi.ini (建议在osroom根目录下)，写入如下配置:
```
[uwsgi]
# 使用uwsgi示范
# uwsgi 启动时所使用的地址与端口
socket = 127.0.0.1:6001
# 指向网站目录
chdir=/home/work/project/osroom
# python 启动程序文件
wsgi-file = start.py

# python 程序内用以启动的 application 变量名
callable = app
master = true
enable-threads = true

# 启动的线程
processes = 4
vacuum = true
die-on-term = true
harakiri = 30

# 每一个工作进程都生成以后才加载应用程序
lazy = true
disable-logging = true
# 状态检测地址
stats = 127.0.0.1:9191
# pid
pidfile = /tmp/osroom_uwsgi.pid

```
其他配置项可以参考uwsgi文档

> 使用uwsgi启动网站

- 注意：启动前确认osroom的数据库是否已配置正确
- 启动命令

```
# 如果uwsgi装在python虚拟环境，要先进入虚拟环境
uwsgi /home/work/project/osroom/uwsgi.ini
```

附加-方法2：如果uwsgi安装在python虚拟环境中，又不想进入虚拟环境，可以这样启动
```
# venv_osroom是我的虚拟环境目录
/home/work/project/venv_osroom/bin/uwsgi /home/work/project/osroom/uwsgi.ini
```
- 启动成功后:
由于uwsgi.ini配置的端口是6001，所以不能通过其他端口访问网站，需要下面配置Nginx转发到6001端口

```
...

*** Operational MODE: preforking ***
*** uWSGI is running in multiple interpreter mode ***
spawned uWSGI master process (pid: 22449)
spawned uWSGI worker 1 (pid: 22450, cores: 1)
spawned uWSGI worker 2 (pid: 22451, cores: 1)
spawned uWSGI worker 3 (pid: 22452, cores: 1)
spawned uWSGI worker 4 (pid: 22453, cores: 1)

...

worker 1 buried after 1 seconds
worker 2 buried after 1 seconds
worker 3 buried after 1 seconds
worker 4 buried after 1 seconds

...
```


