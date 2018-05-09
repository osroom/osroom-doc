## OSROOM部署
> 创建Python虚拟环境(建议)

- 例如在在/home/work创建名为venv-osroom的虚拟环境
```
pip -m venv /home/work/venv-osroom
```
&nbsp;&nbsp;没有安装好python-venv请先安装, Ubuntu安装命令如下:
```
sudo apt-get install python-venv
```


> OSROOM 依赖包安装

 - 进入虚拟环境
 ```shell
# 进入虚拟环境
source /home/work/venv-osroom/bin/activate
# 或
source /home/work/venv-osroom/bin/activate
```

- 进入osroom项目根目录
- 使用pip安装依赖包
```
pip install -r requirements.txt
```

 &nbsp;&nbsp;如果出现类似以下错误信息
 ```
 Command "/xxx/venv-osroom/bin/python3 -u -c "import setuptools, tokenize;__file__='/tmp/pip-install-erphi6km/xxx/setup.py';
 f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record /tmp/pip-record-nhbhzs1a/install-record.txt --single-version-externally-managed --compile --install-headers /home/work/project/venv_osroom/include
 site/python3.5/xxxx" failed with error code 1 in /tmp/pip-install-erphi6km/xxxx/
 ```
 &nbsp;&nbsp;那么请尝试安装python-dev
 &nbsp;&nbsp; Ubuntu系统:
 ```
 # 不一定需要版本号
 sudo apt-get install python3.5-dev
 ```
  &nbsp;&nbsp; 其他使用yum安装工具的Linux发行部系统:
```
  # 不一定需要版本号
 sudo yum install python3.5-devel
  ```
 
 > 创建数据库
 请查看Mongodb文档和Redis文档
 
 > 初始化设置
 
  因为osroom源代码只把配置文件config.py 和 数据库配置文件db_config.py 的sample文件上传到git，所以请先复制修改名称
```
  # 进入到apps/configs
 cp config_sample.py config.py
 cp db_config_sample.py db_config.py
  ```
