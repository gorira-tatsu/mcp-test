import mysql.connector

connect = mysql.connector.connect(host='db', database='test', user='test', password='test')
cur = connect.cursor()


cur.execute(
    ''
)

