


# ports = serial.tools.list_ports.comports()

# for port, desc, hwid in sorted(ports):
#     print(port)
        
# config_logi = {'path_log' : 'logs/',
#                'log_level' : 'debug'}

# logi = Logger(config_logi)

#         # конфиг для сериал порта 
# config_serial  = {'logger' : logi,
#                 'port' : '/dev/ttyACM0',
#                 'bitrate' : 57600,
#                 'timeout' : 1,
#                 'debag' : False}

# serial_port = Rov_SerialPort(config_serial)

# name = 'data/' + '-'.join('-'.join('-'.join(str(datetime.now()).split()).split('.')).split(':')) + '.csv'

# with open(name, mode="a", encoding='utf-8') as w_file:
#         file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
#         file_writer.writerow(['time', 'pressure', 'temp', 'depth'])
        
# while True:
#         data = [str(datetime.now())] + [float(i) for i in serial_port.receiver_data().split(' ')]
        
#         with open(name, mode="a", encoding='utf-8') as w_file:
#                 file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
#                 file_writer.writerow(data)


from datetime import datetime
from distutils import util
from configparser import ConfigParser
from PyQt5 import QtCore
from Logger import *
from Serial import *
from ui_design import *
from pprint import pprint
import sys
import json
import csv
import serial.tools.list_ports


# пути для запуска 
PATH_CONFIG = 'config.json'
PATH_LOG = 'logs/'
PATH_DATA = 'data/'

class ServerSerial(QtCore.QObject):
    '''Класс отвечающий за общение с роботом и джойстиком'''
    telemetry = QtCore.pyqtSignal(list)
    
    def __init__(self, logi):
        super().__init__()

        self.logi = logi

        self.name_file = ''

        self.config_serial  = {'logger' : logi,
                                'port' : '',
                                'bitrate' : 57600,
                                'timeout' : 1,
                                'debag' : False}
        
        self.check_record = False
        

    def connect_and_record(self):
        self.logi.debug('start')

        self.serial_port = SerialPort(self.config_serial)

        self.logi.debug('start serial')

        with open(self.name_file, mode="a", encoding='utf-8') as w_file:
                file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
                file_writer.writerow(['time', 'pressure', 'temp', 'depth'])
                
        while self.check_record:
                data = [str(datetime.now())] + [float(i) for i in self.serial_port.receiver_data().split(' ')]
                
                with open(self.name_file, mode="a", encoding='utf-8') as w_file:
                        file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
                        file_writer.writerow(data)

                        self.telemetry.emit(data)
        
        self.serial_port.close()
        self.logi.debug('finish')

       
class ApplicationGUI(QMainWindow, Ui_UpperPCGUI):
    '''Основной класс приложения'''
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        with open(PATH_CONFIG, 'r') as self.file_config:
            self.config = json.load(self.file_config)

        # конфиг для логера 
        self.config_logi = {'path_log' : PATH_LOG,
                           'log_level' : self.config['DepthSensor']['log_level']}
        
        self.logi = Logger(self.config_logi)

        self.server = ServerSerial(self.logi)

        # создание потоков для опроса сериала 
        self.thread_serial = QtCore.QThread()
        self.thread_update = QtCore.QThread()

        ### настройка для подключение по сериалу ###
        # по умолчанию включен сериал 
        self.Serialconn.setChecked(True)

        # сканирование доступных портов 
        ports = serial.tools.list_ports.comports()
        list_ports = []
        for port, desc, hwid in sorted(ports):
            list_ports.append(str(port))
        self.serial_port_box.addItems(list_ports)
        self.serial_update.clicked.connect(self.port_update)

        # задание вариантов скоростей 
        list_baudrate = ['9600', '19200', '38400','57600', '115200']
        self.serial_baudrate_box.addItems(list_baudrate)
        self.serial_baudrate_box.setCurrentText('57600')

        ### настройка для подключения по UDP ###
        # временная деактивация UDP 
        self.UDP_IP_box.setEnabled(False)
        self.UDP_port_box.setEnabled(False)
        self.UDPconn.setEnabled(False)
        self.UDP_update.setEnabled(False)

        ### настройка записи ###
        self.record_path.setText('Name: ')
        self.record_stop.setEnabled(False)
        self.record_start.clicked.connect(self.rec_start)
        self.record_stop.clicked.connect(self.rec_stop)

        ### обновление интерфейса ###
        self.server.telemetry.connect(self.updategui)
    
    def port_update(self):
        ports = serial.tools.list_ports.comports()
        list_ports = []
        for port, desc, hwid in sorted(ports):
            list_ports.append(str(port))
        self.serial_port_box.clear()
        self.serial_port_box.addItems(list_ports)

             
    def rec_start(self):
        self.record_stop.setEnabled(True)
        self.record_start.setEnabled(False)
        
        self.server.name_file = PATH_DATA + str(datetime.now()).replace('-', ':')[:19] + '.csv'
        self.record_path.setText("Name: /" + self.server.name_file)
        self.server.config_serial['port'] = str(self.serial_port_box.currentText())
        self.server.config_serial['bitrate'] = int(self.serial_baudrate_box.currentText())
        self.server.check_record = True

        self.server.moveToThread(self.thread_serial)
        self.thread_serial.started.connect(self.server.connect_and_record)
        self.thread_serial.start()


    def rec_stop(self):
        self.record_stop.setEnabled(False)
        self.record_start.setEnabled(True)
        self.server.check_record = False
        self.thread_serial.quit()
        self.record_path.setText("Save: /" + self.server.name_file)
        print(self.thread_serial.isRunning())


    def updategui(self,telemetry):
        self.Pressure_value.display(telemetry[1])
        self.Temp_value.display(telemetry[2])
        self.Depth_value.display(telemetry[3])

if __name__ == '__main__':
    # если файл запущен как основной то запуск приложения
    app = QApplication(sys.argv)
    ex = ApplicationGUI()
    ex.show()
    sys.exit(app.exec_())
