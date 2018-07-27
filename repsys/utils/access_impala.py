# encoding:utf-8
# 环境：1.windows，win7，64位企业版
#          2.ananconda版本（因为ananconda集成了python的编程环境方便使用）：Anaconda2-5.0.1-Windows-x86_64（内置python2.7）
# 步骤
#			1.安装Anaconda
#			2.进入anaconda prompt shell
#			3.输出conda list查看默认包和版本
# ***** 安装包的时候用pip命令，不要用conda命令
#			4.安装impyla0.14.0版本命令（如果内置的版本不兼容则需要先卸载：conda remove impyla）
#	 命令:pip install impyla==0.14.0
#			5.安装thrift0.9.3版本（如果内置的版本不兼容则需要先卸载：conda remove thrift,此命令会连带impyla一起卸载掉，需要从第一步重新开始）
#   命令:pip install thrift==0.9.3
#			6.在运行中可能会遇到缺少thrift_sasl包的问题，用以下命令安装：
#   pip install thrift_sasl
#   如果在anaconda上找不到这个包，则可改用：pip install --channel https://conda.anaconda.org/blaze thrift_sasl

# 注：
#   1.thrift_sasl如果安装不了：
#   a.windos系统：将文件夹thrift_sasl放到 \Anaconda2\Lib\site-packages下面；
#   b.Linux系统：将文件夹thrift_sasl放到  /anaconda2/lib/python2.7/site-packages/下面；

#   2. 如果报no module puresasl.client ,则需要安装pure-sasl
#   pip install pure-sasl


# 2.1 连接impala
# 下面是封装好的连接代码,将文件放到python工作目录，每次import run()这个方法就行。
from __future__ import print_function
from impala.dbapi import connect
from impala.util import as_pandas
from time import time


def impala_query(username, pwd, sql):
    # 建立连接
    try:
        # conn = connect(host='10.2.8.95', auth_mechanism='PLAIN', port=21050, user='yangyuan', password='yangyuan')
        conn = connect(host='10.2.8.95', auth_mechanism='PLAIN', port=21050, user=username, password=pwd)
    except EnvironmentError:
        print(u"connect failure")
    cursor = conn.cursor()
    total_time = []  # 计时
    result = []

    # 处理sql语句
    if ';' in sql:
        sql_list = sql.split(';')
        for i in range(len(sql_list)):
            sql_list[i] = sql_list[i].strip()  # rstrip()删除末尾空格 ，strip()删除行首和行尾空格符
        while '' in sql_list:
            sql_list.remove('')  # 删除空查询
    else:
        sql_list = [sql.rstrip()]

    print(u"----------------------------【Stats Information】----------------------------")
    # 执行查询   
    print(u"Total sql_count #%s" % len(sql_list))
    for i in range(len(sql_list)):
        print(u"Runing sql #%s,==》" % str(i + 1), end='')
        time_a = time()
        cursor.execute(sql_list[i])
        time_b = time()
        print(u"execute_time[%0.4fs]," % (time_b - time_a), end='')
        if cursor.description == None:
            result.append("null")
        else:
            result.append(as_pandas(cursor))
        time_c = time()
        print(u"return_result_time[%0.4fs],|sql #%s has done|" % (time_c - time_b, str(i + 1)))
        total_time.append(time_c - time_a)
    print(u"Total time [%0.4fs]." % sum(total_time))
    print(u"---------------------【Result：Return a DataFrame List】---------------------")
    cursor.close()
    conn.close()
    return result


if __name__ == '__main__':
    # 当前模块才执行以下代码
    sql = '''--asdfas 
    select now() as 我;;; '''
    df_list = impala_query(sql)
    print(df_list[0])
