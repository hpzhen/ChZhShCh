import sys
import datetime

from external_package import tushare_helper as th
from inner_package import standardized as standard
from inner_package import show

import QUANTAXIS as QA


# original = th.TushareHelper('000001', datetime.date.today()+ datetime.timedelta(days=-1),datetime.date.today() + datetime.timedelta(days=+1),'1min')
original = th.TushareHelper('000001', '2020-01-01', '2020-06-30', 'D')
# original = QA.QA_fetch_stock_day('000001', start, end, format='pd')

original.data_transfer()

sta = standard.StandardHandle(original.data_original)
sta.deal_candle()
sta.get_top_bottom()

date_tickers = original.date_tickers
my_plot = show.PlotShow(date_tickers, '000001')
my_plot.candle_show(original.data_original_ex, [])

date_tickers = sta.date_tickers
my_plot = show.PlotShow(date_tickers, '000001')
# my_plot.candle_show(sta.standardized_list_ex, [])
my_plot.candle_show(sta.standardized_list_ex, sta.top_bottom_list_ex)
my_plot.candle_show(sta.standardized_list_ex,
                    sta.standardized_top_bottom_list_ex)
