import sqlite3
import config

# Set the path to database file
path = config.database_path + "website.db"

# Create tables to database if they don't exist already
def createTables():
    conn = sqlite3.connect(path)
    sql = conn.cursor()
    # Create Weather table
    clause = "create table if not exists Weather ("                 
    clause += "WID integer primary key autoincrement, "     
    clause += "LoggedTime datetime not null, "
    clause += "MeasuredTime text, "
    clause += "Temperature real, "
    clause += "WindSpeed real, "
    clause += "WindDirection real, "
    clause += "Moisture real, "
    clause += "Rain real, "
    clause += "RainDescFi text, "
    clause += "RainDescEn text)"
    sql.execute(clause)

    # Create Photo table
    clause = "create table if not exists Photo ("
    clause += "PID integer primary key autoincrement, "
    clause += "LoggedTIme datetime not null, "
    clause += "MeasuredTime text, "
    clause += "B64Photo text)"
    sql.execute(clause)    

    # Commit the changes to the database
    conn.commit()
    conn.close()

# Insert weather data to table Weather
def insertWeather(parameters):
    conn = sqlite3.connect(path)
    sql = conn.cursor()
    # Clean up Weather table from old data, here we need to trim LoggedTime to Y-m-s format and delete everything that is not 
    # from today.
    clause = "delete from Weather where date(LoggedTime) < date()"
    sql.execute(clause)
    # Insert data from parameters into the Weather table
    clause = "insert into Weather "
    clause += "(LoggedTime, MeasuredTime, Temperature, WindSpeed, WindDirection, Moisture, Rain, RainDescFi, RainDescEn) "
    clause += "values (?, ?, ?, ?, ?, ?, ?, ?, ?)"
    sql.execute(clause, parameters)
    # Commit the changes to the database
    conn.commit()
    conn.close()

# Insert base64 encoded photo to table Photo
def insertPhoto(parameters):
    conn = sqlite3.connect(path)
    sql = conn.cursor()
    # Clean up Weather table from old data, here we need to trim LoggedTime to Y-m-s format and delete everything that is not 
    # from today.
    clause = "delete from Photo where date(LoggedTime) < date()"
    sql.execute(clause)
    # Insert data from parameters into the Photo table
    clause = "insert into Photo "
    clause += "(LoggedTime, MeasuredTime, B64Photo) "
    clause += "values (?, ? , ?)"
    sql.execute(clause, parameters)
    # Commit the changes to the database
    conn.commit()
    conn.close()

# Get the latest weather data
def getLatestWeather():
    conn = sqlite3.connect(path)
    sql = conn.cursor()
    # Get the latest data from the Weather table
    clause = "select LoggedTime, MeasuredTime, Temperature, WindSpeed, WindDirection, Moisture, Rain, RainDescFi, RainDescEn "
    clause += "from Weather "
    clause += "where LoggedTime = (select max(LoggedTime) from Weather)"
    # Get the one result row that this select grabs from database and return it
    value = sql.execute(clause).fetchone()
    conn.close()
    return value

# Get the latest photo
def getLatestPhoto():
    conn = sqlite3.connect(path)
    sql = conn.cursor()
    # Get the latest data from the Photo table
    clause = "select LoggedTime, MeasuredTime, B64Photo from Photo where LoggedTime = (select max(LoggedTime) from Photo)"
    # Get the one result row that this select grabs from database and return it
    value = sql.execute(clause).fetchone()
    conn.close()
    return value

