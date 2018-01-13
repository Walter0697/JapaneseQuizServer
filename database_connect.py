#!/usr/bin/python
#IMPORT LIBRARY FOR CONNECTING TO MYSQL
import MySQLdb
#IMPORT TIME TO CHECK THE TIME
import time
#SET UP CONSTANT FOR MYSQL INFORMATION
from DBconfig import DBHOST, DBUSER, DBPASSWORD, DBNAME

#HANDLER FOR THE DATABASE
class DatabaseHandler:
    connection = None

    def connect(self):
        self.connection = MySQLdb.connect(DBHOST, DBUSER, DBPASSWORD, DBNAME, charset="utf8", use_unicode=True)
        print time.asctime(), "MySQL connected\n"

    def getDictionary(self, sql):
        try:
            cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute(sql)
        except (AttributeError, MySQLdb.OperationalError):
            self.connect()
            cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute(sql)
        return cursor

    def getOutput(self, sql):
        cursor = self.getDictionary(sql)
        numrows = cursor.rowcount
        #fetching output to an array
        fetchoutput = []
        for x in range(0, numrows):
            fetchoutput.append(cursor.fetchone())
        return fetchoutput

    def getArray(self, sql):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
        except (AttributeError, MySQLdb.OperationalError):
            self.connect()
            cursor.self.connection.cursor()
            cursor.execute(sql)
        return cursor

    def getOutputArray(self, sql):
        cursor = self.getArray(sql)
        numrows = cursor.rowcount
        #fetching output to an array
        fetchoutput = []
        for x in range(0, numrows):
            fetchoutput.append(cursor.fetchone()[0])
        return fetchoutput

    def disconnect(self):
        self.connection.close()
        print time.asctime(), "MySQL disconnected"
