from flask import Flask, send_file
from flask_cors import CORS
from MarsWeatherPkg import SQLiteConnection, APIHandler, DataModeling

app = Flask(__name__)

CORS(app)

api = APIHandler.APIHandler()
dbConnection = SQLiteConnection()
model = DataModeling.DataModel(dbConnection)

@app.route('/api/getGraph/')
def index():
    img_io = model.generateHistoricalGraphs()
    return send_file(img_io, mimetype='image/png')


@app.route('/api/createDB/')
def create_Database():
    status = dbConnection.connect()
    dbConnection.createDB()
    dbConnection.disconnect()
    return {'status': status}

@app.route('/api/uploadNew/')
def upload_New():
    status = api.connect()
    data = api.getJSON()

    dbConnection.connect()
    dbConnection.insert(data)
    dbConnection.disconnect()

    return {'status': status}

@app.route('/api/summary/')
def get_Summary():
    status = api.connect()
    data = api.getJSON()
    return {'status' : status,
            'data' : model.getDailySummary(data)}

if __name__ == '__main__':
    app.run(debug=True)