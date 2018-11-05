import  tushare as ts
from pyecharts import Bar


ts.set_token('5e812a941fcf85624b893ed6e099f93e932bb69b2f1b69fb7644e645')

pro=ts.pro_api()

# df=pro.trade_cal(exchange='', start_date='20180901', end_date='20181001', fields='cal_date,is_open,pretrade_date', is_open='0')
#
# print(df)

# data1=pro.stock_basic(exchange='',list_status='L',fields='ts_code,symbol,name')
# print(data1)
# print(data1.columns)
#
#
# data2=pro.daily(ts_code='601211.SH',start_date='20170101',end_date='20181103')
# print(data2)


bar=Bar('图表')
bar.add("a",['a','b','c','d'],[1,2,3,4])
bar.render()