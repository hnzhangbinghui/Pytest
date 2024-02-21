# coding:utf-8

import cx_Oracle

sel_sql = "SELECT FCODE ,fname FROM T_BASE_USER tbu WHERE rownum <=10"
sel_slq2="SELECT FCODE ,'Ysstech123!@#' AS 默认密码  FROM T_BASE_USER tbu WHERE rownum <=10"
sel_slq3="SELECT FCODE ,'Ysstech123!@#' AS 默认密码  FROM T_BASE_USER tbu"
data = "ACPBOOT/ACPBOOT@192.168.99.105:1521/ORCL"


# 以列表形式返回数据库查询结果的所有数据；
def link_oracle(sql, peizhi=data):
    # 链接数据库
    conn = cx_Oracle.connect(peizhi)
    # 执行sql
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    # 输出查询结果
    result = []
    for row in rows:
        result.append(row)
    # 关闭链接
    cursor.close()
    conn.close()
    return list(result)


print(link_oracle(sel_slq3))


# 以列表形式返回查询结果的某一个值，是以列表的形式返回；
def link_oracle2(sql, peizhi=data):
    # 链接数据库
    conn = cx_Oracle.connect(peizhi)
    # 执行sql
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    # 输出查询结果
    fcode_list = []
    fname_list=[]
    for row in rows:
        fcode_list.append(row[0])
        fname_list.append(row[1])
    # 关闭链接
    cursor.close()
    conn.close()
    return list(fcode_list)




