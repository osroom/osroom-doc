### 安装mongodb
- Ubuntu16.04 apt-get安装Mongodb 3.4 或3.6版本

#### &nbsp;&nbsp;添加安装源

- 下面版本源请选择其中一个版本

- 添加3.4版本源
   添加public key：
```shell
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6 
```
   添加包源：
```shell
echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | sudo tee        /etc/apt/sources.list.d/mongodb-org-3.4.list
```
<br/>

- 添加3.6版本源

   添加public key：
```
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5
```
   添加包源：
```
echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu precise/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list
```

#### &nbsp;&nbsp;更新apt-get
- 更新
```
sudo apt-get update
```
<br/><br/>

#### &nbsp;&nbsp;安装
- 安装
```
sudo apt-get install -y mongodb-org
```
   详情：https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/

<br/><br/><br/>
### 使用
#### &nbsp;&nbsp;进入数据库
- 数据库启动后，默认配置下在命令行输入mongo就可以进入数据库管理

```shell
(venv3) work@ubuntu16:~/project/osroom$ mongo
MongoDB shell version v3.4.10
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.4.10

```

<br/><br/>
#### &nbsp;&nbsp;创建数据库

- use test_db就能创建一个数据库test_db, 之后需要创建一个collection, 否则会被自动删除

```js
> use test_db
> db.createCollection("test_coll")
```

<br/><br/>
#### &nbsp;&nbsp;创建用户

- 先给mongodb自带的collection admin 创建一个用户

```js
> use admin
> db.createUser(
   {
     user: "dba",
     pwd: "123456",
     roles: [ { role: "userAdminAnyDatabase", db: "admin" },
              { role: "dbAdminAnyDatabase", db: "admin" }]
   }
 )
```

<br/><br/>

- 为自己创建的库新建用户

```js
> use test
> db.createCollection("test_coll")
> db.createUser(
    {
        user:'work',
        pwd:'123456',
        roles:[{role:'readWrite', db:'test'}]
    })
```

<br/><br/>

- 更新一个库的用户方式如下
```
> use test
> db.updateUser(
    "dba",
    {
     roles : [ { role: "dbAdminAnyDatabase", db: "admin" },
                { role: "userAdminAnyDatabase", db: "admin" }]
    }
)
```

<br/><br/>
#### &nbsp;&nbsp;数据库个角色role说明

- Built-In Roles(内置角色)
```
    1. 数据库用户角色：read、readWrite;
    2. 数据库管理角色：dbAdmin、dbOwner、userAdmin；
    3. 集群管理角色：clusterAdmin、clusterManager、clusterMonitor、hostManager；
    4. 备份恢复角色：backup、restore；
    5. 所有数据库角色：readAnyDatabase、readWriteAnyDatabase、userAdminAnyDatabase、dbAdminAnyDatabase
    6. 超级用户角色：root
    // 这里还有几个角色间接或直接提供了系统超级用户的访问（dbOwner 、userAdmin、userAdminAnyDatabase）
    7. 内部角色：__system
```

<br/><br/>

- 具体

```
    Read：允许用户读取指定数据库
    readWrite：允许用户读写指定数据库
    dbAdmin：允许用户在指定数据库中执行管理函数，如索引创建、删除，查看统计或访问system.profile
    userAdmin：允许用户向system.users集合写入，可以找指定数据库里创建、删除和管理用户
    clusterAdmin：只在admin数据库中可用，赋予用户所有分片和复制集相关函数的管理权限。
    readAnyDatabase：只在admin数据库中可用，赋予用户所有数据库的读权限
    readWriteAnyDatabase：只在admin数据库中可用，赋予用户所有数据库的读写权限
    userAdminAnyDatabase：只在admin数据库中可用，赋予用户所有数据库的userAdmin权限
    dbAdminAnyDatabase：只在admin数据库中可用，赋予用户所有数据库的dbAdmin权限。
    root：只在admin数据库中可用。超级账号，超级权限
```

<br/><br/>
#### &nbsp;&nbsp;OSROOM需要的库
- 使用osroom系统，请先创建三个数据库，库名自定义(建议使用库名称为osr_web, osr_user, osr_sys)

<br/><br/>

- 注意mongodb的每个库都需要创建一个用户/密码(可以全部一样的用户名和密码)

<br/><br/>

- 创建后修改mongo配置文件mongodb.conf 开启安全验证(用户验证)
