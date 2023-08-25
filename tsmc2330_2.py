import pandas as pd
import numpy as np
import datetime

list2 = []
for i in range(2) :
    path = "C:\\Users\\USER\\Desktop\\Python_fangru\\2330\\"
    file = f'STOCK_DAY_2330_2021{i+1:02d}.csv'


    daily_df = pd.read_csv( path+file,
                           header=1,
                           engine='python',
                           thousands=',',  # 把千位數逗號看成字串逗號  --> 轉成int
                           encoding='Big5')

    s_bool = daily_df['日期'].str.contains('\d{3}[-/]\d{2}[-/]\d{2}', regex=True)
    daily_df = daily_df[s_bool]   # 篩選出想要的列(橫)
    daily_df = daily_df[['日期','開盤價','最高價','最低價','收盤價','成交股數']]   # 指定要留下的欄(直)

    # 更改欄位名稱
    daily_df = daily_df.rename(columns={'日期':'Date',
                                        '開盤價':'Open',
                                        '最高價':'High',
                                        '最低價':'Low',
                                        '收盤價':'Close',
                                        '成交股數':'Volumn'})

    # 民國日期(字串) 變成 西洋日期(datetime 日期格式) --> 用Series 的 dt 處理
    for n,item in enumerate(daily_df['Date']) :
        list1 = item.split('/')
        list1[0] = str(int(list1[0])+1911)
        str1 = '-'.join(list1)  # '2021-01-14'
        daily_df.iloc[n,0] = str1

    daily_df['Date'] = pd.to_datetime(daily_df['Date'])

    # 添加所有的表格物件(12個)成一個表單
    list2.append(daily_df)

df_2330 = pd.concat(list2, axis=0 )
df_2330 = df_2330.reset_index(drop=True)
# print(df_2330)

# 日期改成列索引
df_2330 = df_2330.set_index('Date')
print(df_2330)

# 開始畫圖
import mplfinance as mpf
# mpf.plot(df_2330)
mpf.plot(df_2330,type='candle',mav=(5,20,60))   # mav=(5 週線,20 月線,60 季線 )
