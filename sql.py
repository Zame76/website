import sqlite3

path = "static/db/website.db"

def createTables():
    conn = sqlite3.connect(path)
    sql = conn.cursor()
    clause = "create table if not exists Weather ("                 
    clause += "WID integer primary key autoincrement, "     
    clause += "Time datetime not null, "
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
    clause += "(Time, Temperature, WindSpeed, WindDirection, Moisture, Rain, RainDescFi, RainDescEn) "
    clause += "values (?, ?, ?, ?, ?, ?, ?, ?)"
    sql.execute(clause, parameters)
    conn.commit()
    conn.close()

def getLatestWeather():
    conn = sqlite3.connect(path)
    sql = conn.cursor()
    clause = "select Time, Temperature, WindSpeed, WindDirection, Moisture, Rain, RainDescFi, RainDescEn from Weather where Time = (select max(Time) from Weather)"
    value = sql.execute(clause).fetchone()
    conn.close
    return value
