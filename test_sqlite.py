import sqlite3 as lite
from sqlalchemy import create_engine

import pandas as pd
import datetime
from datetime import timedelta

'''select consecutive rows'''

ids = [i+1 for i in range(9)]
# print(ids)

numbers = [11, 108, 151, 97, 144, 1450, 198, 187, 134]
dt = datetime.datetime.strptime("2017-01-01", '%Y-%m-%d')
dts = [dt + timedelta(days=i) for i in range(9)]
# dts = [datetime.datetime.strftime(dt, '%Y-%m-%d') for dt in dts]  # 轉成字串
product = pd.DataFrame(
    {
        "ID": ids,
        "Date": dts,
        "number": numbers
    },
    columns=["ID", "Date", "number"])  # 組合成 DataFrame

print(product)

# write to sqlite
try:
    con = lite.connect("db/sample.db")
    product.to_sql('product', con=con)
    con.commit()


except Exception as e:
    print(e)
finally:
    con.close()

#
try:
    con = lite.connect("db/sample.db")
    sql = "SELECT * FROM product where number >=100"
    result = con.execute(sql)
    print(result)
finally:
    con.close()
