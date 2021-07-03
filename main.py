import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
from pyowm import OWM
from pyowm.utils.config import get_default_config


class WeatherCheck(QtWidgets.QMainWindow):
	def __init__(self):
		super(WeatherCheck, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.init_UI()
	
	def init_UI(self):
		self.setWindowTitle('Weather')
		self.setWindowIcon(QIcon('sunny.ico'))

		self.ui.lineEdit.setPlaceholderText('Нью-Йорк, США')
		self.ui.pushButton.clicked.connect(self.weather)

	def weather(self):
		try:
			config_dict = get_default_config()
			config_dict['language'] = 'ru'
			owm = OWM('267f53ba6ee5620175b02e58315c4a56', config_dict)
			mgr = owm.weather_manager()

			lineEdit = self.ui.lineEdit.text()
			observation = mgr.weather_at_place(lineEdit)
			w = observation.weather
			temp = w.temperature('celsius')["temp"]
			wind = w.wind()['speed']
			self.ui.textEdit.setText(f'Температура сейчас {temp}° \nПогода: {w.detailed_status} \nВлажность {w.humidity}% \nСкорость ветра: {wind} м/с ')
		except:
			self.ui.textEdit.setText('Город не найден')


app = QtWidgets.QApplication([])
application = WeatherCheck()
application.show()

sys.exit(app.exec())