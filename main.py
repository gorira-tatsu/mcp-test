import mysql.connector

connect = mysql.connector.connect(host='db', database='test', user='test', password='test')
cur = connect.cursor(buffered=True)
# If you want to get it in dictionary type, write dictionary=True as an argument
# example cur = connect.cursor(dictionary=True)

# If test data is not inserted, insert it.
try:
    cur.execute(
        'select * from users'
    )
    if cur.fetchone() is None:
        cur.execute("INSERT INTO users (username, password, email) values ('gorira', 'gorira', 'gorira@example.com')")
        cur.execute("INSERT INTO users (username, password, email) values ('panda', 'panda', 'panda@example.com')")
        cur.execute("INSERT INTO users (username, password, email) values ('rabbit', 'rabbit', 'rabbit@example.com')")
        cur.execute("INSERT INTO users (username, password, email) values ('dog', 'dog', 'dog@example.com')")
        cur.execute("INSERT INTO users (username, password, email) values ('cat', 'cat', 'cat@example.com')")
        connect.commit()
except:
    cur.rollback()

# Sample code starts here.
try:
    cur.execute('SELECT * FROM users')
    print(cur.fetchone())
    print(cur.fetchmany(2))
    print(cur.fetchall())
except:
    pass

try:
    cur.execute("INSERT INTO users (username,password,email) VALUES ('gorira','gorira','gorira@examle.com')")
    connect.commit()
except mysql.connector.errors.IntegrityError:
    print("すでに挿入されています")
