#import datetime
import pymysql



db = pymysql.connect(host="localhost", user="root", password="", db="tictactoe")
cursor = db.cursor()
try:
    cursor.execute("SELECT * FROM gameresults")
    data = cursor.fetchall()
    for row in data:
        id = row[0]
        Data = row[1]
        Gracz1 = row[2]
        Gracz2 = row[3]
        Result = row[4]
        print(f"""Game results! GameID: {id}, Time of game: {Data}, Player1: {Gracz1},
            Player2: {Gracz2}, Scrim results (Winner/Time): {Result}""")
    db.commit()

except pymysql.Error as e:
    print("Error: %d: %s" %(e.args[0], e.args[1]))

db.close()

#now = datetime.datetime.now()
#print (now.strftime("%Y-%m-%d %H:%M:%S"))