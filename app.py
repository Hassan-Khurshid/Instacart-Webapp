from flask import *
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import exc
from flask_migrate import Migrate 
#from config import DevelopmentConfig
import db_functions as db_functions




app = Flask(__name__)


# Database setup #
db = SQLAlchemy(app=app)
migrate = Migrate(app=app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/queryresults", methods=['GET','POST'])
def runQuery():
    if request.method == 'POST':
        
        query = request.form['query']
        print(query)

        database_type = request.form['dboption']
        print(database_type)


        result = db_functions.executeQuery(query)

        return render_template('queryresults.html')



if __name__ == '__main__':
    app.run(debug=True)

