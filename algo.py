import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as pt
from matplotlib import style
style.use('ggplot')

time = np.array([10,100,1000,10000,100000])

f_1        =   lambda n : 10000
f_log_n    =   lambda n : np.log(n)
f_n        =   lambda n : 3*n+2
f_nlog_n   =   lambda n : n*np.log(n)
f_nn       =   lambda n : 2*n**2 + 3*n+2
f_nnn      =   lambda n : n*n*n + 10000*n**2
f_2_n      =   lambda n : 2**n + 10000*n**10000

def time_complexity(time) -> pd.DataFrame :
    """
    时间效率:算法运行速度的快慢.
    """
    return f_1(time) , f_log_n(time) , f_n(time) , f_nlog_n(time) , f_nn(time) , f_nnn(time) , f_2_n(time)
    return \
        f"""
        f_1 :       {f_1(time)} , 
        f_logn :    {f_log_n(time)} , 
        f_n :       {f_n(time)} , 
        f_nlogn :   {f_n_log_n(time)} ,
        f_nn :      {f_nn(time)} , 
        f_nnn :     {f_nnn(time)} ,
        f_2n :      {f_2_n(time)}
        """

"""
模型評估: 確認模型是否適合，
    可以使用統計假設檢驗來檢查模型的統計顯著性，
    確保模型解釋了數據的變異.
    
    假設檢驗:H0:a=0,b=0H0:a=0,b=0(模型不顯著）
    對立假設:H1:a≠0H1:a=0 或 b≠0b=0(模型顯著）

模型解釋: 解釋最終模型的參數，
    例如aa可能表示算法的時間複雜度的某個指數,而bb可能表示常數項.
"""

if __name__ == '__main__' :

    f1 , f2 , f3 , f4 , f5 , f6 , f7 = time_complexity(time)
    # pt.plot(time,f1)
    pt.plot(time,f2)
    pt.plot(time,f3)
    pt.plot(time,f4)
    # pt.plot(time,f5)
    # pt.plot(time,f6)
    # pt.plot(time,f7)
    pt.legend(['f2','f3','f4'])
    pt.show()

