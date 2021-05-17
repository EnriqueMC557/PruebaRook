# -*- coding: utf-8 -*-
import pymysql
import psutil
import time
import datetime
import requests

class RookDataBase:
	def __init__(self):
		# Inicia conexion con BDD
		self.connection = pymysql.connect(
			host = 'localhost',
			user = 'emc',
			password = '12345678',
			db = 'RookBDD'
			)
		self.cursor = self.connection.cursor()
		print('Conexion exitosa')

	def close(self):
		# Termina conexion con BDD
		self.connection.close()
		print('Conexion terminada')

	def insertTemperature(self):
		# Inserta temperatura y timestamp en BDD
		self.localTime()
		#self.JapanTime() # Descomentar para utilizar tiempo de Japon
		self.temperature()
		sql = f"""INSERT INTO data (timestamp, variable_name, value)
			  VALUES ('{self.time}', 'temperature', {self.temp})"""
		self.cursor.execute(sql)
		self.connection.commit()

	def insertCPUload(self):
		# Inserta carga de CPU y timestamp en BDD
		self.localTime()
		#self.JapanTime() # Descomentar para utilizar tiempo de Japon
		self.load()
		sql = f"""INSERT INTO data (timestamp, variable_name, value)
			  VALUES ('{self.time}', 'load', {self.loadCPU})"""
		self.cursor.execute(sql)
		self.connection.commit()

	def select_all(self):
		# Consulta en BDD los valores de temperatura y carga de CPU
		self.localTime()
		#self.JapanTime() # Descomentar para utilizar tiempo de Japon

		sql_1 = f"""SELECT value FROM data WHERE
				variable_name = 'temperature' AND
				timestamp >= DATE_SUB('{self.time}',INTERVAL 8 HOUR)"""
		sql_2 = f"""SELECT value FROM data WHERE
				variable_name = 'load' AND
				timestamp >= DATE_SUB('{self.time}',INTERVAL 8 HOUR)"""
		sql_3 = f"""SELECT timestamp FROM data WHERE
				variable_name = 'temperature' AND
				timestamp >= DATE_SUB('{self.time}',INTERVAL 8 HOUR)"""

		self.cursor.execute(sql_1)
		self.temperatureValues = self.cursor.fetchall()

		self.cursor.execute(sql_2)
		self.loadValues = self.cursor.fetchall()

		self.cursor.execute(sql_3)
		self.timeValues = self.cursor.fetchall()
		self.timeValues = [time[0] for time in self.timeValues]

	def JapanTime(self):
		# Consulta hora en Japon utilizando World Time API
		response = requests.get('http://worldtimeapi.org/api/timezone/Asia/Tokyo')
		time = response.json()['datetime']
		time = datetime.datetime.fromisoformat(time).strftime('%Y-%m-%d %H:%M:%S')
		self.time = time

	def localTime(self):
		# Consulta hora del sistema
		now = time.time()
		now = datetime.datetime.fromtimestamp(now).strftime('%Y-%m-%d %H:%M:%S')
		self.time = now

	def temperature(self):
		# Consulta temperatura del sistema
		temperatureFile = open('/sys/class/thermal/thermal_zone0/temp')
		temperature = float(temperatureFile.read())
		temperatureFile.close()
		self.temp = temperature/1000

	def load(self):
		# Consulta carga de CPU
		load = psutil.cpu_percent()
		self.loadCPU = load

if __name__ == '__main__':
	db = RookDataBase()
	db.insertTemperature()
	db.insertCPUload()
	db.close()
