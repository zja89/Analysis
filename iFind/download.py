from settings import code_list
import os
Flag = True
from iFinDPy import *

thsLogin = THS_iFinDLogin('htqh1015', '990252')


def download(st='2019-01-27',et='2021-01-28'):
    for c in code_list:
        fname = "%s.txt" % c
        # if os.path.exists(fname):
        #     continue

        data= THS_HistoryQuotes(c,'floatSharesOfAShares;floatCapitalOfAShares;volume','Interval:D,CPS:1,baseDate:1900-01-01,Currency:YSHB,fill:Previous',st,et,True)
        with open(fname,"w") as f:
            f.write(data.decode())