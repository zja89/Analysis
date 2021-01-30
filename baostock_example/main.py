import baostock as bs
import pandas as pd
import matplotlib.pyplot as plt
#### 登陆系统 ####
lg = bs.login()

eds = ['2021-01-27','2021-01-28','2021-01-29']
# code = "sh.600703"
code = "sz.000425"
code = "sz.002648"
code = "sz.002216"
for ed in eds:
    f = plt.figure()
    f.set_figwidth(50)
    f.set_figheight(20)
    rs = bs.query_history_k_data_plus(code,
        "date,time,code,open,high,low,close,volume,amount",
        start_date='2020-10-01', end_date=ed,
        frequency="5")

    price_list = []
    volume_list = []
    records = {}
    for d in rs.data:
        price = float(d[4])+float(d[5])
        price = round(price/2,2)
        volume = int(d[7])+records.get(price,0)
        records.update({price:volume})
    print(rs.data[-1])
    prices = sorted(records.keys())
    print(prices)
    volums = [records[k] for k in sorted(records.keys())]
    l1=plt.plot(prices,volums)
    for a,b in zip(prices, volums):
        plt.text(a, b, str(a))
    plt.title(ed)
plt.show()