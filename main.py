import mysql.connector

connect = mysql.connector.connect(host='db', database='test', user='test', password='test')
cur = connect.cursor(buffered=True)
# If you want to get it in dictionary type, write dictionary=True as an argument
# example cur = connect.cursor(dictionary=True)


cur.execute('SELECT * FROM users')
print(cur.fetchone())
print(cur.fetchmany(2))
print(cur.fetchall())

try:
    cur.execute("INSERT INTO users (username,password,email) VALUES ('gorira','gorira','gorira@examle.com')")
    connect.commit()
except mysql.connector.errors.IntegrityError:
    print("Already inserted.")
