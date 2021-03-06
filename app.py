from flask import *
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import exc
#from flask_migrate import Migrate 
#from config import DevelopmentConfig
import db_functions as db_functions
import time


app = Flask(__name__)
application=app
# # Database setup #

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/queryresults", methods=['GET','POST'])
def runQuery():
    if request.method == 'POST':
        
        query = request.form['query']
        if query == "":
            return render_template('index.html')
        service_type = request.form['serviceop']
        database_type = request.form['dbop']

        # capture start time #
        start_time = time.time()

        # execute user query #
        result = db_functions.executeQuery(query, service_type, database_type)
       
        # capture end time #
        end_time = time.time()

        # render result #
        return render_template('index.html', 
                                query=result[1], 
                                col_names=result[0], 
                                service_type=service_type, 
                                db_type=database_type, 
                                time=(end_time-start_time))



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

