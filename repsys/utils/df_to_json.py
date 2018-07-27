# encoding:utf-8

from repsys.utils import access_impala as ac


def df_to_json(df):
    df_m = df.to_json(orient='records')
    return df_m
#
# s='''
# select
# substring(a.auditing_date,1,10) date_c
# ,sum(a.amount) amount
# ,count(1) cnt
# from edw.cmn_listing a
# where
# a.auditing_date>=to_date(date_add(now(),-7))
# group by date_c
# order by date_c
# '''
#
# data = ac.impala_query(s)
#
# data_m=df_to_json(data[0])
# print data_m
