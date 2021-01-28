"""
http://tushare.org/trading.html#id5
"""
import tushare as ts
import matplotlib.pyplot as plt
pro = ts.pro_api('b7bbd6907437d1f894145e7487709d27ee220b6c3772205ef05c83fb')

df = ts.get_tick_data('600703',date='2021-01-28',src='tt')
df.head(10)
# print(df)
# print(df["price"],df["volume"])
ax = df.plot.bar(x="price",y="volume",rot=0)
plt.show()

