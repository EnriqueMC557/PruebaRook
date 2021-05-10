import pymysql
import psutil
import time
from datetime import datetime
		
def timestamp():
	#Revisar formato de timestamp porque marca error de sintaxis
	now = time.time()
	now = datetime.fromtimestamp(now).strftime('%Y-%m-%d %H:%M:%S')
	return now
	
def temperature():
	temperatureFile = open('/sys/class/thermal/thermal_zone0/temp')
	temperature = float(temperatureFile.read())
	temperatureFile.close()
	return temperature/1000
	
def load():
	load = psutil.cpu_percent(interval = 1)
	return load

class RookDataBase:
	def __init__(self):
		self.connection = pymysql.connect(
			host = 'localhost',
			user = 'emc',
			password = '12345678',
			db = 'RookDB'
			)
		self.cursor = self.connection.cursor()
		print('Conexión exitosa')
	
	def close(self):
		self.connection.close()
	
	def insertTemperature(self):
		sql = f"""INSERT INTO data (timestamp, variable_name, value)
				  VALUES (NOW(), 'temperature', {temperature()})"""
		self.cursor.execute(sql)
		self.connection.commit()

	def insertCPUload(self):
		sql = f"""INSERT INTO data (timestamp, variable_name, value)
				  VALUES (NOW(), 'load', {load()})"""
		self.cursor.execute(sql)
		self.connection.commit()
		
	def select_all(self):
		sql = "SELECT * FROM data"
		try:
			self.cursor.execute(sql)
			data = self.cursor.fetchall()
			
			for dato in data:
				print(dato)
				print('----')
				
		except Exception as e:
			raise

db = RookDataBase()
db.insertTemperature()
db.insertCPUload()
db.close()
