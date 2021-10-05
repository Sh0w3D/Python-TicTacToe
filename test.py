import pymysql



db = pymysql.connect(host="localhost", user="root", password="", db="sistema")

cursor = db.cursor()

try:
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    for row in data:
        id = row[0]
        user = row[1]
        email = row[2]
        print("Gracze ID: {0}, nick: {1}, email: {2}". format(id, user, email))
    db.commit()

except pymysql.Error as e:
    print("Error: %d: %s" %(e.args[0], e.args[1]))

db.close()