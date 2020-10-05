import pymysql

connection = pymysql.connect(
    host = 'instacart-db.cbujeonilgtq.us-east-2.rds.amazonaws.com',
    port = 3306,
    user = 'group3',
    password = 'group3pw!',
    db = 'cs527_instacart'
)

def executeQuery(query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result