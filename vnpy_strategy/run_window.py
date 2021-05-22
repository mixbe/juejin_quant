from vnpy.event import EventEngine

from vnpy.trader.engine import MainEngine
from vnpy.trader.ui import MainWindow, create_qapp

from vnpy.gateway.binance import BinanceGateway  # 现货
from vnpy.gateway.binances import BinancesGateway  # 合约

from vnpy.app.cta_strategy import CtaStrategyApp  # CTA策略
from vnpy.app.data_manager import DataManagerApp  # 数据管理, csv_data
from vnpy.app.data_recorder import DataRecorderApp  # 录行情数据
from vnpy.app.algo_trading import AlgoTradingApp  # 算法交易
from vnpy.app.cta_backtester import CtaBacktesterApp  # 回测研究
from vnpy.app.risk_manager import RiskManagerApp  # 风控管理
from vnpy.app.spread_trading import SpreadTradingApp  # 价差交易

if __name__ == '__main__':
    qapp = create_qapp()

    event_engine = EventEngine()

    main_engine = MainEngine(event_engine)

    # 币安现货
    main_engine.add_gateway(BinanceGateway)
    # 币安期货
    main_engine.add_gateway(BinancesGateway)
    # 策略
    main_engine.add_app(CtaStrategyApp)
    # 回测
    main_engine.add_app(CtaBacktesterApp)
    # 数据
    main_engine.add_app(DataManagerApp)
    # 算法交易
    main_engine.add_app(AlgoTradingApp)
    # 数据记录
    main_engine.add_app(DataRecorderApp)
    # 风险控制
    main_engine.add_app(RiskManagerApp)
    # 高频交易
    main_engine.add_app(SpreadTradingApp)

    main_window = MainWindow(main_engine, event_engine)
    main_window.showMaximized()

    qapp.exec()
