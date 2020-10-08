from flask import *
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import exc
#from flask_migrate import Migrate 
#from config import DevelopmentConfig
import db_functions as db_functions
import time


app = Flask(__name__)

# # Database setup #
# db = SQLAlchemy(app=app)



# # mysql
# db_username = 'group3'
# db_password = 'group3pw!'
# db_host = 'instacart-db.cbujeonilgtq.us-east-2.rds.amazonaws.com'
# db_db = 'cs527_instacart'

# # redshift
# db_rs_username = 'group3'
# db_rs_password = 'group3PW!'
# db_rs_host = 'redshift-cluster-1.cw5prwl0hut7.us-east-2.redshift.amazonaws.com'
# db_rs_db = 'instacart_red'


# SQLALCHEMY_BINDS = {
#     'mysql':        'mysql+pymysql://{}:{}@{}/{}'.format(db_username, db_password, db_host, db_db),
#     'appmeta':      'jdbc:redshift://redshift-cluster-1.cw5prwl0hut7.us-east-2.redshift.amazonaws.com:5439/instacart_red'
# }
# db.create_all()


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/queryresults", methods=['GET','POST'])
def runQuery():
    if request.method == 'POST':
        
        query = request.form['query']
        print('QUERY: ', query)

        if query == "":
            return render_template('index.html')

        service_type = request.form['serviceop']
        print('SERVICE TYPE: ',service_type)

        database_type = request.form['dbop']
        print('DATABASE TYPE: ', database_type)

        start_time = time.time()
        result = db_functions.executeQuery(query, service_type, database_type)
        end_time = time.time()
        return render_template('index.html', query=result, service_type=service_type, db_type=database_type, time=(end_time-start_time))



if __name__ == '__main__':
    app.run(debug=True)

