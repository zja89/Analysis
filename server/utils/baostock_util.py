import baostock as bs
lg = bs.login()

def get_history_volume(code,sd,ed):
    rs = bs.query_history_k_data_plus(code,
                                      "date,time,code,open,high,low,close,volume,amount",
                                      start_date=sd, end_date=ed,
                                      frequency="5")
    records = {}
    for d in rs.data:
        date, time, code, open, high, low, close, volume, amount = d
        price = (float(high)+float(low))/2
        price = round(price, 2)
        total_volume = int(volume) + records.get(price, 0)
        records.update({price: total_volume})
    prices = sorted(records.keys())
    volums = [records[k] for k in sorted(records.keys())]
    return prices,volums