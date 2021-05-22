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

##  4.1、命令方式回测

```bash
python backtest_fixed_time.py
```



## 4.2、图像界面方式回测







# 正在更新中……


