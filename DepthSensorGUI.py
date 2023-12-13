import threading
import json
from time import sleep
from Logger import *
from Serial import *
from pprint import pprint
import csv
import serial.tools.list_ports
from datetime import datetime


ports = serial.tools.list_ports.comports()

for port, desc, hwid in sorted(ports):
    print(port)
        
config_logi = {'path_log' : 'C:/Users/Yarik/YandexDisk/Детская подводная робототехника/3. Навесное оборудование/Датчик глубины/Софт/DepthSensor/logs/',
               'log_level' : 'debug'}

logi = Logger(config_logi)

        # конфиг для сериал порта 
config_serial  = {'logger' : logi,
                'port' : 'COM18',
                'bitrate' : 57600,
                'timeout' : 1,
                'debag' : False}

serial_port = Rov_SerialPort(config_serial)

name = 'data/' + '-'.join('-'.join('-'.join(str(datetime.now()).split()).split('.')).split(':')) + '.csv'

with open(name, mode="a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
        file_writer.writerow(['time', 'pressure', 'temp', 'depth'])
        
while True:
        data = [str(datetime.now())] + [float(i) for i in serial_port.receiver_data().split(' ')]
        
        with open(name, mode="a", encoding='utf-8') as w_file:
                file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
                file_writer.writerow(data)