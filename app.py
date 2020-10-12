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
        print(service_type)
        print(database_type)

        # capture start time #
        start_time = time.time()

        # execute user query #
        result = db_functions.executeQuery(query, service_type, database_type)
        # if result == 'Error!':
        #     return render_template('index.html', query=result, service_type=service_type, db_type=database_type)

        # fetch columns names from internal view #
        col_names = db_functions.getColumnsFromView(service_type, database_type)
        # if col_names == 'Error!':
        #     return render_template('index.html', query=col_names, service_type=service_type, db_type=database_type)
    
        # drop view #
        dropRes = db_functions.dropView(service_type, database_type)
        # if dropRes == 'Error!':
        #     return render_template('index.html', query=dropRes, service_type=service_type, db_type=database_type)
       
        # capture end time #
        end_time = time.time()

        # render result #
        return render_template('index.html', 
                                query=result, 
                                col_names=col_names, 
                                service_type=service_type, 
                                db_type=database_type, 
                                time=(end_time-start_time))



if __name__ == '__main__':
    app.run(debug=True)

