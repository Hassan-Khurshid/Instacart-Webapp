import pymysql
import psycopg2

mysql_insta = pymysql.connect(
    host = 'instacart-db.cbujeonilgtq.us-east-2.rds.amazonaws.com',
    port = 3306,
    user = 'group3',
    password = 'group3pw!',
    db = 'cs527_instacart'
)

mysql_abc = pymysql.connect(
    host = 'instacart-db.cbujeonilgtq.us-east-2.rds.amazonaws.com',
    port = 3306,
    user = 'group3',
    password = 'group3pw!',
    db = 'abc_retail'
)

redshift = psycopg2.connect(
    user = "group3",
    password = "group3PW!",
    host = "redshift-cluster-1.cw5prwl0hut7.us-east-2.redshift.amazonaws.com",
    port = '5439',
    database = "instacart_red"
)

"""
Executes query requested by user. 
Creates a VIEW and issues a SELECT * query to return results for user
"""

def executeQuery(query, service_type, db_type):
    if service_type == 'mysql':
        if db_type =='abc':
            cursor = mysql_abc.cursor()
        else:
            cursor = mysql_insta.cursor()
    else:
        cursor = redshift.cursor()

    ## create internal view ##
    cursor.execute('CREATE VIEW CURVIEW AS '+ query)
    cursor.execute('SELECT * FROM CURVIEW')
    result = cursor.fetchall()
    return result


"""
 Drops view. Issued after every user request.
"""
def dropView( service_type, db_type):
    if service_type == 'mysql':
        if db_type =='abc':
            cursor = mysql_abc.cursor()
        else:
            cursor = mysql_insta.cursor()
    else:
        cursor = redshift.cursor()
    cursor.execute('DROP VIEW CURVIEW')
    return ""

"""
Obtains column names from view created in executeQuery().
"""
def getColumnsFromView(service_type, db_type):
    if service_type == 'mysql':
        if db_type =='abc':
            cursor = mysql_abc.cursor()
        else:
            cursor = mysql_insta.cursor()
    else:
        cursor = redshift.cursor()
    cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'CURVIEW'  ORDER BY ordinal_position ASC;")
    return cursor.fetchall()
   
    