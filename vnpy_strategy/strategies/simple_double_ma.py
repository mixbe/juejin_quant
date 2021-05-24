from typing import Any

from vnpy.app.cta_strategy import (
    CtaTemplate,
    StopOrder,
    TickData,
    BarData,
    TradeData,
    OrderData,
    BarGenerator,
    ArrayManager
)
from vnpy.trader.constant import Interval


class SimpleDoubleMA(CtaTemplate):
    """
    一个简单的双均线策略
    """

    # 定义参数
    fast_window = 10
    slow_window = 20

    # 定义变量
    fast_ma0 = 0.0
    fast_ma1 = 0.0
    slow_ma0 = 0.0
    slow_ma1 = 0.0

    parameters = ["fast_window", "slow_window"]
    variables = ["fast_ma0", "fast_ma1", "slow_ma0", "slow_ma1"]

    def __init__(self, cta_engine: Any, strategy_name: str, vt_symbol: str, setting: dict):
        super().__init__(cta_engine, strategy_name, vt_symbol, setting)
        # K线合成器：从Tick合成分钟K线用， 这里合成轴线数据
        self.bg_4_hour = BarGenerator(self.on_bar, 4, self.on_4hour_bar, Interval.HOUR)
        # 时间序列容器：计算技术指标用
        self.am = ArrayManager()

    def on_init(self):
        self.write_log("策略初始化")
        # 加载10天的历史数据用于初始化回放
        self.load_bar(20)

    def on_start(self):
        self.write_log("策略启动")
        # 通知图形界面更新（策略最新状态）
        # 不调用该函数则界面不会变化
        self.put_event()

    def on_4hour_bar(self, bar: BarData):
        am = self.am
        am.update_bar(bar)
        # 若缓存的K线数量尚不够计算技术指标，则直接返回
        if not self.am.inited:
            return
        # 计算快速均线
        fast_ma = self.am.sma(self.fast_window, array=True)
        # T时刻的值
        self.fast_ma0 = fast_ma[-1]
        # T-1时刻的值
        self.fast_ma1 = fast_ma[-2]

        # 计算慢速均线
        slow_ma = self.am.sma(self.slow_window, array=True)
        self.slow_ma0 = slow_ma[-1]
        self.slow_ma1 = slow_ma[-2]

        # 是否是金叉
        cross_over = (self.fast_ma0 > self.slow_ma0) and (self.fast_ma1 < self.slow_ma1)
        # 是否是死叉
        cross_below = (self.fast_ma0 < self.slow_ma0) and (self.fast_ma1 > self.slow_ma1)

        if cross_over:
            # 为了保证成交，在K线收盘价上加5发出限价单
            price = bar.close_price + 5
            # 当前无仓位，则直接开多
            if self.pos == 0:
                self.buy(price, 1)
            # 当前持有空头仓位，则先平空，再开多
            elif self.pos < 0:
                self.cover(bar.close_price, 1)
                self.buy(bar.close_price, 1)
        if cross_below:
            if self.pos == 0:
                self.short(bar.close_price, 1)
            elif self.pos > 0:
                self.sell(bar.close_price, 1)
                self.short(bar.close_price, 1)
        self.put_event()

    def on_stop(self):
        self.write_log("策略停止")
        self.put_event()

    def on_tick(self, tick: TickData):
        """
        通过该函数收到Tick推送。
        :param tick:
        :return:
        """
        pass

    def on_bar(self, bar: BarData):
        """
        通过该函数收到新的1分钟K线推送。
        :param bar:
        :return:
        """
        self.bg_4_hour.update_bar(bar)

    def on_order(self, order: OrderData):
        """
        通过该函数收到委托状态更新推送。
        :param order:
        :return:
        """
        self.put_event()

    def on_trade(self, trade: TradeData):
        """
        通过该函数收到成交推送。
        :param trade:
        :return:
        """
        self.put_event()

    def on_stop_order(self, stop_order: StopOrder):
        """
        通过该函数收到本地停止单推送。
        :param stop_order:
        :return:
        """
        self.put_event()
