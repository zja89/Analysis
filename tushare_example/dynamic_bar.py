import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation

import tushare as ts
pro = ts.pro_api('b7bbd6907437d1f894145e7487709d27ee220b6c3772205ef05c83fb')

df = ts.get_tick_data('600703',date='2021-01-28',src='tt')

a = df.groupby(["price"]).agg({"volume":"sum"})

a.plot.bar()
plt.xticks(rotation=90)
plt.show()