import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation
import tushare as ts
from datetime import timedelta,datetime

pro = ts.pro_api('b7bbd6907437d1f894145e7487709d27ee220b6c3772205ef05c83fb')

days = 4
now = datetime.now().date()

fd = now-timedelta(days=days)

ax = None
# code = "000425"
code = '600703'
for d in [str(fd+timedelta(days=i)) for i in range(days+1)]:
    df = ts.get_tick_data(code,date=d,src='tt')
    a = df.groupby(["price"]).agg({"volume":"sum"})
    a = a.head(90)
    if not ax:
        ax = a.plot()
    a.plot(ax=ax,figsize=(30,10),legend=d)
    plt.xticks(rotation=30)
    plt.title(d)
plt.show()