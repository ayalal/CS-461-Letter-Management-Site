from __future__ import print_function
from __future__ import unicode_literals
import mysql.connector
from mysql.connector import errorcode
import numpy  as np
import pandas as pd
import string
import csv
import json
import sys

DB_NAME = 'testing'

#set tables
TABLES = []

TABLES.append("CREATE TABLE STUDENT(sid INT NOT NULL AUTO_INCREMENT, sname VARCHAR(255) NOT NULL, spwd VARCHAR(255) NOT NULL, PRIMARY KEY (sid))")
TABLES.append("CREATE TABLE TEACHER(tid INT NOT NULL AUTO_INCREMENT, tname VARCHAR(255) NOT NULL, tpwd VARCHAR(255) NOT NULL, PRIMARY KEY (tid))")
TABLES.append("CREATE TABLE FILEINFO(id INT NOT NULL AUTO_INCREMENT, format VARCHAR(255) NOT NULL, position VARCHAR(255) NOT NULL, uid INT NOT NULL, PRIMARY KEY (id))")
TABLES.append("CREATE TABLE CONTENT(id INT NOT NULL AUTO_INCREMENT,sFileId INT, sid INT NOT NULL, req VARCHAR(255), tFileId INT, tid INT NOT NULL, feedback VARCHAR(5000), PRIMARY KEY (id))")

#method to create database
def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="sunlight155" )

mycursor = mydb.cursor(buffered=True)

try:
      mydb.database = DB_NAME
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
          create_database(mycursor)
          mydb.database = DB_NAME
    else:
          print(err)
          exit(1)


print("CONTENT")
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

sql = "DROP TABLE IF EXISTS content"
mycursor.execute(sql)

sql = "DROP TABLE IF EXISTS student"
mycursor.execute(sql)

sql = "DROP TABLE IF EXISTS teacher"
mycursor.execute(sql)

sql = "DROP TABLE IF EXISTS fileinfo"
mycursor.execute(sql)



for x in range(len(TABLES)):
    sql = TABLES[x]
    mycursor.execute(sql)

print("CONTENT")
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

print("INsert Testing - CONTENT")
sql = "INSERT IGNORE INTO content(sFileId, sid, req, tFileId, tid, feedback) VALUES (%s, %s, %s, %s, %s, %s)"
val = ["111", "111", "None", "211", "211", "None"]
mycursor.execute(sql, val)
sql = "INSERT IGNORE INTO content(sFileId, sid, req, tFileId, tid, feedback) VALUES (%s, %s, %s, %s, %s, %s)"
val = ["222", "222", "None", "222", "222", "None"]
mycursor.execute(sql, val)


mycursor.execute("SELECT * FROM content")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)


print("INsert Testing - STUDENT")
sql = "INSERT IGNORE INTO student(sname, spwd) VALUES (%s, %s)"
val = ["Divid", "123111"]
mycursor.execute(sql, val)

sql = "INSERT IGNORE INTO student(sname, spwd) VALUES (%s, %s)"
val = ["TOM", "123222"]
mycursor.execute(sql, val)

mycursor.execute("SELECT * FROM student")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

print("INsert Testing - TEACHER")
sql = "INSERT IGNORE INTO teacher(Tname, Tpwd) VALUES (%s, %s)"
val = ["Knight", "111111"]
mycursor.execute(sql, val)
sql = "INSERT IGNORE INTO teacher(Tname, Tpwd) VALUES (%s, %s)"
val = ["Mike", "222222"]
mycursor.execute(sql, val)

mycursor.execute("SELECT * FROM teacher")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

print("INsert Testing - FILEINFO")
sql = "INSERT IGNORE INTO fileinfo(format, position, uid) VALUES (%s, %s, %s)"
val = ["pdf", "c:\\", "1"]
mycursor.execute(sql, val)
sql = "INSERT IGNORE INTO fileinfo(format, position, uid) VALUES (%s, %s, %s)"
val = ["text", "c:\\", "2"]
mycursor.execute(sql, val)

mycursor.execute("SELECT * FROM fileinfo")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
