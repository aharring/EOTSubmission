# Oct 6th 
# Created venv
# Installed Flask
# Installed mssql via homebrew
# Starting with basic 'Hello World' from inside venv using flask
# Created Practice db on mysql with table greeting, 2 fields, one varchar, one int
# Connect to db, return row with greetingnumber 1
# Bit rough and ready until I find my ground
# Password removed for github - also wondering about whether people usually upload their dbs to github or not

from flask import Flask
from flask_mysqldb import MySQL 

app = Flask(__name__)

#@app.route('/')
#def index():
#    return "Hello World"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'practice'

mysql = MySQL(app)
if mysql:
    print("Connection Successful")
    # Create a connection cursor

    @app.route('/')
    def greeting():
        cursor = mysql.connection.cursor()
        # Executing the query
        cursor.execute('select greeting from greeting where greetingnumber = 1')
# Want to change this to take the number the person puts in - eventually
# Getting the result
        agreeting = cursor.fetchone()
        cursor.close()
        return (str(agreeting))
else:
    print("Connection failed") 

if __name__ == '__main__':
    app.run(debug='True')
