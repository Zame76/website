import sqlite3

path = "static/db/website.db"

def createTables():
    conn = sqlite3.connect(path)
    sql = conn.cursor()
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
    conn.commit()
    conn.close()

def insertWeather(parameters):
    conn = sqlite3.connect(path)
    sql = conn.cursor()
    clause = "insert into Weather "
    clause += "(LoggedTime, MeasuredTime, Temperature, WindSpeed, WindDirection, Moisture, Rain, RainDescFi, RainDescEn) "
    clause += "values (?, ?, ?, ?, ?, ?, ?, ?, ?)"
    sql.execute(clause, parameters)
    conn.commit()
    conn.close()

def getLatestWeather():
    conn = sqlite3.connect(path)
    sql = conn.cursor()
    clause = "select LoggedTime, MeasuredTime, Temperature, WindSpeed, WindDirection, Moisture, Rain, RainDescFi, RainDescEn "
    clause += "from Weather "
    clause += "where LoggedTime = (select max(LoggedTime) from Weather)"
    value = sql.execute(clause).fetchone()
    conn.close
    return value
