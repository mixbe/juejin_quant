from vnpy_ctabacktester.engine import BacktestingEngine, OptimizationSetting
from datetime import datetime
from vnpy.trader.object import Interval
from strategies.simple_double_ma import SimpleDoubleMA


def run_backtesting(strategy_class, setting, vt_symbol, interval, start, end, rate, slippage, size, pricetick, capital):
    engine = BacktestingEngine()
    engine.set_parameters(
        vt_symbol=vt_symbol,
        interval=interval,
        start=start,
        end=end,
        rate=rate,
        slippage=slippage,
        size=size,
        pricetick=pricetick,
        capital=capital
    )
    engine.add_strategy(strategy_class, setting)
    engine.load_data()
    engine.run_backtesting()

    engine.calculate_result()  # 计算回测的结果
    engine.calculate_statistics()  # 计算一些统计指标

    engine.show_chart()  # 绘制图表


if __name__ == '__main__':
    run_backtesting(
        strategy_class=SimpleDoubleMA,
        setting={},
        vt_symbol="ethusdt.BINANCE",
        interval=Interval.MINUTE,
        start=datetime(2020, 1, 1),
        end=datetime(2021, 5, 20),
        rate=1 / 1000,
        slippage=0.1,
        size=1,
        pricetick=0.01,
        capital=2000,
    )
