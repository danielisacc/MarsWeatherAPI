from MarsWeather import DBConnection, SQLiteConnection, APIHandler, DataModeling
# Connect to the API and load JSON response into data variable
# api = APIHandler.APIHandler()
# api.connect()
# data = api.getJSON()

# Create DB connection, createDB will create missing tables
dbConnection = SQLiteConnection()

dbConnection.connect()
print(dbConnection.execute("""SELECT * FROM api_keys"""))
# dbConnection.createDB()

# Send JSON API data into the DB
# dbConnection.insert(data)
# model = DataModeling.DataModel(dbConnection)
# model.generateHistoricalGraphs()

# for key, value in model.getDailySummary(data).items():
#     print(f"{key}: {value}")

# # Disconnect from the DB commiting before closing connection.
dbConnection.disconnect()
