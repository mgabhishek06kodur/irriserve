from flask import Flask
from flask_restful import Resource, Api
#from flask.ext.mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
#import grovepi 
import Adafruit_DHT
sensor = Adafruit_DHT.DHT11

# Example using a Raspberry Pi with DHT sensor
# connected to GPIO23.
pin = 18

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://infobegi_a:infobegi_@localhost:3306/infobegi_IrriServe'
api = Api(app)
#sensor = 7
#app.config['MYSQL_HOST'] = 'sql3.infobeginner.tech'
#app.config['MYSQL_USER'] = 'infobegi_a'
#app.config['MYSQL_PASSWORD'] = 'infobegi_'
#app.config['MYSQL_DB'] = 'infobegi_IrriServe'
#mysql = MySQL(app)

@app.route('/')
def show_all():
   return render_template('http://infobeginner.tech/soil.html', user = user.query.all() )

db = SQLAlchemy(app)
class temprature(db.Model):
   id = db.Column('id', db.Integer, primary_key = False)
   #temp = db.Column('user',db.Integer(100))
   #city = db.Column(db.String(50))  
   #addr = db.Column(db.String(200))
   #pin = db.Column(db.String(10))
   #def __init__(self, temp):
        #self.temp = user
    #self.city = city
    #self.addr = addr
    #self.pin = pin

class TempHum(Resource):
    def get(self):
         print("Test")
         #[temp,hum] = grovepi.dht(sensor,0)
         humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
         print(humidity, temperature)
         #return('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
         cur = mysql.connection.cursor()
         cur.execute('''SELECT user FROM user WHERE id = 1''')
         rv = cur.fetchall()
         if humidity is not None and temperature is not None:
            return('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
         else:
            return('Failed to get reading. Try again!')
          #{'temperature' : temp,
               #  'humidity' : hum }
         return str(rv)
api.add_resource(TempHum, '/')
#api.add_resource(temprature, '/')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5006, debug=True)
    app.run(debug=True)






#from flask import Flask 
#app = Flask(__name__)
#@app.route('/')
#def index():
#if __name__ == '__main__':

