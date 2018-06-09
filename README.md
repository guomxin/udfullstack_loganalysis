# Log Analysis项目

## 安装要求
### 软件及数据
- 安装Python 3.6
- pip install psycopg2
- 安装postgresql
  - 设置用户postgres的密码为111111
  - 设置postgresql.conf中listen_addresses为'\*'
  - 设置pg_hba.conf中IPv4 local connections的访问方式为md5
- 数据生成和加载参照[此链接](https://classroom.udacity.com/nanodegrees/nd004-cn/parts/d3335c49-3556-488a-9f63-c0d28b16ff12/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/262a84d7-86dc-487d-98f9-648aa7ca5a0f/concepts/a9cf98c8-0325-4c68-b972-58d5957f1a91)中的'Download the data'部分
### 克隆git仓库
```bash
$ git clone https://github.com/guomxin/udfullstack_loganalysis.git
```

## 运行
### What are the most popular three articles of all time?
log表中path字段值如'/article/%'的行为article浏览日志，path字段去掉前9个字符(article_slug)与articles表中的slug字段对应；<br>
log表按article_slug进行分组并计数就是article被浏览的次数，同时利用article_slug与articles表进行关联取得article的title。<br>
使用命令行，进入代码文件所在的目录，运行如下命令：
```bash
$ python get_popular_articles.py
```
###  Who are the most popular article authors of all time? 
log表中path字段值如'/article/%'的行为article浏览日志，取path字段去掉前9个字符形成临时表article_views；<br>
article_views临时表与articles表在slug字段进行关联，这样就获得了每个被浏览的article的author信息；<br>
同时articles表的author字段与authors表的id字段进行关联，这样就获得了author的name；<br>
基于authors.name进行分组和计数，得出每个author的article的浏览次数。<br>
使用命令行，进入代码文件所在的目录，运行如下命令：
```bash
$ python get_popular_authors.py
```
###  On which days did more than 1% of requests lead to errors? 
基于log表形成临时表，这个临时表包含两个字段date(提取time中的日期)和status_value(status为'200 OK'时为0，否则为1)；<br>
对上述临时表按date进行分组，sum(\*)/count(\*)既是访问失败率，并按失败率进行降序排序；<br>
python程序中顺序扫描sql的返回结果，遇到失败率小于等于1%时退出。<br>
使用命令行，进入代码文件所在的目录，运行如下命令：
```bash
$ python get_reqerror_days.py
```
