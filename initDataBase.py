import pymysql

def initDataBase(nameDB):
	connection =  pymysql.connect(
			host = 'localhost',
			user = 'emc',
			password = '12345678',
			)
	cursor = connection.cursor()
	cursor.execute(f"CREATE DATABASE {nameDB}")
	connection.close()

def initTable(nameDB, nameTable):
	connection =  pymysql.connect(
			host = 'localhost',
			user = 'emc',
			password = '12345678',
			db = nameDB
			)
	cursor = connection.cursor()
	sql = f"""CREATE TABLE {nameTable} (
			 id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
			 timestamp TIMESTAMP NOT NULL,
			 variable_name TEXT NOT NULL,
			 value FLOAT NOT NULL
			 )AUTO_INCREMENT = 1"""
	cursor.execute(sql)
	connection.close()	

if __name__ == '__main__':
	initDataBase('RookBDD')
	initTable('RookBDD', 'data')
