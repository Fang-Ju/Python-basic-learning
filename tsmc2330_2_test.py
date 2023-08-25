import pandas as pd
import numpy as np
import datetime

list2 = []
for i in range(2) :
    path = "C:\\Users\\USER\\Desktop\\Python_fangru\\2330\\"
    file = f'STOCK_DAY_2330_2021{i+1:02d}.csv'

    daily_df = pd.read_csv(path + file,
                           header=1,
                           engine='python',
                           thousands=',',
                           # skipfooter = 6,
                           encoding='Big5')
    # print(daily_df.info()) #檢查資料型態

    s_bool = daily_df['日期'].str.contains('\d{3}[-/]\d{2}[-/]\d{2}', regex=True)
    # print(s_bool)
    daily_df = daily_df[s_bool]
    daily_df = daily_df[['日期', '開盤價', '最高價', '最低價', '收盤價', '成交股數']]
    daily_df = daily_df.rename(columns={'日期': 'Date',
                                        '開盤價': 'Open',
                                        '最高價': 'High',
                                        '最低價': 'Low',
                                        '收盤價': 'Close',
                                        '成交股數': 'Volumu'})  # 一維陣列series

    for n, item in enumerate(daily_df['Date']):
        list1 = item.split('/')
        list1[0] = str(int(list1[0]) + 1911)
        str1 = '-'.join(list1)  # '2021-01-15'
        daily_df.iloc[n, 0] = str1

    daily_df['Date'] = pd.to_datetime(daily_df['Date'])  # Date這個欄位變成時間格式

    list2.append(daily_df)

df_2330 = pd.concat(list2, axis=0)
df_2330 = df_2330.reset_index(drop=True)

daily_df = df_2330.set_index('Date')

import mplfinance as mpf

mpf.plot(df_2330, type='candle', mav=(5, 20, 60))