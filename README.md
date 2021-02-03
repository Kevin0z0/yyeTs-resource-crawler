# yyeTs-resource-spider

呜呜呜

![](http://file.dsb.ink/rrys.png)

直接查询的网站：https://v.dsb.ink

此程序可爬取大部分人人影视数据，具体bug还没测试

安装requirements

```bash
pip install -r requirements-mongo.txt #安装mongodb版的模块
pip install -r requirements-mysql.txt #安装mysql版的模块
```

修改settings.json中的数据（当前为默认设置）

​	布尔值只能设置为布尔值，true为需要爬取的数据，false则不爬取

​	pageNum：可选择"1-737"多页面 或者 "2" 单页面爬取

​	level：可选择只爬取 "e" ，也可以选择"abe"，"abc"等多种组合爬取，如果选择"all"，则会爬取所有影视信息， 不想爬取没有分级的用"abcde"即可

​	export：默认为导出csv格式，当前仅支持mysql和mongodb，如有需要，自行修改下列代码替换"csv"

```json
{
    "db": "mongodb",
    "host": "localhost",
    "port": 27017,
    "username": "",
    "password": "",
    "dbname": "rrys",
    "table": "rrys"
}
```
```json
{
    "db": "mysql",
    "host": "localhost",
    "port": 3306,
    "username": "",
    "password": "",
    "dbname": "rrys",
    "table": "rrys"
}
```


#### 英文对应的中文

    线程=>threads
    
    链接=>url
    
    排名=>rank
    
    剧种=>dramaType
    
    评分=>score
    
    原名=>formerName
    
    地区=>region
    
    语言=>language
    
    首播=>premiereDate
    
    制作公司/电视台=>company
    
    类型=>type
    
    翻译=>translator
    
    IMDB=>imdb
    
    别名=>alias
    
    编剧=>screenwriter
    
    导演=>directors
    
    主演=>actors
    
    简介=>introduction
    
    图片链接=>imgurl


最后运行

```bash
python main.py
```

有什么问题可以联系邮箱zkw644720@gmail.com
