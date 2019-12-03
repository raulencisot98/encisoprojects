
from PyQt5 import QtCore, QtGui, QtWidgets


import smbus2
import bme280

import psycopg2

from matplotlib import pyplot as plt

time from import


conn = psycopg2.connect ( ' dbname = Proyecto_Raul_Abraham_DiegoA ' )
puerto =  1
direccion =  0x 76 
bus = smbus2.SMBus (puerto)
parametros_calibracion = bme280.load_calibration_params (bus, direccion)


def  sensarTemperatura ():

	
	datos = bme280.sample (bus, direccion, parametros_calibracion)
	temperatura = datos.temperature
	temperatura =  redonda (temperatura, 3 )
	print ( " Temperatura: "  +  str (temperatura) +  " ºC " )
	cur = conn.cursor ()
	tiempo =  int (time.time ())
	comando =  " insertar en valores de temperatura ( "  +  str (tiempo) +  " , "  +  str (temperatura) +  " ) "
	cur.execute (comando)
	conn.commit ()
	cur.close ()


def  sensarPresion ():
	datos = bme280.sample (bus, direccion, parametros_calibracion)
	presion = datos.pressure
	presionando =  redondo (presionando, 3 )
	print ( " Presion: "  +  str (presion) +  " hPa " )
	cur = conn.cursor ()
	tiempo =  int (time.time ())
	comando =  " insertar en valores de presiones ( "  +  str (tiempo) +  " , "  +  str (presion) +  " ) "
	cur.execute (comando)
	conn.commit ()
	cur.close ()


def  sensarHumedad ():

	datos = bme280.sample (bus, direccion, parametros_calibracion)
	humedad = datos.humedad
	humedad =  redonda (humedad, 3 )
	print ( " Humedad: "  +  str (humedad) +  "  % r H " )
	cur = conn.cursor ()
	tiempo =  int (time.time ())
	comando =  " insertar en valores de humedades ( "  +  str (tiempo) +  " , "  +  str (humedad) +  " ) "
	cur.execute (comando)
	conn.commit ()
	cur.close ()


def  medirTodo ():

	sensarTemperatura ()
	sensarHumedad ()
	sensarPresion ()
	imprimir ( "  " )
	

def  mostrarTemperatura ():

	print ( " Mostrando temperatura ... " )
	cur = conn.cursor ()
        cur.execute ( ' select * from temperaturas ' )
	datos = cur.fetchall ()
	tiempo = []
	temperatura = []
	para dato en datos:
		tiempo.append (dato [ 0 ])
		temperatura.append (dato [ 1 ])

	plt.plot (tiempo, temperatura)

	plt.show ()


def  mostrarPresion ():

	print ( " Mostrando presion ... " )
	cur = conn.cursor ()
	cur.execute ( ' select * from presiones ' )

	datos = cur.fetchall ()
        tiempo = []
	presionando = []
	para dato en datos:
		tiempo.append (dato [ 0 ])
		presion.append (dato [ 1 ])

	plt.plot (tiempo, presionar)
	plt.show ()

def  mostrarHumedad ():
	print ( " Mostrando humedad ... " )
	cur = conn.cursor ()
	cur.execute ( ' select * from humedades ' )
	datos = cur.fetchall ()
	tiempo = []
	humedad = []
	para dato en datos:
		tiempo.append (dato [ 0 ])
		humedad.append (dato [ 1 ])

	plt.plot (tiempo, humedad)
	plt.show ()

class  Ui_MainWindow ( objeto ):
	def  setupUi ( self , MainWindow ):
		MainWindow.setObjectName ( " MainWindow " )
		MainWindow.resize ( 882 , 702 )

		self .centralwidget = QtWidgets.QWidget (MainWindow)
		self .centralwidget.setObjectName ( " centralwidget " )

		self .botonTemperatura = QtWidgets.QPushButton ( self .centralwidget)
		self .botonTemperatura.setGeometry (QtCore.QRect ( 60 , 90 , 191 , 91 ))
		self .botonTemperatura.setObjectName ( " botonTemperatura " )

		self .botonTemperatura.clicked.connect (sensarTemperatura)


		self .botonPresion = QtWidgets.QPushButton ( self .centralwidget)
		self .botonPresion.setGeometry (QtCore.QRect ( 570 , 90 , 191 , 91 ))
		self .botonPresion.setObjectName ( " botonPresion " )

		self .botonPresion.clicked.connect (sensarPresion)

		self .botonHumedad = QtWidgets.QPushButton ( self .centralwidget)
		self .botonHumedad.setGeometry (QtCore.QRect ( 310 , 90 , 191 , 91 ))
		self .botonHumedad.setObjectName ( " botonHumedad " )

		self .botonHumedad.clicked.connect (sensarHumedad)

		self .botonVerTemperatura = QtWidgets.QPushButton ( self .centralwidget)
		self .botonVerTemperatura.setGeometry (QtCore.QRect ( 60 , 240 , 191 , 81 ))
		self .botonVerTemperatura.setObjectName ( " botonVerTemperatura " )

		self .botonVerTemperatura.clicked.connect (mostrarTemperatura)


		self .botonVerHumedad = QtWidgets.QPushButton ( self .centralwidget)
		self .botonVerHumedad.setGeometry (QtCore.QRect ( 310 , 250 , 191 , 81 ))
		self .botonVerHumedad.setObjectName ( " botonVerHumedad " )
	
		self .botonVerHumedad.clicked.connect (mostrarHumedad)

		self .botonVerPresion = QtWidgets.QPushButton ( self .centralwidget)
		self .botonVerPresion.setGeometry (QtCore.QRect ( 570 , 250 , 191 , 81 ))
		self .botonVerPresion.setObjectName ( " botonVerPresion " )
	
		self .botonVerPresion.clicked.connect (mostrarPresion)

		self .timer = QtCore.QTimer ( self .centralwidget)
		self .timer.setInterval ( 5000 )
		self .timer.timeout.connect (medirTodo)
		self .timer.start ()
		MainWindow.setCentralWidget ( self .centralwidget)
		self .menubar = QtWidgets.QMenuBar (MainWindow)
		self .menubar.setGeometry (QtCore.QRect ( 0 , 0 , 882 , 28 ))
		self .menubar.setObjectName ( " barra de menú " )
		MainWindow.setMenuBar ( self .menubar)
		self .statusbar = QtWidgets.QStatusBar (MainWindow)
		self .statusbar.setObjectName ( " barra de estado " )
		MainWindow.setStatusBar ( self .statusbar)

		self .retranslateUi (MainWindow)
		QtCore.QMetaObject.connectSlotsByName (MainWindow)

	def  retranslateUi ( self , MainWindow ):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle (_translate ( " MainWindow " , " MainWindow " ))

		self .botonTemperatura.setText (_translate ( " MainWindow " , " Temperatura " ))
		self .botonPresion.setText (_translate ( " MainWindow " , " Presion " ))
		self .botonHumedad.setText (_translate ( " MainWindow " , " Humedad " ))
		self .botonVerTemperatura.setText (_translate ( " MainWindow " , " Ver temperatura " ))
		self .botonVerHumedad.setText (_translate ( " MainWindow " , " Ver Humedad " ))
		self .botonVerPresion.setText (_translate ( " MainWindow " , " Ver presión " ))


if  __name__  ==  " _main_ " :
	import sys
	apply = QtWidgets.QApplication (sys.argv)
	MainWindow = QtWidgets.QMainWindow ()
	ui = Ui_MainWindow ()
	ui.setupUi (MainWindow)
	MainWindow.show ()
	sys.exit (app.exec_ ())
