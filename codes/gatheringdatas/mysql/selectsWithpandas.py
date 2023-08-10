# mysql connect package
# pip --> conda
import pymysql

# connect Mysql (1. connect 에러 나있을 경우 오타확인)
# ip, port, username, password, database name
ip = 'localhost'   # 127.0.0.1 / db_cars없을 경우 192.168.0.30 
port = '3306'
username ='yojulab'
password = '!yojulab*'
database ='db_cars'

# editor - statement 
connect = pymysql.connect(host=ip, user=username, passwd=password, database=database)

# make select statement(2. workbench에서 쿼리 오류 없는지 확인 )
sql_query = 'select * from car_infors;' 

# execute select query
import pandas 

# reture resultset and then display (df에 자료가 담긴다.)
df = pandas.read_sql(sql=sql_query, con=connect)

# close
connect.close()

pass

# F5 -> debug에서 df 확인/ debug console에서 print(df) 입력하면 값 확인 