#-*- encoding: utf-8 -*-

import pyodbc

otherDbaseDict = {}

connOtherDbase = pyodbc.connect("Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\\work\\2013-12.accdb;")
otherDbaseTables = connOtherDbase.cursor().tables()

counter = 0

for tblOther in otherDbaseTables:
    if tblOther.table_name.startswith("tbl"): #ignores MS sys tables
        nameOther = tblOther.table_name
        cursor = connOtherDbase.cursor()
        selectSQL = 'SELECT * FROM {}'.format(nameOther) #generate SQL select syntax
        cursor.execute(selectSQL)
        rows = cursor.fetchall()
        for row in rows:
            counter = counter + 1 #counter digit used to create unique key, since table names repeat
            otherDbaseDict.update({nameOther+str(counter):row})

connMainDbase = pyodbc.connect(("Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
                                "DBQ=C:\\main.accdb;"))
mainDbaseTables = connMainDbase.cursor().tables()
