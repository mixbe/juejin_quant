[TOC]



## 1. 更新内容



[详细查看Github更新日志](https://github.com/vnpy/vnpy/commit/f081fe8d7548236bc041f4dba35c919511063962)

主要看了下2.4.0版本做了很大的调整

* 将Deribit接口剥离到vnpy_deribit项目中，并升级到2.0.1版本
* 剥离CTA策略模块下的穷举和遗传优化算法到vnpy.trader.optimize模块下
* 遗传算法优化完成后，输出所有回测过的参数对应结果（而不只是最优结果）
* CTA策略引擎加载策略文件时，增加模块重载的操作，使得任何策略文件修改可以立即生效
* CTA策略引擎扫描特定目录下的策略文件时，使用glob函数（替换原有的os.walk），避免对子目录中文件的错误加载
* 将CTA策略模块剥离到vnpy_ctastrategy项目中
* 将CTA回测模块剥离到vnpy_ctabacktester项目中
* 将XTP接口剥离到vnpy_xtp项目中，并升级到2.2.27.4版本
* 将事前风控模块剥离到vnpy_riskmanager项目中
* 将数据管理模块剥离到vnpy_datamanager项目中
* 将Deribit接口剥离到vnpy_bybit项目中，并升级到2021.6.21版本



## 2 如何运行VNPY2.4.0

### 2.1 环境配置

* [基本的环境配置，安装参考上一篇](https://mp.weixin.qq.com/s?__biz=MzA3NDYxNDc3MQ==&amp;mid=2652390042&amp;idx=1&amp;sn=1b76748baa613014f9a0fe3d0922811d&amp;chksm=8491f006b3e6791072f6f76777e9b6f3ffd38912e0ad03b36b7a5ef81932b23b04bf57a9daa3&token=2142790632&lang=zh_CN#rd)

* **系统**： Mac
* **Python环境**： 3.8.8

### 2.2 拉取最新的代码

* 拉取代码

```bash
# 拉取代码
git clone https://github.com/vnpy/vnpy.git
# 切一个分支，如：local_dev
git checkout -b local_dev
```

* 安装依赖

> 下面几个常用的模块已经拆出去作为一个独立的项目，如果要运行`VNPY`项目，下面几个包是需要安装的

```bash
pip install vnpy-ctabacktester
pip install vnpy-ctastrategy
pip install vnpy-datamanager
pip install vnpy-riskmanager
```



### 2.3 新建一个目录

> 为了原始项目干净，新建一个目录(名称随意)，在这个目录可以写自己的策略代码，工具类等

- 比如我自己新建了一个目录`workspace`,
- 在`workspace`目录下再新建两个目录：
  - `.vntrader`:  存放配置文件的地方(mac系统下默认存放路径是` ~/.vntrader`, 不过编辑什么的不方便)
  - `strategies`: 存放策略代码的地方

### 2.4 实现代码

> 代码：https://github.com/mixbe/juejin_quant



![目录结构](https://i.loli.net/2021/06/27/oBipTZRY7NfdxXI.png)

* 策略代码： `simple_double_ma`
* 启动App(图像界面)： `run_app.py`
* 回测(命令行)：`run_backtest.py`

## 3. 问题

> 系统的策略，还有自己写的策略，都加载不到

**版本升级有风险，升级到2.4.0后，发现自己写的策略程序都无法加载，阅读源代码，才发现官方没有做到系统兼容，等待下一版修复。**

Mac，Linux用户要运行代码，肯定需要改下源码,测试就OK了：

* 包`vnpy_ctastrategy` ，文件`engin` , 803行

* 包`vnpy_ctabacktester`， 文件`engin`, 95行

```python
# 源代码 pathname: str = str(path) + f"\\*.{suffix}"
pathname: str = str(path) + f"/*.{suffix}"
```

## 4.总结

新的版本问题肯定是有的，下载源码，运行调试，不断探索。


