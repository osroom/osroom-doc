### 环境要求
#### &nbsp;&nbsp;操作系统

- OSROOM支持Linux中部署, Windows未测试过
<br/><br/>
- 建议使用Ubuntu 16.04或14.04,其他Linux系统还未测试
<br/><br/>
#### &nbsp;&nbsp;Pyhotn要求
- Python 3.4以上版本, 比如Python 3.4, Python 3.5
<br/><br/><br/>
### Pyhton依赖包安装
#### &nbsp;&nbsp;创建Python虚拟环境(建议)
- 例如在在/home/work创建名为venv-osroom的虚拟环境

```
python -m venv /home/work/venv-osroom
或
python3 -m venv /home/work/venv-osroom
```
<br/><br/>

- 没有安装好python-venv请先安装, Ubuntu安装命令如下:
```
sudo apt-get install python-venv
```
<br/><br/>
#### &nbsp;&nbsp;安装依赖包

- 进入虚拟环境

```shell
    source /home/work/venv-osroom/bin/activate
    # 或
    . /home/work/venv-osroom/bin/activate
```
<br/><br/>

-进入osroom项目根目录

<br/><br/>
- 使用pip安装依赖包

```
pip install -r requirements.txt
```

<br/><br/>

#### &nbsp;&nbsp;安装需求包异常情况:

- 情况1:错误信息

 ```shell
 Command "/xxx/venv-osroom/bin/python3 -u -c "import setuptools, tokenize;

 __file__='/tmp/pip-install-erphi6km/xxx/setup.py';

 f=getattr(tokenize, 'open', open)(__file__);
 code=f.read().replace('\r\n', '\n');f.close();
 exec(compile(code, __file__, 'exec'))" install --record /tmp/pip-record-nhbhzs1a/install-record.txt
  --single-version-externally-managed --compile
  --install-headers /home/work/project/venv_osroom/include
 site/python3.5/xxxx" failed with error code 1 in /tmp/pip-install-erphi6km/xxxx/

 ```
 
 &nbsp;&nbsp;那么请尝试安装python-dev
 &nbsp;&nbsp; Ubuntu系统:

 ```shell
 # 不一定需要版本号
 sudo apt-get install python3.5-dev
 ```

  &nbsp;&nbsp; 其他使用yum安装工具的Linux发行部系统:

```shell
  # 不一定需要版本号
 sudo yum install python3.5-devel
```

<br/><br/>

- 情况2:错误信息

```shell
 Command "python setup.py egg_info" failed with error code 1 in ...

 ```

 &nbsp;&nbsp;那么请尝试安装 setuptools

 &nbsp;&nbsp; Ubuntu系统:

 ```shell

 pip install --upgrade setuptools

 ```

<br/><br/><br/>
### 配置数据库
#### &nbsp;&nbsp;安装
- 请看[Mongodb安装文档](./mongodb)与[Redis安装文档](./redis)
<br/><br/>
#### &nbsp;&nbsp;初始化配置
<br/><br/>
因为osroom源代码只把配置文件config.py 和 数据库配置文件db_config.py 的sample文件上传到git，所以请先复制修改名称
<br/>
```
 # 进入到apps/configs
 cp config_sample.py config.py
 cp db_config_sample.py db_config.py
<br/><br/>  ```
 - 编辑db_config.py, 在配置中对应位置填写好数据库用户名和密码
<br/>
```python
 DB_CONFIG = {
    "redis": {
        "password": "<Your password>",
        "host": [
            "127.0.0.1"
        ],
        "port": [
            "6379"
        ]
    },
    "mongodb": {
        "mongo_web": {
            "password": "<Your password>",
            "username": "work",
            "config": {
                "fsync": False,
                "replica_set": None
            },
            "host": [
                "127.0.0.1:27017"
            ],
            "dbname": "osr_web"
        },
        "mongo_user": {
            "password": "<Your password>",
            "username": "work",
            "config": {
                "fsync": False,
                "replica_set": None
            },
            "host": [
                "127.0.0.1:27017"
            ],
            "dbname": "osr_user"
        },
        "mongo_sys": {
            "password": "<Your password>",
            "username": "work",
            "config": {
                "fsync": False,
                "replica_set": None
            },
            "host": [
                "127.0.0.1:27017"
            ],
            "dbname": "osr_sys"
        }
    }
}
```
<br/><br/><br/>
### 初始化第一个用户

- 进入项目的Python虚拟环境
<br/><br/>
- 进入根目录运行start.py add_user
  &nbsp;&nbsp; 按如下操作和提示创建第一个用户
```
(venv_osroom) work@osroom:~/project/osroom$ python start.py add_user
 * [User] add
Input username:root
Input email:xiaopingwoo@163.com
Input password(Password at least 8 characters):
[Warning]: 密码至少8个字符！ 至少包含数字，字母，特殊字符中的任意两种

Input password(Password at least 8 characters):
 * Create root role...
Create root user role successfully
 * Create root user...
 * Create a root user role successfully
 * Create the average user role...
 * Create a generic user role successfully
The basic information is as follows
Username: root
Email: h*****irr@***.com
User role: Root
Password: #D****qw123
End

```
<br/><br/><br/>
### 访问测试
使用自带的服务测试是否能够成功运行osroom（测试用, 实际部署产品不会使用该方式启动运行）
<br/><br/>
#### &nbsp;&nbsp;启动OSROOM

- 进入osroom项目目录
<br/>
```
# 如果需要外部访问，--host 为0.0.0.0 , --port 指定已开放的端口,默认5000
python start.py runserver --host 127.0.0.1 --port 5000
```
<br/><br/>
- 打开浏览器访问 127.0.0.1:5000

