## 安装redis
### Ubuntu apt-get 安装
```
sudo apt-get install redis-server
```

### 建议配置一个密码

> 编辑/etc/redis.conf配置密码

```
  将
    #requirepass foobared
  修改为
    requirepass your-password
```

### 重启redis
```
sudo /etc/init.d/redis-server restart
```
