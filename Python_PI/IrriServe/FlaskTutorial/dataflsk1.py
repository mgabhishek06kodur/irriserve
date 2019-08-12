from flsk import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'infobegi_'
app.config['MYSQL_PASSWORD'] = 'infobegi_a'
app.config['MYSQL_DB'] = 'infobeginner_Irriserve'

mysql = MySQL(app)

@app.route('/')
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    fetchdata = cur.fetchall()
    cur.close()
    return render_template('home.html', data = fetchdata)


if __name__ == "__main__":
    app.run(debug=True)
    
