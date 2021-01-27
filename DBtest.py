import mysql.connector
word = input("Enter a word in English and press Enter: ")
con = mysql.connector.connect(
    user="ardit700_student", 
    password = "ardit700_student", 
    host="108.167.140.122", 
    database = "ardit700_pm1database"
)
cursor = con.cursor()
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()
if results:
    for result in results:
        print(result[1])
else:
    print("We couldn't find any results about that.")


"""
mport psycopg2

# first connect, create cursor object write a aql query commit changes close connection
 
def creat_table():
    connection=psycopg2.connect("dbname='library' user='postgres' password='3452Anj1!' host='localhost' port='5432' ")
    cursor=connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    connection.commit()
    connection.close

def insertData(item,quantity,price):
    connection=psycopg2.connect("lite.db")
    cursor=connection.cursor()
    cursor.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))
    connection.commit()
    connection.close


def view():
    connection=psycopg2.connect("dbname='library' user='postgres' password='3452Anj1!' host='localhost' port='5432' ")
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM store")
    rows=cursor.fetchall()
    connection.close()
    return rows

def delete_row(item):
    connection=psycopg2.connect("dbname='library' user='postgres' password='3452Anj1!' host='localhost' port='5432')
    cursor=connection.cursor()
    cursor.execute("DELETE FROM store WHERE item=?",(item,))
    connection.commit()
    connection.close()

def updateItem(quantity,price,item):
    connection=psycopg2.connect("dbname='library' user='postgres' password='3452Anj1!' host='localhost' port='5432' ")
    cursor=connection.cursor()
    cursor.execute("UPDATE store SET quantity=?,price=? WHERE item=?",(quantity,price,item))
    connection.commit()
    connection.close()

creat_table()

#delete_row("coffee cup")
#insertData("wine glass",10,6)
#insertData("champagne glass",10,12)
#print(view())




"""