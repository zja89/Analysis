import baostock as bs
lg = bs.login()

def get_history_volume(code,sd,ed):
    rs = bs.query_history_k_data_plus(code,
                                      "date,time,code,open,high,low,close,volume,amount",
                                      start_date=sd, end_date=ed,
                                      frequency="5")
    records = {}
    current_data = {}
    date_list = []
    for d in rs.data:
        date, time, code, open, high, low, close, volume, amount = d
        price = (float(high) + float(low)) / 2
        price = round(price, 2)
        if date not in date_list:
            date_list.append(date)
        if date in records:
            records[date][price] = int(volume)+records[date].get(price,0)
        else:
            records[date] = {price:int(volume)}
    data = []
    for k,v in records.items():
        for _price,_volume in v.items():
            # data.append([_price,date_list.index(k),_volume])
            data.append([_price, k, _volume])
    print(date_list)
    return date_list,data