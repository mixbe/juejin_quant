from datetime import datetime
from time import sleep

from vnpy.event import EventEngine
from vnpy.gateway.binance import BinanceGateway
from vnpy.gateway.binances import BinancesGateway
from vnpy_datamanager.engine import ManagerEngine
from vnpy.trader.constant import Exchange
from vnpy.trader.engine import MainEngine
from vnpy.trader.object import Interval

# 币安现货的
binance_settings = {
    "key": "xxxx",
    "secret": "xxx",
    "session_number": 3,
    "proxy_host": "",
    "proxy_port": 0
}

# 币安期货的， 需要
binances_settings = {
    "key": "xxx",
    "secret": "xxxx",
    "会话数": 3,
    "服务器": "REAL",
    "合约模式": "正向",
    "代理地址": "",
    "代理端口": 0
}

if __name__ == '__main__':
    # 初始化事件引擎
    event_engine = EventEngine()
    # 初始化主引擎
    main_engine = MainEngine(event_engine)

    # 加载币安现货的网关, 现货代码(小写)：btcusdt
    main_engine.add_gateway(BinanceGateway)
    main_engine.connect(binance_settings, "BINANCE")

    # 加载币安合约的网关
    main_engine.add_gateway(BinancesGateway)
    main_engine.connect(binances_settings, "BINANCES")

    main_engine.init_engines()
    sleep(15)
    engine = ManagerEngine(main_engine, event_engine)

    # 合约代码(大写)：BTCUSDT， 周期(Interval.MINUTE,Interval.HOUR,Interval.DAILY)
    # engine.download_bar_data("BTCUSDT", Exchange.BINANCE, Interval.MINUTE, datetime(2016, 1, 1))

    # 现货代码(小写)：btcusdt, 周期(Interval.MINUTE,Interval.HOUR,Interval.DAILY)
    engine.download_bar_data("bnbusdt", Exchange.BINANCE, Interval.HOUR, datetime(2016, 1, 1))
    main_engine.close()
