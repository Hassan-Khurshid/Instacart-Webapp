import pymysql
import psycopg2



mysql = pymysql.connect(
    host = 'instacart-db.cbujeonilgtq.us-east-2.rds.amazonaws.com',
    port = 3306,
    user = 'group3',
    password = 'group3pw!',
    db = 'cs527_instacart'
)



redshift = psycopg2.connect(
    user = "group3",
    password = "group3PW!",
    host = "redshift-cluster-1.cw5prwl0hut7.us-east-2.redshift.amazonaws.com",
    port = '5439',
    database = "instacart_red"
)

def executeQuery(query, database_type):
    if database_type == 'mysql':
        cursor = mysql.cursor()
    else:
        cursor = redshift.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result