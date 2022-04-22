from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'chirag'
app.config['MYSQL_PASSWORD'] = 'chirag2016'
app.config['MYSQL_DB'] = 'test'

@app.route('/', methods = ['GET'])
def hello():
    return "hello" 

@app.route('/users', methods = ['GET'])
def users():
    cur = mysql.connection.cursor()
    cur.execute('''Select * from doctor''')
    rv = cur.fetchall()
    print(rv)
    return "hello user"

@app.route('/form', methods = ['GET', 'POST'])
def get_form():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute('''Select * from doctor''')
        rv = cur.fetchall()
        print(rv)
        return render_template('form.html',data = rv)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5001, debug=True)