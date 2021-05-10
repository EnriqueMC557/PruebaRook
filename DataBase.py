import pymysql

class RookDataBase:
	def __init__(self):
		self.connection = pymysql.connect(
			host = 'localhost',
			user = 'emc',
			password = '12345678',
			db = 'RookDB'
			)
		self.cursor = self.connection.cursor()
	
	def close(self):
		self.connection.close()
	
	def insertTemperature(self, temperature):
		values = (NOW(), 'temperature', temperature)
		sql = """INSERT INTO data (timestamp, variable_name, value)
				 VALUES (?, ?, ?)"""
		self.cursor.execute(sql, values)
		self.connection.commit()

	def insertCPUload(self, load):
		values = (NOW(), 'load', load)
		sql = """INSERT INTO data (timestamp, variable_name, value)
				 VALUES (?, ?, ?)"""
		self.cursor.execute(sql, values)
		self.connection.commit()
		
	def select_all(self):
		sql = 'SELECT * FROM data'
		try:
			self.cursor.execute(sql)
			data = self.cursor.fetchall()
			
			for dato in data:
				print(dato)
				print('----')
				
		except Exception as e:
			raise

db = RookDataBase()
db.select_all()
db.close()
