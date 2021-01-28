import json
import matplotlib.pyplot as plt
from settings import code_list
import download
def cal(c,et):
    with open("%s.txt"%c,"r") as f:
        data = f.read()
    data = json.loads(data)
    dates = data["tables"][0]["time"]
    floatSharesOfAShares = data["tables"][0]["table"]["floatSharesOfAShares"]
    floatCapitalOfAShares = data["tables"][0]["table"]["floatCapitalOfAShares"]
    volume = data["tables"][0]["table"]["volume"]


    # origin_floatSharesOfAShares = floatSharesOfAShares[1]
    # origin_price = floatCapitalOfAShares[1]/origin_floatSharesOfAShares
    # cal = {origin_price:origin_floatSharesOfAShares}
    records = {}
    for i,d in enumerate(dates):
        current_price = floatCapitalOfAShares[i] / floatSharesOfAShares[i]
        current_price = round(current_price, 3)
        if i == 0:
            records = {floatCapitalOfAShares[i]/floatSharesOfAShares[i]:floatSharesOfAShares[i]}
            print(records,floatCapitalOfAShares[i],floatSharesOfAShares[i],floatSharesOfAShares[i])
        else:
            current_price = floatCapitalOfAShares[i]/floatSharesOfAShares[i]
            current_price = round(current_price, 3)
            out_num = volume[i]
            if not out_num:
                continue
            for p in sorted(records.keys()):
                n = records.get(p,0)
                if n >= out_num:
                    nn = n - out_num
                    out_num = 0
                else:
                    out_num = out_num - n
                    nn = 0
                records.update({p: nn})
                if out_num == 0:
                    break
            precious_num = records.get(current_price, 0)
            current_num = precious_num + volume[i]
            records.update({current_price: current_num})
            # print(current_price)
            # print(dates[i], current_price, floatCapitalOfAShares[i], floatSharesOfAShares[i])


    print(records)

    price = [k for k in records.keys()]
    num = [records[k] for k in records.keys()]
    print(price)
    print(num)
    print(min([k for k in records.keys() if records[k]]))
    l1=plt.bar(price,num)
    plt.title(c+" - "+et)
    plt.show()

from download import download

et = '2021-01-27'
download(et=et)
for c in code_list:
    cal(c,et)