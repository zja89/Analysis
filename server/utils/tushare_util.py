import tushare as ts
from datetime import datetime

a = ['603345', '603566', '600298', '600460', '600104', '601138', '601766', '600690', '600031', '601816', '600703', '600966', '600597', '600143', '600309', '600598', '600596', '603195', '600563', '601899', '600362', '603515', '600089', '601618', '600585', '601727', '600406', '600893']
b = ['002423', '002236', '000885', '002380', '003816', '000905', '000100', '002607', '000488', '000651', '000333', '002415', '000895', '002714', '002157', '000876', '000930', '002352', '002385', '000713', '002648', '002216', '000962', '002511', '000725', '000157', '000425', '002475']

code_list = []
# pro = ts.set_token('b7bbd6907437d1f894145e7487709d27ee220b6c3772205ef05c83fb')
pro = ts.pro_api()
data = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
print(data)
for index, row in data.iterrows():
    if row["symbol"] in a:
        code_list.append([row["symbol"],row["name"],row["ts_code"]])
    if row["symbol"] in b:
        code_list.append([row["symbol"],row["name"],row["ts_code"]])

print(code_list)

if __name__ == "__main__":
    pass
