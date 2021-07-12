# juejin_quant （公众号）

> 分享股票，基金，数字货币量化思路和量化策略；

掘金者量化文章中的项目代码

# 1、环境

* Python 3.8.x
* [vnpy 2.30](https://github.com/vnpy/vnpy)，在此特别感谢vnpy社区
* [MongoDB](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/)



# 2、安装

* 安装mongoDB

安装教程，参考： https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/

建库建表的语句

```bash
use admin
db.createUser({user:'admin', pwd:'xxxx', roles: [ { role: "userAdminAnyDatabase", db: "admin" } ]})

use vnpy
db.createUser({ user: "root", pwd: "xxxx", roles: [{ role: "readWrite", db: "vnpy" }] })
```

* 安装`vnpy`

> 安装vnpy,别直接`pip install vnpy`， 因为`pypi.org`上的库已经好久没有更新了，所以用下面的安装方式

```bash
 pip install git+https://github.com/vnpy/vnpy.git
```

* 安装一些缺失的包

```bash
 pip install tzlocal
 pip install plotly
 pip install pymongo
 pip install mongoengine
 pip install quickfix
```

# 3、项目结构



```
├── README.md
├── .vntrader  # 这个文件自己创建，没有，默认是`~/.vntrader/`,但是为了编辑方便，我会在项目创建这个目录（注意主要信息的泄露）
│   ├── cta_backtester_setting.json
│   ├── cta_strategy_data.json
│   ├── cta_strategy_setting.json
│   ├── data_recorder_setting.json
│   ├── database.db
│   ├── log
│   │   └── vt_20210522.log
│   ├── risk_manager_setting.json
│   └── vt_setting.json
└── vnpy_strategy    
    ├── backtest_fixed_time.py   # 运行回测
    ├── run_window.py            # 通过图像界面操作
    ├── strategies               # 自己写的量化策略,都在这个目录
    │   └── simple_double_ma.py  
    └── utils                    # 回测使用的数据，都会放在这个目录
        └── download_data_binance.py  

```



# 4、如何回测
> 回测之前下载数据

##  4.1、命令方式回测

```bash
python run_backtest.py
```
回测结果
```
2021-05-24 23:18:06.187119	首个交易日：	2017-09-05
2021-05-24 23:18:06.187126	最后交易日：	2018-05-20
2021-05-24 23:18:06.187131	总交易日：	258
2021-05-24 23:18:06.187137	盈利交易日：	139
2021-05-24 23:18:06.187142	亏损交易日：	117
2021-05-24 23:18:06.187151	起始资金：	300,000.00
2021-05-24 23:18:06.187159	结束资金：	300,969.58
2021-05-24 23:18:06.187165	总收益率：	0.32%
2021-05-24 23:18:06.187170	年化收益：	0.30%
2021-05-24 23:18:06.187177	最大回撤: 	-608.35
2021-05-24 23:18:06.187183	百分比最大回撤: -0.20%
2021-05-24 23:18:06.187188	最长回撤天数: 	8
2021-05-24 23:18:06.187194	总盈亏：	969.58
2021-05-24 23:18:06.187200	总手续费：	101.55
2021-05-24 23:18:06.187208	总滑点：	0.00
2021-05-24 23:18:06.187215	总成交金额：	101,552.30
2021-05-24 23:18:06.187220	总成交笔数：	171
2021-05-24 23:18:06.187226	日均盈亏：	3.76
2021-05-24 23:18:06.187231	日均手续费：	0.39
2021-05-24 23:18:06.187237	日均滑点：	0.00
2021-05-24 23:18:06.187243	日均成交金额：	393.61
2021-05-24 23:18:06.187250	日均成交笔数：	0.6627906976744186
2021-05-24 23:18:06.187256	日均收益率：	0.00%
2021-05-24 23:18:06.187262	收益标准差：	0.02%
2021-05-24 23:18:06.187267	Sharpe Ratio：	1.11
2021-05-24 23:18:06.187273	收益回撤比：	1.60
2021-05-24 23:18:06.187780	策略统计指标计算完成
```
![image-20210524232021676.png](https://i.loli.net/2021/05/25/UCO4DEQ5JaFywGl.png)

## 4.2、图像界面方式回测
启动`run_window.py`文件，即可启动图像界面回测。启动成功后，整个界面如下所示。

```
 python run_window.py
```

![image-20210524232632779.png](https://i.loli.net/2021/05/25/NJYfe8XTVchMnad.png)

图像界面回测结果如下：
![image-20210524232934415.png](https://i.loli.net/2021/05/25/ymg38ZuFciYRhxn.png)

* 回测之前，一定要先下载数据，有问题，可以多去看看官方的文档;




# 公众号

![公众号](https://i.loli.net/2021/07/12/pwiIrB79Gzb5K2M.png)

