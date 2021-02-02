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
            data.append([_price, k, _volume])
    return date_list,data


def get_total_num(code):
    rs = bs.query_history_k_data_plus(code,
                                      "date,code,volume,turn",
                                      start_date='2020-12-01', end_date='2020-12-01',
                                      frequency="d", adjustflag="3")
    data = rs.data
    date,_code,volume,turn = data[0]
    total_num = int(volume)/(float(turn)/100)
    total_num = int(total_num)
    return total_num

