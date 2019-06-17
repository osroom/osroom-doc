## 安装redis
#### &nbsp;&nbsp;安装
- Ubuntu 使用apt-get安装
```
sudo apt-get install redis-server
```

#### &nbsp;&nbsp;配置密码

> 编辑/etc/redis.conf配置密码

```
  将
    #requirepass foobared
  修改为
    requirepass your-password
```

#### &nbsp;&nbsp;重启redis
```
sudo /etc/init.d/redis-server restart
```
