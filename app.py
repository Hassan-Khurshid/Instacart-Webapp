from flask import *
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import exc
#from flask_migrate import Migrate 
#from config import DevelopmentConfig
import db_functions as db_functions




app = Flask(__name__)


# Database setup #
db = SQLAlchemy(app=app)
#migrate = Migrate(app=app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/queryresults", methods=['GET','POST'])
def runQuery():
    if request.method == 'POST':
        
        query = request.form['query']
        print('QUERY: ', query)

        database_type = request.form['dboption']
        print('DATABASE TYPE: ',database_type)


        result = db_functions.executeQuery(query)
        print('QUERY RESULT: ',result)
        return render_template('index.html', query=result)



if __name__ == '__main__':
    app.run(debug=True)

